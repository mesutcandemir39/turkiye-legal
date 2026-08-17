---
argument-hint: ''
description: Koşullu salıverilmenin süre, iyi hâl ve suç tipi şartlarını denetlemek,
  geri alma sebeplerini değerlendirmek ve koşullu salıverilme kararına itirazı kurgulamak
  gerektiğinde kullanılır.
name: kosullu-saliverilme
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
  - ad: Ceza ve Güvenlik Tedbirlerinin İnfazı Hakkında Kanun
    numara: '5275'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Koşullu Salıverilme Şartları ve Denetimi

## Görev
Hükümlünün koşullu salıverilmeden yararlanıp yararlanamayacağını, hangi tarihte yararlanacağını ve geri alma riskini 5275 m.107 ve m.108 çerçevesinde denetlemek.

## Soğuk başlangıç (intake)
- Hükümlü cezasının ne kadarını fiilen çekti?
- İyi hâl değerlendirmesi (5275 m.89) olumlu mu; disiplin cezası var mı?
- Suç mükerrir mi (5275 m.108 ayrı rejim)?
- Suç tipi koşullu salıverilmeyi kısıtlayan kataloğa giriyor mu?

## Denetim şeması
1. Süre şartı: 5275 m.107/2 uyarınca infaz kurumunda geçirilmesi gereken asgari süre; süreli hapiste genel oran ile özel suç tiplerindeki ağırlaştırılmış oranlar ayrılır. Ağırlaştırılmış müebbette ve müebbette farklı asgari fiilî infaz süreleri uygulanır (m.107/2-3). Ara sonuç: aday tarih.
2. İyi hâl şartı: 5275 m.89 uyarınca idare ve gözlem kurulunca yapılan iyi hâl değerlendirmesi şarttır; olumsuz değerlendirme koşullu salıverilmeyi erteler. Disiplin cezalarının kaldırılmış olup olmadığı (m.48) kontrol edilir.
3. Mükerrirlik: ikinci defa mükerrirler için 5275 m.108 daha ağır oran ve denetim süresi getirir; bu rejim ayrıca uygulanır.
4. Geri alma: 5275 m.107/12 vd. — denetim süresi içinde kasıtlı suç işlenmesi veya yükümlülüklere uyulmaması hâlinde koşullu salıverilme geri alınır; bu durumda bakiye ceza aynen infaz edilir. İspat yükü: yükümlülük ihlali iddiasını denetimli serbestlik müdürlüğü/savcılık ortaya koyar.
5. İtiraz: koşullu salıverilme kararına/red kararına karşı infaz hâkimliği ve itiraz mercii yolu (4675 sayılı Kanun, CMK itiraz hükümleri). İlkesel içtihat için karararama.yargitay.gov.tr Yargıtay 1. CD ve CGK kararları taranır; künye `[DOĞRULANMADI]`.
6. Ara sonuç: yararlanma tarihi + geri alma riski değerlendirmesi.

## Çıktı modülleri
- Şart denetim çizelgesi (süre / iyi hâl / suç tipi / mükerrirlik).
- Geri alma risk notu.
- Karara itiraz dilekçesi taslak tetiği.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

