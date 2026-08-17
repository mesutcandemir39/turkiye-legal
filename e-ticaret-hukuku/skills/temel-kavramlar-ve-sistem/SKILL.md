---
argument-hint: ''
description: E-ticaret uyuşmazlığının hangi kanun kümelerine değdiğini ve tarafların
  sıfatını (hizmet sağlayıcı, aracı hizmet sağlayıcı, tüketici, tacir) belirlemek
  gerektiğinde; alanın norm haritasını çıkarmak iç
name: temel-kavramlar-ve-sistem
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


# Temel Kavramlar ve Sistematik

## Görev
E-ticaretle ilgili bir olayda hangi kanunların ve yönetmeliklerin uygulanacağını, tarafların hukuki sıfatını ve hangi yükümlülük katmanının tetiklendiğini belirlemek; sonraki becerilere doğru giriş kapısını açmak.

## Soğuk başlangıç (intake)
- Müvekkil hangi rolde: kendi ürün/hizmetini satan mı (hizmet sağlayıcı), yoksa başkalarının satışına aracılık eden platform mu (aracı hizmet sağlayıcı)?
- Karşı taraf tüketici mi (gerçek kişi, ticari amaç dışı) yoksa tacir/işletme mi?
- Yıllık net işlem hacmi ve işlem sayısı yaklaşık ne? (ETAHS eşikleri için)
- Olayın çekirdeği ne: sözleşme/iade mi, ticari ileti mi, veri mi, içerik kaldırma mı, yaptırım mı?

## Denetim şeması
1. Sıfat tespiti: 6563 m.2 tanımlarına göre "hizmet sağlayıcı" ve "aracı hizmet sağlayıcı" ayrımı yapılır. 7416 sayılı Kanun sonrası "elektronik ticaret hizmet sağlayıcı (ETHS)" ve "elektronik ticaret aracı hizmet sağlayıcı (ETAHS)" kavramları ile net işlem hacmine bağlı kademeli yükümlülükler devreye girer.
2. İlişki tipi: Karşı taraf 6502 m.3 anlamında tüketici ise hem 6563 hem 6502 (mesafeli sözleşme, m.48) uygulanır; B2B ise 6502 dışında kalır, 6563 + TBK/TTK yürür.
3. Norm kümesi haritası: ticari iletişim → 6563 m.6-7 + Ticari Elektronik İleti Yönetmeliği + İYS; veri → 6698 KVKK; içerik/barındırma → 5651; haksız rekabet → TTK m.54-55.
4. Yükümlülük katmanı: bilgi verme (6563 m.3), sözleşme öncesi bilgilendirme ve sipariş (m.4-5), ETBİS kaydı (m.11), aracı sorumluluğu (m.9).
5. Ara sonuç: olaya değen 2-4 norm kümesi listelenir, her biri için sorumlu beceri işaretlenir.
İspat yükü: yükümlülüğün yerine getirildiğini ispat külfeti kural olarak sağlayıcıdadır (bilgilendirme/onay kayıtları).

## Çıktı modülleri
- Taraf sıfatı ve ölçek tablosu.
- Uygulanacak normlar matrisi (kanun-madde-yönetmelik).
- İlgili alt-beceriye yönlendirme notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

