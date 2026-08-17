---
argument-hint: ''
description: Loglar, imajlar, e-posta, mesaj kayıtları gibi dijital delillerin hukuka
  uygun elde edilmesi, bütünlüğünün korunması ve mahkemede değerlendirilebilirliğini
  denetlemek gerektiğinde kullanılır.
name: dijital-delil-elde-etme-degerlendirme
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Elektronik Ticaretin Düzenlenmesine Dair Kanun
    numara: '5651'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dijital Delilin Elde Edilmesi ve Değerlendirilmesi

## Görev
Dijital delillerin hukuka uygun şekilde elde edilip edilmediğini, bütünlük zincirinin korunup korunmadığını ve yargılamada değerlendirilebilirliğini denetlemek; itiraz veya delil tespiti stratejisi kurmak.

## Soğuk başlangıç (intake)
1. Hangi dijital delil? (log, disk imajı, e-posta, WhatsApp/mesaj, ekran görüntüsü?)
2. Nasıl elde edildi? (CMK m.134 kararıyla mı, taraf rızasıyla mı, tek taraflı mı?)
3. Bütünlük korundu mu? (hash, imaj, zaman damgası, gözetim zinciri var mı?)
4. Delil kim aleyhine ve hangi yargılamada (ceza/hukuk) kullanılacak?

## Denetim şeması
1. **Elde etme yetkisi.** Ceza yargılamasında bilgisayar, program ve kütüklerde arama, kopyalama ve elkoyma CMK m.134'e tabidir: kural olarak hâkim kararı, sistemdeki verilerin yedeklenmesi ve istem halinde bir kopyasının ilgiliye verilmesi gerekir. Genel arama-elkoyma rejimi (CMK m.116-123) tamamlayıcıdır.
2. **Hukuka aykırı delil yasağı.** Hukuka aykırı elde edilen delil hükme esas alınamaz (Anayasa m.38/6; CMK m.206/2-a, m.217/2, m.230/1). Özel hayata/haberleşmeye müdahale ile elde edilen kayıtlar TCK m.132-134 kapsamında ayrıca suç oluşturabilir; bir suçun işlendiğini gösteren tesadüfen elde edilmiş kayıtların durumu ayrıca değerlendirilir.
3. **Bütünlük ve zincir.** İmaj alma, hash (özet) değeri, zaman damgası ve gözetim zinciri (chain of custody) belgelenmelidir; bütünlüğü ispatlanamayan delilin değeri tartışmalıdır. Ekran görüntüsü/mesaj çıktısı tek başına zayıf delildir, teknik doğrulama ile desteklenmelidir.
4. **Hukuk yargılamasında.** HMK uyarınca senet/belge ve diğer deliller rejimi (HMK m.199 belge tanımı elektronik verileri kapsar) ile delil tespiti (HMK m.400 vd.) yolları kullanılır. **İspat yükü** delili sunan taraftadır; karşı taraf bütünlük ve hukuka uygunluk itirazını ileri sürer.
5. **Ara sonuç.** Delilin elde edilme usulü, bütünlüğü ve değerlendirilebilirliği; itiraz veya delil tespiti talebi gerekli mi belirlenir.

## Çıktı modülleri
- Delil değerlendirme tablosu (kaynak, yetki, bütünlük, hukuka uygunluk).
- Hukuka aykırılık/itiraz dilekçesi iskeleti.
- Delil tespiti veya bilirkişi (adli bilişim) talebi taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

