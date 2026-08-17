---
argument-hint: ''
description: İhalenin idarece veya KİK kararıyla iptali, bütün tekliflerin reddi ya
  da ihalenin sonuçlanamaması hallerinin sonuçları ve isteklinin hak arama yolları
  değerlendirilirken kullanılır.
name: ihale-iptali-ve-itirazen-sonuc
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
  - ad: Koruma Amaçlı Imar Planları Hakkında Kanun
    numara: '4734'
    tur: kanun
  - ad: Tarih Medeniyetini Koruma Kanunu
    numara: '4735'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İhalenin İptali ve Sürecin Sonlanması

## Görev
İhalenin iptali (idarece m.39/m.40 veya KİK kararıyla) ve bütün tekliflerin reddi hallerinin hukuka uygunluğunu, sonuçlarını ve isteklinin haklarını (teminat iadesi, masraf) değerlendirmek.

## Soğuk başlangıç (intake)
1. İptal kimden geldi: idarenin kendi kararı mı, KİK kararıyla mı?
2. İptal gerekçesi nedir (yeterli rekabet oluşmaması, doküman aykırılığı, ödenek yokluğu vb.)?
3. İptal kararı kesinleşen ihale kararından önce mi sonra mı?
4. Geçici teminatlar iade edildi mi?

## Denetim şeması
1. **İdarenin takdiri (m.39):** İhale yetkilisi, ihale komisyonunun gerekçeli kararı üzerine ihaleyi yapıp yapmamakta serbesttir; ihale iptal edilirse hiçbir taahhüt altına girmiş sayılmaz. Ancak takdir keyfî olamaz, gerekçe denetlenir.
2. **Bütün tekliflerin reddi (m.40):** Komisyon, gerekçesini belirtmek kaydıyla bütün teklifleri reddederek ihaleyi iptal edebilir. İptal hukuka aykırıysa düzeltici işlem/iptal denetimine konu olur.
3. **KİK kaynaklı iptal:** İtirazen şikâyet sonucu Kurul ihalenin iptaline karar verebilir; bu karar idareyi bağlar.
4. **Sonuçlar:** İptalde isteklilere bildirim yapılır, geçici teminatlar iade edilir; istekli kural olarak masraf/menfi zararını talep edemez, ancak idarenin hukuka aykırı/kusurlu iptalinde tam yargı davası gündeme gelebilir.
5. **Ara sonuç:** İptal kararına karşı da süresinde (gerekçenin öğrenilmesinden itibaren) şikâyet-itirazen şikâyet yolu işletilir; aksi halde dava hakkı düşer.

İspat yükü: İptalin keyfîliğini iddia eden istekli, gerekçenin gerçek dışılığını/orantısızlığını gösterir.

## Çıktı modülleri
- İptal türü ve dayanağı sınıflandırması.
- Teminat iadesi ve masraf/zarar değerlendirmesi.
- İptale karşı başvuru/dava yol haritası.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

