---
argument-hint: ''
description: Raporun ulaştığı sonuca hangi yöntem, kabul, varsayım ve veriyle vardığını;
  gerekçenin denetlenebilir olup olmadığını ve kabullerin dosya gerçeğiyle örtüşüp
  örtüşmediğini incelemek istendiğinde kullan
name: metodoloji-dayanak-denetimi
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  - ad: Sağlık Turizmi Kanunu
    numara: '6754'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Metodoloji ve Bilimsel Dayanak Denetimi

## Görev
Raporun "neden böyle sonuca varıldı" sorusuna verdiği yanıtı denetlemek: yöntem, kabul, varsayım ve veri kaynağı açık mı, dosya verisiyle örtüşüyor mu, sonuç gerekçeyle bağlanmış mı (HMK m.279)?

## Soğuk başlangıç (intake)
- Rapor hangi yöntemi/standardı kullandığını açıkça söylüyor mu?
- Kabuller ve varsayımlar dosyadaki hangi veriye dayanıyor?
- Bilirkişi keşif/inceleme yapmış mı; yoksa eksik veriyle mi çalışmış?
- Sonuç ile gerekçe arasında izlenebilir bir mantık zinciri var mı?

## Denetim şeması
1. **Gerekçe zorunluluğu (HMK m.279):** Rapor; inceleme konusu, gerekçe ve sonuçtan oluşur; bilirkişi kanaatini gerekçeleriyle açıklar. Gerekçesiz "kanaatimce" türü ifadeler denetlenemez; başlı başına itiraz sebebidir.
2. **Yöntem şeffaflığı:** Kullanılan teknik standart, formül veya yöntem adıyla belirtilmeli; "tecrübeye dayanarak" gibi soyut dayanak yetersizdir. Yöntem tekrar uygulandığında aynı sonuca götürebilmeli.
3. **Kabul-veri örtüşmesi:** Her kritik kabul, dosyadaki belge/delile çıpalanır. Dosyada olmayan veya çelişen bir varsayıma dayanan sonuç sakattır. Eksik veriyle çalışılmışsa, eksiğin sonucu nasıl etkilediği gösterilir.
4. **Sonuç-gerekçe bağı:** Gerekçeden mantıken çıkmayan sonuç (atlama/gediği) işaretlenir.
5. **Ara sonuç:** Yöntem eksik açıklanmış ama düzeltilebilir → **ek rapor**; yöntem temelden hatalı veya bilimsel dayanağı yok → **yeni bilirkişi/heyet** (HMK m.281). Karşı uzman mütalaası yöntem eleştirisini güçlendirir.

## Çıktı modülleri
- Yöntem-kabul-veri-sonuç izleme zinciri çıktısı.
- Dosyayla çelişen veya dayanaksız kabullerin listesi.
- Metodolojik itiraz paragrafı taslağı (madde atıflı).
- Karşı uzman görüşüyle desteklenecek noktaların notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

