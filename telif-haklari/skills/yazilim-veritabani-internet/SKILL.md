---
argument-hint: ''
description: Bilgisayar programı, veri tabanı veya çevrimiçi paylaşılan içerik üzerindeki
  telif sorunlarını çözmek gerektiğinde; yazılımın eser niteliği, dekompilasyon istisnası,
  veri tabanı korumasi ve internette
name: yazilim-veritabani-internet
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
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yazılım, Veri Tabanı ve İnternet İçeriği

## Görev
Bilgisayar programları, veri tabanları ve çevrimiçi içerik özelinde telif korumasının kapsamını, özel istisnaları ve internet ihlallerinde sorumluluk zincirini değerlendirmek.

## Soğuk başlangıç (intake)
- Konu yazılım kodu, arayüz, veri tabanı yapısı/içeriği mi yoksa web içeriği mi?
- Kod/içerik kim tarafından, iş ilişkisi içinde mi üretildi?
- İhlal kopyalama, tersine mühendislik, lisans aşımı mı; yoksa internette paylaşım mı?
- Platform/aracı hizmet sağlayıcı mı, içerik sağlayıcı mı sorumlu tutuluyor?

## Denetim şeması
1. Yazılımın eser niteliği: Bilgisayar programları ilim-edebiyat eseri olarak korunur (m.2/1); koruma ifade biçimine (kaynak/amaç kod) yöneliktir, fikir-algoritma-arayüz işlevi olarak korunmaz. Hazırlık tasarımları da kapsama girer.
2. Yazılıma özgü istisnalar (m.38): Yedekleme, hata düzeltme ve birlikte çalışabilirlik için sınırlı dekompilasyon (tersine mühendislik) belirli şartlarla serbesttir; bunların ötesi ihlaldir. Çalışan eserinde mali haklar işverene aittir (m.18/2).
3. Veri tabanı: Eser niteliğindeki (seçme/düzenlemede hususiyet) veri tabanı m.6/11 kapsamında korunur; içerik tek tek korunmasa da derlemedeki yaratıcı seçim korunur. Salt yatırıma dayalı sui generis koruma ile karıştırma.
4. İnternette umuma iletim: İçeriğin çevrimiçi erişime sunulması m.25 kapsamında işaret-ses-görüntü nakli/umuma iletim ve erişilebilir kılma hakkını ilgilendirir; izinsiz yükleme ihlaldir.
5. Aracı sorumluluğu: Yer/erişim/içerik sağlayıcı ayrımı (5651 sayılı Kanun) ile FSEK ihlali birlikte değerlendirilir; uyar-kaldır mekanizması ve aracıya bildirim süreci kontrol edilir. Asıl fail içerik sağlayıcıdır; aracının sorumluluğu bildirim sonrası harekete geçmemeye bağlanır.
6. Ara sonuç: Koruma kapsamı, uygulanan istisna ve sorumlu süje (içerik/aracı) belirlenir.

İspat yükü: kod/içerik benzerliği ve erişimi davacı (genelde bilirkişi/kaynak kod karşılaştırması ile); istisna/lisans savunmasını davalı ispatlar.

## Çıktı modülleri
- Yazılım/veri tabanı koruma kapsamı ve istisna notu.
- İnternet ihlali sorumluluk zinciri (içerik/aracı, uyar-kaldır).
- Kaynak kod karşılaştırması/bilirkişi talep önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

