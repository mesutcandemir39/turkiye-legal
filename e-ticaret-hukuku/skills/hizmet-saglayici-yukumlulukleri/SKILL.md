---
argument-hint: ''
description: Bir e-ticaret sitesinin veya satıcının 6563 kapsamındaki bilgi verme,
  sözleşme öncesi bilgilendirme ve sipariş sürecine ilişkin yükümlülüklerini denetlemek
  veya kurmak gerektiğinde kullanılır.
name: hizmet-saglayici-yukumlulukleri
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
  - ad: Elektronik Ticaretin Düzenlenmesi Hakkında Kanun
    numara: '6563'
    tur: kanun
  - ad: Tüketicinin Korunması Hakkında Kanun
    numara: '6502'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Hizmet Sağlayıcı Bilgi ve Sipariş Yükümlülükleri

## Görev
6563 sayılı Kanun kapsamında hizmet sağlayıcının (kendi mal/hizmetini elektronik ortamda sunan) bilgi verme, sözleşme öncesi bilgilendirme ve sipariş akışına ilişkin yükümlülüklerini denetlemek; eksiklikleri ve yaptırım riskini tespit etmek.

## Soğuk başlangıç (intake)
- Sitede/uygulamada iletişim ve kimlik bilgileri (unvan, MERSIS, adres, e-posta) görünür mü?
- Sipariş öncesi teknik adımlar, sözleşme metninin saklanıp saklanmayacağı, hata düzeltme imkânı belirtiliyor mu?
- Sipariş sonrası teyit (onay) gönderiliyor mu?
- Karşı taraf tüketici mi tacir mi? (yükümlülüklerin kapsamı değişir)

## Denetim şeması
1. Bilgi verme yükümlülüğü (6563 m.3): hizmet sağlayıcının güncel tanıtıcı bilgilerini (ad/unvan, MERSIS no, iletişim, ETBİS bilgileri) elektronik ortamda kolay erişilebilir biçimde bulundurması zorunludur. Eksiklik m.12 idari para cezası riskidir.
2. Sözleşme öncesi bilgilendirme (6563 m.4): sözleşmenin kurulması için izlenecek teknik adımlar, sözleşme metninin saklanıp saklanmayacağı ve sonradan erişim imkânı, veri giriş hatalarının belirlenmesi ve düzeltilmesine ilişkin teknik araçlar bildirilir. Tacirler/esnaf ile aksi kararlaştırılabilir (m.4/2).
3. Sipariş (6563 m.5): sipariş veren kişinin ödeme yükümlülüğü altına girdiği açıkça gösterilir; sipariş alındığının gecikmeksizin elektronik iletişim araçlarıyla teyidi yapılır; sipariş ve teyitler taraflarca gecikmesiz erişilebilir tutulur. Hata düzeltme imkânı sağlanır.
4. Tüketici ise: 6502 m.48 ve Mesafeli Sözleşmeler Yönetmeliği'ndeki ön bilgilendirme katmanı ek olarak uygulanır (bkz. mesafeli-sozlesmeler becerisi).
5. İspat yükü: bilgilendirmenin yapıldığını ve teyitlerin gönderildiğini sağlayıcı ispatlar (log, kayıt, ekran görüntüsü).
Ara sonuç: her madde için "uygun / eksik / riskli" notu ve giderme önerisi.

## Çıktı modülleri
- Yükümlülük kontrol listesi (m.3-4-5 bazında).
- Eksiklik ve idari para cezası risk notu.
- Sipariş akışı düzeltme tavsiyesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

