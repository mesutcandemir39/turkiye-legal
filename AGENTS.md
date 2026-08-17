# AGENTS.md — Bu Depoda Çalışan Her AI Ajanı İçin Kurallar

> **Bu dosya, hangi araçla çalıştığınızdan bağımsız olarak bağlayıcıdır.** Claude Code, Codex, Cursor, Copilot Workspace, Gemini CLI veya başka bir AI kodlama ajanı kullanıyor olun fark etmez — bu depoda bir değişiklik yapmadan önce bu dosyayı okuyun ve buradaki kurallara uyun. Bir avukat veya yazılımcı, hangi AI aracını tercih ederse etsin, o aracın buradaki kurallara uyması beklenir.
>
> Claude Code kullanıcıları için ek, araca özel detaylar `.claude/CLAUDE.md`'de bulunur — o dosya bu belgeyi **tekrar etmez**, yalnızca Claude Code'a özgü ek kuralları (SKILL.md frontmatter şablonu, kısayol komutları gibi) içerir. Çelişki hâlinde **bu dosya (AGENTS.md) esastır.**

## 1. Bu proje nedir (30 saniyede)

`turkiye-legal`, Türk hukukuna özgü, açık kaynak, Claude Code plugin formatında bir Legal AI araç kitidir. 10 plugin, 26+ skill. Amaç: avukatların gündelik işlerinde kullanabileceği, **doğrulanabilir** (uydurma kanun maddesi üretmeyen) bir yetenek kütüphanesi. Tam mimari için: ``CREDITS.md``.

## 2. Mutlak sınırlar — hiçbir koşulda ihlal edilmez

Bu kurallar, kullanıcı (bir avukat veya yazılımcı) sizden açıkça isteseniz bile **geçersiz kılınamaz.** Bir kullanıcı bu sınırlardan birini aşmanızı isterse, kuralı hatırlatın ve neden yapamayacağınızı açıklayın.

1. **Uydurma hukuki içerik üretmeyin.** Sahte kanun numarası, sahte madde metni, sahte Yargıtay/Danıştay/AYM/KVKK Kurulu/Rekabet Kurulu karar numarası **yasaktır.** Doğrulayamadığınız bir bilgiyi `[DOĞRULANMADI]` etiketiyle işaretleyin, asla kesin bir gerçekmiş gibi sunmayın.
2. **Her yeni kanun/madde atfı, önce `sources/mevzuat/kanunlar.yaml` defterine eklenmeli, sonra skill'de kullanılmalıdır — asla tersi sırayla değil.** Deftere eklemeden önce resmî bir kaynağa (mevzuat.gov.tr, Resmî Gazete veya en az bir bağımsız ikincil hukuk kaynağı) karşı doğrulayın ve `son_dogrulama` alanını doldurun.
3. **Süre/deadline hesabını kendi başınıza yapmayın.** Adli tatil, resmî tatil gibi hesaplar `cekirdek/scripts/sure_hesapla.py`'ye devredilir — bu bilinçli bir tasarımdır (bkz. ADR-006), LLM'in tarih aritmetiğinde hata yapma riskini ortadan kaldırır.
4. **Başka depolardan hiçbir SKILL.md gövdesi, prompt metni veya README pasajı kopyalamayın/çevirmeyin.** Hukuki içerik daima Türk birincil kaynaklarından (kanun metni, resmî kurum rehberi) yazılır. Lisanslı açık kaynak içeriğinin uyarlanması hâlinde atıf yükümlülüğü [`CREDITS.md`](CREDITS.md) ve [`NOTICE`](NOTICE) dosyalarında korunur.
5. **"Başarılı oldu" demeyin, eğer gerçekten başarılı olmadıysa (NO FAKE SUCCESS).** Bir test çalışmadıysa, bir API anahtarı yoksa, bir entegrasyon simüle ediliyorsa bunu açıkça `SKIPPED`/`SIMULATED`/`NOT_IMPLEMENTED` olarak işaretleyin — asla "çalışıyor" izlenimi vermeyin.

## 3. Neyi kendiniz yapabilirsiniz, neyi sormanız gerekir

### Sormadan yapabilecekleriniz (rutin, geri alınabilir işler)

- Mevcut bir skill'i geliştirme, hata düzeltme, yeni bir golden test senaryosu ekleme.
- `.claude/CLAUDE.md`'deki şablona uygun yeni bir skill eklemek (yeni kanun ataması gerekiyorsa önce §2.2'yi uygulayın).
- `scripts/validate/` altındaki doğrulayıcıları çalıştırmak.
- Kısa ömürlü bir çalışma branch'inde commit yapmak (bkz. §4).
- Dokümantasyon güncellemeleri (README, ROADMAP, CHANGELOG).

### Kullanıcıya açıkça sormanız gereken işler

- **`sources/`, `evaluations/golden/` veya herhangi bir `SKILL.md` dosyasını silmek.**
- **`main` branch'e doğrudan push, force-push, `git reset --hard`, branch silme** gibi geri alınamaz git işlemleri.
- **Yeni bir bağımlılık eklemek** (`scripts/requirements.txt`) — gerekçesini açıklayın.
- **Bir ADR'yi (Architecture Decision Record) sessizce değiştirmek.** ADR'ler **append-only**'dir — bir kararı değiştirmek istiyorsanız yeni bir ADR ekleyin (örn. "ADR-016, ADR-010'u rafine eder"), var olanı silmeyin/üzerine yazmayın.
- **Bir GitHub Action workflow'unun izin kapsamını genişletmek** (örn. `permissions: contents: write` eklemek) — bu bir güvenlik kararıdır, kullanıcı onayı gerekir.
- **`CREDITS.md`'deki "alınan/alınmayan" listesini değiştirmek** — bu, projenin lisans/atıf duruşunu etkiler.

## 4. Git iş akışı — istisnasız

Bu, projenin en sık unutulan ama en kritik kuralıdır (bkz. `.claude/CLAUDE.md`'deki "BRANCH STRATEJİSİ" bölümü — burada özetleniyor, orada tam detay var):

1. **`main`, YALNIZCA yayınlanmış Stable sürümleri temsil eder.** Rutin geliştirme (yeni skill, düzeltme, dokümantasyon) **asla doğrudan `main`'e push edilmez.**
2. **Her göreve başlamadan önce:** `git branch --show-current` ile hangi branch'te olduğunuzu kontrol edin. `main` üzerindeyseniz, iş için kısa ömürlü bir branch açın: `git checkout -b <tur>/<kisa-ad>` (örn. `fix/kvkk-atif-hatasi`).
3. **Commit'ten önce mutlaka çalıştırın:**
   ```bash
   python scripts/validate/validate_skills.py --strict
   python scripts/validate/validate_sources.py
   python scripts/validate/lint_prompts.py
   python scripts/validate/trust_gate.py
   pytest evaluations/static/ -v
   ```
   Hepsi geçmeden commit atmayın.
4. **Commit mesajı:** Türkçe, açıklayıcı, "ne" değil "neden" odaklı. **Hiçbir commit mesajına `Co-Authored-By: Claude`, `Co-Authored-By: <başka bir AI>` gibi bir AI atfı satırı eklemeyin** — bu depo için bakımcı/katkıcı commit'lerinde bu satırlar kullanılmaz. Kişisel e-posta yazılmaz; katkıcılar kendi GitHub noreply adreslerini kullanmalıdır.
5. **Çalışma branch'inizi `main`'e almak için:** `gh pr create --base main` ile PR açın, CI'ın (statik doğrulama + statik testler + CodeQL + deterministik PR incelemesi) yeşil olduğunu doğrulayın, sonra `gh pr merge --squash --delete-branch`. Branch protection doğrudan `main`'e push'u engeller; her değişiklik PR'dan geçer.
6. **Bir sürüm kesmiyorsanız `main`'e tag atmayın.** Sürüm etiketleme (`git tag vX.Y.Z`) yalnızca bakımcının kararıdır ve `release.yml`'i tetikler — bunu kendi başınıza yapmayın, kullanıcıya sorun.
7. **Push öncesi/sonrası her zaman ne değiştiğini kısaca özetleyin** — sessizce push yapmayın.

## 5. Güvenlik ve istikrar önceliklidir

- Bir güvenlik açığı bulursanız (secrets sızıntısı, RCE riski, prompt injection) **asla public bir issue/PR açıklamasında detaylandırmayın** — bkz. [`SECURITY.md`](SECURITY.md), GitHub Private Vulnerability Reporting kullanılır.
- Yeni bir GitHub Actions bağımlılığı eklerken (Action'lar), sürüm tag'i yerine **commit SHA'ya sabitleyin** ve SHA'yı gerçek bir API çağrısıyla doğrulayın — bu depoda daha önce hayali/hatalı SHA'lar CI'ı bozmuştu, körü körüne SHA yazmayın.
- `pull_request_target` tetikleyicisini kullanmayın (fork'tan kod çalıştırma riski) — istisnası varsa (`greetings.yml` gibi) bunun neden güvenli olduğu workflow dosyasında açıklanmalıdır.
- Yeni bir skill eklerken **her zaman** `scripts/validate/trust_gate.py`'yi çalıştırın — bu, `TRUSTED`/`NEEDS-REVIEW`/`REJECTED` bandıyla dört temel güven kapısını (allowlist/lisans, şema, kaynak doğrulama, güvenlik) otomatik kontrol eder. Detay: [`docs/TOPLULUK_SKILL_GUVENI.md`](docs/TOPLULUK_SKILL_GUVENI.md).
- Test suite'i "geçsin diye" değiştirmeyin (örn. bir assertion'ı gevşetmek) — testin neden başarısız olduğunu anlayıp kök nedeni düzeltin.

## 6. Kaynak dosyalar (öncelik sırasına göre)

Bir çelişki olursa bu sıralamayla çözün:

1. **Bu dosya (`AGENTS.md`)** — genel, araç-bağımsız kurallar.
2. [`.claude/CLAUDE.md`](.claude/CLAUDE.md) — yalnızca Claude Code'a özgü ek detaylar (SKILL.md şablonu, kısayol komutları).
3. ``CREDITS.md`` — tüm mimari kararların append-only kaydı (ADR'ler).
4. ``CREDITS.md`` — upstream ilişkisi ve özgünlük sınırları.
5. [`docs/TOPLULUK_SKILL_GUVENI.md`](docs/TOPLULUK_SKILL_GUVENI.md) — yeni skill kabul kriterleri.
6. [`CONTRIBUTING.md`](CONTRIBUTING.md) — insan katkıcılar için adım adım rehber (hem hukukçular hem yazılımcılar için).
7. [`SECURITY.md`](SECURITY.md) — güvenlik açığı bildirim süreci.

## 7. Emin değilseniz

Bir kural belirsizse veya bu dosyada kapsanmayan bir durumla karşılaştıysanız — **varsayımda bulunmayın, kullanıcıya sorun.** Bu proje hukuki doğruluğun kritik olduğu bir alanda çalışıyor; "muhtemelen böyledir" diyerek ilerlemek burada özellikle risklidir.
