---
argument-hint: ''
description: Cep telefonu, internet, dijital platform, spor salonu gibi abonelik sözleşmelerinde
  tüketicinin her zaman fesih hakkını, bedel iadesini ve taahhüt/cezai şart denetimini
  değerlendirmek gerektiğinde kul
name: abonelik-ve-suregelen-edim
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
  - ad: Tüketicinin Korunması Hakkında Kanun
    numara: '6502'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Abonelik ve Sürekli Edimli Sözleşmeler

## Görev
Abonelik ve sürekli edimli tüketici sözleşmelerinde tüketicinin fesih hakkını, fesih usulünü, peşin alınan bedelin iadesini ve taahhütlü aboneliklerdeki cezai şart/erken cayma bedeli denetimini altlamak.

## Soğuk başlangıç (intake)
- Abonelik konusu ne (haberleşme, internet, dijital içerik, üyelik) ve süresi belirli mi?
- Taahhüt/kampanya var mı; erken çıkışta bedel öngörülmüş mü?
- Tüketici feshetmek mi istiyor, yoksa fesih engelleniyor mu?
- Peşin ödenen bir bedel var mı, fesih usulü sözleşmede nasıl düzenlenmiş?

## Denetim şeması
1. **Fesih hakkı (TKHK m.52):** Tüketici, belirsiz süreli veya süresi bir yıldan uzun belirli süreli abonelik sözleşmesini herhangi bir gerekçe göstermeden ve cezai şart ödemeden istediği zaman feshedebilir.
2. **Fesih usulü ve kolaylığı (m.52):** Sağlayıcı, aboneliğin kurulduğu yöntemi/araçları ile aynı kolaylıkta fesih imkânı sunmak zorundadır; fesih, talebin ulaşmasından itibaren kısa sürede (Yönetmelikte öngörülen gün) hüküm doğurur.
3. **Bedel iadesi:** Fesih halinde tüketici, ifa edilmemiş kısma ilişkin peşin ödediği bedelin iadesini isteyebilir; kullanılmayan dönem orantılı biçimde geri verilir.
4. **Taahhüt ve cezai şart denetimi:** Taahhütlü aboneliklerde erken fesih bedeli, ancak sağlayıcının sunduğu cihaz/indirim gibi somut bir avantajla orantılıysa ve önceden açıkça bildirilmişse geçerlidir; orantısız ya da müzakere edilmemiş cezai şart m.5 haksız şart denetimine tabidir.
5. **Sektörel mevzuat:** Elektronik haberleşmede BTK düzenlemeleri tamamlayıcıdır; ancak TKHK m.52'nin tüketici lehine emredici fesih hakkı saklıdır.
6. **Ara sonuç:** Fesih hakkı doğmuş mu, erken çıkış bedeli geçerli mi, ne kadar bedel iade edilmeli?

## Çıktı modülleri
- Fesih hakkı ve usul değerlendirmesi.
- Fesih bildirimi taslağı.
- İade edilecek bedel hesabı.
- Cezai şart geçerlilik analizi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

