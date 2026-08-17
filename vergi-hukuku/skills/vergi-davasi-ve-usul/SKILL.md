---
argument-hint: ''
description: Vergi/ceza ihbarnamesi veya ödeme emrine karşı açılacak davada görevli-yetkili
  mahkemeyi, süreyi, dava şartlarını ve yürütmenin durdurulmasını belirlemek için
  kullanılır.
name: vergi-davasi-ve-usul
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
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  - ad: Gelir Vergisi Kanunu
    numara: '193'
    tur: kanun
  - ad: Kurumlar Vergisi Kanunu
    numara: '5520'
    tur: kanun
  - ad: Katma Değer Vergisi Kanunu
    numara: '3065'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Vergi Davası, Görev-Yetki ve Süreler

## Görev
Vergi uyuşmazlığını yargıya taşırken doğru mahkemeyi, doğru süreyi, dava türünü ve yürütmenin durması/durdurulması rejimini belirleyerek dava açılabilirliğini güvenceye almak.

## Soğuk başlangıç (intake)
1. Dava konusu işlem nedir (vergi/ceza ihbarnamesi, ödeme emri, düzeltme reddi, ihtirazi kayıtla beyan)?
2. İşlem hangi tarihte tebliğ edildi?
3. Daha önce uzlaşma/düzeltme talep edildi mi (süre durması var mı)?
4. İşlemi tesis eden idare (vergi dairesi) hangi yer?
5. Talep iptal mi, tahsilatın durdurulması mı?

## Denetim şeması
1. **Görev:** Vergi mahkemeleri 2576 sayılı Kanun ve İYUK kapsamında genel vergi/ceza uyuşmazlıklarına bakar; kaçakçılık suçu (VUK m.359) ceza mahkemesindedir. İdari işlem niteliği taşımayan özel hukuk ilişkisi değilse idari yargı yolu açıktır.
2. **Yetki:** İYUK m.37 — vergi uyuşmazlıklarında yetkili mahkeme, tarhiyatı/işlemi yapan vergi dairesinin bulunduğu yer vergi mahkemesidir.
3. **Süre:** İYUK m.7 genel kural 30 gün (tebliğden itibaren); ödeme emrine karşı AATUHK m.58 uyarınca 15 gün. Süreler hak düşürücüdür; uzlaşma talebi varsa VUK Ek m.7 ile durma hesabını uygula.
4. **Dava şartları:** Ehliyet ve menfaat (İYUK m.2), kesin/yürütülebilir işlem şartı, idari merci tecavüzü kontrolü (İYUK m.14-15). Dilekçe unsurları İYUK m.3 (taraflar, konu, sebepler, dayandığı deliller, tebliğ tarihi).
5. **Yürütmenin durması/durdurulması:** İYUK m.27/4 — vergi mahkemesinde dava açılması, tarh edilen vergi/ceza ve gecikme faizinin tahsilini kendiliğinden durdurur; ancak ihtirazi kayıtla beyan üzerine açılan dava ile ödeme emrine karşı açılan davada otomatik durma yoktur, ayrıca yürütmenin durdurulması (İYUK m.27/2 — açıkça hukuka aykırılık + telafisi güç zarar) talep edilir.
6. **Kanun yolları:** İstinaf (BİM) ve temyiz (Danıştay) parasal sınır ve İYUK m.45-46 çerçevesinde. Ara sonuç: dava açılabilir mi, hangi sürede, hangi mahkemede, durma rejimi nedir?

## Çıktı modülleri
- Görev-yetki-süre tespit kartı.
- Yürütmenin durması/durdurulması analiz notu (otomatik mi, talep mi?).
- Dava dilekçesi iskeleti (İYUK m.3 unsurlarıyla).
- Kanun yolu ve parasal sınır takvimi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

