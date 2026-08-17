---
argument-hint: ''
description: İYUK'a uygun iptal/tam yargı dava dilekçesi, savunmaya cevap ve diğer
  layihaların hazırlanmasında kullanılır; dilekçenin zorunlu unsurları, talep sonucu
  ve delil bağlama disiplini gerektiğinde başvuru
name: dilekce-ve-layiha-taslagi
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
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dava Dilekçesi ve Layiha Taslağı

## Görev
İYUK m.3 ve m.5'e uygun, zorunlu unsurları eksiksiz, vakıa-hukuki sebep-talep mimarisi oturmuş bir dava dilekçesi veya layiha taslağı üretmek; bilinmeyen bilgileri [doldurulacak] yer tutucusuyla işaretlemek.

## Soğuk başlangıç (intake)
- Davacı ve davalı idare kim; işlemin tarih/sayısı nedir?
- Talep iptal mi, tam yargı mı, her ikisi mi; tazminat tutarı belirli mi?
- YD talep edilecek mi?
- Eldeki deliller (işlem örneği, tebliğ belgesi, yazışmalar) neler?

## Denetim şeması
1. **Zorunlu unsurlar** (İYUK m.3): Tarafların ad-soyad/unvan ve adresleri, davanın konusu ve sebepleri ile dayandığı deliller, dava konusu işlemin yazılı bildirim tarihi, vergi davalarında ihbarnamenin tarih ve numarası gibi bilgiler. Eksik dilekçe m.15/1-d uyarınca reddedilebilir.
2. **Aynı dilekçeyle birden çok işlem** (İYUK m.5): Aralarında maddi/hukuki bağlılık ya da sebep-sonuç ilişkisi bulunan birden fazla işlem aynı dilekçeyle dava edilebilir; birden fazla kişi müşterek dilekçeyle dava açabilir.
3. **Vakıa-hukuki sebep-talep**: Olaylar kronolojik ve sade; hukuki sebepler iptalde beş unsura, tam yargıda sorumluluk-illiyet-zarara bağlanır; talep sonucu net (işlemin iptali / belirli tutarda tazminat / YD).
4. **Delil bağlama**: Her iddianın yanına dayandığı belge eklenir; resen araştırma ilkesine güvenmeden temel belgeler sunulur. İdaredeki belgeler için mahkemeden getirtilmesi talep edilir.
5. **Islah/talep artırımı** (İYUK m.16/4): Tam yargıda bilirkişi sonrası talep ıslahla bir kez artırılabilir; dilekçede bu hak saklı tutulur.
6. **Ara sonuç — usul disiplini**: Harç, dilekçe sayısı (davalı sayısı + 1 nüsha esprisi UYAP'ta elektronik karşılığıyla) ve süre bilgileri kontrol edilir; uydurma esas/karar no'ya yer verilmez, içtihat ilkesel atıfla ve [DOĞRULANMADI] işaretiyle anılır.

## Çıktı modülleri
- Başlık, taraflar, konu, açıklamalar, hukuki sebepler, deliller, talep sonucu bölümleriyle tam taslak
- YD talep paragrafı (gerekirse)
- Eksik bilgi/[doldurulacak] listesi ve ekler dizini



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

