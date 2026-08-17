---
argument-hint: ''
description: Beraat, mahkûmiyet, düşme gibi hüküm türlerini ayırt etmek; cezanın ertelenmesi,
  hükmün açıklanmasının geri bırakılması ve adli para cezasına çevirmeyi değerlendirmek
  gerektiğinde kullanılır.
name: hukum-ve-erteleme-hagb
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
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Hüküm Türleri, Erteleme ve HAGB

## Görev
Mahkemenin verebileceği hüküm türlerini ve cezaya bağlı bireyselleştirme kurumlarını (erteleme, HAGB, seçenek yaptırım) değerlendirmek; sanık lehine talepleri kurmak.

## Soğuk başlangıç (intake)
- Yargılama sonunda hangi hüküm bekleniyor/verildi?
- Verilecek hapis cezası 2 yıl ve altında mı (HAGB/erteleme eşiği)?
- Sanığın sabıkası var mı; daha önce HAGB/erteleme uygulandı mı?
- Mağdurun zararı giderildi mi, sanık kabul ediyor mu?
- Hüküm tefhim edildiyse kanun yolu süresi işliyor mu?

## Denetim şeması
1. **Hüküm türleri.** Mahkeme beraat, ceza verilmesine yer olmadığı, mahkûmiyet, güvenlik tedbirine hükmedilmesi, davanın reddi veya düşmesine karar verir (CMK m.223). Hangi koşulda hangi hükmün verileceği m.223/2-9'da ayrılır.
2. **HAGB.** 2 yıl veya altı hapis/adli para cezasında, sanık daha önce kasıtlı suçtan mahkûm olmamışsa, zarar giderilmişse ve mahkemece yeniden suç işlemeyeceği kanaati oluşursa hükmün açıklanması geri bırakılabilir (CMK m.231/5-6). 5 yıl denetim süresi uygulanır; sanığın kabulü gerekir. Karara itiraz yolu açıktır (m.231/12).
3. **Cezanın ertelenmesi.** 2 yıl veya altı hapis cezası, koşulları varsa ertelenebilir (TCK m.51); 1-3 yıl denetim süresi belirlenir.
4. **Seçenek yaptırımlar.** Kısa süreli hapis (1 yıl ve altı), adli para cezasına veya TCK m.50'deki tedbirlere çevrilebilir.
5. **Sıra ilkesi.** Uygulamada önce ceza belirlenir, sonra seçenek yaptırım/erteleme/HAGB sırasıyla değerlendirilir; her birinin reddi gerekçelendirilmelidir.
6. **Ara sonuç.** Eşik ve koşullar sağlanıyorsa ilgili kurumun uygulanması talep edilir; reddedilirse gerekçesizlik kanun yolu sebebi olur.

## Çıktı modülleri
- Hüküm türü ve bireyselleştirme uygunluk tablosu.
- HAGB/erteleme/seçenek yaptırım talebi gerekçesi.
- Zarar giderimi ve kabul beyanı notu.
- Karara itiraz/kanun yolu yönlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

