---
argument-hint: ''
description: Birden çok kişiye ait taşınmazda paydaşlar arası uyuşmazlık, payın devri,
  yönetim, ortaklığın aynen taksim veya satış yoluyla giderilmesi (izale-i şuyu) söz
  konusu olduğunda; paylı ile elbirliği mülki
name: paylasma-ve-ortakligin-giderilmesi
turkiye_legal:
  attribution:
    license: Apache-2.0
    original_author: Mesut Can Demir
    original_repository: https://github.com/mesutcandemir39/turkiye-legal
  category: litigation
  inputs:
  - '[giriş tanımlanmadı — beceri gövdesinden çıkarılacak]'
  jurisdiction:
    country: TR
    legal_system: civil_law
    scope:
    - TR
  outputs:
  - '[çıktı tanımlanmadı — beceri gövdesinden çıkarılacak]'
  requires_human_review: false
  risk_level: medium
  sources:
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  - ad: Tapu Kanunu
    numara: '3402'
    tur: kanun
  - ad: Kat Özel Koşulu Olmak Üzere Yapılan Satış Mukavelelerine Dair Kanun
    numara: '2644'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Paylı/Elbirliği Mülkiyet ve Ortaklığın Giderilmesi

## Görev
Ortak mülkiyet türünü belirlemek, paydaşların yetki ve yükümlülüklerini saptamak ve ortaklığın giderilmesini (aynen taksim/satış) doğru usulle yürütmek.

## Soğuk başlangıç (intake)
- Mülkiyet türü: paylı (müşterek) mı, elbirliği (iştirak/tereke) mi?
- Talep: payın devri, yönetim/kullanım, önalım, ortaklığın giderilmesi mi?
- Aynen taksim mümkün mü (yüzölçüm, imar, bölünebilirlik) yoksa satış mı gerekecek?
- Yasal önalım hakkı kullanılacak bir pay devri var mı; süre işliyor mu?

## Denetim şeması
1. **Mülkiyet türünü ayır.** Paylı mülkiyette her paydaşın belirli bir payı vardır, payını serbestçe devredebilir (TMK m.688-689). Elbirliği mülkiyette pay belirsizdir, tasarruf oybirliği gerektirir (TMK m.701-703); tereke önce paylı mülkiyete çevrilmeden tek tek pay devri yapılamaz.
2. **Yönetim/kullanımı çöz.** Olağan yönetim çoğunluk, önemli işler ve tasarruf nitelikli kararlar nitelikli çoğunluk/oybirliği (TMK m.690-692). Paydaş giderlere payı oranında katlanır (TMK m.694).
3. **Yasal önalımı denetle.** Paylı mülkiyette paydaş, payın üçüncü kişiye satışında yasal önalım hakkını kullanabilir (TMK m.732-733); satışın bildiriminden 3 ay ve her halde 2 yıl içinde dava (TMK m.733/3) hak düşürücü süresi. Önalım davası alıcıya karşı açılır.
4. **Ortaklığın giderilmesini planla.** Her paydaş paylaşmayı isteyebilir (TMK m.698); öncelik aynen taksim (TMK m.699), bölünemiyorsa satış suretiyle (açık artırma) giderilir. Paylaşmayı engelleyen sözleşme/amaç (en çok 10 yıl) ve uygun olmayan zaman istisnası gözetilir.
5. **Usul.** Ortaklığın giderilmesi davası sulh hukuk mahkemesinde (HMK m.4) görülür; tüm paydaşlar davaya dahil edilir (zorunlu dava arkadaşlığı). Aynen taksimde fen ve kıymet bilirkişisi.
6. **Ara sonuç.** Aynen taksim mi satış mı, önalım süresi, husumet çevresi netleştirilir.

## Çıktı modülleri
- Mülkiyet türü–yetki–talep tablosu.
- Önalım veya ortaklığın giderilmesi dava dilekçesi iskeleti.
- Aynen taksim/satış fizibilitesi ve önalım hak düşürücü süre notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

