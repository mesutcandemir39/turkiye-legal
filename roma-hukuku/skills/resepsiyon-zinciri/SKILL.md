---
argument-hint: ''
description: Bir TMK veya TBK hükmünün İsviçre (ZGB/OR) ve Pandekt üzerinden Roma
  kökenine kadar geriye götürülmesi; iktibas sırasında yapılan değişikliklerin ve
  kavram dönüşümünün izi sürülecekse kullanılır.
name: resepsiyon-zinciri
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Resepsiyon Zinciri ve İsviçre Tesiri

## Görev
Yürürlükteki bir Türk özel hukuk normunu, resepsiyon zinciri boyunca (İsviçre ZGB/OR → Pandekt → Roma) geriye götürmek ve iktibas sürecinde yaşanan dönüşümleri tespit etmek.

## Soğuk başlangıç (intake)
- Hangi yürürlükteki madde inceleniyor (TMK m.X / TBK m.X)?
- 1926 metni (743/818) ile 2001/2011 metni (4721/6098) arasında fark gerekli mi?
- İsviçre kaynak maddesi (ZGB/OR) karşılaştırması isteniyor mu?
- Amaç salt köken mi, yoksa yorum argümanı üretmek mi?

## Denetim şeması
1. Yürürlükteki normu sabitle: TMK 4721 veya TBK 6098'deki madde ve fıkra. Örnek eksenler: TMK m.1 (yorum/boşluk), TMK m.2-3 (dürüstlük-iyiniyet), TMK m.683 (mülkiyet), TBK m.1 (icap-kabul), TBK m.49 (haksız fiil), TBK m.77 (sebepsiz zenginleşme).
2. Tarihî iktibas hattını kur: 4721 sayılı TMK, 1926 tarihli 743 sayılı Türk Kanunu Medenisi'nin; 6098 sayılı TBK ise 818 sayılı Borçlar Kanunu'nun halefidir. 743/818 ise İsviçre Medenî Kanunu (ZGB) ve İsviçre Borçlar Kanunu (OR) iktibasıdır.
3. İsviçre kaynağına bağla: ilgili ZGB/OR maddesini eşleştir; lafzî ve sistematik farkları işaretle (çeviri/uyarlama kaynaklı sapmalar dahil).
4. Pandekt katmanını ekle: 19. yüzyıl Alman Pandekt bilimi (Savigny, Windscheid) kavramı nasıl dogmatize etti; ZGB/OR bu birikimden nasıl beslendi.
5. Roma köküne in: kavramı Corpus Iuris Civilis'teki kuruma kadar götür (atıf: D./Inst./Gai.). Maxim varsa doğru Latince ile ver.
6. Dönüşümü ayrıştır: Roma'dan bugüne anlam kayması, kapsam genişlemesi/daralması veya yeni eklenen unsuru (ör. modern dürüstlük kuralının objektifleşmesi) açıkça yaz. Ara sonuç: zincirin her halkasında neyin korunduğunu, neyin değiştiğini tablola.

İspat/dayanak: yürürlükteki norm madde ile; tarihî kanunlar numara ile (743, 818); Roma kaynağı fragmanla; doktrin künyesi [DOĞRULANMADI].

## Çıktı modülleri
- Resepsiyon zinciri tablosu: TMK/TBK → ZGB/OR → Pandekt → Roma.
- 1926 ile güncel metin farkları notu.
- Dönüşüm/sapma listesi.
- Yorum argümanına dönüştürme önerisi (tarihî-sistematik, TMK m.1).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

