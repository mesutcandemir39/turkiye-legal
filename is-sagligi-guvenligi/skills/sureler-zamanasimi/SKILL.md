---
argument-hint: ''
description: İş kazası tazminatı, SGK rücuu, idari ceza itirazı, bildirim ve ceza
  yargılamasındaki süre ve zamanaşımlarını hesaplamak ve hak kaybını önlemek için
  kullanılır.
name: sureler-zamanasimi
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
  - ad: İş Sağlığı ve Güvenliği Kanunu
    numara: '6331'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler ve Zamanaşımı

## Görev
İSG dosyasındaki tüm süre ve zamanaşımlarını eksiksiz tespit etmek, başlangıç anlarını doğru belirlemek ve hak düşürücü riskleri uyarmak.

## Soğuk başlangıç (intake)
- Olay/kaza tarihi, zararın/maluliyetin öğrenildiği tarih (zamanaşımı başlangıcı için kritik)?
- İdari ceza/karar tebliğ tarihi?
- Bildirimler (SGK, kolluk) ne zaman yapıldı?
- Ceza yargılaması varsa fiilin tarihi ve suç tipi?

## Denetim şeması
1. **İş kazası tazminatı zamanaşımı:** İşçinin/hak sahiplerinin işverene karşı tazminat talebi sözleşmeye dayalı olduğundan kural olarak on yıllık zamanaşımına tabidir (TBK m.146); bedensel zararda zararın gelişimi ve maluliyetin kesinleşmesi başlangıcı etkiler. Ceza zamanaşımının daha uzun olduğu hallerde uzamış (ceza) zamanaşımı uygulanabilir (TBK m.72/1 son cümle). Güncel içtihatla doğrula.
2. **SGK rücu zamanaşımı:** Halefiyet/rücuun niteliğine göre belirlenir; başlangıç ve süre için karararama.yargitay.gov.tr içtihadını `[DOĞRULANMADI]` olarak teyit et, bellekten süre verme.
3. **İdari para cezasına itiraz (5326 m.27):** Tebliğden itibaren on beş gün; sulh ceza kararına itiraz da kısa süreli. Kabahat için soruşturma ve yerine getirme zamanaşımları (5326 m.20) ayrıca işler.
4. **Bildirim süreleri:** İş kazasının SGK'ya bildirimi kazadan sonraki üç iş günü içinde (5510 m.13/2); gecikme idari ceza ve rücu sonucu doğurur.
5. **Ceza zamanaşımı:** TCK m.66 dava zamanaşımı suç tipine göre. **Ara sonuç:** Her süreyi başlangıç anı + süre + bitiş tarihiyle tablola; en yakın tarihi öne çıkar.

## Çıktı modülleri
- Süre/zamanaşımı takvimi (başlangıç-süre-bitiş).
- Hak düşürücü/itiraz süreleri uyarı listesi.
- Doğrulanacak içtihat süreleri için kaynak notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

