---
argument-hint: ''
description: İş ilişkisi sona ererken ibraname, çalışma belgesi, SGK çıkış, gizlilik/rekabet
  yasağının devamı ve çıkış görüşmesi belgelerinin hazırlanması gerektiğinde kullanılır.
name: cikis-ibra-ve-rekabet-sonrasi
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Çıkış İşlemleri, İbraname ve Rekabet Sonrası

## Görev
İş ilişkisinin sonlanmasında tüm çıkış belgelerini hukuka uygun ve geçerli biçimde üretmek; özellikle ibranamenin geçerlilik şartlarını ve fesih sonrası rekabet/gizlilik yükümlülüklerini güvence altına almak.

## Soğuk başlangıç (intake)
1. Fesih kim ve hangi sebeple yapıldı, çıkış tarihi nedir?
2. Ödenecek alacaklar net mi, banka üzerinden mi ödenecek?
3. Sözleşmede rekabet yasağı/gizlilik kaydı var mı, devam edecek mi?
4. Çalışma belgesi, SGK çıkış bildirimi ve referans talebi var mı?

## Denetim şeması
1. **İbraname geçerlilik şartları (TBK m.420)**: İbra sözleşmesi **yazılı**, fesihten **en az 1 ay sonra** tarihli, alacak türü-tutarı açıkça belirtilmiş ve ödemenin **banka aracılığıyla** yapılmış olması gerekir. Bu şartları taşımayan ibra **kesin hükümsüz**; tam ödeme içermeyen belge makbuz hükmündedir.
2. **Çalışma belgesi (4857 m.28)**: İşveren, istek halinde işin türü ve süresini gösteren belgeyi vermek zorunda; gerçeğe aykırı belge sorumluluk doğurur.
3. **SGK çıkış (5510)**: İşten ayrılış bildirgesi süresinde verilmeli; gecikme idari para cezası doğurur.
4. **Rekabet yasağının devamı (TBK m.444-447)**: Yasağın fesihten sonra işlemesi için geçerlilik şartları (yer-zaman-konu sınırı, korunmaya değer menfaat) sürmeli; işveren haklı sebep olmadan feshederse veya işçi işverenin kusuruyla haklı feshederse **rekabet yasağı sona erer (m.447/2)**.
5. **Gizlilik**: Sözleşmesel gizlilik ve sır saklama borcu iş ilişkisi sonrası da sürebilir; süre ve kapsam makul olmalı.
6. **Ara sonuç**: Erken tarihli/elden ödemeli ibra geçersiz → dava riski; rekabet yasağının ayakta olup olmadığı fesih şekline bağlı.

## Çıktı modülleri
- Geçerli ibraname taslağı (1 ay + banka ödemesi notlu).
- Çalışma belgesi ve çıkış görüşmesi tutanağı taslağı.
- Rekabet/gizlilik yükümlülüğü hatırlatma yazısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

