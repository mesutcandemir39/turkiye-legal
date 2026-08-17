---
argument-hint: ''
description: Eşyanın geç teslimi, kaybı veya hasarı sonrası ihbar/rezerv sürelerinin
  tutturulması, zararın belgelenmesi ve talebin doğru muhataba yöneltilmesi gerektiğinde
  kullanılır; hak kaybı doğuran sürelere od
name: gecikme-ziya-hasar-talepleri
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


# Gecikme, Ziya ve Hasar Taleplerinin Yönetimi

## Görev
Zarar olayı sonrası hak sahibinin yapması gereken ihbar/rezerv işlemlerini süresinde planlamak, zararı belgelemek ve talebi doğru taşıyıcıya yöneltmek; hak kaybını önlemek.

## Soğuk başlangıç (intake)
1. Olay ne: gecikme mi, tam/kısmi ziya mı, hasar mı; hasar açık mı gizli mi?
2. Eşya teslim alındı mı; teslim tarihi nedir; ihbar/rezerv yapıldı mı?
3. Taşıma iç hukuka mı (TTK) yoksa CMR'ye mi tabi?
4. Zarar nasıl belgelendi (tutanak, fotoğraf, ekspertiz, fatura)?

## Denetim şeması
1. **İhbar/rezerv süreleri (TTK):** TTK m.889 — açıkça belli hasarda teslim sırasında, gizli hasarda teslimi izleyen 7 gün içinde yazılı bildirim; gecikmede teslimden itibaren 21 gün içinde bildirim. Süre kaçırılırsa eşyanın doğru teslim edildiği varsayılır.
2. **İhbar/rezerv süreleri (CMR):** CMR m.30 — açık hasarda teslimde, gizli hasarda 7 gün, gecikmede 21 gün. Rezervsiz teslim, iyi teslim karinesi doğurur.
3. **Ziyanın belgelenmesi:** Tam ziya halinde teslim için kararlaştırılan sürenin (kural olarak 30 gün, sözleşmesel sürenin sonu) geçmesiyle eşya kaybolmuş sayılabilir (CMR m.20). Tutanak, ekspertiz ve değer belgeleri toplanmalı.
4. **Muhatabın belirlenmesi:** Akdî taşıyıcı, fiilî taşıyıcı (TTK m.879) ve komisyoncu (m.926-928) arasında doğru muhatap seçilmeli; müteselsil sorumluluk değerlendirilmeli.
5. **Tazminatın kapsamı:** Ziya/hasarda eşya değeri ve m.882 sınırı; CMR m.23/4 uyarınca taşıma ücreti ve masraflar.
6. **Zamanaşımı:** TTK m.855 / CMR m.32 (1 yıl; kasıt-ağır kusurda 3 yıl). Yazılı talep CMR'de süreyi durdurur (m.32/2).
7. **Ara sonuç:** Hangi taleplerin canlı, hangilerinin sürede/zamanaşımında düştüğü.

## Çıktı modülleri
- İhbar/rezerv süre takvimi ve hak kaybı uyarı listesi.
- Zarar belgeleme kontrol listesi (tutanak/ekspertiz/fatura).
- Talep mektubu taslağı (muhatap, dayanak madde, tutar, süre durdurma).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

