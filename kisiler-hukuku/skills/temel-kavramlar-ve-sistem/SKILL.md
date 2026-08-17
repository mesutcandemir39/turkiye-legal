---
argument-hint: ''
description: Bir uyuşmazlıkta hangi kişi türünün ve hangi ehliyet katmanının söz konusu
  olduğunu, meselenin gerçek/tüzel kişi ya da koruma/ehliyet eksenine düştüğünü konumlandırmak
  için kullanılır.
name: temel-kavramlar-ve-sistem
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


# Kişiler Hukuku Temel Kavramları ve Sistematiği

## Görev
Somut olayın kişiler hukuku içindeki yerini sabitlemek: süjenin türü (gerçek/tüzel kişi), ehliyet durumu ve uyuşmazlığın hangi alt-rejime (ehliyet, kişilik hakkı koruması, ad, yerleşim yeri, dernek/vakıf) düştüğünü belirleyip doğru denetim şemasına yönlendirmek.

## Soğuk başlangıç (intake)
- Süje kim: gerçek kişi mi, dernek/vakıf/şirket gibi tüzel kişi mi?
- Gerçek kişiyse ehliyet durumu ne: ergin mi (18+), küçük mü, ayırt etme gücü var mı, kısıtlı/vesayet altında mı?
- Uyuşmazlık bir işlemin geçerliliği mi, yoksa kişilik değerine (şeref, beden, özel hayat, ad) bir saldırı mı?
- Hangi sonuç isteniyor: işlemin iptali/butlanı, saldırının durdurulması, tazminat, ad değişikliği, tescil?

## Denetim şeması
1. **Süje ayrımı** — Gerçek kişi (TMK m.8 vd.) mi tüzel kişi (m.47 vd.) mi? Tüzel kişide tür (dernek m.56 vd., vakıf m.101 vd., ticaret şirketi) ve organ yapısı (m.50) belirlenir.
2. **Hak ehliyeti** — TMK m.8: herkes eşit hak ehliyetine sahiptir; m.28: kişilik sağ ve tam doğumla başlar, ölümle biter; cenin koşullu hak ehlidir.
3. **Fiil ehliyeti katmanları** — TMK m.9-16: (a) tam ehliyetli (ergin + ayırt etme gücü + kısıtlı değil); (b) tam ehliyetsiz (ayırt etme gücü yok, m.14-15); (c) sınırlı ehliyetsiz (ayırt etme gücü olan küçük/kısıtlı, m.16); (d) sınırlı ehliyetli (kendisine yasal danışman atanan, m.429). Hangi katman, işlemin tek başına yapılıp yapılamayacağını belirler.
4. **Eksen seçimi** — İşlem geçerliliği sorunuysa ehliyet/temsil becerisine; kişilik değerine saldırı varsa m.24-25 koruma şemasına; ad sorunuysa m.26-27 becerisine; tüzel kişi sorunuysa dernek/vakıf becerisine yönlendir.
5. **Genel süzgeç** — TMK m.2 dürüstlük kuralı her sonucu denetler; ehliyetsizliğin dürüstlüğe aykırı biçimde ileri sürülmesi korunmaz.

## Çıktı modülleri
- Süje ve ehliyet teşhis tablosu (tür + katman + dayanak madde).
- Uyuşmazlığın düştüğü alt-rejim ve yönlendirilecek beceri.
- Görevli/yetkili mahkeme ön notu (TMK m.19 yerleşim yeri).
- Açık sorular ve `[doldurulacak]` veri yerleri.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

