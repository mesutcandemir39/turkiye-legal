# cekirdek — Plugin Profili

`cekirdek`, bir büroya özgü bir plugin değildir; diğer tüm `turkiye-legal` plugin'lerinin dayandığı **paylaşılan altyapıdır.** Bu yüzden diğer plugin'lerdeki gibi bir "cold-start büro profili mülakatı" içermez.

## Bu plugin ne sağlar

1. **[Kaynak hiyerarşisi](references/kaynak_hiyerarsisi.md)** — Anayasa → Kanun → ... → Doktrin sıralaması ve İBK/daire kararı ayrımı.
2. **[`[DOĞRULANMADI]` protokolü](references/dogrulanmadi_protokolu.md)** — model kendi bilgisinden konuştuğunda nasıl işaretleneceği.
3. **[Süre kuralları tablosu](references/sure_kurallari.yaml)** ve **[`sure_hesapla.py`](scripts/sure_hesapla.py)** — deterministik adli tatil hesaplayıcı (bkz. `skills/sure-hesapla/SKILL.md`).

## Diğer plugin'ler bunu nasıl kullanır

Herhangi bir `turkiye-legal` skill'i:
- Hukuki bir iddiada bulunmadan önce `references/kaynak_hiyerarsisi.md`'deki sıralamaya uyar,
- Doğrulanmamış bir bilgi paylaşırken `references/dogrulanmadi_protokolu.md`'deki formatı kullanır,
- Bir tarih/süre hesabı gerektiğinde kendi aritmetiğini yapmak yerine `cekirdek/scripts/sure_hesapla.py`'yi çağırır.

Bu üç kural, `.claude/CLAUDE.md`'deki repo-genelindeki mutlak sınırların somutlaştırılmış hâlidir.
