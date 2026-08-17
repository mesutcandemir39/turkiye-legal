---
argument-hint: ''
description: İdari itiraz tüketildikten sonra gümrük uyuşmazlığını vergi/idare mahkemesine
  taşımak gerektiğinde; görev-yetki, dava türü, süreler ve yürütmenin durdurulmasını
  planlamak için kullanılır.
name: idari-dava-ve-yargi
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
  - ad: Gümrük Müsait Müşterek Gümrük Bölgeleri Hakkında Kanun
    numara: '4458'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İdari Dava ve Yargı Yolu

## Görev
Gümrük ek tahakkuk ve ceza kararlarına karşı idari itiraz tüketildikten sonra açılacak iptal/tam yargı davasını planlamak; görevli mahkeme, dava türü, süreler ve yürütmenin durdurulması ile kanun yollarını doğru kurgulamak.

## Soğuk başlangıç (intake)
- İdari itiraz reddedildi mi; ret kararı/zımni ret tarihi nedir?
- Uyuşmazlık esas olarak vergisel (ek tahakkuk, vergi cezası) mi yoksa salt idari işlem mi?
- Dava açma süresi içinde miyiz; tahsilat işlemi (ödeme emri) başladı mı?
- Tahsilatı durdurmak için yürütmenin durdurulması ve teminat gerekli mi?

## Denetim şeması
1. Görev: Gümrük vergileri ve bunlara bağlı cezalardan doğan uyuşmazlıklar vergi mahkemesinin görev alanındadır; vergiyle ilgisi olmayan salt idari işlemler idare mahkemesinde görülür. Doğru görevli mahkeme dava şartıdır.
2. Yetki: Kural olarak işlemi/tahakkuku yapan gümrük idaresinin bulunduğu yer mahkemesi yetkilidir (İYUK m.37 vd. çerçevesinde).
3. Dava türü: Ek tahakkuk/cezanın iptali için iptal davası; ödenmiş tutarın iadesi veya zarar için tam yargı davası açılır (İYUK m.2).
4. Süre: İdari itirazın reddinin (veya zımni reddin) tebliğinden itibaren İYUK m.7 süresi içinde (vergi mahkemesinde 30 gün) dava açılır. Sürenin doğru başlangıç anı (ret tebliği/zımni ret) titizlikle saptanır.
5. Yürütmenin durdurulması: Tahsilatı durdurmak için İYUK m.27 uyarınca YD talep edilir; teminat ve telafisi güç zarar koşulları değerlendirilir.
6. İspat ve deliller: Beyanname, fatura, menşe/kıymet belgeleri, idari işlem dosyası ve gerekirse bilirkişi/ekspertiz; ispat yükü dağılımı esasa göre kurulur.
7. Kanun yolları: İlk derece kararına karşı istinaf (BİM), istinaf üzerine temyiz (Danıştay) yolları ve süreleri gözetilir.
8. Ara sonuç: Görevli/yetkili mahkeme, dava türü, süre ve YD stratejisi netleşir; dava dilekçesi iskeleti hazırlanır.

## Çıktı modülleri
- Görev-yetki-süre-YD karar tablosu
- İptal/tam yargı dava dilekçesi taslağı [doldurulacak alanlarla]
- Delil dizini ve ispat yükü planı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

