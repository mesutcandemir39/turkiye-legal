---
argument-hint: ''
description: Ceza infaz kurumu işlem ve kararlarına karşı infaz hâkimliğine şikâyet,
  süre, görev-yetki ve itiraz mercii yolunu kurgulamak gerektiğinde kullanılır.
name: infaz-hakimligi-basvuru
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
  - ad: Ceza ve Güvenlik Tedbirlerinin İnfazı Hakkında Kanun
    numara: '5275'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İnfaz Hâkimliğine Başvuru ve İtiraz

## Görev
İnfaz kurumu idaresinin işlem ve kararlarına ya da infaz savcılığı uygulamalarına karşı 4675 sayılı İnfaz Hâkimliği Kanunu yolunu doğru biçimde işletmek.

## Soğuk başlangıç (intake)
- Hangi işlem/karar şikâyet konusu (disiplin, nakil, infaz hesabı, hak kısıtlaması)?
- İşlem hükümlüye ne zaman tebliğ/uygulanıp öğrenildi (süre için)?
- Hangi infaz kurumu/savcılık yetki alanındasınız (yetki için)?
- Daha önce idareye başvuru yapıldı mı?

## Denetim şeması
1. Görev: 4675 sayılı Kanun m.4 uyarınca infaz kurumu idaresinin işlem ve eylemlerine ilişkin şikâyetleri infaz hâkimliği inceler; ceza yargılamasıyla ilgili olmayan, infaza özgü uyuşmazlıklar bu yola tabidir. Ara sonuç: konu infaz hâkimliği görevinde mi?
2. Süre: şikâyet, işlemin öğrenildiği tarihten itibaren kanunda öngörülen süre içinde (4675 m.5) yapılmalıdır; sürenin kaçırılması başvuruyu usulden reddettirir. İspat yükü: süreye uygunluğu başvurucu, aksini idare ortaya koyar.
3. Yetki: hükümlünün bulunduğu infaz kurumunun yargı çevresindeki infaz hâkimliği yetkilidir.
4. İnceleme ve karar: infaz hâkimi dosya üzerinden inceler, gerekirse bilgi/belge ister; kabul, ret veya işlemin iptaline karar verir (4675 m.6).
5. İtiraz: infaz hâkimliği kararına karşı ağır ceza mahkemesine (CMK itiraz hükümleri çerçevesinde) itiraz yolu açıktır (4675 m.6). Ara sonuç: itiraz mercii ve süresi.
6. İlkesel içtihat: görev sınırı ve süre başlangıcı için karararama.yargitay.gov.tr; tutulma koşulları ihlalinde AYM bireysel başvuru (kararlarbilgibankasi.anayasa.gov.tr). Künye `[DOĞRULANMADI]`.
7. Ara sonuç: görev/yetki/süre üçlüsü + başvuru stratejisi.

## Çıktı modülleri
- Görev-yetki-süre kontrol çizelgesi.
- Şikâyet dayanak listesi.
- İnfaz hâkimliği şikâyet ve itiraz dilekçesi tetiği.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

