---
argument-hint: ''
description: Maketten/projeden konut satışı, taksitli ödeme, cayma, teslim gecikmesi
  veya teminat sorunları söz konusu olduğunda; 6502 sayılı TKHK çerçevesinde tüketicinin
  haklarını ve satıcının yükümlülüklerini d
name: on-odemeli-konut-tuketici
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Ön Ödemeli Konut Satışı ve Tüketici Koruması

## Görev
Henüz inşa edilmemiş ya da inşa hâlindeki konutun bedelinin önceden/taksitle ödendiği satışları, tüketici lehine emredici kurallar süzgecinden geçirmek: şekil, cayma, teslim süresi, devir ve teminat (yapı denetimi/bina tamamlama sigortası) yükümlülüklerini denetlemek.

## Soğuk başlangıç (intake)
- Alıcı tüketici mi (ticari/mesleki amaç dışı); satıcı/yapı sahibi kim?
- Sözleşme noterde resmî şekilde mi yapıldı; satış vaadi/sözleşme tarihi ne?
- Bedel peşin mi taksitli mi ödendi; cayma süresi içinde mi?
- Teslim tarihi geçti mi; teminat (bina tamamlama sigortası/banka teminatı) sağlandı mı?

## Denetim şeması
1. **Kapsam ve şekil**: Ön ödemeli konut satışı, tüketicinin bedeli önceden/taksitle ödediği, konutun gelecekte teslim edileceği satıştır (6502 m.40). Sözleşme yazılı/noterde resmî şekilde kurulur ve teminat şartına bağlanır; şekle ve zorunlu içeriğe aykırılık tüketici aleyhine ileri sürülemez (m.41, ilgili yönetmelik).
2. **Cayma hakkı**: Tüketici, sebep göstermeden ve cezasız olarak 14 gün içinde cayabilir (m.43); satıcı caymadan sonra makul sürede ödenenleri iade eder.
3. **Teslim süresi**: Konut en geç sözleşme tarihinden itibaren 48 ayı geçmeyecek şekilde teslim edilmelidir (m.44); gecikme tüketiciye sözleşmeden dönme/tazminat imkânı verir.
4. **Devir ve dönme**: Tüketici, yükümlülüklerini ifa ederek sözleşmeyi devredebilir; sözleşmeden dönmede satıcı, ödenen bedeli (sınırlı kesintiyle) iade eder (m.42-45).
5. **Teminat zorunluluğu**: Satıcı, projedeki konutların belli oranını aşan satışlarda bina tamamlama sigortası veya muadili teminatı sağlamakla yükümlüdür (m.40/son ve yönetmelik); teminat yoksa tüketici lehine sonuç doğar.
6. **Yargı yolu**: Uyuşmazlık tüketici hakem heyeti parasal sınırını aşıyorsa tüketici mahkemesinde görülür (m.68, m.73); değer sınırına dikkat edilir.
7. **Ara sonuç**: Emredici kurallara aykırılık tüketici lehine; cayma/dönme/teslim gecikmesi taleplerinin uygun yargı yoluna yönlendirilmesi.

## Çıktı modülleri
- Cayma/dönme bildirimi taslağı (süre, iade talebi).
- Teslim gecikmesi nedeniyle dönme/tazminat dilekçesi iskeleti.
- Tüketici hakem heyeti/tüketici mahkemesi yönlendirme ve parasal sınır notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

