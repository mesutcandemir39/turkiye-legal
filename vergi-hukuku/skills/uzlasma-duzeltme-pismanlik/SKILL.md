---
argument-hint: ''
description: Tarhiyat öncesi/sonrası uzlaşma, vergi hatasında düzeltme-şikâyet ve
  pişmanlık yollarından hangisinin uygun olduğunu seçmek; dava öncesi idari çözüm
  değerlendirilirken kullanılır.
name: uzlasma-duzeltme-pismanlik
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


# Uzlaşma, Düzeltme ve Pişmanlık

## Görev
Bir vergi/ceza uyuşmazlığında idari çözüm yollarını (uzlaşma, düzeltme-şikâyet, pişmanlık, cezada indirim) karşılaştırıp en uygun olanı seçmek ve dava süresiyle ilişkisini kurmak.

## Soğuk başlangıç (intake)
1. Henüz tarhiyat tamamlanmadı mı (tarhiyat öncesi) yoksa ihbarname tebliğ edildi mi (tarhiyat sonrası)?
2. Uyuşmazlık miktar/değerlendirme farkı mı, yoksa açık bir vergi hatası mı?
3. Beyan dışı bırakılan matrah var mı (pişmanlık ihtimali)?
4. Tebliğ tarihi ve kalan dava açma süresi nedir?
5. Kaçakçılık (VUK m.359) fiili iddiası var mı?

## Denetim şeması
1. **Yol elemesi:** Açık vergi hatası (hesap hatası, mükellefin şahsında/mevzuda/dönemde hata — VUK m.117-118) varsa düzeltme; takdir/değerlendirme farkı varsa uzlaşma; beyan eksikliği henüz tespit edilmeden bildirilecekse pişmanlık.
2. **Uzlaşma:** Tarhiyat öncesi uzlaşma VUK Ek m.11 (inceleme aşamasında, ihbarname öncesi); tarhiyat sonrası uzlaşma VUK Ek m.1 vd. (ihbarname tebliğinden itibaren 30 gün içinde başvuru). Vergi ziyaının kaçakçılık (m.359) fiilinden kaynaklandığı tarhiyat uzlaşma kapsamı dışındadır.
3. **Sürenin durması:** Uzlaşma talebi dava açma süresini durdurur; uzlaşma sağlanamaz/temin edilemezse kalan süre (en az 15 gün) içinde dava açılır (VUK Ek m.7). Bu köprüyü mutlaka kur.
4. **Düzeltme-şikâyet:** VUK m.116-126 — düzeltme talebi reddedilirse Hazine ve Maliye Bakanlığına şikâyet (m.124), oradan da ret/zımni ret üzerine vergi mahkemesinde dava. Dava açma süresi geçmiş hatalarda bu yol bir "ikinci şans" sağlar.
5. **Pişmanlık:** VUK m.371 — haber verme dilekçesi, 15 gün içinde beyan ve ödeme şartı; sağlanırsa vergi ziyaı cezası kesilmez ve kaçakçılık yönünden koruma sağlanabilir. İnceleme/ihbar başlamadan başvuru şarttır.
6. **İndirim:** VUK m.376 — cezada indirim, dava açmama ve süresinde ödeme şartıyla. Ara sonuç: seçilen yolun tutar, süre ve dava hakkına etkisi netleştirilir.

## Çıktı modülleri
- Yol karşılaştırma matrisi (uygunluk / tutar etkisi / dava hakkı / süre).
- Seçilen yola uygun başvuru/dilekçe taslağı (uzlaşma, düzeltme veya pişmanlık).
- Süre köprüsü takvimi (talep → sonuç → kalan dava süresi).
- Müvekkile karar notu (lehe-aleyhe değerlendirme).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

