---
argument-hint: ''
description: Taşıma alacak ve tazminat taleplerinde ihbar/rezerv süreleri ile zamanaşımının
  (TTK 1/3 yıl, CMR 1/3 yıl) hesaplanması, başlangıç anının ve durma-kesilme hallerinin
  belirlenmesi gerektiğinde kullanılı
name: sureler-ve-zamanasimi
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


# Süreler ve Zamanaşımı

## Görev
Taşımaya özgü kısa zamanaşımı ve hak düşürücü/ihbar sürelerini doğru hesaplamak; başlangıç anı, durma ve kesilme hallerini saptayarak hak kaybını önlemek.

## Soğuk başlangıç (intake)
1. Talep neyden doğuyor: ziya, hasar, gecikme, taşıma ücreti mi?
2. Taşıma TTK'ya mı CMR'ye mi tabi?
3. Teslim/teslim için kararlaştırılan tarih nedir; olaydan bu yana ne kadar geçti?
4. Taşıyıcının kastı veya ağır kusuru iddia ediliyor mu?

## Denetim şeması
1. **TTK zamanaşımı:** TTK m.855/1 — taşıma sözleşmesinden doğan bütün istemler bir yılda zamanaşımına uğrar. m.855/2 — taşıyıcının kastı veya kasta eş kusuru (m.886 anlamında) varsa süre üç yıldır.
2. **Başlangıç anı (TTK):** Genel kural teslim tarihi; ziyada eşyanın teslim edilmesi gereken tarih; gecikmede teslim tarihi (m.855/3 atfıyla belirlenir).
3. **CMR zamanaşımı:** CMR m.32 — kural 1 yıl; kasıt veya lex fori'ye göre kasta eş kusurda 3 yıl. Başlangıç: kısmi ziya/hasar/gecikmede teslim günü; tam ziyada teslim için kararlaştırılan sürenin bitiminden 30 gün (veya kararlaştırılmamışsa 60 gün) sonra (m.32/1).
4. **Durma/kesilme (CMR):** m.32/2 — yazılı talep zamanaşımını durdurur; taşıyıcının yazılı reddi ve belgelerin iadesiyle yeniden işler. Sonraki aynı konulu taleplerin durdurucu etkisi yoktur.
5. **İhbar/rezerv süreleri:** Ayrıca TTK m.889 / CMR m.30 süreleri (teslimde, 7 gün, 21 gün) hak/karine kaybına yol açar — zamanaşımından ayrı izlenir.
6. **Defi niteliği:** Zamanaşımı def'i taraflarca ileri sürülmedikçe hâkim re'sen dikkate almaz (TBK m.161).
7. **Ara sonuç:** Talebin canlı/zamanaşımına uğramış olduğu ve durdurma imkânları.

## Çıktı modülleri
- Zamanaşımı hesap tablosu (başlangıç, süre, bitiş; TTK/CMR ayrı).
- İhbar/rezerv süresi takvimi.
- Süreyi durdurma/kesme stratejisi notu (yazılı talep, dava, takip).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

