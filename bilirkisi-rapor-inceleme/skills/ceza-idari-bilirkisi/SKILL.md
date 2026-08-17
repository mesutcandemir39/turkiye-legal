---
argument-hint: ''
description: Bilirkişi raporu ceza muhakemesinden (CMK) veya idari yargıdan (İYUK)
  geliyorsa, bu kollara özgü usul kuralları, ATK ve rapora karşı savunma/itiraz olanaklarını
  değerlendirmek istendiğinde kullanılır.
name: ceza-idari-bilirkisi
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  - ad: Sağlık Turizmi Kanunu
    numara: '6754'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Ceza ve İdari Yargıda Bilirkişi Raporu

## Görev
Hukuk yargılamasından farklı işleyen ceza ve idari yargı kollarındaki bilirkişi rejimini denetlemek: CMK m.62-73 ve İYUK m.31 yollamasıyla HMK kurallarını doğru uygulayıp rapora karşı savunma/itirazı kurmak.

## Soğuk başlangıç (intake)
- Rapor ceza dosyasından mı (soruşturma/kovuşturma) yoksa idari yargıdan mı geliyor?
- Ceza dosyasında rapor resmî bilirkişiden mi, ATK'dan mı, yoksa özel uzmandan mı?
- İdari davada bilirkişi keşfi/incelemesi yapıldı mı?
- Rapor aleyhe ve hangi noktada hatalı?

## Denetim şeması
1. **Ceza muhakemesi (CMK m.63-67):** Bilirkişi atanması, görev kapsamı ve rapor içeriği CMK m.67'ye göre denetlenir; çözümü uzmanlığı gerektiren hâllerde başvurulur. Bilirkişi hukuki sorunda görüş veremez. Taraflar uzman mütalaası (CMK m.67/son ve m.178 kapsamında) sunarak rapora karşı koyabilir.
2. **ATK raporları:** Adli Tıp Kurumu raporlarına da itiraz edilebilir; rapora karşı bilimsel/yöntemsel itiraz, üst kurul/yeni inceleme talebiyle desteklenir. ATK raporu da hâkimi mutlak bağlamaz.
3. **İdari yargı (İYUK m.31):** İYUK; bilirkişi, keşif ve delil tespitinde HMK'ya yollar. Bu nedenle HMK m.266-282 denetim mantığı idari davada da geçerlidir; rapora itiraz HMK m.281 çerçevesinde sunulur.
4. **Uzmanlık alanı sınırı (6754 s.K. m.3):** Her üç kolda da alan dışı ve hukuki nitelendirme içeren görüş itiraz sebebidir.
5. **Ara sonuç:** Yargı koluna göre doğru usul kuralı seçilir; rapora karşı uygun araç (itiraz, uzman mütalaası, yeni/ek inceleme) belirlenir.

## Çıktı modülleri
- Yargı koluna göre uygulanacak usul kuralları haritası (CMK / İYUK→HMK).
- Rapora karşı kullanılabilecek araçların listesi (itiraz / uzman mütalaası / yeni inceleme).
- ATK/resmî rapor için özel itiraz notları.
- Kola uygun itiraz/savunma paragrafı taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

