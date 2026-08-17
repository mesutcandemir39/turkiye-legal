---
argument-hint: ''
description: Bağımsız bölümlere bağlanan arsa paylarının hatalı/dengesiz olması, kat
  irtifakı kurulması ya da iskân sonrası kat mülkiyetine geçiş gerektiğinde; arsa
  payı düzeltme davası ve KMK kuruluş işlemleri iç
name: arsa-payi-kat-irtifaki
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Arsa Payı Düzeltimi, Kat İrtifakı ve Kat Mülkiyetine Geçiş

## Görev
Bağımsız bölümlere bağlı arsa payı ilişkisini doğru kurmak: kat irtifakı/kat mülkiyetinin kuruluşunu denetlemek ve bağımsız bölümün değeriyle orantısız (hatalı) arsa paylarının düzeltilmesi davasını yürütmek.

## Soğuk başlangıç (intake)
- Yapıda kat irtifakı mı, kat mülkiyeti mi kurulu; yoksa hiç kurulmamış mı (cins tashihi/iskân durumu)?
- Arsa payları bağımsız bölümlerin değeriyle orantılı mı; hangi bölüm lehine/aleyhine sapma var?
- Düzeltme talebi tüm malikleri mi etkiliyor; yönetim planı ve proje mevcut mu?
- İskân (yapı kullanma izni) alındı mı; kat mülkiyetine geçiş için belgeler tam mı?

## Denetim şeması
1. **Kavram**: Kat irtifakı, henüz tamamlanmamış yapıda bağımsız bölümler üzerinde ileride kat mülkiyeti kurulmak üzere arsa payına bağlı kurulan irtifaktır (634 sayılı KMK m.2, m.3, m.10). Kat mülkiyeti ise tamamlanmış yapıda bağımsız bölüm üzerindeki tam mülkiyettir.
2. **Arsa payının niteliği**: Her bağımsız bölüme, değeriyle orantılı arsa payı özgülenir (KMK m.3/2). Arsa payı bağımsız bölümden ayrı devredilemez, ona bağlı (bütünleyici) gider.
3. **Arsa payı düzeltimi**: Arsa payları, bağımsız bölümlerin değeriyle oransızsa, her kat maliki/irtifak sahibi hâkimden düzeltme isteyebilir (KMK m.3/son'a göre, projedeki değerler esas alınarak). Dava, oransızlığın değerleme (bilirkişi) ile ortaya konmasına dayanır ve tüm bağımsız bölüm maliklerine husumet yöneltilir.
4. **Kat mülkiyetine geçiş**: Yapı tamamlanıp yapı kullanma izni (iskân) alınınca, kat irtifakı kat mülkiyetine çevrilir (KMK m.14, m.12'deki belgelerle). Resen veya malik talebiyle tapuda dönüşüm yapılır.
5. **Kuruluş belgeleri (KMK m.12)**: Mimari proje, yapı kullanma izni, yönetim planı ve liste; eksiklik kuruluşu engeller.
6. **Ara sonuç**: Oransız paylar düzeltme davasıyla projedeki değerlere göre yeniden belirlenir; tamamlanan yapıda kat irtifakı kat mülkiyetine dönüştürülür.

## Çıktı modülleri
- Arsa payı düzeltme dava dilekçesi iskeleti (oransızlık iddiası, değerleme, husumet listesi).
- Kat mülkiyetine geçiş belge kontrol listesi (proje, iskân, yönetim planı).
- Görev/yetki notu: sulh hukuk mahkemesi (KMK Ek m.1; HMK m.4), taşınmazın yeri.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

