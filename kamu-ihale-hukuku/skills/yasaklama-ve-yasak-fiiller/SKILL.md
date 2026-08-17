---
argument-hint: ''
description: İhalelere katılmaktan yasaklama kararı, yasak fiil ve davranışların (m.17)
  tespiti, yasaklamanın kapsamı, süresi ve iptali tartışıldığında kullanılacak yaptırım
  becerisidir.
name: yasaklama-ve-yasak-fiiller
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
  - ad: Koruma Amaçlı Imar Planları Hakkında Kanun
    numara: '4734'
    tur: kanun
  - ad: Tarih Medeniyetini Koruma Kanunu
    numara: '4735'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yasaklama Kararları ve Yasak Fiiller

## Görev
İhale sürecinde veya sözleşme aşamasında işlenen yasak fiiller nedeniyle verilen ihalelere katılmaktan yasaklama kararının hukuka uygunluğunu, kapsamını, süresini ve iptal yolunu değerlendirmek.

## Soğuk başlangıç (intake)
1. Yasaklama hangi fiile dayanıyor: ihale sürecindeki yasak fiil (4734 m.17) mi, sözleşme ihlali (4735 m.25) mi?
2. Kararı veren idare yetkili mi; karar Resmî Gazete'de yayımlandı mı?
3. Yasaklama süresi (1-2 yıl) fiile uygun mu?
4. Yasaklamanın kapsamına giren gerçek/tüzel kişiler ve ortaklar doğru belirlenmiş mi?

## Denetim şeması
1. **Yasak fiiller (4734 m.17):** Hile, vaat, tehdit, nüfuz kullanma, rekabeti/ihale kararını etkileyecek davranış, sahte belge düzenleme, alternatif teklif verme yasağı ihlali vb. somut delille ortaya konmalıdır.
2. **Sözleşme aşaması fiilleri (4735 m.25):** Sözleşme uygulamasındaki yasak fiil ve davranışlar (taahhüdü yerine getirmeme, sahtecilik vb.) ayrı yasaklama sebebidir.
3. **Yaptırım (4734 m.58, 4735 m.26):** İlgililer hakkında bir yıldan az olmamak üzere iki yıla kadar ihalelere katılmaktan yasaklama kararı verilir; karar Resmî Gazete'de yayımlanır ve yayımdan itibaren hüküm doğurur. Yasaklama kapsamı tüzel kişide ortakları/yetkilileri de etkileyebilir.
4. **Ölçülülük ve sebep:** Fiil ile yasaklama süresi orantılı olmalı; sebep yokluğu/eksikliği veya yetki/şekil sakatlığı iptal sebebidir.
5. **İptal yolu:** Yasaklama bir idari işlemdir; 2577 sayılı İYUK'a göre yetkili idare mahkemesinde iptal davası açılır (yürütmenin durdurulması talep edilebilir). Ayrıca fiil suç teşkil ediyorsa ceza soruşturması paralel yürüyebilir.
6. **Ara sonuç:** Yasaklamanın kapsamı (kişi/süre) ve dava süresi dikkatle hesaplanır.

İspat yükü: Yasak fiili iddia eden idare somut delille ispatlar; ilgili savunma ve aksini ortaya koyar.

## Çıktı modülleri
- Fiil-yaptırım uyum (ölçülülük) değerlendirmesi.
- Yasaklama kapsamı (kişi/süre) tablosu.
- İptal davası dilekçe iskeleti ve YD talebi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

