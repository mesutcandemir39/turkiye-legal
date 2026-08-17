---
argument-hint: ''
description: Ortak gider ve avans aidatının belirlenmesi, tahsili, ödemeyen malike
  karşı icra takibi ve gecikme tazminatı ile işletme projesine itiraz gündeme geldiğinde;
  gider paylaşım esasları, kanuni ipotek ve
name: aidat-ve-ortak-gider
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
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Aidat, Ortak Gider ve İşletme Projesi

## Görev
Anagayrimenkulün ortak giderlerine ve işletme avansına katılma borcunu belirlemek; ödemeyen malike karşı tahsil yollarını (icra takibi, dava, kanuni ipotek) kurmak; işletme projesine itirazı değerlendirmek.

## Soğuk başlangıç (intake)
- Talep edilen alacak hangi döneme ait; işletme projesi/bütçe kabul edilmiş mi?
- Gider türü genel ortak gider mi (m.20/b) yoksa kullanıma/arsa payına bağlı özel gider mi?
- Borçlu kat maliki mi, kiracı mı; borçtan müteselsil sorumlu olan kim?
- Gecikme süresi ne kadar; gecikme tazminatı işletilmiş mi?

## Denetim şeması
1. **Katılma borcunun kaynağı (KMK m.20)**: Kat malikleri, aksine sözleşme olmadıkça: (a) kapıcı, kaloriferci, bekçi, bahçıvan ve yönetici giderleri ile yönetim için toplanacak avansa **eşit olarak**; (b) anagayrimenkulün sigortası ve bütün ortak yerlerin bakım, koruma, güçlendirme ve onarım giderlerine **arsa payları oranında** katılır (m.20/1-a,b).
2. **İşletme projesi (m.37)**: Yönetici, bir işletme projesi (tahmini gelir-gider ve her malike düşen pay) hazırlar; karara bağlanır ya da işletme projesi maliklere tebliğ edilir. Tebliğden itibaren **7 gün** içinde itiraz edilmezse proje kesinleşir ve **İİK m.68 anlamında belge** (ilam niteliğinde sayılan belge) hâline gelir.
3. **Temerrüt ve gecikme tazminatı (m.20/2)**: Gider/avans payını ödemeyen malik, gecikilen günler için aylık **yüzde beş (%5)** hesabıyla gecikme tazminatı öder. Bu, sözleşmesel cezadan bağımsız kanuni bir yaptırımdır.
4. **Müteselsil sorumluluk**: Bağımsız bölümün kiracısı/intifa hakkı sahibi de işletme giderlerinden malikle birlikte müteselsilen sorumlu olabilir (m.22/1 — kiracının sorumluluğu kira borcuyla sınırlı). Bağımsız bölümü sonradan iktisap eden, eski malikle birlikte ödenmeyen giderlerden sorumludur (m.22/1).
5. **Kanuni ipotek hakkı (m.22/2)**: Gider/avans payını ödemeyen malikin bağımsız bölümü üzerinde, diğer kat malikleri lehine **kanuni ipotek hakkı** tescil ettirilebilir; yöneticinin de bu yetkisi vardır.
6. **Takip yolu**: Kesinleşmiş işletme projesi/karar defterindeki gider tablosu ile ilamsız icra (İİK m.42 vd.) veya m.68 belgesine dayalı takip; itiraz edilirse itirazın iptali (İİK m.67) ya da kaldırılması (m.68).
7. **Ara sonuç**: Geçerli işletme projesi + gider tablosu → takip; itiraz → itirazın iptali; teminat için kanuni ipotek.

## Çıktı modülleri
- Gider paylaşım hesap tablosu (eşit / arsa payı oranlı; m.20/a-b).
- İcra takip talebi ve %5 gecikme tazminatı hesabı.
- İşletme projesine itiraz veya itirazın iptali dilekçe iskeleti.
- Kanuni ipotek tescili başvuru notu (m.22/2).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

