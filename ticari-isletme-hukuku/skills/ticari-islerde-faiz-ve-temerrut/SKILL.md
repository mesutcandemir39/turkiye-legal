---
argument-hint: ''
description: Bir ticari alacakta uygulanacak faiz turunu ve oranini (ticari temerrut
  faizi, avans faizi, kapital faizi), faiz baslangic tarihini ve bilesik faiz sinirlarini
  belirlemek gerektiginde kullanilir.
name: ticari-islerde-faiz-ve-temerrut
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


# Ticari İşlerde Faiz ve Temerrüt

## Görev
Ticari bir alacakta hangi faizin, hangi oranla, hangi tarihten itibaren işleyeceğini doğru hesaplamak. Ticari işlerde faiz rejimi genel hükümlerden ayrılır; yanlış faiz türü talep, eksik tahsil veya ret riskidir.

## Soğuk başlangıç (intake)
1. İş her iki/bir taraf için ticari mi (TTK m.3, m.19)?
2. Sözleşmede faiz oranı kararlaştırılmış mı?
3. Borç para borcu mu; muacceliyet ve temerrüt ne zaman doğdu?
4. Temerrüt için ihtar gerekli mi, yoksa kesin vade var mı?

## Denetim şeması
1. **Faizin niteliği:** İş ticari ise faiz oranı serbestçe belirlenebilir (TTK m.8/1). Oran kararlaştırılmamışsa: kapital (anapara) faizi ve temerrüt faizi için ticari faiz uygulanır — 3095 sayılı Kanun m.1-2 ve TTK m.9 yollamasıyla. Ticari işlerde temerrüt faizinde, TCMB'nin kısa vadeli avanslar için uyguladığı oran (avans faizi) talep edilebilir (3095 m.2/2); bu oran genel temerrüt faizinden yüksekse uygulanır.
2. **Temerrüt anı:** TBK m.117 — kesin vadede vade gelmesiyle, aksi halde ihtarla temerrüt doğar. Faiz başlangıcı temerrüt tarihidir. Tacirler arası bazı işlemlerde sözleşmedeki vade yeterli olabilir.
3. **Bileşik faiz (faize faiz):** Kural yasak (TBK m.388 sınırı); ancak TTK m.8/2 — ticari işlerde, üç aydan aşağı olmamak üzere ve sözleşmede kararlaştırılmışsa cari hesap ile borçlunun her ikisi de tacir olan ödünç sözleşmelerinde bileşik faiz mümkündür. Bu istisna dar yorumlanır.
4. **İspat yükü:** Faiz talep eden işin ticari niteliğini, oran iddiasını ve temerrüt tarihini ispatlar. Karşı taraf ödeme veya faizsizlik anlaşmasını ispatlar.
5. **Ara sonuç:** Ticari iş + para borcu + temerrüt → avans faizi oranıyla temerrüt faizi; sözleşmesel oran varsa o; bileşik faiz ancak m.8/2 şartlarıyla.

## Çıktı modülleri
- Faiz türü/oran/başlangıç tarihi tablosu (dayanak: TTK m.8-9, 3095 m.2).
- Faiz hesabı için bilirkişiye yöneltilecek sorular.
- Talep sonucunda faiz fıkrası lafzı (işleyecek faiz dahil).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

