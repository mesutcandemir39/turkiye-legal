# Topluluk Skill Güven Katmanı

> `anthropics/claude-for-legal`'in `legal-builder-hub` plugin'i, Claude Cowork üzerinde üçüncü parti/topluluk skill'lerini bir güvenlik/lisans/güncellik kapısından geçiren, çalışma zamanında (runtime) çalışan bir "app store" katmanıdır. `turkiye-legal` böyle bir çalışma-zamanı marketplace'i **sunmaz** — kullanıcılar `claude plugin install` ile doğrudan bu depodan kurar, üçüncü bir keşif katmanı yoktur. Bu yüzden `legal-builder-hub` **birebir taşınmadı**. Bunun yerine, bu belge ve `scripts/validate/trust_gate.py`, **aynı güven kriterlerini GitHub PR sürecinde mekanik olarak zorlayan** işlevsel bir eşdeğer sunar.ADR-015.

## Neden bu belge var

Bu depoya yeni bir skill (kod katkısı olarak, `claude-for-legal`'deki gibi kullanıcının kendi yüklediği bağımsız bir üçüncü parti paket olarak değil) eklenmek istendiğinde, hangi kriterlerin karşılanması gerektiği burada tanımlanır. `CONTRIBUTING.md` katkı sürecini anlatır; bu belge **neyin kabul edilebilir olduğunu** tanımlar.

## Dört kapı (gate)

Bir skill, aşağıdaki dört kapının **hepsinden** geçmeden `main`'e alınmaz. `scripts/validate/trust_gate.py` bu dört kapıyı otomatik olarak çalıştırır ve `TRUSTED` / `NEEDS-REVIEW` / `REJECTED` şeklinde bir sonuç üretir.

### 1. Allowlist / Lisans Kapısı

Her `SKILL.md`'nin `turkiye_legal.attribution` bloğu eksiksiz olmalı ve `license: "Apache-2.0"` olmalıdır (bkz. `scripts/validate/schema/skill.schema.json`). Apache-2.0 uyumsuz bir lisansla (örn. kaynağı belirsiz, "tüm hakları saklıdır" ibaresi taşıyan) bir metin bu depoya **giremez**.

### 2. Şema / Yapı Kapısı

`scripts/validate/validate_skills.py --strict` geçmelidir — frontmatter şemaya uygun olmalı, `risk_level: high|critical` ise `requires_human_review: true` olmalıdır.

### 3. Kaynak Doğrulama Kapısı (freshness / provenance)

`scripts/validate/validate_sources.py` geçmelidir — her `tur: kanun` atfı `sources/mevzuat/kanunlar.yaml` defterinde bulunmalı, ad eşleşmeli, `durum: yururlukten_kalkti` olmamalıdır. Deftere yeni bir kanun eklenmeden önce (bkz. `sources/mevzuat/kanunlar.yaml` başlığındaki kural) resmî bir kaynağa karşı doğrulanmalı ve `son_dogrulama` alanı doldurulmalıdır — bu, "freshness" kriterinin somut karşılığıdır: doğrulanmamış veya eski (yürürlükten kalkmış) bir kaynağa dayanan skill bu kapıdan geçemez.

### 4. Güvenlik / Halüsinasyon Kapısı

`scripts/validate/lint_prompts.py` geçmelidir — uydurma Yargıtay/Danıştay karar numarası deseni, yabancı hukuk sızıntısı (GDPR, "Avrupa Birliği" vb.) veya bilinen prompt injection deseni içermemelidir.

## Karar bantları

| Sonuç | Ne demek | Ne olur |
|---|---|---|
| **TRUSTED** | Dört kapının hepsi geçti | Bakımcı içerik/üslup incelemesi yapıp merge edebilir |
| **NEEDS-REVIEW** | Allowlist/lisans kapısı başarısız ama yapısal/güvenlik kapıları geçti | Bakımcı, atıf/lisans eksikliğini elle düzeltip tekrar değerlendirir — otomatik red değildir |
| **REJECTED** | Şema, kaynak doğrulama veya güvenlik kapılarından biri başarısız | Merge **edilemez**, katkıcı düzeltip tekrar PR açmalıdır |

## Re-scan-on-update (güncellemede yeniden tarama)

`legal-builder-hub`'ın "bir skill güncellendiğinde tekrar taranır" ilkesi, bu depoda **doğal olarak** sağlanır: her PR (yeni skill veya mevcut bir skill'in güncellemesi fark etmeksizin) `.github/workflows/validate-skills.yml` ve `ci.yml` üzerinden aynı dört kapıdan geçer — ayrı bir mekanizma icat etmeye gerek yoktur.

## Install log (kurulum kaydı)

`legal-builder-hub`'ın kurulum logu, bu depoda `CHANGELOG.md` (her yeni skill'in hangi sürümde eklendiği) ve ilgili plugin'in kendi `README.md`'sindeki İçerik tablosu ile karşılanır — her yeni skill bu iki yere mutlaka eklenir (bkz. `CONTRIBUTING.md` Bölüm 2).

## Bu güven katmanının kapsamadığı şey

Bu dört kapı **içerik doğruluğunu tam olarak garanti etmez** — örn. bir kanun maddesinin yorumunun doğru olup olmadığı hâlâ bir insan (mümkünse hukuk geçmişi olan bir bakımcı) tarafından değerlendirilmelidir. Kapılar, **mekanik olarak denetlenebilir** kriterleri (şema, atıf, kaynak varlığı, yasaklı desen) zorlar; hukuki isabet nihayetinde insan incelemesine kalır — bu, projenin `requires_human_review` ilkesiyle tutarlıdır.
