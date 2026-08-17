---
argument-hint: ''
description: Sınır dışı, infaz, sağlık veya yaşamsal tehlike gibi telafisi imkânsız
  zarar riski bulunan hallerde geçici tedbir (ivedi koruma) talep edilirken kullanılır.
name: tedbir-ve-ivedi-koruma
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  - ad: Anayasa Mahkemesinin Kuruluşu ve Yargılama Usulü Hakkında Kanun
    numara: '6216'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tedbir ve İvedi Koruma Talebi

## Görev
İçtüzük m.73 kapsamında, başvurucunun yaşamına veya maddi-manevi bütünlüğüne yönelik ciddi ve telafisi imkânsız zarar tehlikesinde AYM'den geçici tedbir kararı talep etmek.

## Soğuk başlangıç (intake)
- Hangi icra/işlem yakın ve telafisi imkânsız zarar doğuruyor (sınır dışı, infaz, tıbbi durum)?
- Zarar gerçekleşirse esas hakkındaki kararın anlamı kalır mı?
- Tehlikenin yakınlığını ve ciddiyetini gösteren belgeler var mı?
- Asıl başvuru yapıldı mı, eşzamanlı mı yapılacak?

## Denetim şeması
1. Dayanak — İçtüzük m.73: başvurucunun yaşamına ya da maddi veya manevi bütünlüğüne yönelik ciddi tehlike bulunması hâlinde Bölüm, esas inceleme sonuçlanıncaya kadar gerekli tedbirlere resen veya talep üzerine karar verebilir.
2. Eşik — tehlikenin (a) ciddi, (b) yakın/gerçek ve (c) telafisi imkânsız olması aranır. Soyut/uzak risk yetmez; somut belgeyle ortaya konmalıdır.
3. Tipik haller — sınır dışı/iade kararında işkence-kötü muamele riski (m.17), ağır hastada infazın ertelenmemesi, hayati tıbbi müdahaleye erişimin engellenmesi.
4. Usul — tedbir talebi, başvuru formuyla birlikte veya başvuru derdestken ayrıca ve gecikmeksizin yapılır; aciliyet gerekçesi öne çıkarılır. AYM tedbiri reddedebilir, kabul edebilir veya koşula bağlayabilir; tedbire uyulmaması ayrı sonuç doğurabilir.
5. Süreklilik — tedbir, esas karara kadar veya AYM aksini belirtene dek sürer; koşullar değişirse kaldırılması istenebilir.

İspat yükü: yakın ve ağır tehlikeyi somut belgeyle başvurucu ortaya koyar.

Ara sonuç: "tedbir koşulları var / zayıf / yok" değerlendirmesi.

## Çıktı modülleri
- Tedbir talebi dilekçesi taslağı (aciliyet + telafisizlik gerekçesi).
- Tehlikeyi belgeleyen ek listesi.
- Asıl başvuruyla ilişkilendirme.
- Tedbir reddi halinde alternatif yol notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

