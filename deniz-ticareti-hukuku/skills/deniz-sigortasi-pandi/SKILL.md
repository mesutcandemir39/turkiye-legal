---
argument-hint: ''
description: Gemi (tekne), yük veya sorumluluk (P&I) sigortalarında riziko, beyan
  yükümlülüğü, tazminat ve rücu uyuşmazlıkları çıktığında; poliçe ve kulüp kuralları
  çerçevesinde teminat kapsamını ve sigortacının r
name: deniz-sigortasi-pandi
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


# Deniz Sigortası ve P&I

## Görev
Tekne, yük veya sorumluluk (P&I) sigortasında rizikonun teminat kapsamında olup olmadığını, sigortalının beyan ve özen yükümlülüklerini, tazminat hesabını ve sigortacının halefiyet/rücu hakkını değerlendirmek.

## Soğuk başlangıç (intake)
- Sigorta türü nedir (tekne/H&M, yük/kargo, sorumluluk/P&I)?
- Poliçe hangi klozlara tabi (örn. Institute Clauses) ve P&I kulüp kuralları nasıl?
- Riziko gerçekleşti mi; sebep nedir; istisna kapsamına giriyor mu?
- Sigortalı beyan ve değişiklik bildirim yükümlülüklerini yerine getirdi mi?

## Denetim şeması
1. **Sözleşme ve uygulanacak kurallar**: Deniz sigortasına TTK m.1401 vd. genel hükümleri ile poliçe/kloz ve P&I kulüp kuralları birlikte uygulanır; emredici ve düzenleyici hükümleri ayırt et.
2. **Beyan yükümlülüğü**: Sigortalının riziko sözleşme yapılırken doğru beyan ve sonradan ağırlaşmayı bildirme borcunu denetle; ihlalin sigortacıya cayma/tazminattan kaçınma hakkı verip vermediğini değerlendir.
3. **Teminat ve istisnalar**: Rizikonun teminat kapsamında olup olmadığını, klozdaki istisnaları (savaş, kötü niyet, denize elverişsizlik bilgisi) ve sigortalının özen borcunu kontrol et.
4. **Tazminat hesabı ve sovtaj**: Tam/kısmi zıya, müşterek avarya katkısı, kurtarma masrafı ve sovtaj (hurda) değerini dikkate alarak tazminatı hesapla; sigorta bedeli ile sigorta değeri ilişkisini (aşkın/eksik sigorta) uygula.
5. **Halefiyet/rücu ve ara sonuç**: Ödeme yapan sigortacı, sigortalının zarar verene karşı haklarına halef olur (TTK m.1472); P&I'da kulübün rücu ve "pay to be paid" kuralını değerlendir. Çıktıda teminat kararını ve rücu yolunu gerekçelendir; sigorta tazminatı zamanaşımına dikkat et.

## Çıktı modülleri
- Teminat/istisna değerlendirme tablosu
- Tazminat hesap taslağı (zıya türü, sovtaj, avarya)
- Rücu/halefiyet ve kulüp kuralı strateji notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

