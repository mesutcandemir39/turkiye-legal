---
argument-hint: ''
description: Profesyonel sporcu sözleşmesi, transfer, geçici transfer veya tek taraflı
  fesih uyuşmazlıklarını değerlendirmek, sözleşme taslağı veya fesih/alacak stratejisi
  hazırlamak gerektiğinde kullanın.
name: sporcu-sozlesmesi-transfer
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
  - ad: Çalışma ve Sosyal Güvenlik Bakanlığı Kuruluş ve Görevleri Hakkında Kanun
    numara: '7405'
    tur: kanun
  - ad: Tıbbi Deontoloji Tüzüğü Hakkında Kanun
    numara: '6222'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Sporcu Sözleşmeleri ve Transfer Hukuku

## Görev
Profesyonel sporcu sözleşmesinin kuruluşu, içeriği, transferi ve feshini ilgili federasyon statü/transfer talimatı ve TBK çerçevesinde değerlendirmek; sözleşme taslağı, fesih bildirimi veya tazminat/alacak hesabı üretmektir.

## Soğuk başlangıç (intake)
1. Sözleşme türü: profesyonel sporcu sözleşmesi, geçici transfer (kiralık), menajer sözleşmesi?
2. Süre, ücret, prim ve fesih hükümleri nasıl düzenlenmiş?
3. Uyuşmazlık ne: ödenmeyen ücret/prim, tek taraflı fesih, transfer engeli?
4. Sözleşmede tahkim/uyuşmazlık çözüm şartı var mı?
5. Milletlerarası transfer ve FIFA boyutu var mı?

## Denetim şeması
1. **Geçerlilik ve şekil**: Profesyonel sözleşmenin federasyona tescili ve şekil şartları (Profesyonel Futbolcuların Statüsü ve Transferleri Talimatı ya da ilgili branş statüsü) kontrol edilir; tescilsiz sözleşmenin sonuçları değerlendirilir.
2. **İçerik denetimi**: Ücret, prim, opsiyon, satın alma/geri alma hükümleri, bonservis ve cezai şart (TBK m.179-182) incelenir; aşırı cezai şartta TBK m.182/3 indirimi gündeme gelir.
3. **Fesih**: Haklı sebeple fesih (sporcu açısından ödememe, kulüp açısından disiplinsizlik) ile haksız tek taraflı fesih ayrımı; sözleşmenin korunması ilkesi (sportif haklı sebep, korumalı dönem) ve fesih tazminatının hesabı.
4. **Transfer**: Transfer dönemi kuralları, kiralık (geçici transfer) şartları, dayanışma katkı payı ve yetiştirme tazminatı (uluslararası transferde FIFA RSTP esasları) kontrol edilir.
5. **Görevli merci**: Talimattaki uyuşmazlık çözüm kurulu/tahkim; sözleşmedeki tahkim şartı ve milletlerarası unsurda FIFA/CAS.
6. **Ara sonuç**: Talebin türü (alacak, fesih tazminatı, transfer engelinin kaldırılması) ve dayanağı sabitlenir.

## Çıktı modülleri
- Sözleşme/transfer risk tablosu (madde madde)
- Fesih bildirimi veya alacak dilekçesi taslağı
- Tazminat/prim hesap çerçevesi
- Görevli merci ve süre notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

