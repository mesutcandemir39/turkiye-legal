---
argument-hint: ''
description: Bir ticari davranisin (aldatici reklam, kotuleme, sirlarin ifsasi, baskasinin
  emegi/itibarindan yararlanma, calisanlari ayartma) haksiz rekabet olusturup olusturmadigini
  ve tespit-men-ref-tazminat yap
name: haksiz-rekabet-denetimi
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Haksız Rekabet Denetimi ve Yaptırımları

## Görev
Bir davranışın TTK anlamında haksız rekabet oluşturup oluşturmadığını saptamak ve uygun hukuki/cezai yaptırımları kurmak. Haksız rekabet, dürüst rekabeti ve katılanların menfaatini korur; tacir-tacir dışı herkese karşı uygulanır.

## Soğuk başlangıç (intake)
1. Şikâyet edilen davranış ne (reklam, kötüleme, taklit, sır ifşası, ayartma)?
2. Davranış rekabeti etkiliyor mu; aldatıcı/dürüstlüğe aykırı mı?
3. Zarar veya zarar tehlikesi var mı; müvekkilin durumu nasıl etkilendi?
4. Davranışın öğrenildiği ve gerçekleştiği tarihler ne (zamanaşımı)?

## Denetim şeması
1. **Genel hüküm:** TTK m.54 — rakipler arasında veya tedarik edenlerle müşteriler arasındaki ilişkileri etkileyen aldatıcı veya dürüstlük kuralına aykırı davranışlar haksız rekabettir. Kusur şart değildir (tespit/men için); tazminat için kusur aranır.
2. **Örnek haller:** TTK m.55 — (a) dürüstlüğe aykırı reklam ve satış yöntemleri (kötüleme, yanıltıcı bilgi, gerçeğe aykırı üstünlük iddiası), (b) sözleşmeyi ihlale veya sona erdirmeye yöneltme, (c) başkasının iş ürünlerinden yetkisiz yararlanma, (d) üretim/iş sırlarını hukuka aykırı ifşa, (e) iş şartlarına uymama, (f) dürüstlüğe aykırı genel işlem koşulları kullanma. Liste örnekleyicidir; m.54 genel hükmü tamamlar.
3. **Hukuki sorumluluk talepleri:** TTK m.56 — menfaati ihlal edilen veya tehlikeye giren: (i) fiilin haksız olduğunun tespiti, (ii) men (durdurma/önleme), (iii) sonucun ortadan kaldırılması (ref) ve beyanların düzeltilmesi, (iv) kusur varsa maddi tazminat, (v) TBK m.58 koşullarıyla manevi tazminat, (vi) lehe sağlanan menfaatin devri (vekâletsiz iş görme). Müşteriler ve mesleki kuruluşlar da m.56/2 ile dava açabilir.
4. **Cezai sorumluluk:** TTK m.62 — sayılan hallerde şikâyet üzerine cezai yaptırım; tüzel kişiler için m.63.
5. **Zamanaşımı:** TTK m.60 — dava hakkı, öğrenmeden itibaren 1 yıl ve her hâlde doğumundan itibaren 3 yıl geçince zamanaşımına uğrar. İhtiyati tedbir (TTK m.61) ile durum dondurulabilir. Ara sonuç: m.54/55 unsuru + menfaat ihlali → m.56 talepleri + gerekiyorsa tedbir.

## Çıktı modülleri
- Davranışın m.55 alt bendiyle eşleştirilmesi ve nitelendirme notu.
- Talep matrisi (tespit/men/ref/maddi-manevi tazminat) ve zamanaşımı durumu.
- İhtiyati tedbir talebi ve dava dilekçesi talep sonucu taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

