<!--
  Teşekkürler! Bu PR'ı hukukçu olarak mı yoksa yazılımcı olarak mı açtığınızdan
  emin değilseniz endişelenmeyin — ilgili bölümü doldurmanız yeterli, diğerini
  boş bırakabilirsiniz. Her iki bölüm de sizi ilgilendiriyorsa ikisini de doldurun.
-->

## Bu PR ne yapıyor?

<!-- Kısa açıklama: hangi sorunu çözüyor veya hangi özelliği ekliyor? -->

## Değişiklik türü

- [ ] Yeni skill / agent / routine
- [ ] Mevcut skill / agent güncellemesi
- [ ] Kaynak defteri güncellemesi (`sources/`)
- [ ] Hata düzeltmesi (teknik)
- [ ] Hukuki hata düzeltmesi (yanlış madde, güncel olmayan mevzuat vb.)
- [ ] Dokümantasyon
- [ ] Altyapı / CI / script
- [ ] Diğer: <!-- açıklayın -->

---

## 🔧 Teknik Değişiklikler İçin Checklist

*Kod, script, workflow veya validator değişikliği yapıyorsanız bu bölümü doldurun.*

- [ ] `python scripts/validate/validate_skills.py --strict` yerelde geçti
- [ ] `pytest evaluations/static/ -v` yerelde geçti
- [ ] Yeni bir bağımlılık eklediysem gerekçesini yukarıda açıkladım
- [ ] GitHub Actions değişikliği yaptıysam `permissions: contents: read` prensibine uydum ve `pull_request_target` kullanmadım
- [ ] Üçüncü parti bir Action eklediysem commit SHA'ya sabitledim (tag değil)
- [ ] Metadata şemasında (`skill.schema.json`) değişiklik yaptıysam mevcut tüm `SKILL.md` dosyalarını bu şemaya göre güncelledim

## ⚖️ Hukuki İçerik / Skill Değişiklikleri İçin Checklist

*Bir `SKILL.md`, `agents/*.md`, `references/` veya `sources/` dosyasını ekliyor ya da değiştiriyorsanız bu bölümü doldurun.*

- [ ] Bu skill/değişiklik **Türk hukukuna** uygundur; yabancı hukuk sistemi (ABD, AB mevzuatı vb.) varsayımı içermez
- [ ] Kullanılan her kanun/madde atfı `sources/mevzuat/` kayıt defterinde mevcuttur veya bu PR ile birlikte deftere ekleniyor
- [ ] Bu skill **sahte karar numarası veya sahte kanun metni üretmiyor** — halüsinasyon riskine karşı en az bir örnek senaryoyla test ettim
- [ ] Golden test dosyası (`evaluations/golden/`) ekledim veya güncelledim
- [ ] Model kendi bilgisinden konuştuğu durumlar için `[DOĞRULANMADI]` etiketleme mantığı korunuyor

### ⚠️ Zorunlu Onay Bloğu

- [ ] **Bu skill/agent hukuki tavsiye vermez**, yalnızca taslak/ön analiz sunar; nihai karar her zaman insan avukat kontrolündedir.
- [ ] Bu skill ceza, icra, işe iade, süre kaçırma gibi **hak kaybı riski taşıyan** bir konuyu ele alıyorsa, frontmatter'da `requires_human_review: true` alanını ekledim.

---

## Kaynak Atıfları

<!-- Bu PR'da kullanılan kanun, yönetmelik, içtihat vb. kaynakları listeleyin -->
<!-- Örnek: 6698 sayılı KVKK m.10 — RG 07.04.2016/29677 -->

## İlgili Issue

<!-- Varsa: Closes #123 -->

---

<sub>Bu depoya katkı sağlayarak [`CONTRIBUTING.md`](../CONTRIBUTING.md) ve [`CODE_OF_CONDUCT.md`](../CODE_OF_CONDUCT.md) kurallarını kabul etmiş olursunuz. GitHub web arayüzünden ilk kez katkı veriyorsanız [`CONTRIBUTING.md`'nin "Hukukçular İçin"](../CONTRIBUTING.md#bölüm-1--hukukçular-için-katkı-rehberi) bölümüne bakın — hiç terminal kullanmadan katkı verebilirsiniz.</sub>
