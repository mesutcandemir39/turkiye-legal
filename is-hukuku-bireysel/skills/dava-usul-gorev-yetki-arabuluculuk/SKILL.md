---
argument-hint: ''
description: İş uyuşmazlığında dava şartı arabuluculuk, görevli ve yetkili mahkeme,
  harç-yargılama usulü ve dava açma adımları gerektiğinde; işçilik alacağı veya işe
  iade davasının usul iskeletini kurmak için kull
name: dava-usul-gorev-yetki-arabuluculuk
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
  - ad: İş Kanunu
    numara: '4857'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dava, Usul, Görev-Yetki ve Zorunlu Arabuluculuk

## Görev
İş uyuşmazlığını doğru usul rejimine oturtmak: zorunlu arabuluculuk, görev-yetki, yargılama usulü ve dava açılış adımlarını belirlemek.

## Soğuk başlangıç (intake)
1. Talep konusu nedir (işçilik alacağı, işe iade, hizmet tespiti, tazminat)?
2. İşyeri ve işverenin adresi nerede; işçi işi nerede gördü?
3. Fesih/dava açma tarihleri ve süre durumu nedir?
4. Daha önce arabuluculuğa başvuruldu mu?

## Denetim şeması
1. **Dava şartı arabuluculuk (7036 m.3):** İşçi-işveren arasındaki kıdem, ihbar, fazla çalışma, ücret, yıllık izin gibi alacak ve tazminat talepleri ile işe iade davaları için arabuluculuk **dava şartıdır**. İş kazası/meslek hastalığından kaynaklı maddi-manevi tazminat ve bunlara ilişkin rücu davaları kapsam dışı (bunlar için ihtiyaridir). Başvuru olmadan açılan dava, dava şartı yokluğundan usulden reddedilir.
2. **Görev (7036 m.5):** İş mahkemeleri görevlidir; iş mahkemesi yoksa o yer asliye hukuk mahkemesi iş mahkemesi sıfatıyla bakar.
3. **Yetki (7036 m.6):** Davalı gerçek/tüzel kişinin davanın açıldığı tarihteki yerleşim yeri ile işin/işlemin yapıldığı yer mahkemesi yetkilidir; bu yetki kesindir (aksine sözleşme yapılamaz).
4. **Usul:** İş mahkemelerinde kural olarak **basit yargılama usulü** uygulanır (HMK m.316 vd.); dilekçeler dilekçe-cevap ile sınırlıdır, ön inceleme ve tahkikat hızlandırılmıştır.
5. **Ara sonuç:** Önce arabuluculuk → son tutanak → süresinde dava (işe iadede 2 hafta). Dava dilekçesine son tutanağın aslı/onaylı örneği eklenmezse bir haftalık kesin süre verilir; eklenmezse dava usulden reddedilir.
6. **Faiz ve talep:** Alacak türüne göre faiz türü (mevduat/yasal) ve başlangıcı talep sonucunda doğru gösterilir; belirsiz alacak/kısmi dava tercihi değerlendirilir.

## Çıktı modülleri
- Arabuluculuk kapsam kontrolü (zorunlu/ihtiyari).
- Görevli ve yetkili mahkeme tespiti.
- Süre takvimi ve dava açılış kontrol listesi.
- Faiz/talep türü ve dava türü (belirsiz alacak vb.) önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

