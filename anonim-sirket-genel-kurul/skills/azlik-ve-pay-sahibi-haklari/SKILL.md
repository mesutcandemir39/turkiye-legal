---
argument-hint: ''
description: Azligin cagri ve gundeme madde ekletme, finansal tablolarin ertelenmesi,
  ozel denetci atanmasi ve haklı sebeple fesih gibi haklari ile pay sahibinin bilgi
  alma-inceleme hakki kullanilacaksa kullanilir
name: azlik-ve-pay-sahibi-haklari
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
  version: 0.1.0
user-invocable: true
---


# Azlık ve Pay Sahibi Hakları

## Görev
Sermayenin onda birini (halka açıkta yirmide birini) oluşturan azlığın ve tek tek pay sahiplerinin genel kurul çevresindeki haklarını harekete geçirmek veya bunlara karşı şirketi savunmak.

## Soğuk başlangıç (intake)
1. Müvekkilin/grubun pay oranı azlık eşiğini (1/10; halka açıkta 1/20) karşılıyor mu?
2. Talep çağrı/gündem mi, finansal tablo ertelemesi mi, özel denetim mi, fesih mi?
3. Bilgi alma-inceleme talebi GK'de gündeme getirildi ve reddedildi mi?
4. YK çağrı/gündem talebini reddetti mi; mahkeme yoluna gidilecek mi?

## Denetim şeması
1. **Çağrı ve gündem:** Azlık, gerektirici sebepleri ve gündemi belirterek YK'den GK'yi toplantıya çağırmasını veya gündeme madde eklenmesini noter aracılığıyla isteyebilir (m.411). YK reddeder veya yedi iş günü içinde olumlu cevap vermezse, azlık şirket merkezinin bulunduğu yer asliye ticaret mahkemesinden çağrı/gündem iznini ister (m.412).
2. **Finansal tabloların ertelenmesi:** Finansal tabloların müzakeresi ve buna bağlı konular, azlığın istemi üzerine bir ay sonraya **bir kez** ertelenir; ikinci erteleme için yeni/ciddi sebep gerekir (m.420). Bu hak gündeme bağlılıktan bağımsızdır.
3. **Özel denetçi:** Pay sahibi, kullanılması bilgi alma/inceleme hakkına bağlı belirli olayların açıklığa kavuşması için özel denetim isteyebilir; GK kabul ederse mahkemeden, reddederse azlık (sermayenin onda biri/halka açıkta yirmide biri) mahkemeden özel denetçi atanmasını talep eder (m.438-439).
4. **Bilgi alma ve inceleme:** Her pay sahibi GK'de YK'den şirket işleri, denetçiden denetim hakkında bilgi isteyebilir; bilgi verilmesi dürüstlük kuralına uygun olmalı, şirket sırrı sınırı gözetilmelidir (m.437). Haksız ret, bu konudaki kararı iptale ve özel denetim talebine zemin hazırlar.
5. **Haklı sebeple fesih:** Sermayenin onda birini (halka açıkta yirmide birini) temsil eden pay sahipleri, haklı sebeplerin varlığında şirketin feshini mahkemeden isteyebilir; mahkeme fesih yerine duruma uygun başka çözüme de (örn. paylarının gerçek değerle alınması) hükmedebilir (m.531).
6. **İspat yükü/ara sonuç:** Azlık eşiği ve haklı sebebi talep eden ispatlar. Usulüne uygun talep reddedilmişse mahkeme yolu açılır; aksi hâlde talep dava şartı yokluğundan reddedilir.

## Çıktı modülleri
- Noter ihtarnamesi/çağrı-gündem talep taslağı.
- Mahkemeye özel denetçi/çağrı izni başvuru iskeleti.
- Azlık hakları eşik ve süre kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

