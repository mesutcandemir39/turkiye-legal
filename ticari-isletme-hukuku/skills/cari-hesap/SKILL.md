---
argument-hint: ''
description: Taraflar arasinda karsilikli alacaklarin bir hesaba kaydedilip donem
  sonunda bakiyenin tespit edildigi cari hesap iliskisinin kurulmasi, bakiyenin tahakkuku,
  faiz, sozlesmenin sona ermesi ve bakiyenin
name: cari-hesap
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
  requires_human_review: true
  risk_level: high
  sources:
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Cari Hesap İlişkisi

## Görev
Cari hesap sözleşmesinin varlığını, işleyişini ve sona ermesini değerlendirmek; dönem sonu bakiyesinin nasıl kesinleştiğini ve talep edilebileceğini belirlemek. Cari hesap, ticari ilişkilerde alacakların netleştirilmesinin özel rejimidir.

## Soğuk başlangıç (intake)
1. Taraflar arasında yazılı cari hesap sözleşmesi var mı (TTK m.89 şekil)?
2. Hesap dönemleri ve bakiye tespit usulü ne?
3. Bakiyeye itiraz edildi mi; tanınma (kabul) gerçekleşti mi?
4. İlişki sona erdi mi; faiz ve zamanaşımı durumu ne?

## Denetim şeması
1. **Tanım ve şekil:** TTK m.89 — iki kişinin (en az biri tacir olması şart değil, ama uygulamada ticari) para, mal, hizmet ve diğer hususlardan doğan alacaklarını ayrı ayrı istemekten karşılıklı olarak vazgeçip bunları kalem kalem alacak-borç şekline çevirerek hesabın kesilmesinden sonra çıkacak bakiyeyi isteyebilecekleri sözleşmedir. Sözleşme yazılı şekle tabidir (m.89/2).
2. **İşleyiş ve hesap dışı kalanlar:** TTK m.90 — belirli alacaklar (örn. takas edilemeyen, özel amaca tahsisli) cari hesaba geçirilemez. Kalemlerin hesaba kaydı, alacağı yenilemez kural olarak (m.91 — aksi kararlaştırılmadıkça).
3. **Faiz:** TTK m.92-93 — aksi kararlaştırılmadıkça her kalem için kaydı tarihinden faiz işler; bileşik faiz ancak TTK m.8/2 şartlarıyla.
4. **Bakiyenin tespiti ve tanınması:** TTK m.94 — dönem sonunda bakiye tespit edilip karşı tarafa bildirilir; bildirimi alan, süresi içinde itiraz etmezse bakiyeyi kabul (tanıma) etmiş sayılır. Tanınan bakiye yeni hesap döneminin ilk kalemi olur.
5. **Sona erme ve zamanaşımı:** TTK m.99 sona erme halleri; TTK m.101 — cari hesabın tasfiyesine, bakiyeye ve faizlere ilişkin davalar 5 yıllık zamanaşımına tabidir. Ara sonuç: yazılı sözleşme + dönem sonu bakiye + tanıma → bakiye muaccel ve dava edilebilir.

## Çıktı modülleri
- Cari hesap geçerlilik ve işleyiş notu (yazılı şekil, kalemler).
- Bakiye tespiti ve tanınma değerlendirmesi.
- Bakiyenin tahsili dava/icra talebi ve zamanaşımı uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

