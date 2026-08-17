---
argument-hint: ''
description: Raporun, mahkemenin verdiği görevlendirme kararının ve sorulan soruların
  sınırları içinde kalıp kalmadığını; kapsam aşımı veya eksik yanıt bulunup bulunmadığını
  denetlemek istendiğinde kullanılır.
name: gorev-kapsami-uygunluk
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  - ad: Sağlık Turizmi Kanunu
    numara: '6754'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Görevlendirme Kapsamı ve Uygunluk Denetimi

## Görev
Raporu görevlendirme kararının çıpasına oturtmak: bilirkişiye yazılı olarak bildirilen görev kapsamı ve süre (HMK m.273) ile raporun fiilen yanıtladığı hususları karşılaştırıp **kapsam aşımı** ve **eksik yanıt** kusurlarını tespit etmek.

## Soğuk başlangıç (intake)
- Görevlendirme kararının tam metni ve bilirkişiye sorulan sorular elinizde mi?
- Bilirkişiye verilen kesin süre içinde mi rapor sunulmuş?
- Rapor, sorulmayan bir hususta görüş bildiriyor mu?
- Sorulduğu hâlde yanıtsız kalan soru var mı?

## Denetim şeması
1. **Yazılı kapsamla karşılaştırma (HMK m.273):** Görev, kapsamı ve süresi yazılı bildirilir. Sorular tek tek listelenir; her sorunun raporda karşılığı işaretlenir. Karşılıksız kalan → **eksik**; sorulmadığı hâlde yanıtlanan → **aşım**.
2. **Hukuki nitelendirme aşımı (HMK m.266, m.279/son):** Bilirkişinin "kusur oranı %X, davalı sorumludur, şu tazminata hükmedilmeli" gibi hukuki sonuç çıkarması görev sınırının aşılmasıdır; nitelendirme hâkime aittir.
3. **Uzmanlık alanı sınırı (6754 s.K. m.3):** Bilirkişi yalnızca uzmanlık ve teknik alanında görüş verebilir; alan dışı görüş ret/itiraz sebebidir. Heyet raporlarında her üyenin alanı kontrol edilir.
4. **Bizzat ifa (HMK m.277):** Görev devredilemez; rapor fiilen başka kişiye hazırlatılmışsa aşımdır.
5. **Ara sonuç:** Eksik yanıtlar → **ek rapor** talebi; aşım ve alan dışı görüş → **esasa itiraz / rapora itibar edilmemesi** talebi (HMK m.281, m.282).

## Çıktı modülleri
- Soru-yanıt eşleştirme tablosu (sorulan / yanıtlanan / eksik / aşım).
- Hukuki nitelendirme aşımı içeren paragrafların listesi.
- Uzmanlık alanı uyumsuzluğu notu.
- Kapsam temelli itiraz paragrafı taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

