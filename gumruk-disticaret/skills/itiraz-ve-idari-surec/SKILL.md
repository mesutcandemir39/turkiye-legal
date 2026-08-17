---
argument-hint: ''
description: Gümrük işlem, ek tahakkuk veya ceza kararına karşı dava yolundan önceki
  zorunlu idari itiraz ve uzlaşma süreçlerini yönetmek gerektiğinde; mercileri, süreleri
  ve başvuru stratejisini kurmak için kulla
name: itiraz-ve-idari-surec
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
  - ad: Gümrük Müsait Müşterek Gümrük Bölgeleri Hakkında Kanun
    numara: '4458'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İdari İtiraz ve Uzlaşma Süreci

## Görev
Gümrük idaresinin işlem, ek tahakkuk veya ceza kararına karşı 4458 m.242 idari itiraz yolunu ve m.244 uzlaşma müessesesini doğru mercii ve süreyle yürütmek; dava öncesi en uygun çözüm yolunu seçmek.

## Soğuk başlangıç (intake)
- Karar hangi gümrük idaresince düzenlendi ve hangi tarihte tebliğ edildi?
- İtiraz süresi geçti mi (tebliğden itibaren 15 gün)?
- Uzlaşmaya konu edilebilir bir vergi/ceza farkı var mı; tutar uzlaşma kapsamında mı?
- İtiraz daha önce yapıldı mı, reddedildi mi (açık ret/zımni ret)?

## Denetim şeması
1. İdari itiraz mercii ve süre: 4458 m.242 uyarınca karara karşı, tebliğ tarihinden itibaren 15 gün içinde kararı veren idarenin bağlı olduğu üst mercie (Gümrük Müdürlüğü kararına karşı Bölge/Gümrük ve Dış Ticaret Bölge Müdürlüğü) itiraz edilir. İtiraz idari dava açma süresinden önce tüketilmesi gereken bir aşamadır.
2. İtirazın sonuçlanması: İtiraz mercii 30 gün içinde karar verir; süresinde cevap verilmemesi zımni ret sayılır ve dava süresini başlatır.
3. Uzlaşma (m.244): Beyan ile idare arasındaki kıymet, sınıflandırma, menşe gibi konulardan kaynaklanan vergi farkları ve bunlara bağlı cezalar uzlaşmaya konu olabilir; uzlaşma başvurusu dava açma süresini etkiler ve uzlaşılan tutarda dava açılamaz. İtiraz ve uzlaşma yollarının ilişkisi ve mükerrer kullanılamayacağı gözetilir.
4. Strateji süzgeci: Hukuki sebep güçlüyse itiraz/dava; tutar belirsiz ve uzlaşma indirimi avantajlıysa uzlaşma tercih edilir. Ödeme yapılırken ihtirazi kayıt ve dava hakkının saklanması değerlendirilir.
5. İspat ve dosya: İtiraz dilekçesine beyanname, fatura, menşe belgeleri, ekspertiz raporu ve hukuki gerekçeler eklenir; süre tutum delili (tebliğ alındısı) saklanır.
6. Ara sonuç: Uygun mercii, süre ve yol (itiraz/uzlaşma/dava) belirlenir; başvuru hazırlanır ve dava süresine köprü kurulur.

## Çıktı modülleri
- Süre ve mercii haritası (tebliğ → itiraz → ret → dava)
- Gerekçeli idari itiraz dilekçesi taslağı [doldurulacak yer tutucularıyla]
- Uzlaşma-itiraz-dava karşılaştırmalı karar notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

