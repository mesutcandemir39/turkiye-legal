---
argument-hint: ''
description: Bir internet aktörünün içerik, yer, erişim veya toplu kullanım sağlayıcı
  sıfatının ve buna bağlı yükümlülük ile sorumluluk sınırlarının (uyar-kaldır, log
  tutma, bilgi verme) belirlenmesi gerektiğinde
name: saglayici-sorumluluk-rejimi
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
  - ad: Telekomunikasyon Kanunu
    numara: '5809'
    tur: kanun
  - ad: Elektronik Ticaretin Düzenlenmesine Dair Kanun
    numara: '5651'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İçerik, Yer ve Erişim Sağlayıcı Sorumluluk Rejimi

## Görev
İnternet aktörünün 5651 kapsamındaki sıfatını kesin biçimde belirlemek ve bu sıfata bağlı yükümlülükler ile hukuki/cezai sorumluluk sınırlarını tespit ederek uyum veya savunma çerçevesini kurmak.

## Soğuk başlangıç (intake)
1. Aktör ne yapıyor: içeriği kendisi mi üretiyor, başkasının içeriğini mi barındırıyor, salt erişim mi sağlıyor, ortak alan/wifi mı sunuyor?
2. Şikâyet konusu içerik üçüncü kişiye mi ait; aktör bundan haberdar edildi mi?
3. Log/trafik kaydı tutuluyor mu, ne kadar süreyle; bilgi talebi geldi mi?
4. Aktör yurt içinde mi yurt dışında mı; temsilci var mı?

## Denetim şeması
1. **Sıfat tespiti**: 5651 m.2 — içerik sağlayıcı (kendi ürettiği içerik), yer sağlayıcı (barındıran), erişim sağlayıcı (internet erişimi sunan), toplu kullanım sağlayıcı (ortak erişim). Ara sonuç: hangi sıfat, dolayısıyla hangi rejim.
2. **İçerik sağlayıcı**: m.4 — kendi içeriğinden tam sorumlu; bağlantı verdiği başkasının içeriğinden kural olarak sorumlu değildir (benimseme/sunuş hali istisna). Sorumluluk doğrudan ve tam.
3. **Yer sağlayıcı**: m.5 — hukuka aykırı içeriği denetleme yükümlülüğü yok; ancak m.8/m.9 kapsamında haberdar edilip teknik imkân varsa kaldırma (uyar-kaldır) ve trafik bilgisi saklama/sunma yükümlülüğü var. Haberdar edilmeden sorumluluk doğmaz.
4. **Erişim sağlayıcı**: m.6 — kendisine bildirilen erişim engelleme kararını uygulama, trafik bilgisini saklama (yönetmelikteki süreyle) ve faaliyete son verirken bildirim yükümlülüğü; içeriği kontrol/araştırma yükümlülüğü yok.
5. **Yaptırım**: Bilgi/belge verme, log tutma ve karar uygulama yükümlülüklerinin ihlali idari para cezası (m.5, m.6 ve ilgili hükümler) doğurur; ayrıca içerikle bağlantılı TCK suçları (ör. m.243-245) ayrı değerlendirilir.

İspat açısından log/trafik kayıtları, uyar-kaldır bildirimi ve haberdar edilme tarihi belirleyicidir; haberdar edilme anı sorumluluğun başlangıcını işaretler.

## Çıktı modülleri
- Sağlayıcı sıfatı ve yükümlülük matrisi.
- Uyar-kaldır/bilgi talebi yanıt taslağı.
- Sorumluluk sınırı ve risk değerlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

