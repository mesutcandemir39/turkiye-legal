---
argument-hint: ''
description: Kartel veya hâkim durum ihlalinden zarar gören tarafın üç kata kadar
  tazminat (m.58) talebini, zarar ve illiyet ispatını, zamanaşımını ve görevli mahkemeyi
  değerlendirmek istendiğinde kullanılır.
name: ozel-hukuk-tazminat
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
  - ad: Rekabetin Korunması Hakkında Kanun
    numara: '4054'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Rekabet İhlalinden Özel Hukuk Tazminatı (m.57-58)

## Görev
Rekabet ihlali nedeniyle zarar gören teşebbüs veya tüketicinin 4054 m.57-58 kapsamında tazminat (üç kata kadar) talebini kurgulamak; zarar, illiyet ve kusur ispatını, zamanaşımını ve usul boyutunu yönetmek.

## Soğuk başlangıç (intake)
- İddia edilen ihlal: kartel (fiyat tespiti), dışlayıcı kötüye kullanma, başka m.4/m.6 ihlali mi?
- Rekabet Kurulu'nun ihlali tespit eden kesinleşmiş bir kararı var mı (follow-on) yoksa bağımsız dava mı (stand-alone)?
- Zarar türü: fazladan ödenen fiyat (overcharge), kâr kaybı, pazardan dışlanma?
- İhlal/zararın öğrenilme tarihi ve dava açılabilirlik durumu?

## Denetim şeması
1. **Hukuki temel (m.57)** — rekabeti sınırlayan davranışlarla zarar verenler, zarar görenin zararını tazminle yükümlüdür; sorumluluk haksız fiil esaslarına dayanır (TBK m.49 vd. ile birlikte okunur).
2. **Üç kat tazminat (m.58)** — zarar görenin gerçek zararı yanında, kartel/anlaşma sonucu ortaya çıkan zararda mahkeme, zarar görenin talebiyle, verilen zararın üç katına kadar tazminata hükmedebilir; bu caydırıcı bir özel hukuk yaptırımıdır.
3. **Unsurlar** — hukuka aykırılık (ihlalin varlığı), kusur, zarar ve illiyet bağı ispatlanmalı. Follow-on davada kesinleşmiş Kurul kararı ihlali güçlü biçimde ortaya koyar; zarar miktarı ve illiyet yine ispat gerektirir.
4. **Zararın hesabı** — fiyat farkı (but-for fiyat), kâr kaybı; iktisadi modelleme ve bilirkişi devreye girer. Geçişkenlik (passing-on) savunması değerlendirilir.
5. **Zamanaşımı** — haksız fiil zamanaşımı kuralları (TBK m.72: zararın ve failin öğrenilmesinden itibaren kısa süre, her hâlde uzun süre) çerçevesinde; Kurul kararının kesinleşmesinin zamanaşımına etkisi dikkatle değerlendirilir.
6. **Görev/yetki** — uyuşmazlık ticari nitelikteyse asliye ticaret mahkemesi; dava şartı arabuluculuk (ticari uyuşmazlık) ihtimali kontrol edilir.

## Çıktı modülleri
- Follow-on / stand-alone yol kararı.
- Zarar kalemleri ve hesap yöntemi taslağı.
- Üç kat tazminat talebi gerekçesi.
- Zamanaşımı ve görev/yetki + arabuluculuk kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

