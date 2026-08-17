---
argument-hint: ''
description: Toplanti tutanaginin icerigi, baskanlik divani, Bakanlik temsilcisi imzasi,
  kararlarin ticaret siciline tescil ve ilani ile internet sitesi yukumlulukleri konusunda
  taslak veya denetim gerektiginde ku
name: genel-kurul-tutanagi-ve-tescil
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


# Genel Kurul Tutanağı ve Tescil

## Görev
Genel kurul tutanağını mevzuata uygun düzenlemek; tescile tabi kararların ticaret siciline tescil ve ilanı ile internet sitesi yükümlülüklerini denetlemek.

## Soğuk başlangıç (intake)
1. Toplantı başkanlığı (divan) usulüne uygun oluştu mu; Bakanlık temsilcisi imzası gerekli mi?
2. Hangi kararlar tescile tabi (esas sözleşme değişikliği, sermaye, organ seçimi)?
3. Toplantı fiziki mi, elektronik genel kurul (EGK) mı?
4. Tutanak ve ekleri (hazır bulunanlar listesi, vekâletnameler) tam mı?

## Denetim şeması
1. **Tutanak içeriği:** Tutanak; toplantı yeri-tarihi, hazır pay/oy miktarı, gündem, kararlar, her karara ilişkin oy sonuçları, muhalefet şerhleri ve sorulan soruların cevaplarını içerir; toplantı başkanlığı ve Bakanlık temsilcisi (varsa) tarafından imzalanır (m.422). Eksik/çelişkili tutanak ispatı zayıflatır ve iptal riskine zemin hazırlar.
2. **Muhalefet şerhi:** İptal davası açacak pay sahibinin (toplantıda hazır olup) karara karşı **muhalefetini tutanağa geçirtmiş** olması gerekir (m.446/1-b); bu kayıt davacı sıfatının ön şartıdır. Şerhin açık ve karara özgülenmiş olması önemlidir.
3. **Tescil ve ilan:** Tescile tabi kararlar, toplantıyı izleyen süre içinde ticaret siciline tescil ve TTSG'de ilan ettirilir; YK tescil ödevini yerine getirir. İptal davasında üç aylık süre, kararın alınmasından (kural) işler; tescil tarihi ayrıca ilan ve sicil kaydı için önemlidir.
4. **İnternet sitesi/EGK:** m.1524 kapsamındaki şirketlerde internet sitesine konulması zorunlu içerikler ile pay senetleri borsada işlem gören şirketlerde elektronik genel kurul (EGK) zorunluluğu denetlenir; EGK'de m.1527 ve ilgili yönetmelik uygulanır.
5. **İspat yükü/ara sonuç:** Tutanağın usule uygunluğunu şirket gösterir. Tutanağın imzasız/eksik olması veya zorunlu tescilin yapılmaması, üçüncü kişilere karşı hüküm ve sorumluluk sonuçları doğurur; karar geçerliliğini doğrudan değil, ispat ve aleniyet yönünden etkiler.

## Çıktı modülleri
- Genel kurul tutanağı taslağı (divan + temsilci imza blokları).
- Muhalefet şerhi örnek metni.
- Tescil/ilan ve internet sitesi yükümlülük kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

