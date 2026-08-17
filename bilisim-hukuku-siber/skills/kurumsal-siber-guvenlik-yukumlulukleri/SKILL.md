---
argument-hint: ''
description: Bir kurumun siber güvenlik ve veri güvenliği yükümlülüklerini (KVKK m.12
  teknik-idari tedbirler, sektörel düzenlemeler, politika ve sözleşme mimarisi) değerlendirmek
  ve uyum boşluğunu çıkarmak gerekti
name: kurumsal-siber-guvenlik-yukumlulukleri
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


# Kurumsal Siber Güvenlik Yükümlülükleri ve Uyum

## Görev
Kurumun siber/veri güvenliği hukuki yükümlülüklerini saptamak; politika, teknik-idari tedbir ve sözleşme mimarisindeki boşlukları çıkarıp uyum yol haritası kurmak.

## Soğuk başlangıç (intake)
1. Kurumun faaliyeti ve sektörü ne? (banka/ödeme, sağlık, telekom, e-ticaret, genel?)
2. Hangi ve ne kadar kişisel veri işleniyor, işleyen/bulut kullanılıyor mu?
3. Mevcut politika, olay müdahale planı, log yönetimi var mı?
4. Tetikleyici ne? (denetim, ihlal sonrası, yatırım/due diligence, proaktif uyum?)

## Denetim şeması
1. **Genel veri güvenliği (KVKK m.12).** Veri sorumlusu, kişisel verilerin hukuka aykırı işlenmesini ve erişilmesini önlemek ile muhafazasını sağlamak üzere uygun **teknik ve idari tedbirleri** almakla yükümlüdür; işleyen ile müştereken sorumludur. Tedbirlerin alındığını ispat yükü kurumdadır. Eksiklik m.18 idari para cezası ve ihlal halinde ağırlaştırılmış sorumluluk doğurur.
2. **Sektörel katman.** Bankacılık/ödeme (BDDK, 6493 ve bilgi sistemleri düzenlemeleri), elektronik haberleşme (BTK/5809 ve ağ güvenliği), kritik altyapı düzenlemeleri ve varsa kurumun tabi olduğu özel rejim eklenir. TS ISO/IEC 27001 ve ilgili standartlar uyum ölçütü olarak referans alınır (sözleşme/idari beklenti düzeyinde).
3. **Belge ve süreç denetimi.** Veri envanteri, saklama-imha politikası, erişim yönetimi, log kayıtları, olay müdahale ve iş sürekliliği planı, sızma testi/zafiyet yönetimi, farkındalık eğitimleri kontrol edilir.
4. **Sözleşme mimarisi.** Veri işleyen sözleşmeleri, gizlilik ve güvenlik taahhütleri, SLA/güvenlik ekleri, sorumluluk sınırlamaları (TBK çerçevesinde geçerlilik), yurt dışı aktarım şartları denetlenir.
5. **Ara sonuç.** Yükümlülük-mevcut durum karşılaştırmasıyla **uyum boşluğu** ve öncelik/risk sıralaması çıkarılır.

## Çıktı modülleri
- Yükümlülük envanteri (genel KVKK + sektörel + standart).
- Uyum boşluğu raporu (boşluk, risk, öncelik, aksiyon).
- Politika/sözleşme eki şablon önerileri.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

