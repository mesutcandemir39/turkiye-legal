---
argument-hint: ''
description: İki ya da daha çok geminin çarpışması (çatma) veya başka bir deniz kazasından
  kaynaklanan zararlarda; kusur paylaşımını, zararın dağıtımını ve üçüncü kişilere
  karşı sorumluluğu belirlemek için kullan.
name: catma-deniz-kazalari
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


# Çatma ve Deniz Kazaları

## Görev
Çatma veya benzeri bir deniz kazasında zararın hangi gemiye/donatana yükleneceğini, kusurun nasıl paylaştırılacağını ve üçüncü kişiler (yük ve can zararı) bakımından sorumluluğun nasıl dağıtılacağını belirlemek.

## Soğuk başlangıç (intake)
- Kaç gemi karıştı; çarpışma fiziksel mi yoksa manevra/dalga etkisiyle dolaylı mı?
- Kaza anındaki seyir verileri (rota, hız, AIS/VDR kayıtları, gemi jurnali) mevcut mu?
- Kusur tek tarafta mı, karşılıklı mı, yoksa belirsiz mi; mücbir sebep iddiası var mı?
- Zarar yalnızca gemilerde mi, yoksa yük ve can zararı da var mı?

## Denetim şeması
1. **Çatma kavramı ve kapsam**: Olayın TTK m.1286 vd. anlamında çatma olup olmadığını belirle; doğrudan temas olmadan manevra/dalga etkisiyle verilen zararlar da çatma hükümlerine girebilir.
2. **Kusur tespiti ve paylaşım**: Kusursuz/mücbir sebep halinde zarara herkes kendi katlanır; tek taraf kusurluysa o donatan sorumludur; karşılıklı kusurda zarar **kusur oranına göre** paylaştırılır (TTK m.1289 vd.). Kusur oranı belirlenemezse eşit paylaşım esasını uygula.
3. **Üçüncü kişi zararları**: Yük zararlarında donatanların sorumluluğunun kusur oranıyla sınırlı (kısmi/müteselsil olmayan) niteliğini; can ve beden zararlarında ise müteselsil sorumluluk ve iç ilişkide rücu mekanizmasını ayrıştır.
4. **Kılavuz ve teknik kusur etkisi**: Zorunlu kılavuzun kusuru, geminin kendi gemi adamlarının seyir kusuru gibi hususların sorumluluğa etkisini değerlendir.
5. **İspat ve ara sonuç**: Kusur, seyir kayıtları ve bilirkişi/sörvey raporlarıyla ispatlanır; deniz raporu (gemi jurnali, kaptan ifadesi) önemli delildir. Çatmadan doğan taleplerde **iki yıllık** zamanaşımını (TTK m.1297) hesapla. Çıktıda kusur oranını ve zarar dağıtım tablosunu gerekçelendir.

## Çıktı modülleri
- Kusur oranı ve zarar dağıtım tablosu
- Delil/seyir kaydı dizini (AIS, VDR, jurnal, sörvey)
- Rücu ve sorumluluk sınırı stratejisi notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

