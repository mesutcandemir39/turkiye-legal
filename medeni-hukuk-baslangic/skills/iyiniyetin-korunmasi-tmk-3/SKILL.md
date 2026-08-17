---
argument-hint: ''
description: Bir hakkın kazanılması veya bir hukuki sonucun doğumu kişinin bir durumu
  bilmemesine bağlandığında; iyiniyet karinesi, gösterilmesi gereken özen ve iyiniyetin
  sağladığı koruma tartışıldığında TMK m.3
name: iyiniyetin-korunmasi-tmk-3
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
  version: 0.1.0
user-invocable: true
---


# İyiniyetin Korunması (TMK m.3)

## Görev
Kanunun bir hakkın doğumunu iyiniyete bağladığı hâllerde (taşınır iktisabı, tapuya güven, ehliyetsizlik vb.) iyiniyetin varlığını, özen ölçütünü ve sağladığı korumanın kapsamını denetlemek.

## Soğuk başlangıç (intake)
- Hangi hakkın kazanımı/sonucu iyiniyete bağlı (ör. taşınır mülkiyeti TMK m.988 vd., tapuya güven m.1023, evlenme hükümleri)?
- Kişi hangi durumu bilmiyordu ve bunu bilmemesi durumun gereğine uygun mu?
- Karşı taraf, kişinin gerekli özeni göstermediğini mi ileri sürüyor?
- İyiniyetin hangi anda (kazanım anı) bulunması gerekiyor?

## Denetim şeması
1. **İyiniyet karinesi** — TMK m.3/1: kanunun iyiniyete hukuki sonuç bağladığı hâllerde asıl olan iyiniyettin varlığıdır; iyiniyetin yokluğunu (kötüniyeti) iddia eden ispatlar (m.6 ile bağ).
2. **İyiniyetin konusu** — İyiniyet, bir hakkın kazanılmasına engel olan hukuki sakatlığı (ör. devredenin yetkisizliği, sicildeki yolsuzluğu) *bilmemek*tir; bilmesi hâlinde korunmaz.
3. **Özen sınırı — m.3/2** — Durumun gerektirdiği özeni göstermeyen kişi iyiniyet iddiasında bulunamaz. Özen ölçütü objektiftir; basit bir araştırmayla anlaşılabilecek sakatlığı görmeyen iyiniyetli sayılmaz. Tacir için özen ağırlaşır.
4. **Zaman** — İyiniyet, hakkın kazanıldığı anda bulunmalıdır; sonradan öğrenme kazanımı geri almaz, önceden bilme korumayı düşürür.
5. **Koruma kapsamı** — Şartlar sağlanırsa kişi, gerçek hak durumuna rağmen hakkı kazanır (ör. emin sıfatıyla zilyetten iyiniyetle iktisap, tapu kaydına güven). Koruma istisnaidir; ilgili özel normun kendi sınırlarına tabidir.
6. **m.2 ile ayrım** — m.3 bilgisizliğin korunması (sübjektif bilgi durumu), m.2 davranışın dürüstlüğüdür.

## Çıktı modülleri
- İyiniyete bağlı kazanım normunun tespiti.
- Karine + ispat yükü dağılımı (kötüniyet iddiası).
- Özen denetimi (m.3/2) ve zaman tespiti.
- Koruma sonucu + ilkesel içtihat `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

