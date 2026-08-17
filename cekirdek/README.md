# cekirdek

**Kademe:** Tier 0 — Temel (diğer tüm plugin'ler buna dayanır)

Bu plugin, kullanıcıya doğrudan hitap eden bir hukuk alanı değildir; tüm `turkiye-legal` plugin'lerinin paylaştığı ortak altyapıdır.

## İçerik

| Tür | Ad | Ne yapar |
|---|---|---|
| Skill | `sure-hesapla` | HMK'ya tabi bir sürenin adli tatil (m.102, m.104) nedeniyle uzayıp uzamadığını deterministik olarak hesaplar |
| Skill | `veri-maskeleme` | T.C. kimlik (checksum doğrulamalı), IBAN, telefon, e-posta, kart numarası gibi biçimsel kişisel verileri modele gitmeden önce maskeler |
| Skill | `surum-kontrolu` | Kurulu sürümü GitHub'daki en son Stable Release ile karşılaştırır; güncelleme varsa çalıştırmayı dener — davranış oturumun izin moduna göre değişir (ADR-011); istenirse haftalık otomatik kontrol için zamanlanmış görev kurulumu da sunar (ADR-012) |
| Referans | `kaynak_hiyerarsisi.md` | Anayasa → Kanun → ... → Doktrin sıralaması, İBK/daire kararı ayrımı |
| Referans | `dogrulanmadi_protokolu.md` | Model kendi bilgisinden konuştuğunda `[DOĞRULANMADI]` etiketleme kuralı |
| Referans | `sure_kurallari.yaml` | Süre hesaplayıcının dayandığı, kaynak atıflı kural tablosu |
| Script | `sure_hesapla.py` | `sure-hesapla` skill'inin çağırdığı deterministik Python hesaplayıcı |
| Script | `veri_maskele.py` | `veri-maskeleme` skill'inin çağırdığı deterministik Python maskeleyici (15 birim testle doğrulandı) |
| Script | `surum_kontrol.py` | `surum-kontrolu` skill'inin çağırdığı, GitHub Releases API'sine karşı çalışan sürüm karşılaştırıcı (10 birim testle doğrulandı) |

## Kurulum

```bash
claude plugin install cekirdek@turkiye-legal
```

Diğer plugin'ler `cekirdek`'i otomatik varsayım olarak referans alır; ayrıca kurmanıza gerek kalmadan da `sure_hesapla.py` diğer skill'ler tarafından çağrılabilir.

Detay: ``CREDITS.md`` ADR-006.
