---
argument-hint: ''
description: Eşyada ziya, hasar veya teslimde gecikme nedeniyle taşıyıcının sorumluluğunun
  kurulup kurulmadığını, kurtuluş sebeplerini ve sorumluluk sınırını adım adım denetlemek
  gerektiğinde kullanılır; taşıma uy
name: tasiyici-sorumlulugu-semasi
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


# Taşıyıcının Sorumluluğu Denetim Şeması

## Görev
Taşıyıcının ziya, hasar veya gecikmeden doğan sorumluluğunu objektif sorumluluk esasına göre kurmak, kurtuluş kademelerini denetlemek ve tazminatın hangi sınıra tabi olduğunu belirlemek.

## Soğuk başlangıç (intake)
1. Zarar türü nedir: tam/kısmi ziya (kayıp), hasar (hâsâr), yoksa teslimde gecikme mi?
2. Eşya teslim alma ile teslim arasındaki hangi aşamada zarar gördü; teslim gerçekleşti mi?
3. Eşyanın brüt ağırlığı, cinsi ve beyan edilen değeri nedir; özel değer/menfaat beyanı yapıldı mı (TTK m.880)?
4. Taşıyıcı tarafında kasıt veya pervasızca davranış iddiası var mı?

## Denetim şeması
1. **Sorumluluğun kurulması:** TTK m.875 — taşıyıcı, eşyayı teslim aldığı andan teslim edinceye kadar ziya, hasar ve gecikmeden kusuru aranmaksızın sorumludur. CMR'de karşılığı m.17/1.
2. **Genel kurtuluş:** TTK m.876 — kaçınılmaz olay, gönderen/gönderilen kusuru, eşyanın kendine özgü ayıbı ispatlanırsa taşıyıcı kurtulur. CMR m.17/2.
3. **Özel risk sebepleri (kanıt kolaylığı):** TTK m.878 — örtüsüz araç, ambalaj yokluğu, yükleme/boşaltmanın gönderence yapılması, eşyanın özel doğası, yetersiz işaretleme, canlı hayvan gibi hallerde sebep-zarar bağlantısı karine sayılır. CMR m.17/4 ve m.18/2.
4. **İspat yükü:** Zararın taşıma süresinde doğduğunu hak sahibi; kurtuluş sebebini taşıyıcı ispatlar (TTK m.875, m.876; CMR m.18/1).
5. **Sorumluluk sınırı:** TTK m.882/1 — kg başına 8,33 ÖÇH (SDR); gecikmede taşıma ücretinin üç katı (m.882/3). CMR m.23 ve m.25.
6. **Sınırın kalkması:** TTK m.886 / CMR m.29 — taşıyıcının kastı veya pervasızca ve zararın muhtemel olduğu bilinciyle hareketi varsa sınırlardan yararlanamaz; tam zarar tazmin edilir.
7. **Ara sonuç:** Sorumlu/sorumsuz; tazminatın sınırlı mı sınırsız mı hesaplanacağı.

## Çıktı modülleri
- Sorumluluk kuruluşu ve kurtuluş kademe tablosu.
- Tazminat sınırı hesabı (kg x 8,33 SDR x güncel kur) ve gecikme tavanı.
- Sınırın kalkması (m.886/CMR 29) yönünden risk değerlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

