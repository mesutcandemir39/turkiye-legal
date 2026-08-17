---
argument-hint: ''
description: Santral/altyapı yatırımlarında EPC ve O&M sözleşmeleri, proje finansmanı,
  teminat yapısı, hukuki durum tespiti ve izin-onay zinciri kurulurken kullanılır.
name: enerji-yatirim-epc-finansman
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
  - ad: Elektrik Piyasası Kanunu
    numara: '6446'
    tur: kanun
  - ad: Mühendislik ve Mimarlık Meslek Kanunu
    numara: '4646'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Enerji Yatırımı, EPC ve Proje Finansmanı

## Görev
Enerji yatırım projesinin sözleşmesel ve finansal mimarisini kurmak; EPC/O&M risk dağılımını, proje finansmanı teminat paketini ve izin-onay zincirini denetleyerek kapanışa hazır hale getirmek.

## Soğuk başlangıç (intake)
1. Proje tipi, kapasite ve gelişim aşaması (önlisans/lisans/inşa)?
2. EPC modeli: anahtar teslim mi, ölçüye bağlı mı; tek/çok yüklenici?
3. Finansman: özkaynak/borç oranı, kreditör, teminat beklentisi?
4. Kritik izinler (ÇED, bağlantı, mülkiyet/irtifak, imar) tamam mı?

## Denetim şeması
1. **İzin-onay zinciri**: Lisans/önlisans, ÇED kararı, bağlantı ve sistem kullanım anlaşmaları, mülkiyet/irtifak ve gerekirse 6446 m.19 kamulaştırma; eksik halka projeyi durdurur, tamamlanma takvimine bağlanır.
2. **EPC sözleşmesi**: TBK eser sözleşmesi (m.470 vd.) zemininde anahtar teslim bedel, iş programı, gecikme cezası (cezai şart, TBK m.182), performans testleri ve geçici/kesin kabul; ayıp ve garanti (TBK m.474 vd.) ile teminat süresi.
3. **Teminat paketi**: Avans/performans/bakım teminat mektupları, sigorta (inşaat all-risk, üçüncü kişi mali mesuliyet) ve liquidated damages; kreditör lehine alacak ve hesap rehinleri, lisans üzerinde rehin/şerh imkânı.
4. **Risk tahsisi**: Mevzuat değişikliği, kur, gecikme ve mücbir sebep maddeleri EPC, PPA ve kredi sözleşmeleri arasında tutarlı olmalı (back-to-back); çelişki kreditör için kabul edilemez boşluk doğurur.
5. **Direct agreement / step-in**: Kreditörün lisans ve kilit sözleşmelere müdahale (step-in) ve devir hakları; EPDK izni gereken pay/kontrol değişiklikleri kontrol edilir.

İdari işlem boyutunda iptal riskleri İYUK, sözleşmesel uyuşmazlıklar TBK/tahkim kapsamında ayrı izlenir.

## Çıktı modülleri
- İzin-onay ve kapanış ön koşulları (CP) kontrol listesi.
- EPC/O&M risk dağılım matrisi.
- Teminat paketi ve back-to-back tutarlılık raporu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

