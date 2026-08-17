---
argument-hint: ''
description: Davalı vekili olarak cevap dilekçesi, ilk itirazlar ve karşı dava; ardından
  replik-düplik dilekçeleri hazırlamak ve teksif ilkesini gözetmek gerektiğinde kullanılır.
name: cevap-replik-duplik
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
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Cevap, Replik ve Düplik Dilekçeleri

## Görev
Davalı savunmasını HMK m.126-129 çerçevesinde kurmak; ilk itirazları, esasa cevabı ve varsa karşı davayı doğru zamanda ileri sürmek; dilekçeler aşamasını teksif ilkesine uygun tamamlamak.

## Soğuk başlangıç (intake)
- Dava dilekçesi tebliğ tarihi ne, cevap süresi doluyor mu?
- İlk itiraz var mı (yetki, derdestlik, tahkim, m.116)?
- Karşı dava şartları oluştu mu (HMK m.132-134)?
- Hangi vakıalar inkâr, hangileri itiraf edilecek?

## Denetim şeması
1. Cevap süresi (HMK m.127): Kural iki hafta; gerekçeli talep ve hâkim takdiriyle bir defaya mahsus uzatma. Basit yargılamada iki hafta (m.317). Süre geçerse cevap hakkı düşer, davacının dava dilekçesindeki vakıalar inkâr edilmiş sayılır (m.128 değil; cevap vermeyen davalı vakıaları inkâr etmiş sayılır).
2. İlk itirazlar (HMK m.116-117): Kesin olmayan yetki, derdestlik, tahkim itirazı, iş bölümü; hepsi cevap dilekçesinde birlikte ileri sürülür, sonradan ileri sürülemez.
3. Esasa cevap (m.129): Davacının her vakıasına karşı açık tutum (kabul/inkâr/bilmeme); savunma sebepleri ve karşı deliller. Zamanaşımı def'i mutlaka burada ileri sürülmeli (TBK m.161 — hâkim re'sen dikkate almaz).
4. Karşı dava (m.132-134): Asıl dava ile bağlantı veya takas/mahsup şartı; süresinde ve aynı dilekçede.
5. Replik-düplik (m.136): Davacı cevaba cevap, davalı ikinci cevap verir; teksif ilkesi (m.141) gereği bundan sonra iddia/savunma genişletilemez (ıslah ve karşı tarafın açık muvafakati hariç). Ara sonuç: süre/itiraz/def'i eksiksizse imzaya hazır.

## Çıktı modülleri
- Cevap dilekçesi taslağı (ilk itiraz + esasa cevap + def'iler)
- Karşı dava bloğu (varsa)
- Replik/düplik taslağı
- Süre ve teksif uyarı notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

