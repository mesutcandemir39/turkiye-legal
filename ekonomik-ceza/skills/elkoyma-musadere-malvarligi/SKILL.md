---
argument-hint: ''
description: Ekonomik suç dosyalarında taşınmaz/hak/alacaklara elkoyma (CMK m.128),
  eşya ve kazanç müsaderesi (TCK m.54-55), tedbire itiraz ve malvarlığının iadesi/serbest
  bırakılması söz konusu olduğunda kullanıl
name: elkoyma-musadere-malvarligi
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Kaçakçılıkla Mücadele Kanunu
    numara: '5549'
    tur: kanun
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Elkoyma, Müsadere ve Malvarlığı Tedbirleri

## Görev
Ekonomik suç soruşturma ve kovuşturmasında uygulanan elkoyma/müsadere tedbirlerinin hukuki dayanağını ve sınırlarını denetlemek; tedbire itiraz ve malvarlığının korunması stratejisini kurmak.

## Soğuk başlangıç (intake)
- Hangi malvarlığına, hangi kararla elkonuldu? (taşınmaz, banka hesabı, şirket payı, araç)
- Karar mercii: hâkim/mahkeme kararı mı, gecikmesinde sakınca olan halde savcılık/kolluk mu?
- Tedbir suçla ve elde edilen menfaatle orantılı mı?
- Üçüncü kişinin (iyiniyetli malik) hakkı etkileniyor mu?

## Denetim şeması
1. **Elkoyma dayanağı (CMK)**: Genel elkoyma CMK m.123 vd.; taşınmaz, hak ve alacaklara elkoyma m.128 — bu tedbir ancak kanunda sayılan katalog suçlar (aklama, zimmet, irtikâp, rüşvet, dolandırıcılık nitelikli halleri, vergi kaçakçılığı vb.) bakımından ve suçun işlendiğine dair somut delillere dayanan kuvvetli şüphe varsa uygulanabilir. Hâkim/mahkeme kararı esastır.
2. **Orantılılık ve şüphe yoğunluğu**: m.128 kuvvetli şüphe ve değerin suçtan elde edildiğine dair somut delil arar; tedbir suç konusu değerle orantılı olmalıdır. Bu eşik savunmanın ana itiraz noktasıdır.
3. **Müsadere (TCK m.54-55)**: Eşya müsaderesi (m.54 — suçta kullanılan/üretilen eşya) ile kazanç müsaderesi (m.55 — suçtan elde edilen ve dönüştürülen değerler) ayrılır. İyiniyetli üçüncü kişiye ait eşya müsadere edilemez (m.54/2).
4. **İtiraz yolu**: Elkoyma kararına CMK genel itiraz hükümleri (m.267 vd.) uyarınca itiraz edilir; mercii ve süre kontrol edilir.
5. **İade/serbest bırakma**: Şüphe ortadan kalktığında, tedbir konusu değerin işletmenin faaliyetini durduracak nitelikte olduğunda veya orantısızlıkta, kısmi serbest bırakma/teminatla iade talep edilir.
6. **Ara sonuç**: Tedbirin dayanağı, orantılılığı, üçüncü kişi hakları ve itiraz/iade imkânı netleşir.

## Çıktı modülleri
- Elkoyma dayanağı ve katalog suç kontrolü
- Orantılılık/şüphe eşiği itiraz notu
- Eşya/kazanç müsaderesi ayrımı
- Üçüncü kişi (iyiniyetli malik) hak analizi
- İtiraz veya iade/teminat talebi dilekçe taslağı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

