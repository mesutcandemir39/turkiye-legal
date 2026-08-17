---
argument-hint: ''
description: Dava açma, cevap, kanun yolu sürelerini hesaplamak; zamanaşımı ile hak
  düşürücü süreyi ayırmak ve süre risklerini erken yakalamak gerektiğinde kullanılır.
name: sure-zamanasimi-hakduserme
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


# Süreler, Zamanaşımı ve Hak Düşürücü Süreler

## Görev
Her layihada önce süreyi çözmek: dava açma, cevap, kanun yolu ve maddi hukuk süreleri. Süre kaçırılırsa içerik ne kadar sağlam olursa olsun hak kaybedilir; bu beceri erken uyarı sistemidir.

## Soğuk başlangıç (intake)
- Hangi olay tarihi/tebliğ tarihi süreyi başlatıyor?
- Zamanaşımı mı, hak düşürücü süre mi söz konusu?
- Süreyi durduran/kesen bir işlem var mı (ihtar, dava, başvuru)?
- Süre tatile/adli tatile denk geliyor mu?

## Denetim şeması
1. Zamanaşımı vs. hak düşürücü süre: Zamanaşımı def'i ileri sürülmedikçe hâkim re'sen dikkate almaz (TBK m.161); durur/kesilir (TBK m.153-156). Hak düşürücü süre re'sen gözetilir, durmaz/kesilmez.
2. Maddi hukuk süreleri (örnekler): Genel zamanaşımı TBK m.146 — 10 yıl; haksız fiil TBK m.72 — fiil ve failin öğrenilmesinden 2, her hâlde 10 yıl; ayıpta TBK m.231 / TKHK m.12. Boşanmada affı izleyen hak düşürücü süreler TMK m.161-162.
3. Usul süreleri: HMK cevap iki hafta (m.127); istinaf iki hafta (m.345); İYUK dava açma 60/30 gün (m.7); CMK itiraz yedi gün (m.268), şikâyet TCK m.73 — 6 ay.
4. Sürelerin hesabı (HMK m.92-94): Gün/hafta/ay hesabı; sürenin son günü resmî tatilse ilk iş gününe uzar. Adli tatil (HMK m.102-104) etkisini kontrol edin.
5. Durma/kesilme: Dava açılması, ihtar, icra takibi, kısmi ödeme/ikrar zamanaşımını keser (TBK m.154). Ara sonuç: son gün netleşip risk işaretlenir.

## Çıktı modülleri
- Süre takvimi (başlangıç → son gün)
- Zamanaşımı/hak düşürücü ayrım notu
- Durma-kesilme olayları listesi
- Süre riski uyarısı (kritik/yakın/güvenli)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

