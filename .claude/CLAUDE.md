# CLAUDE.md — turkiye-legal Repo Kuralları (Claude Code'a özel ek)

> **Önce [`AGENTS.md`](../AGENTS.md)'yi okuyun.** Bu dosya, o dosyayı tekrar etmez — yalnızca Claude Code'a özgü ek detayları (SKILL.md frontmatter şablonu, kısayol komutları) içerir. Genel kurallar (mutlak sınırlar, git iş akışı, güvenlik) `AGENTS.md`'dedir ve çelişki hâlinde **`AGENTS.md` esastır.** Codex, Cursor veya başka bir AI ajanı kullanıyorsanız yalnızca `AGENTS.md` sizin için geçerlidir, bu dosya Claude Code'a özgüdür.

Bu dosya, bu depoda çalışan Claude Code oturumları için bağlayıcıdır. Amaç: hukuki doğruluk, güvenlik ve mimari tutarlılığı otomatik olarak korumak.

## Proje nedir

Türkiye hukukuna özgü, açık kaynak, plugin tabanlı bir Legal AI ekosistemi. 10 pratik alanı plugin'i (`cekirdek` + 5 Tier A + 4 Tier B), her biri Claude Code plugin spec'ine uygun (`skills/`, `agents/`, `references/`). **Public** ve açık kaynak — bkz. "Bu depoya özgü notlar" bölümündeki güncel sürüm.

## ⚠️ BRANCH STRATEJİSİ — İSTİSNASIZ UYULUR

**Depo trunk-based çalışır: kalıcı tek dal `main`'dir.** Kalıcı bir `develop` dalı
**yoktur** ve yeniden açılmaz.

1. **Hiçbir değişiklik doğrudan `main`'e push edilmez.** Branch protection bunu
   teknik olarak da engeller (`allow_force_pushes: false`, PR zorunlu,
   `required_status_checks`).
2. **Her iş için kısa ömürlü bir branch açılır.** Adlandırma: `<tur>/<kisa-ad>` —
   `feat/`, `fix/`, `docs/`, `chore/`, `release/`. Örnek: `fix/kvkk-atif-hatasi`.
3. **Commit öncesi doğrulama zorunludur:**
   ```bash
   python scripts/validate/validate_skills.py --strict
   python scripts/validate/validate_sources.py
   python scripts/validate/lint_tool_scope.py --strict
   pytest evaluations/static/ -v
   ```
   Hepsi geçmeden commit atılmaz.
4. **`main`'e alma:** `gh pr create --base main` → CI yeşil → `gh pr merge --squash
   --delete-branch`. Branch merge sonrası silinir; dal biriktirilmez.
5. **Sürüm kesme:** Sürüm numarası (`plugin.json` ve `SKILL.md` `version` alanları,
   README badge'leri, bu dosyanın alt notu) güncellenir, `CHANGELOG.md`'ye yeni
   bölüm eklenir — bu da bir `release/vX.Y.Z` branch'i üzerinden PR ile gelir.
   Merge sonrası `main` üzerinde release yayımlanır.
6. **Release silinmez.** Depoda *immutable releases* açıktır: silinen bir
   release'in tag adı **kalıcı olarak** kullanılamaz hâle gelir. Bir sürümü geri
   almak gerekiyorsa yeni bir yama sürümü çıkarılır, eskisi silinmez.
7. **Acil durum istisnası:** `enforce_admins: false` olduğu için teknik olarak
   bypass mümkündür — ama bu **kullanıcının açık onayı olmadan kullanılmaz.**

## Mutlak sınırlar — asla ihlal edilmez

1. **Uydurma hukuki içerik üretme.** Sahte kanun numarası, sahte madde, sahte Yargıtay/Danıştay/AYM karar numarası **yasaktır**. Kaynağı doğrulanamayan bilgi `[DOĞRULANMADI]` etiketiyle işaretlenir, asla kesin ifadeyle sunulmaz.
2. **Kaynak atfı `sources/mevzuat/kanunlar.yaml` defterine karşı doğrulanabilir olmalı.** Yeni bir kanun/madde atfı eklerken önce deftere bakılır; deftede yoksa önce deftere eklenir (kaynağıyla), sonra skill'de kullanılır. Asla tersi sırayla değil.
3. **Süre/deadline hesabı LLM'de yapılmaz.** Adli tatil, resmî tatil, sürenin tatilde bitmesi gibi hesaplar `cekirdek/scripts/sure_hesapla.py`'ye devredilir. Bu script'i değiştirirken birim testleri güncellenir ve her kural satırı kaynağa atıfla doğrulanır.
4. **`git push` öncesi her zaman kullanıcıya bildir.** Bu depoda push otomatik değildir; kullanıcı "commit ve push yapmayı ihmal etme" demişse bile her push işleminden önce/sonra ne değiştiğini kısaca özetle. Force push, branch silme, `git reset --hard` gibi yıkıcı komutlar kullanıcı açık onayı olmadan **hiçbir zaman** çalıştırılmaz.
5. **Dosya silmeden önce sor.** Özellikle `sources/`, `evaluations/golden/` ve herhangi bir `SKILL.md` silinmeden önce kullanıcıya onay sorulur.
6. **Başka depolardan prompt/skill metni kopyalanmaz.** Hiçbir dış kaynaktan `SKILL.md` gövdesi, README pasajı veya şablon metni alınmaz, çevrilmez. Hukuki içerik daima Türk birincil kaynaklarından (kanun metni, resmî kurum rehberi) yazılır.

## Mimari — nereye ne yazılır

```
<plugin>/.claude-plugin/plugin.json   → plugin manifest (name, version, description)
<plugin>/skills/<ad>/SKILL.md         → tek görevli skill; frontmatter + turkiye_legal: bloğu
<plugin>/agents/<ad>.md               → çok adımlı pipeline veya zamanlanmış iş
<plugin>/references/                  → şablon, kontrol listesi, örnek girdi
sources/mevzuat|ictihat|kurumsal/     → doğrulanmış kaynak kayıt defteri (YAML)
evaluations/static/                   → pytest, LLM'siz, her PR'da zorunlu
evaluations/golden/                   → LLM'li regresyon senaryoları, nightly
scripts/validate/                     → şema, kaynak, lint doğrulayıcılar
```

Yeni bir `routines/` veya `scheduled/` kök dizini **açılmaz** — routine'ler ilgili plugin'in `agents/` dizininde zamanlanmış frontmatter ile, tetikleyicileri `.github/workflows/` ile temsil edilir (bkz. ADR-001).

## SKILL.md frontmatter şablonu

Ayrı `metadata.yaml` **yazılmaz** (ADR-004). Tüm metadata `SKILL.md` frontmatter'ında, hukuki alanlar `turkiye_legal:` altında:

```yaml
---
name: <kebab-case-ad>
description: "Claude Code tetikleme sinyali, <1024 karakter"
argument-hint: "[opsiyonel]"
user-invocable: true
turkiye_legal:
  version: 0.0.1
  category: <plugin kategorisi>
  jurisdiction: { country: TR, legal_system: civil_law, scope: [TR] }
  risk_level: low | medium | high | critical
  requires_human_review: true | false   # risk_level >= high ise true ZORUNLU
  inputs: [...]
  outputs: [...]
  sources:
    - { tur: kanun, numara: "6698", ad: "...", madde: "10" }
    # DİKKAT: alan adı "no" DEĞİL "numara" — "no" YAML 1.1'de unquoted
    # kullanıldığında boolean false'a çözümlenir (PyYAML SafeLoader ile
    # doğrulandı). Bu alanı asla "no:" olarak yazmayın.
  attribution:
    original_author: "Mesut Can Demir"
    original_repository: "https://github.com/mesutcandemir39/turkiye-legal"
    license: "Apache-2.0"
---
```

Yeni bir skill yazmadan önce `scripts/validate/schema/skill.schema.json`'ı kontrol et; şemaya uymayan alan eklemeden önce şemayı güncelle.

### Çift yüzey (Cowork/Code) çıktı notu — isteğe bağlı, yalnız görsel çıktı üreten skill'lerde

`turkiye-legal` şu an yalnız Claude Code'u hedefler — Claude Cowork (Anthropic'in ayrı masaüstü uygulaması) için özel bir entegrasyon **yoktur** ve bu bilinçli bir tercihtir — Cowork bu depoda inşa edilebilecek bir özellik değil, harici bir çalışma yüzeyidir. Ancak ileride **görsel bir çıktı üreten** bir skill (örn. bir dashboard/rapor skill'i) eklenirse, şu deseni izlemesi önerilir: talimatta "Cowork'te satır içi göster, Claude Code'da ayrı bir dosyaya yaz" gibi istemciye göre koşullu bir davranış tanımlanabilir. Bu yalnızca **görsel/HTML çıktı üreten** skill'ler için anlamlıdır — bu depodaki mevcut skill'lerin hiçbiri (hepsi metin tabanlı analiz/triyaj) bu notu gerektirmez, zorunlu bir kural değildir.

## Terminoloji

Doğal, profesyonel avukat dili. "Yasal" değil **"Hukuki"**; "Kontrat" değil **"Sözleşme"**; "Mahkeme kağıdı" değil **"Tensip Zaptı" / "Dilekçe"**. Makine çevirisi kokan ifadeler ("AI slop") kabul edilmez — bir cümle Türkçe bir hukukçunun yazacağı gibi okunmalı.

## Kısayol komutları

Bu depoda `.claude/commands/` altında tanımlı özel komutlar:

- `/validate` → `scripts/validate/` altındaki tüm doğrulayıcıları sırayla çalıştırır
- `/new-skill <plugin> <skill-adi>` → yukarıdaki şablonla yeni skill iskeleti açar
- `/new-plugin <ad>` → yeni plugin dizin yapısını (`.claude-plugin/plugin.json` dahil) kurar

Bu komutlar henüz yazılmadıysa (`.claude/commands/` boşsa), Faz 3'te ekleneceklerdir; o zamana kadar ilgili scriptleri doğrudan `python scripts/validate/...` ile çalıştır.

## Test disiplini

`evaluations/static/` LLM gerektirmez, her PR'da çalışır, **zorunlu geçiş kapısıdır.** `evaluations/golden/` gerçek modele ihtiyaç duyar; API anahtarı yoksa sonucu **`SKIPPED`** olarak raporla, asla `PASS` deme. Çalışmayan/mock bir entegrasyonu `MOCK`, `SIMULATED` veya `NOT_IMPLEMENTED` etiketiyle işaretle — sessizce "çalışıyor" gibi davranma.

## Güvenlik

- GitHub Actions'ta varsayılan izin `permissions: contents: read`.
- `pull_request_target` tetikleyicisi kullanılmaz (fork'tan kod çalıştırma riski).
- Üçüncü parti Actions commit SHA'ya sabitlenir, sürüm tag'ine değil.
- AI PR Review yalnız `PASS/WARN/BLOCK` yorumu yazar; merge yetkisi **yoktur**.
- Kritik güvenlik açığı (özellikle prompt injection) bulunursa **public issue açılmaz** — bkz. `SECURITY.md`.

## Bu depoya özgü notlar

- Repo **public** ve açık kaynak — [github.com/mesutcandemir39/turkiye-legal](https://github.com/mesutcandemir39/turkiye-legal). Kişisel hesap altında (organizasyon değil); bu yüzden `CODEOWNERS`'daki takım referansları (`@turkiye-legal/dev-maintainers` vb.) depo bir organizasyona taşınana kadar fiilen devre dışıdır — bkz. `GOVERNANCE.md`.
- **Commit kimliği:** `Mesut Can Demir <36205327+mesutcandemir39@users.noreply.github.com>` — GitHub'ın noreply adresi. Kişisel e-posta **hiçbir commit'e yazılmaz.**
- **Commit trailer kuralı — istisnasız:** Hiçbir commit mesajına `Co-Authored-By: Claude ...` veya benzeri bir AI atfı satırı eklenmez. DCO `Signed-off-by` trailer'ı da kullanılmaz (`git commit -s` çalıştırılmaz) — bu depo için bakımcı commit'lerinde gerek yoktur. Dış katkıcıların kendi PR'larında kendi DCO imzalarını atması ayrı bir konudur (bkz. `CONTRIBUTING.md`), bu kural yalnız bakımcı/otomatik commit'ler içindir.
- Güncel sürüm: **v0.1.0 (Stable)**. Gerekçe için `CHANGELOG.md`'deki sürüm numarası notuna bakın.
- **Sürüm destek penceresi (ADR-013, unutulmaz):** her zaman yalnızca en güncel **2** Stable sürüm desteklenir — en son yayınlanan Stable her zaman "Stable ve LTS" kabul edilir, bir öncekindeki Stable destekte kalır, ondan eski her Stable otomatik **EOL**'dur. Yeni bir Stable release (`git tag vX.Y.Z` main'de) çıktığında bu pencere kayar ve `SECURITY.md`'deki "Desteklenen Sürümler" tablosu **elle güncellenmelidir** — bu adım release sürecinin bir parçasıdır, atlanmaz.
