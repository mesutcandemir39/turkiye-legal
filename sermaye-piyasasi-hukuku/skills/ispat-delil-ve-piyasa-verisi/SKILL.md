---
argument-hint: ''
description: Sermaye piyasası uyuşmazlıklarında emir/işlem kayıtları, KAP-MKK-Takasbank
  verileri, ses/talimat kayıtları ve bilirkişi incelemesi gibi delillerin toplanması
  ve değerlendirilmesi gerektiğinde kullanıl
name: ispat-delil-ve-piyasa-verisi
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
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İspat, Delil ve Piyasa Verisi

## Görev
Sermaye piyasası uyuşmazlığında ispat planını kurmak; içsel bilgi, fiyat etkisi, işlem zamanlaması ve kusur unsurlarını doğru delil türleriyle bağlamak.

## Soğuk başlangıç (intake)
- İspatlanması gereken çekirdek vakıa nedir (içsel bilgi, yapaylık, yerindelik ihlali, zarar)?
- Hangi kayıtlara erişilebilir: emir/işlem, KAP, MKK, Takasbank, ses/talimat kayıtları?
- Karşı tarafın elindeki ve üçüncü kişideki belgeler için talep gerekiyor mu?
- İspat yükü kimde; karine veya yer değiştirme söz konusu mu?

## Denetim şeması
1. **İspat yükü dağılımı:** Kural olarak iddia eden ispatla yükümlüdür (HMK m.190; cezada CMK m.217 ve şüpheden sanık yararlanır). İzahname/kamuyu aydınlatma sorumluluğunda özen ispatı sorumlu tarafa geçer.
2. **Delil türü-eşleştirme:** İçsel bilgi ve zamanlama için emir/işlem kayıtları, içsel bilgiye erişen listesi, KAP açıklama saatleri; fiyat etkisi için fiyat-hacim analizi ve bilirkişi raporu; varlık/sahiplik için MKK ve Takasbank kayıtları; talimat uyuşmazlığında ses/talimat kayıtları kullanılır.
3. **Delil toplama usulü:** Üçüncü kişi/karşı taraftaki belgeler için belge ibrazı (HMK m.219-220), gerekirse delil tespiti (HMK m.400); Kurul incelemesinde idarenin re'sen araştırma yetkisi not edilir. Ara sonuç: hangi delilin nasıl ve kimden temin edileceği netleşir.
4. **Bilirkişi:** Piyasa analizinin uzmanlık gerektirdiği hallerde bilirkişi incelemesi (HMK m.266); raporun görev kapsamı, metodoloji ve dayanak yönünden denetimi yapılır, çelişki ek rapor/itirazla giderilir.
5. **Hukuka uygunluk:** Ses kaydı, içsel belge gibi delillerin hukuka uygun yolla elde edilmesi (HMK m.189/2) değerlendirilir; hukuka aykırı delil dışlanır.

## Çıktı modülleri
- Vakıa-delil eşleştirme matrisi
- Delil toplama/talep listesi (HMK dayanaklarıyla)
- Bilirkişi sorularına yönelik nokta atışı çerçeve
- İspat yükü ve risk notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

