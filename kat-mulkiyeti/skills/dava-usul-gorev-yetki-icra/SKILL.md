---
argument-hint: ''
description: KMK uyuşmazlığında dava açılmadan önce görevli/yetkili mahkeme, dava
  şartları, süreler, husumet ve aidat alacağının icra takibi ile ihtiyati tedbir stratejisinin
  belirlenmesi gerektiğinde; doğru usul
name: dava-usul-gorev-yetki-icra
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
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kat Mülkiyetinde Usul, Görev-Yetki ve İcra

## Görev
KMK'dan doğan davanın usulî çerçevesini kurmak: görevli ve yetkili mahkemeyi, dava şartlarını ve süreleri, husumeti (kim kime karşı), aidat alacağının icra yolunu ve gerekli ihtiyati tedbir/şerh stratejisini belirlemek.

## Soğuk başlangıç (intake)
- Talep türü ne: karar iptali, aidat/gider alacağı, projeye/ortak yere aykırılığın giderilmesi, çıkarma, yönetici hesabı?
- Uyuşmazlık tek anagayrimenkulü mü yoksa toplu yapıyı mı ilgilendiriyor?
- İşliyor olabilecek süreler var mı (karar iptalinde 1 ay/6 ay; işletme projesine itirazda 7 gün)?
- Aidat alacağı için icra takibi başlatılacak mı; itiraz bekleniyor mu?

## Denetim şeması
1. **Görev (KMK m.33 ve Ek hükümler)**: Kat mülkiyetinden kaynaklanan davalar — karar iptali, gider alacağı, projeye aykırılık, yönetici hesabı, çıkarma — kural olarak **sulh hukuk mahkemesinde** görülür. Görev kesindir, re'sen gözetilir.
2. **Yetki**: Davalarda yetki **anagayrimenkulün bulunduğu yer** mahkemesine aittir; taşınmazın aynına ilişkin nitelik nedeniyle bu yetki kesindir (HMK m.12 ile uyumlu). Sözleşmeyle değiştirilemez.
3. **Süreler**: Karar iptalinde m.33/1 süreleri (katılıp aykırı oy kullanan için 1 ay; katılmayan için öğrenmeden 1 ay, her hâlde 6 ay); işletme projesine itirazda 7 gün (m.37); gider alacağında genel zamanaşımı (TBK m.146/m.147 — periyodik edim niteliğine göre değerlendirilir) işler.
4. **Husumet**: Karar iptali ve aykırılık davaları diğer kat maliklerine veya temsilen yöneticiye; aidat alacağı borçlu malike (ve gerektiğinde müteselsil sorumlu kiracıya, m.22) yöneltilir. Çıkarma davasında husumet ilgili malike kurulur.
5. **İcra yolu**: Kesinleşmiş işletme projesi/karar gider tablosuyla ilamsız icra (İİK m.42 vd.); m.37 belgesi İİK m.68 kapsamında değerlendirilir; itiraz hâlinde itirazın iptali (İİK m.67) veya kaldırılması (m.68). Teminat için KMK m.22/2 kanuni ipoteği tescil ettirilir.
6. **İhtiyati tedbir (HMK m.389 vd.)**: Devam eden izinsiz inşaatın durdurulması, ortak yere el atmanın men'i veya kararın icrasının ertelenmesi için tedbir istenir; yaklaşık ispat ve teminat gerekir.
7. **Ara sonuç**: Sulh hukuk + anagayrimenkulün yeri + süre kontrolü + doğru husumet → dava; alacakta İİK yolu + kanuni ipotek.

## Çıktı modülleri
- Görev/yetki ve süre kontrol listesi.
- Husumet tablosu (karar iptali / alacak / çıkarma için davalı tayini).
- İcra takip ve itirazın iptali yol haritası.
- İhtiyati tedbir/şerh dilekçesi iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

