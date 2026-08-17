---
argument-hint: ''
description: Tapu kaydı gerçek hak durumunu yansıtmadığında (muvazaa, mirastan mal
  kaçırma, sahtecilik, vekâlet kötüye kullanımı, hata) tapu iptali ve tescil davasını
  kurmak; tescile güven ve iyiniyetli üçüncü kiş
name: tapu-iptali-tescil-muvazaa
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


# Tapu İptali-Tescil, Muris Muvazaası ve Yolsuz Tescil

## Görev
Tapu kaydı ile gerçek hak durumu arasındaki çelişkiyi gidermek: yolsuz veya muvazaalı tescili iptal ettirip gerçek hak sahibi adına tescili sağlamak; tescile güvenen iyiniyetli üçüncü kişinin korunup korunmadığını belirlemek.

## Soğuk başlangıç (intake)
- Tapu şu an kimin adına; müvekkil hak iddiasını neye dayandırıyor (miras, muvazaa, sahtecilik, vekâlet aşımı, hata)?
- Devir bedelli görünüp gerçekte bedelsiz mi (muris muvazaası şüphesi); mirasçıdan mal kaçırma iddiası var mı?
- Yolsuz/muvazaalı devirden sonra taşınmaz üçüncü kişiye geçti mi; o kişi iyiniyetli mi?
- Kayıt üzerinde ipotek, haciz, şerh var mı; ihtiyati tedbir gerekiyor mu?

## Denetim şeması
1. **Sicilin gücü**: Tapu kaydı doğruluk karinesi taşır (TMK m.7, m.992); ayni haklar tescille doğar (m.1021). İddia eden aksini ispatla yükümlüdür (m.6).
2. **Yolsuz tescil (m.1024-1025)**: Geçerli hukuki sebebe dayanmayan tescil yolsuzdur; gerçek hak sahibi tapu iptali ve tescil ister (m.1025). Sahtecilik, vekâletin kötüye kullanılması, ehliyetsizlik bu kapsamdadır.
3. **Muris muvazaası**: Miras bırakanın, mirasçıdan mal kaçırmak amacıyla gerçekte bağışladığı taşınmazı satış/ölünceye kadar bakma gibi göstermesi hâlinde işlem muvazaa nedeniyle geçersizdir (TBK m.19; TMK m.2). Saklı paya bağlı olmaksızın tüm mirasçılar dava açabilir; amaç (mal kaçırma kastı) ve bedel-emsal karşılaştırması ile araştırılır [ilkeler için karararama.yargitay.gov.tr].
4. **Tenkis ile ayrım**: Gerçek bir bağış varsa muvazaa değil, saklı pay ihlali söz konusudur ve yol tenkistir (TMK m.560 vd.); muvazaa ile tenkis talebi terditli ileri sürülebilir.
5. **Tescile güven savunması (m.1023)**: Yolsuz/muvazaalı kayda iyiniyetle güvenip ayni hak kazanan üçüncü kişi korunur; bu hâlde aynen iade mümkün olmaz, tazminata gidilir. İyiniyetin sınırı m.3'tür; durumun gerektirdiği özen gösterilmemişse koruma yoktur.
6. **Tedbir**: Kaydın üçüncü kişiye devrini önlemek için tapuya ihtiyati tedbir şerhi istenir (HMK m.389 vd.; TMK m.1010).
7. **Ara sonuç**: İyiniyetli kazanım yoksa iptal-tescil; varsa gerçek hak sahibine tazminat (gerekirse m.1007 yolu).

## Çıktı modülleri
- Tapu iptali ve tescil dava dilekçesi iskeleti (kayıt, sebep, terditli tenkis talebi).
- Muvazaa/iyiniyet değerlendirme tablosu (bedel-emsal, özen, devir zinciri).
- İhtiyati tedbir/şerh dilekçesi notu; yetki HMK m.12 (taşınmazın yeri).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

