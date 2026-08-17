# is-hukuku

**Kademe:** Tier A · **Dayanak:** 4857 sayılı İş Kanunu

## İçerik

| Tür | Ad | Ne yapar |
|---|---|---|
| Skill | `fesih-triyaj` | Fesih bildirimini triyaj eder: ihbar süresi (m.17, kıdeme göre 2/4/6/8 hafta), kıdem tazminatı ön değerlendirmesi, işe iade için 1 aylık zorunlu arabuluculuk başvuru süresi (m.20, **kritik**) |
| Skill | `is-sozlesmesi-review` | İş sözleşmesini imza öncesi denetler: yazılı sözleşme zorunluluğu, deneme süresi sınırı (azami 2 ay), zorunlu bilgilendirme unsurları |
| Skill | `yillik-izin-hesaplayici` | Kıdeme göre asgari yıllık ücretli izin hak edişini hesaplar (m.53: 14/20/26 gün eşikleri + yaş istisnası) |
| Skill | `fazla-mesai-hesaplayici` | Haftalık 45 saati aşan çalışmayı ve %50 zamlı ücretini hesaplar, 270 saatlik yıllık üst sınırı kontrol eder (m.41) |

## Kurulum

```bash
claude plugin install is-hukuku@turkiye-legal
```

## Kullanım

```
/is-hukuku:fesih-triyaj [işe başlama tarihi] [fesih tebliğ tarihi] [gerekçe]
/is-hukuku:is-sozlesmesi-review [iş sözleşmesi metni]
/is-hukuku:yillik-izin-hesaplayici [işe başlama tarihi] [hesaplama tarihi]
/is-hukuku:fazla-mesai-hesaplayici [haftalık çalışma saati] [saatlik ücret]
```

`risk_level: critical` — işe iade süresi kaçırılırsa hak kaybı olur. Çıktı her zaman bir avukat tarafından teyit edilmelidir.
