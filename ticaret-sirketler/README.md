# ticaret-sirketler

**Kademe:** Tier B — dar kapsamlı · **Dayanak:** 6102 sayılı Türk Ticaret Kanunu

## İçerik

| Tür | Ad | Ne yapar |
|---|---|---|
| Skill | `genel-kurul-belge-kontrolu` | Genel kurul çağrı belgesi veya toplantı tutanağının yapısal tamlığını kontrol eder (toplantı tarihi/yeri, gündem, çağrı usulü, katılımcı listesi, nisap, kararlar, imza) |

## Kurulum

```bash
claude plugin install ticaret-sirketler@turkiye-legal
```

## Dürüstlük notu

TTK m.414 çağrı süresi (2 hafta) ve m.418/m.421 toplantı-karar nisapları (olağan genel kurul 1/4, esas sözleşme değişikliği 1/2 → ikinci toplantıda 1/3) 2026-08-17 tarihinde bağımsız kaynaklarla doğrulandı ve skill'e eklendi. Kapsam dışı kalan tek nokta: işletme konusu değişikliği/tasfiye gibi özel hâllerde m.421'in ötesindeki ağırlaştırılmış nisaplar — bunlar hâlâ `good-first-legal-issue`'dur.
