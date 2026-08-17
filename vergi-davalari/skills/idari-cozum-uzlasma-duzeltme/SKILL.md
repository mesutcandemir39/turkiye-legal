---
argument-hint: ''
description: Dava açmadan önce uzlaşma, düzeltme-şikâyet ve izaha davet gibi idari
  çözüm yollarının uygunluğunu, süre ve dava hakkına etkisini değerlendirip seçim
  yapmak için kullanılır.
name: idari-cozum-uzlasma-duzeltme
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
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İdari Çözüm Yolları (Uzlaşma, Düzeltme, İzaha Davet)

## Görev
Uyuşmazlığı dava yoluna taşımadan önce idari çözüm seçeneklerini (uzlaşma, düzeltme-şikâyet, izaha davet) maliyet-fayda ve dava hakkına etki bakımından değerlendirmek; doğru yolu seçerek ceza ve süre avantajını kullanmak.

## Soğuk başlangıç (intake)
1. Uyuşmazlık bir hukuki yorum farkından mı, yoksa açık bir hesap/maddi hatadan mı kaynaklanıyor?
2. Henüz ihbarname tebliğ edildi mi, yoksa inceleme aşamasında mı (izaha davet imkânı var mı)?
3. Vergi aslı + ceza tutarı ne; uzlaşmada makul indirim beklenir mi?
4. Müvekkilin önceliği hızlı kesinlik mi, yoksa esasta haklılığın tescili mi?

## Denetim şeması
1. **Vergi hatası mı, ihtilaf mı.** Açık vergi hatası (hesap hatası, mükellefte/konuda/dönemde yanılma — VUK m.117-118) varsa düzeltme-şikâyet yolu (m.116-126) daha hızlı ve ucuzdur. Hukuki yorum farkı düzeltmeye konu olmaz, dava/uzlaşma gerekir.
2. **Uzlaşma.** Tarhiyat öncesi (VUK Ek m.11) inceleme sonrası ihbarname öncesinde; tarhiyat sonrası (Ek m.1 vd.) ihbarname tebliğinden sonra 30 gün içinde. Uzlaşmanın vaki olması dava hakkını sona erdirir (Ek m.7); kapsamı ve ceza indirimi tartılır. VUK m.359 fiilleri ve usulsüzlük cezalarının uzlaşma kapsamı dışı kaldığı not edilir.
3. **İzaha davet.** VUK m.370 — ön tespit aşamasında izah ile vergi ziyaı cezasında indirimli kapanış imkânı; sahte belge sınırlamaları kontrol edilir.
4. **Süreye etki.** Uzlaşma talebi dava süresini durdurur (Ek m.7); uzlaşma temin edilemezse kalan süre (en az 15 gün) içinde dava. Düzeltme-şikâyet reddi sonrası dava süresi ayrı işler (VUK m.124). Ara sonuç: seçilen yolun süreyi nasıl etkilediği takvime işlenir.
5. **Seçim.** Ceza indirimi (VUK m.376), uzlaşma indirimi ve dava şansı yan yana konularak öneri yapılır; yollar birbirini dışlayabildiğinden tek bir strateji seçilir.

## Çıktı modülleri
- İdari yol karşılaştırma tablosu (kapsam / indirim / dava hakkı / süre).
- Uzlaşma veya düzeltme-şikâyet başvuru taslağı.
- Strateji önerisi ve süre uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

