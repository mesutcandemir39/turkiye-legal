---
argument-hint: ''
description: İş, ticari, tüketici, kira ve benzeri uyuşmazlıklarda dava açmadan önce
  zorunlu arabuluculuk başvurusunu yönetmek; kapsam, süre ve son tutanak sonrası dava
  açma adımını belirlemek gerektiğinde kullanı
name: dava-sarti-arabuluculuk
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
  - ad: Şehircilik ve Şehir Plancılarının Statüsü Hakkında Kanun
    numara: '4686'
    tur: kanun
  - ad: Hukuk Uyuşmazlıklarında Arabuluculuk Kanunu
    numara: '6325'
    tur: kanun
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dava Şartı (Zorunlu) Arabuluculuk

## Görev
Dava açmadan önce arabuluculuğun zorunlu olduğu uyuşmazlıklarda kapsamı, süreyi ve son
tutanaktan sonraki dava açma penceresini doğru yönetmek. Arabulucuya başvurmadan açılan
dava **usulden reddedilir**; bu beceri o riski engeller.

## Soğuk başlangıç (intake)
1. Uyuşmazlık iş, ticari, tüketici, kira/komşu/kat mülkiyeti gibi zorunlu bir alana mı
   giriyor?
2. Alacak/talep türü nedir (ör. işçilik alacağı, ticari alacak, tahliye)?
3. Daha önce arabuluculuğa başvuruldu mu, son tutanak alındı mı?
4. Anlaşmama halinde dava açma süresi ne zaman doluyor?

## Denetim şeması
1. **Kapsam belirleme**: İş uyuşmazlıkları **7036 m.3** (işçi-işveren alacak/tazminat ve
   işe iade); ticari uyuşmazlıklar **TTK m.5/A** (konusu para alacağı/tazminat olan ticari
   davalar); tüketici **TKHK m.73/A**; kira, taşınır/taşınmaz paylaştırma ve ortaklığın
   giderilmesi, komşu hukuku, kat mülkiyeti **HUAK m.18/B**. İş kazası/meslek hastalığından
   maddi-manevi tazminat ve tespit istisnası gözetilir.
2. **Zamanaşımı/hak düşürücü süre**: Arabuluculuk başvurusu **zamanaşımını durdurur, hak
   düşürücü süreyi işlemez kılar** (**HUAK m.18/A-15**). Bu koruma başvuru tarihinden son
   tutanağa kadar sürer.
3. **Yetki ve atama**: Başvuru, karşı tarafın yerleşim yeri/işin yapıldığı yer adliyesi
   arabuluculuk bürosuna yapılır; arabulucu komisyonca atanır (**HUAK m.18/A**).
4. **Anlaşmama ve dava açma**: Anlaşmama son tutanağının düzenlendiği tarihten itibaren
   **2 hafta** içinde dava açılmalı; aksi halde tekrar arabuluculuk şarttır. Dava
   dilekçesine son tutanağın aslı/örneği eklenmezse mahkeme **1 haftalık kesin süre**
   verir, sunulmazsa dava şartı yokluğundan usulden reddedilir (**HUAK m.18/A-2**).
5. **Ara sonuç**: Kapsam teyidi, süre takvimi ve eksik belge listesi.

## Çıktı modülleri
- Kapsam/istisna kontrol tablosu (alan-madde eşleştirmesi).
- Arabuluculuk başvuru dilekçesi taslağı.
- Son tutanak sonrası 2 haftalık dava açma takvimi ve hatırlatma notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

