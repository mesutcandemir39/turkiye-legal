---
argument-hint: ''
description: Bir uyuşmazlığın konu itibarıyla tahkime veya arabuluculuğa elverişli
  olup olmadığını, kamu düzeni ve emredici hükümler süzgecinden geçirerek belirlemek
  gerektiğinde kullanılır.
name: tahkime-elverislilik-kapsam
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


# Tahkime ve Arabuluculuğa Elverişlilik

## Görev
Uyuşmazlığın alternatif çözüm yoluna konu edilip edilemeyeceğini kapı eşiğinde
belirlemek. Elverişsiz bir konu için kurulan tahkim/arabuluculuk emek ve süre kaybı
doğurur; bu süzgeç en başta uygulanır.

## Soğuk başlangıç (intake)
1. Uyuşmazlık konusu nedir (ayni hak, statü, alacak, idari işlem)?
2. Taraflar bu hak üzerinde serbestçe tasarruf edebilir mi?
3. Konu bir kamu düzeni alanına mı (boşanma statüsü, ceza, vergi tarhı) giriyor?
4. Hedef yol tahkim mi arabuluculuk mu?

## Denetim şeması
1. **Tahkim elverişliliği**: **HMK m.408** — taşınmaz üzerindeki **ayni haklara** ilişkin
   ve **iki tarafın iradesine tabi olmayan** uyuşmazlıklar tahkime elverişsizdir.
   Milletlerarası tahkimde de aynı çekirdek geçerlidir (**MTK m.1/4**).
2. **Arabuluculuk elverişliliği**: **HUAK m.1/2** — tarafların üzerinde serbestçe
   tasarruf edebileceği işler. **Aile içi şiddet** iddiası içeren uyuşmazlıklar
   arabuluculuğa elverişsizdir.
3. **Kamu düzeni/emredici hüküm süzgeci**: Boşanma/soybağı gibi **statü** belirleyen
   davalar, ceza yargılaması, idari/vergi uyuşmazlıkları kural olarak dışlanır.
   Tahkim/arabuluculuk yalnızca tarafların tasarrufundaki **maddi sonuçları** (ör. nafaka
   miktarı değil ama mal rejimi tasfiyesindeki alacak gibi tasarruf edilebilir kısımlar)
   yönünden mümkün olabilir; sınır dikkatle çizilir.
4. **Karma uyuşmazlık**: Bir kısmı elverişli bir kısmı değilse ayrıştırma yapılır;
   elverişli kısım tahkim/arabuluculuğa, diğeri devlet yargısına yönlendirilir.
5. **Ara sonuç**: Elverişlilik kararı, dayanak madde ve istisna notu.

## Çıktı modülleri
- Elverişlilik karar tablosu (konu-yol-dayanak-istisna).
- Karma uyuşmazlık ayrıştırma haritası.
- Devlet yargısına yönlendirme gerekiyorsa görev/yetki kısa notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

