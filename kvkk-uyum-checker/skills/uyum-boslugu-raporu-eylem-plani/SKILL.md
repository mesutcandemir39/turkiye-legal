---
argument-hint: ''
description: Tüm denetim bulgularının tek raporda birleştirilmesi, risk önceliklendirmesi
  ve sorumlu-termin atanmış düzeltici eylem planı çıkarılması gerektiğinde kullanılır.
name: uyum-boslugu-raporu-eylem-plani
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Uyum Boşluğu Raporu ve Eylem Planı

## Görev
Önceki becerilerin bulgularını tek bir uyum boşluğu (gap analysis) raporunda birleştirmek; her bulguyu risk seviyesine göre önceliklendirip sorumlu ve termin atanmış düzeltici eylem planına bağlamak. Bu, denetimin nihai teslim çıktısıdır.

## Soğuk başlangıç (intake)
1. Hangi başlıklarda denetim tamamlandı (envanter, aydınlatma, aktarım/VERBİS, güvenlik, ihlal, başvuru, çerez)?
2. Yönetimin risk iştahı ve düzeltme için kaynağı/önceliği nedir?
3. Yasal/ticari olarak hangi bulgular acil (yaptırım riski yüksek)?
4. Yeniden denetim ne zaman planlanacak?

## Denetim şeması
1. **Bulgu konsolidasyonu**: Her başlıktan gelen bulgular tek tabloda toplanır — bulgu, ilgili madde (m.4/5/6/7/9/10/12/13/16), kanıt durumu, mevcut durum (Uygun/Kısmen/Uygunsuz).
2. **Risk skorlama (m.18 ağırlıklı)**: Her bulguya olasılık × etki verilir; etki = idari para cezası riski (m.18) + ilgili kişi zararı/tazminat + itibar. Yüksek/orta/düşük olarak sınıflanır. Özel nitelikli veri (m.6), yurt dışı aktarım ve güvenlik bulguları kural olarak yüksek başlar.
3. **Önceliklendirme**: "Hızlı kazanım" (düşük efor-yüksek etki) ile "yapısal" (yüksek efor) bulgular ayrılır; aydınlatma/başvuru gibi belge düzeltmeleri çoğunlukla hızlı kazanımdır.
4. **Eylem planı**: Her bulguya düzeltici aksiyon, sorumlu kişi/birim, termin ve doğrulama yöntemi atanır.
5. **Hesap verebilirlik döngüsü (m.4)**: Plan, periyodik gözden geçirme ve yeniden denetim tarihiyle kapatılır; uyum tek seferlik değil sürekli süreçtir.
6. **Ara sonuç**: Skorlanmamış ve sorumlu atanmamış bulgu, rapor değil yalnızca gözlemdir.

İspat yükü (accountability): Veri sorumlusu, m.4 ve tüm yükümlülüklere uyumu işleyen süreç ve belgelerle ispatlayabilmelidir; rapor bu ispat altyapısının haritasıdır.

## Çıktı modülleri
- Konsolide uyum boşluğu (gap analysis) skor tablosu.
- Önceliklendirilmiş düzeltici eylem planı (bulgu–aksiyon–sorumlu–termin).
- Yönetici özeti ve yeniden denetim takvimi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

