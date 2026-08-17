---
argument-hint: ''
description: Davanın doğru mahkemede ve doğru taraflara karşı açılıp açılmadığını;
  görev, yetki, sıfat ve dava şartlarını denetlemek gerektiğinde kullanılır.
name: gorev-yetki-husumet
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
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Görev, Yetki ve Husumet Denetimi

## Görev
Layihayı yazmadan önce davanın doğru mahkemede, doğru davalıya karşı ve dava şartları sağlanarak açıldığını denetlemek. Görev ve dava şartları kamu düzenindendir; eksikse esasa girilmeden dava reddedilir.

## Soğuk başlangıç (intake)
- Talep konusu ve değeri nedir? (görevli mahkemeyi belirler)
- Davalının yerleşim yeri / işlemin yapıldığı yer / ifa yeri neresi?
- Taraflar doğru tespit edildi mi (gerçek/tüzel kişi, temsil)?
- Zorunlu arabuluculuk/idari başvuru gibi bir dava şartı var mı?

## Denetim şeması
1. Görev (HMK m.1-4): Görev kanunla belirlenir, kamu düzenindendir ve dava şartıdır (m.114/1-c). Asliye hukuk genel görevlidir; sulh hukukun görevi HMK m.4'te sayılıdır. Özel görevli mahkemeleri kontrol edin (tüketici, iş, ticaret, aile, fikri-sınai). İstisna: özel kanun aksini öngörebilir.
2. Yetki (HMK m.5-19): Genel yetki davalının yerleşim yeri (m.6). Özel yetki: sözleşmede ifa yeri (m.10), haksız fiilde m.16, taşınmazda kesin yetki m.12. Kesin yetki hâkimce re'sen gözetilir; kesin olmayan yetkiye ilk itiraz gerekir (m.116, m.117).
3. Sıfat/husumet (TMK m.6; HMK genel): Aktif/pasif husumet maddi hukuktan doğar; sıfat yokluğu esastan reddi gerektirir, dava şartı değildir.
4. Dava şartları (HMK m.114-115): Eksik dava şartı tamamlanabilir nitelikteyse süre verilir; değilse usulden ret. Zorunlu arabuluculuk (ör. ticari/işçi-işveren/tüketici uyuşmazlıkları) dava şartıdır; tutanak eklenmeli.
5. İdari yargıda: İYUK m.33-37 yetki kuralları; idari merci tecavüzü ve süre (m.11).
Ara sonuç: görev/yetki/şart sağlanmıyorsa düzeltme yolu (görevsizlik/yetkisizlik, gönderme) veya doğru mahkemeye yönlendirme.

## Çıktı modülleri
- Görevli ve yetkili mahkeme tespiti (madde gerekçeli)
- Taraf/husumet doğrulama tablosu
- Dava şartı kontrol listesi (arabuluculuk, harç, ehliyet)
- Eksiklik halinde düzeltme/yönlendirme önerisi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

