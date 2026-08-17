---
argument-hint: ''
description: Tespit edilen bulguları iki haftalık süre içinde mahkemeye sunulacak
  somut, gerekçeli bir itiraz dilekçesine dönüştürmek; ek rapor, yeni bilirkişi veya
  rapora itibar edilmemesi taleplerini formüle etm
name: itiraz-dilekce-taslagi
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


# Bilirkişi Raporuna İtiraz Dilekçesi Taslağı

## Görev
Denetim bulgularını HMK m.281'e uygun, süresinde ve somutlaştırılmış bir itiraz dilekçesine dökmek; talep sonucunu (ek rapor / yeni heyet / itibar edilmemesi) bulgu ağırlığına göre netleştirmek.

## Soğuk başlangıç (intake)
- Rapor size hangi tarihte tebliğ edildi (iki haftalık sürenin başlangıcı)?
- Hangi bulgular dilekçeye girecek ve her biri hangi dayanağa çıpalı?
- Asıl talebiniz ek rapor mu, yeni bilirkişi mi, rapora itibar edilmemesi mi?
- Karşı uzman mütalaası ekleyecek misiniz?

## Denetim şeması
1. **Süre kontrolü (HMK m.281):** İtiraz, raporun tebliğinden itibaren iki hafta içinde yapılır. Son gün hesaplanır; süre geçecekse ek süre/mazeret değerlendirilir. Süre dilekçenin en üstünde teyit edilir.
2. **Somutlaştırma zorunluluğu:** "Rapor hatalıdır" gibi soyut itiraz sonuç doğurmaz; her itiraz, rapordaki sayfa/paragraf + görevlendirme sorusu + dosya deliliyle gerekçelendirilir.
3. **Talep sınıflandırması (HMK m.281):** Eksik/belirsiz husus → eksikliğin tamamlanması (ek rapor); yöntem/tarafsızlık kusuru → yeni bilirkişi/heyet; hukuki nitelendirme aşımı/caizsizlik → rapora itibar edilmemesi (HMK m.282 ile rapor hâkimi bağlamaz vurgusu).
4. **Dilekçe mimarisi:** Başlık ve süre teyidi; özet; bulgu bulgu itirazlar (her biri dayanaklı); varsa karşı uzman mütalaasına atıf; talep sonucu. Yer tutucular **[doldurulacak]** olarak işaretlenir.
5. **Ara sonuç:** Dilekçe, tek tek bulguların talep sonucuyla bağlandığı, denetlenebilir bir metne dönüşür.

## Çıktı modülleri
- Süre teyitli dilekçe başlığı ve özet bloğu.
- Numaralı, dayanaklı itiraz maddeleri (sayfa + soru + delil çıpalı).
- Talep sonucu paragrafı (ek rapor / yeni heyet / itibar edilmemesi).
- Eklenecek belge/mütalaa dizini ve [doldurulacak] kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

