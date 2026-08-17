---
argument-hint: ''
description: Kiraya veren tahliye istediğinde veya kiracı tahliye tehdidiyle karşılaştığında
  hangi tahliye sebebinin uygulanabilir olduğunu, şekil ve süre şartlarını ve dava
  yolunu belirlemek için bu beceriyi kull
name: tahliye-sebepleri-ve-denetim
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tahliye Sebepleri ve Dava Yolu

## Görev
Konut/çatılı işyeri kirasında tahliye talebini doğru kanuni sebebe oturtmak; her sebebin şekil, süre, bildirim ve ispat şartlarını ayrı ayrı denetlemek; uygun dava/icra yolunu seçmek.

## Soğuk başlangıç (intake)
- Tahliye gerekçesi ne (ihtiyaç, yeniden inşa, taahhüt, ödememe, iki haklı ihtar)?
- Sözleşme belirli/belirsiz süreli mi; dönem sonu ne zaman?
- Daha önce ihtar/bildirim yapıldı mı; tarihleri?
- Taşınmaz el değiştirdi mi (yeni malik)?

## Denetim şeması
1. **Gereksinim — kiraya veren/yakınları (TBK m.350/1)**: Kiraya veren, kendisi, eşi, altsoyu, üstsoyu veya bakmakla yükümlü olduğu kişiler için konut/işyeri **gerçek, samimi ve zorunlu** ihtiyaç ileri sürebilir. Dava süresi m.353'e tabidir.
2. **Yeniden inşa/imar (TBK m.350/2)**: Taşınmazın yeniden inşası veya imarı zorunlu ve esaslı onarımı, kullanım sırasında mümkün değilse tahliye istenebilir.
3. **Yeni malik gereksinimi (TBK m.351)**: Edinme tarihinden başlayarak bir ay içinde durumu kiracıya yazılı bildirmek koşuluyla, altı ay sonra gereksinim sebebiyle dava açabilir; ya da sözleşme süresinin/feshe ilişkin sürelerin sonunu bekleyebilir.
4. **Yazılı tahliye taahhüdü (TBK m.352/1)**: Kiracı, kiralananı belli tarihte boşaltmayı yazılı taahhüt etmiş ve boşaltmamışsa; kiraya veren bu tarihten başlayarak bir ay içinde icra/dava ile tahliye isteyebilir.
5. **İki haklı ihtar (TBK m.352/2)**: Kiracı bir kira yılı içinde iki haklı ihtara sebep olmuşsa, kira yılının/dönemin bitiminden başlayarak bir ay içinde dava.
6. **Temerrüt (TBK m.315)**: Ayrı denetim şeması (bkz. temerrüt becerisi).
7. **Dava süreleri (TBK m.353)** ve **yeniden kiralama yasağı (TBK m.355)**: Tahliye sonrası taşınmaz, haklı sebep olmaksızın üç yıl başkasına kiralanamaz.

## Çıktı modülleri
- Sebep-süre-şekil eşleştirme tablosu.
- Tahliye dava dilekçesi iskeleti.
- Süre uyarı takvimi (hak düşürücü tarihler).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

