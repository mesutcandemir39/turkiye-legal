---
argument-hint: ''
description: Yargıtay, Danıştay, AYM, BAM/BİM veya ilk derece kararını müvekkilin
  anlayacağı dile çevirmek; ne kazanıldı ne kaybedildi, gerekçe ne, hangi yol açık
  sorularını yanıtlamak gerektiğinde kullanılır.
name: karar-sadelestirme
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Mahkeme Kararı Sadeleştirme

## Görev
Bir mahkeme kararını (ilk derece, istinaf, temyiz, AYM bireysel başvuru) müvekkilin "kazandık mı,
ne demek, şimdi ne olacak" sorularına cevap verecek şekilde yalınlaştırmak; hüküm fıkrasını,
gerekçeyi ve sonraki yolu net aktarmak.

## Soğuk başlangıç (intake)
1. Karar hangi merciden ve hangi aşama (ilk derece, BAM/BİM, Yargıtay/Danıştay, AYM)?
2. Müvekkil hangi tarafta ve sonuç onun lehine mi aleyhine mi?
3. Karar kesin mi, yoksa kanun yolu açık mı?
4. Okuyucunun en çok merak ettiği nokta (para, süre, sonraki adım)?

## Denetim şeması
1. HÜKÜM FIKRASINI BUL: Kararın bağlayıcı kısmı gerekçe değil hüküm fıkrasıdır. Sade metin önce
   "mahkeme ne karar verdi" sorusunu hüküm fıkrasından yanıtlar (kabul/ret/kısmen kabul,
   tazminat miktarı, vekâlet ücreti, yargılama gideri).
2. LEHE/ALEYHE NETLİĞİ: Sonucun müvekkil için anlamı açık yazılır; "davanın reddi" gibi ifadeler
   "talebimiz kabul edilmedi / karşı tarafın talebi reddedildi" diye okuyucuya göre çevrilir.
3. GEREKÇE ÖZÜ: Mahkemenin asıl dayandığı hukuki sebep (madde atfıyla) 2-3 cümlede verilir;
   yan değerlendirmeler özetlenir.
4. KANUN YOLU VE SÜRE (kritik sonuç): Karara karşı istinaf (HMK m.345 / İYUK m.45) veya temyiz
   (HMK m.361 / İYUK m.46) yolu ve süresi takvim tarihiyle belirtilir; kesinse "bu karar
   kesindir" denir. AYM bireysel başvuruda 30 günlük süre (6216 s. K. m.47) ayrıca anılır.
5. İÇTİHAT HİJYENİ: Kararın künyesi (mahkeme/daire/esas-karar no/tarih) aktarılırken doğrulanır;
   numara uydurulmaz, gerekirse karararama.yargitay.gov.tr / karararama.danistay.gov.tr ile
   teyit edilir, belirsizse "[DOĞRULANMADI]" bırakılır.
6. ARA SONUÇ: Hüküm fıkrası, lehe/aleyhe yorumu ve süre eksiksiz mi denetlenir.

## Çıktı modülleri
- "Sonuç tek cümlede" özeti.
- Ne kazandık / ne kaybettik tablosu (talep bazında).
- Gerekçe özü (madde atıflı).
- Sonraki adım ve son tarih; kesinlik notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

