# Changelog

Bu dosya [Keep a Changelog](https://keepachangelog.com/tr/1.1.0/) standardını izler
ve bu proje [Semantic Versioning](https://semver.org/lang/tr/) kullanır.

## [Unreleased]

- Devam eden çalışmalar için GitHub Milestones sayfasına bakınız.

---

## [0.1.0] — 2026-08-18

İlk kararlı sürüm.

### Eklendi

**Beceri kütüphanesi**
- 81 pratik alanında **923 yapılandırılmış beceri** — aile hukukundan enerji
  hukukuna, sağlık hukukundan yapay zekâ hukukuna kadar.
- Her beceri `SKILL.md` frontmatter şemasına uyar; risk seviyesi, girdi/çıktı
  tanımı ve kaynak atıfları zorunludur.

**Eklenti sistemi**
- **91 kurulabilir Claude Code eklentisi** (81 pratik alanı + 10 altyapı).
- `claude plugin marketplace add` ile tek komutla kurulum.
- Kök `.claude-plugin/marketplace.json` tüm eklentileri kayıt altına alır.

**MCP sunucuları**
- `turkiye-legal-mevzuat` — `madde_getir`, `kanun_metni_getir`, `mevzuat_ara`,
  `bilinen_kanunlar` (kaynak: mevzuat.gov.tr).
- `turkiye-legal-ictihat` — `ictihat_ara`, `karar_getir`.
- Depo Claude Code'da açıldığında `.mcp.json` üzerinden otomatik devreye girer.

**Doğruluk altyapısı**
- `sources/mevzuat/kanunlar.yaml` — **58 doğrulanmış kanun kaydı**. Deftere
  yazılmamış bir kanuna atıf yapılamaz.
- `validate_skills.py` — şema doğrulaması (921 dosya).
- `validate_sources.py` — kaynak defterine karşı atıf denetimi.
- `lint_prompts.py` — halüsinasyon ve yabancı hukuk sızıntısı taraması.
- `lint_tool_scope.py` — araç yetkisi denetimi.
- `evaluations/static/` — 54 statik regresyon testi (dil modeli gerektirmez).
- `evaluations/golden/` — gerçek model üzerinde regresyon senaryoları.
- `cekirdek/scripts/sure_hesapla.py` — deterministik adli tatil ve süre hesaplayıcı.
- `[DOĞRULANMADI]` etiketleme protokolü.

**CI/CD**
- `pr_review.py` — **tamamen deterministik PR incelemesi.** Harici API veya dil
  modeli çağrısı yapmaz; puanlama doğrulayıcıların gerçek çıktısından türetilir.
  Aynı girdi her zaman aynı sonucu verir.
- Haftalık depo sağlık kontrolü — yalnızca gerçek bir bozulma tespit ederse
  issue açar, rutin bildirim gürültüsü üretmez.
- CodeQL statik analiz, OpenSSF Scorecard, fuzzing.
- Üçüncü parti Action'lar commit SHA'ya sabitlenmiştir.

**Yönetişim ve dokümantasyon**
- Apache-2.0 lisansı, `NOTICE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`,
  `GOVERNANCE.md`, `SECURITY.md`.
- Türkçe ve İngilizce README.
- Hukukçular için terminal bilgisi gerektirmeyen katkı rehberi.

### İş akışı

Depo trunk-based çalışır: tek kalıcı dal `main`. Her değişiklik kısa ömürlü bir
branch üzerinden PR ile gelir; branch protection doğrudan push'u engeller.

Depoda *immutable releases* açıktır — yayımlanmış bir release **silinmez**;
silinen release'in tag adı kalıcı olarak kullanılamaz hâle gelir. Geri alma
gerekiyorsa yeni bir yama sürümü çıkarılır.

### Bilinen sınırlar

- 10 altyapı eklentisinin (`cekirdek`, `kvkk-uyum`, `is-hukuku`, `sozlesme`,
  `icra-iflas`, `mevzuat-takip`, `dava-takip`, `ticaret-sirketler`,
  `fikri-mulkiyet`, `idare-vergi`) `skills/` dizinleri henüz boştur; hook, script
  ve referans sağlarlar. `M3 — Eklenti Bütünlüğü` altında takip edilmektedir.
- `sources/ictihat/` defteri henüz gerçek bir emsal karar kaynağına bağlı
  değildir — `M2 — İçtihat Katmanı`.
