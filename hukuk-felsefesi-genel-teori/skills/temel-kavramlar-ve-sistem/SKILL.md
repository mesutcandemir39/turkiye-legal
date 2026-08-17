---
argument-hint: ''
description: Hukuk felsefesi ile genel teorinin temel kavramlarını (norm, geçerlilik,
  meşruiyet, hak, yaptırım, kaynak) ve ekol haritasını netleştirmek; bir teorik soruyu
  doğru kategoriye yerleştirip pozitif hukuk
name: temel-kavramlar-ve-sistem
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Sistematik

## Görev
Genel hukuk teorisinin temel kavram dağarcığını ve ekollerini bir analiz aracı olarak
sunmak; soruyu geçerlilik, yorum, boşluk veya adalet kategorilerinden hangisine ait olduğunu
belirleyip Türk pozitif hukukuna (TMK m.1, Anayasa m.2/11/138) raptetmek.

## Soğuk başlangıç (intake)
- Soru pozitif bir norm yokken mi soruluyor (boşluk), yoksa var olan normun anlamı/geçerliliği
  mi tartışılıyor?
- Amaç akademik tartışma/sınav mı, yoksa bir uyuşmazlıkta argüman üretmek mi?
- Hangi hukuk dalı bağlamı var (özel/kamu/ceza)? Soyut soru çoğu zaman somut dalda görünür.
- Karşılaştırmalı/yabancı malzeme isteniyor mu, yoksa yalnızca Türk hukuku mu?

## Denetim şeması
1. **Kavramı yerine oturt.** Norm (kural/ilke ayrımı), geçerlilik (yürürlük + bağlayıcılık),
   meşruiyet (içeriksel haklılık), yürürlük (etkililik) ve müeyyide kavramlarını ayır.
   Bunların karıştırılması çoğu teorik hatanın kaynağıdır.
2. **Norm hiyerarşisini kur.** Anayasa m.11 ve m.90/son ışığında Anayasa > milletlerarası
   andlaşma (temel haklarda) > kanun > tüzük/yönetmelik basamağını çıkar; Kelsenci basamak
   teorisinin pozitif karşılığı budur. Üst norma aykırı alt norm tartışmasını burada konumla.
3. **Ekolü araç seç.** Pozitivizm geçerliliği kaynağa bağlar; doğal hukuk içeriğe; realizm
   yargıç davranışına; menfaat/değer içtihadı korunan çıkara. Hangi ekolün soruyu çözdüğünü
   belirt, "tek doğru ekol" iddiasından kaçın.
4. **Pozitif bağı kur.** Her teorik tezi TMK m.1 (hâkimin hukuk yaratması/bilimsel görüş ve
   içtihada başvurma), TMK m.2 (dürüstlük) veya Anayasa m.138 (hâkimin hukuka uygunluğu)
   gibi bir pozitif dayanağa bağla. Ara sonuç: teori → pozitif sonuç köprüsü.
5. **İspat/dayanak yükü.** Teorik iddiayı ulaşılabilir doktrin eserine ve varsa yerleşik
   içtihada dayandır; karar künyesi doğrulanmadıkça [DOĞRULANMADI] işaretle.

## Çıktı modülleri
- Kavram-ayrım tablosu (geçerlilik/meşruiyet/yürürlük).
- Soru tipi etiketi ve ilgili ekol(ler) listesi.
- Pozitif dayanak haritası (madde atıflarıyla).
- İleri çalışma için doktrin okuma listesi (yazar-eser, sayfa [DOĞRULANMADI]).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

