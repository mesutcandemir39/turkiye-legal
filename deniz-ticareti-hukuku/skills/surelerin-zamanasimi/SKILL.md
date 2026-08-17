---
argument-hint: ''
description: Deniz ticareti alacak ve taleplerinde hangi sürenin geçtiğini, kesilme-durma
  hallerini ve ihbar/protesto sürelerini hesaplamak; dava ya da savunmada zamanaşımı
  definin gündeme geleceği her durumda kul
name: surelerin-zamanasimi
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


# Süreler ve Zamanaşımı

## Görev
Deniz ticareti taleplerinde uygulanacak zamanaşımı süresini doğru tespit etmek; başlangıç anını, kesilme ve durma hallerini, ihbar/protesto sürelerini hesaplamak; zamanaşımı definin geçerli olup olmadığını değerlendirmek.

## Soğuk başlangıç (intake)
- Talep hangi olaydan doğuyor (taşıma, çatma, kurtarma, avarya, sigorta)?
- Olayın/zararın gerçekleştiği ve öğrenildiği tarih nedir?
- Araya giren dava, ihtiyati haciz, ikrar veya yazılı talep var mı (kesilme)?
- İhbar/protesto süreleri korunmuş mu?

## Denetim şeması
1. **Talebin türü ve süresi**: Eşyaya ilişkin deniz taşımasından doğan taşıyana karşı taleplerde **bir yıllık** zamanaşımını (TTK m.1188) uygula; çatmadan doğan tazminat taleplerinde **iki yıllık** süreyi (TTK m.1297) hesapla. Kurtarma, avarya ve sigorta için ilgili özel süreleri ayrıca teyit et.
2. **Başlangıç anı**: Sürenin başlangıcını olaya göre belirle — taşımada eşyanın teslim edildiği veya edilmesi gereken gün; çatmada kaza günü; rücu taleplerinde ise asıl borcun ödendiği an gibi.
3. **Kesilme ve durma**: TBK m.154 vd. (dava açılması, icra takibi, ikrar, hakeme başvuru) kesilme sebeplerini ve TBK m.153 durma sebeplerini deniz alacağına uyarlayarak değerlendir; ihtiyati haczin süreye etkisini gözet.
4. **İhbar/protesto süreleri**: Yük ziya/hasarında açık hasarda teslim anında, gizli hasarda kanuni süre içinde ihbar; sürastarya ve avarya bildirimleri gibi sözleşmesel/yasal sürelerin korunup korunmadığını ayrı tablo ile kontrol et.
5. **İspat ve ara sonuç**: Zamanaşımını def olarak ileri süren taraf ispatlar; kesilme/durmayı iddia eden bunu ispatlar. Çıktıda son günü, kalan süreyi ve definin geçerliliğini gerekçeli sonuca bağla; süreler yaklaşıyorsa derhal koruyucu işlem öner.

## Çıktı modülleri
- Talep türüne göre zamanaşımı süresi tablosu
- Başlangıç-kesilme-durma kronolojisi
- İhbar/protesto kontrol listesi ve son gün uyarısı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

