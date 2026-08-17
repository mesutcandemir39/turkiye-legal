# idare-vergi

**Kademe:** Tier B — dar kapsamlı · **Dayanak:** 2577 sayılı İYUK, 213 sayılı VUK

Türk idare ve vergi yargısına özgü, İYUK m.7 dava açma süresi ve vergi uyuşmazlığı sınıflandırması sağlayan eklenti.

## İçerik

| Tür | Ad | Ne yapar |
|---|---|---|
| Skill | `idari-islem-triyaji` | Bir idari işlem veya vergi ihbarnamesini triyaj eder: idari dava mı vergi uyuşmazlığı mı olduğunu, hangi başvuru yolunun (dava/itiraz/uzlaşma) uygulanabileceğini belirler |

## Kurulum

```bash
claude plugin install idare-vergi@turkiye-legal
```

## Dürüstlük notu

İYUK m.7'deki genel dava açma süresinin kesin gün sayısı bu sürümde doğrulanamadı; skill **hiçbir sayısal süre değeri üretmez**, yalnız sınıflandırma yapar ve kullanıcıyı resmî kaynak doğrulamasına yönlendirir. Bu, `good-first-legal-issue`'dur.
