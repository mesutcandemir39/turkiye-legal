---
argument-hint: ''
description: Sözleşmenin varlığı, içeriği, ifa, ayıp veya ödeme gibi vakıaların nasıl
  ispatlanacağını, ispat yükünün kimde olduğunu ve hangi delillerin kabul edileceğini
  belirlemek gerektiğinde kullanılır.
name: ispat-ve-delil
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


# İsimli Sözleşmelerde İspat ve Delil

## Görev
Sözleşme uyuşmazlığında ispat yükünü TMK m.6 ve tipe özgü kurallara göre dağıtmak, senetle ispat zorunluluğu ve istisnalarını (HMK m.200-203) uygulamak, delil planı kurmak.

## Soğuk başlangıç (intake)
- İspatı gereken vakıa ne (kuruluş, içerik, ifa, ayıp, ödeme)?
- Yazılı sözleşme/senet var mı; bedel miktarı senet sınırını aşıyor mu?
- Eldeki deliller (fatura, e-posta, WhatsApp, tanık, banka kaydı, keşif/bilirkişi konusu)?
- Ticari defter tutan taraf var mı?

## Denetim şeması
1. **İspat yükü (TMK m.6).** Bir vakıadan lehine hak çıkaran onu ispatla yükümlü. Sözleşmenin kurulduğunu iddia eden kuruluşu; ifayı/ödemeyi iddia eden ifayı; ayıbı iddia eden ayıbı ve süresinde ihbarı ispatlar.
2. **Senetle ispat zorunluluğu (HMK m.200).** Dava konusu değeri 2025 için belirlenen parasal sınırı (her yıl güncellenen tutar; `[DOĞRULANMADI]`) aşan hukuki işlemler senetle ispatlanır; senede karşı tanık kural olarak dinlenmez (m.201).
3. **İstisnalar (m.203).** Altsoy-üstsoy, eşler, kardeşler arası işlemler; hukuki işlemin yapıldığı sırada senet alınamaması (yangın/yakın ilişki gibi haklı sebep); delil başlangıcı (m.202) varsa tanık tamamlayıcı delil olur.
4. **Belirli vakıa-delil eşlemesi.** Ödeme → makbuz/banka dekontu/ibra; ayıp → bilirkişi-keşif; teslim → tutanak/irsaliye; kira ödemesi → m.347 ihtara karşı dekont. Ticari defterler HMK m.222 ile sahibi lehine/aleyhine delil.
5. **Elektronik deliller.** Güvenli elektronik imzalı belge senet hükmünde (HMK m.205); imzasız e-posta/mesajlar delil başlangıcı veya takdiri delil olarak değerlendirilir, içerik ve aidiyet tartışılır.
6. **Resmî şekil.** Taşınmaz satışı resmî senetle (TMK m.706, TBK m.237) geçerli; şekil eksikliği geçerlilik sorunu olup ispattan önce gelir. Ara sonuç: vakıa-yük-delil matrisi ve eksik delil listesi.

## Çıktı modülleri
- İspat yükü ve delil planı tablosu.
- Senetle ispat/istisna değerlendirme notu.
- Delil tespiti veya bilirkişi talebi taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

