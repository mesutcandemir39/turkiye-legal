---
argument-hint: ''
description: İdari yaptırım kararına karşı sulh ceza hâkimliğine başvuru ve itiraz
  yolunun usulünü, sürelerini, görev-yetkisini ve karar türlerini yönetmek; başvuru/itiraz
  dilekçesinin yol haritasını kurmak gerekt
name: basvuru-yolu-sulh-ceza
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
  - ad: Kabahatler Kanunu
    numara: '5326'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Sulh Ceza Hâkimliğine Başvuru ve İtiraz

## Görev
İdari yaptırım kararına karşı 5326 m.27-29 usulünü işletmek: doğru merci, süre, dilekçe içeriği ve itiraz yolunu belirlemek.

## Soğuk başlangıç (intake)
- Yaptırım kararı ne zaman tebliğ/tefhim edildi (süre başlangıcı)?
- Kararı veren idare ve kararın bulunduğu yer neresi (yetkili hâkimlik)?
- Karar yalnızca idari para cezası mı, yoksa idari yargının görev alanına giren bir işlemle birlikte mi verildi?
- Daha önce idareye itiraz/başvuru yapıldı mı?

## Denetim şeması
1. **Görevli merci:** İdari yaptırım kararına karşı kural olarak **sulh ceza hâkimliği** görevlidir (5326 m.27/1). İstisna: yaptırım, idari yargının görev alanına giren bir işlemin parçasıysa idari yargı görevlidir (m.27/8). Bu ayrımı en baştan netleştir.
2. **Yetkili hâkimlik:** Yaptırım kararını veren idarenin bulunduğu yer sulh ceza hâkimliği (m.27/1).
3. **Süre:** Kararın tebliği/tefhiminden itibaren **15 gün** içinde başvuru (m.27/1). Süre hak düşürücüdür; mücbir sebep halinde m.27/2'deki imkân değerlendirilir.
4. **Başvuru dilekçesi:** Kabahatin sübutuna, kusura, miktara, yetki/şekil sakatlığına ve zamanaşımına ilişkin somut iddialar; deliller ve tanık listesi. Harç/masraf rejimi kontrol edilir.
5. **İnceleme ve karar:** Hâkimlik dosya üzerinden veya duruşmalı inceleyebilir; başvurunun kabulü (kararın kaldırılması/değiştirilmesi) ya da reddine karar verir (m.28).
6. **İtiraz (m.29):** Hâkimlik kararına karşı, belirli ceza eşiklerinde, tebliğden itibaren **7 gün** içinde bir başka (numara olarak izleyen) sulh ceza hâkimliğine itiraz; itiraz mercii kararı kesindir. Eşik altı cezalarda hâkimlik kararı kesin olabilir; tutar eşiğini kontrol et.

İspat yükü idarede; başvurucu sakatlık ve çürütücü delilleri ileri sürer.

## Çıktı modülleri
- Süre ve merci tespit kartı.
- Başvuru dilekçesi iskeleti (talep sonucu + gerekçe + deliller).
- İtiraz yolu/eşik kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

