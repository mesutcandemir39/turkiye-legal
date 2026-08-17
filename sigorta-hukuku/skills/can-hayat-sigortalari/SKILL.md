---
argument-hint: ''
description: Hayat, ferdi kaza veya sağlık/hastalık sigortalarında lehtar tayini,
  sigorta bedelinin ödenmesi, intihar/suikast gibi özel haller ve tazminat ilkesinin
  uygulanmayacağı durumlar tartışıldığında kullanı
name: can-hayat-sigortalari
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
  - ad: Bankalar Kanunu
    numara: '5684'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Can Sigortaları (Hayat, Kaza, Sağlık)

## Görev
Can sigortalarında sigorta bedelinin kime, hangi şartlarla ve ne miktarda ödeneceğini; lehtar tayini, beyan ve özel istisnaları (intihar, suikast) değerlendirmek.

## Soğuk başlangıç (intake)
1. Hayat, ferdi kaza yoksa sağlık/hastalık sigortası mı?
2. Lehtar belirlenmiş mi, değiştirilebilir mi; sigortalı ile sigorta ettiren aynı kişi mi?
3. Riziko (vefat/maluliyet/hastalık) ne zaman, nasıl gerçekleşti?
4. Bekleme süresi, yaş/sağlık beyanı, teminat dışı haller poliçede nasıl?

## Denetim şeması
1. **Tazminat ilkesi uygulanmaz.** Can sigortalarında kural olarak gerçek zarar değil, kararlaştırılan sigorta bedeli ödenir (TTK m.1487 vd.); zarar sigortasındaki zenginleşme yasağı geçerli değildir. Ferdi kazada bedel esastır.
2. **Lehtar.** TTK m.1493: sigorta ettiren, lehtarı serbestçe tayin ve değiştirebilir; lehtar tayini yazılı bildirimle hüküm doğurur. Lehtar yoksa sigorta bedeli sigorta ettirenin/sigortalının mirasçılarına/terekesine geçer.
3. **Beyan ve yaş.** Hayat sigortasında yanlış yaş beyanı sözleşmeyi kural olarak iptal ettirmez; sigorta bedeli/prim oranlanır (TTK m.1500 mantığı). Sağlık beyanı için genel beyan yükümlülüğü (TTK m.1435 vd.) uygulanır.
4. **Özel istisnalar.** TTK m.1503: sözleşmeden itibaren belirli süre (genel şartlarda üç yıl) sonra intihar halinde dahi sigorta bedeli ödenir; lehtarın sigortalıyı öldürmesi (suikast) halinde o lehtar bedele hak kazanamaz, diğer hak sahipleri korunur. Ara sonuç: istisna devrede mi?
5. **Sağlık/hastalık.** Bekleme süreleri, mevcut hastalık istisnası ve teminat dışı haller poliçeden denetlenir; tüketici sigortalarında haksız şart kontrolü.

## Çıktı modülleri
- Lehtar/hak sahibi belirleme tablosu.
- Sigorta bedeli ödeme değerlendirmesi (tazminat ilkesi yok notu).
- İntihar/suikast ve beyan istisnaları analizi.
- Ödenecek bedel ve dayanak maddeleri.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

