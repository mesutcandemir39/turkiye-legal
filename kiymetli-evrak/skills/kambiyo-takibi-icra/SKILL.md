---
argument-hint: ''
description: Çek-bono-poliçeye dayalı kambiyo senetlerine özgü haciz/iflas yolunu,
  ödeme emrine itiraz ve imza/borç itirazını yürütmek; alacağın icra yoluyla tahsili
  veya borçlu savunması için kullanılır.
name: kambiyo-takibi-icra
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
  - ad: Çek Kanunu
    numara: '5941'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kambiyo Senetlerine Özgü Takip

## Görev
Kambiyo senedine (çek, bono, poliçe) dayalı icra takibini başlatmak veya ona karşı savunma kurmak; özgü takip yolunun şartlarını, ödeme emrine itiraz usulünü ve sürelerini yönetmek.

## Soğuk başlangıç (intake)
- Senet kambiyo vasfını taşıyor mu (şekil şartları tam mı)?
- Takip alacaklısı yetkili hamil mi; vade geldi mi / çek ibraz edildi mi?
- Müvekkil takip alacaklısı mı, borçlu mu; borçlu hangi sıfatla (düzenleyen, ciranta, avalist) takip ediliyor?
- Ödeme emri tebliğ edildi mi; tebliğ tarihi nedir?

## Denetim şeması
1. Yola elverişlilik: senet kambiyo senedi olmalı ve takip yetkili hamil tarafından, vadesi gelmiş/ibraz edilmiş senetle başlatılmalı (İİK m.167). Eksik senetle bu yol kullanılamaz.
2. Ödeme emri ve süre: borçluya İİK m.168 ödeme emri gönderilir; ödeme süresi 10 gün, itiraz süresi 5 gündür.
3. İmza itirazı: borçlu imzaya itiraz ederse bunu açıkça ve ayrıca bildirmek zorundadır (İİK m.170); imza itirazı satışı durdurmaz ama icra mahkemesi inceler. İmza itirazının reddinde para cezası riski vardır.
4. Borca itiraz: imza dışındaki itirazlar (ödeme, zamanaşımı, yetki) İİK m.169-169/a kapsamında icra mahkemesine yapılır; kural olarak takibi kendiliğinden durdurmaz, mahkemeden tedbir/itirazın kabulü gerekir.
5. İtirazın incelenmesi: icra (hukuk) mahkemesi yetkilidir; alacaklı belgelerle, borçlu da yazılı/usulüne uygun delillerle ispatlar. Sebepsiz itirazda tazminat (İİK m.169/a).
6. Menfi tespit/istirdat: borçlu borçlu olmadığını İİK m.72 ile genel mahkemede dava edebilir; takibi durdurmak için teminatla tedbir gerekir.
7. Ara sonuç: süre ve usul tutulmuşsa takip kesinleşir ve haciz-satış aşamasına geçilir; aksi halde itiraz/iptal yolları işletilir.

## Çıktı modülleri
- Takip talebi ve ödeme emri için veri seti (taraf, senet, bedel [doldurulacak]).
- Süre takvimi (tebliğ + 5/10 gün).
- Borçlu için itiraz dilekçesi (imza/borç/zamanaşımı/yetki) taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

