# dava-takip

**Kademe:** Tier B — dar kapsamlı · **Dayanak:** 6100 sayılı Hukuk Muhakemeleri Kanunu

## İçerik

| Tür | Ad | Ne yapar |
|---|---|---|
| Skill | `dilekce-yapi-kontrolu` | HMK m.119'un dokuz bendine göre bir dava dilekçesini var/yok ön kontrolünden geçirir |
| Skill | `dilekce-kalite-skoru` | Aynı dilekçeyi usul, hukuki dayanak, dil/açıklık, delil bağlantısı kategorilerinde 100 üzerinden puanlar |
| Skill | `karsi-arguman-uretimi` | Verilen bir iddia/dilekçe metnindeki argümanlara karşı olası usul ve esas itirazlarını sistematik listeler |
| Skill | `delil-haritasi-cikarma` | Bir metindeki taraf/tarih/vakıa/delil ilişkisini yapılandırılmış bir tabloya döker |
| Skill | `sade-dil-anlatimi` | Hukuki bir metni müvekkilin anlayacağı sade dilde açıklar |
| Agent | `intake-agent` | Bir belgeyi (ihtarname, dilekçe, ödeme emri, fesih bildirimi vb.) sınıflandırıp ilgili skill'e yönlendirir |
| Agent | `durusma-hazirlik` | Birden fazla dosya belgesinden kronoloji, kritik tarihler, tensip özeti ve strateji notları içeren bir duruşma hazırlık özeti çıkarır |

## Kurulum

```bash
claude plugin install dava-takip@turkiye-legal
```

## Dürüstlük notu

HMK m.119'un tam ve kesin bent listesi bu sürümde doğrulanamadı; `dilekce-yapi-kontrolu` yalnızca genel kabul görmüş kategorileri kontrol eder, resmî madde metninin birebir kopyası değildir. Detay: skill'in kendi `SKILL.md` dosyası. Bu, `good-first-legal-issue`'dur.
