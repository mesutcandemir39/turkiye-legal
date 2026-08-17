---
argument-hint: ''
description: Aracı kurum/banka ile yatırımcı arasındaki çerçeve sözleşme, uygunluk-yerindelik,
  emir gerçekleştirme, müşteri varlıklarının korunması ve yatırımcı tazmini sorunları
  gündeme geldiğinde kullanılır.
name: yatirim-kuruluslari-ve-yatirimci-koruma
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


# Yatırım Kuruluşları ve Yatırımcının Korunması

## Görev
Yatırım kuruluşu (aracı kurum/banka) ile yatırımcı arasındaki ilişkiyi SPK m.34 vd. ve yatırım hizmetleri tebliğleri çerçevesinde denetlemek; uygunluk/yerindelik testi, emir gerçekleştirme, müşteri varlıkları ve tazmin yollarını değerlendirmek.

## Soğuk başlangıç (intake)
- Hangi yatırım hizmeti söz konusu: alım-satım aracılığı, portföy yönetimi, danışmanlık mı?
- Çerçeve sözleşme ve uygunluk/yerindelik testi yapıldı mı; risk bildirimi imzalandı mı?
- Şikâyet konusu: yetkisiz işlem, yerindelik ihlali, emir gerçekleştirmeme, varlık kaybı mı?
- Müvekkil yatırımcı mı, yatırım kuruluşu mu; kuruluş faaliyet iznini koruyor mu?

## Denetim şeması
1. **Hizmet nitelendirmesi:** Sunulan hizmetin türü (SPK m.37 yatırım hizmet ve faaliyetleri) belirlenir; her hizmet farklı yükümlülük setine tabidir.
2. **Uygunluk/yerindelik:** Müşteri sınıflandırması ve yerindelik/uygunluk testinin yapılıp yapılmadığı, ürünün müşteri profiline uygunluğu denetlenir; eksiklik kuruluşun sorumluluğunu ağırlaştırır.
3. **Emir ve özen:** Emir gerçekleştirme ilkeleri, en iyi şekilde gerçekleştirme ve özen yükümlülüğü; yetkisiz/talimat dışı işlem iddiası talimat kayıtları ve ses kayıtlarıyla incelenir. Ara sonuç: kusurun kimde olduğu netleşir.
4. **Müşteri varlıkları:** Müşteri varlıklarının kuruluş malvarlığından ayrı tutulması, MKK/Takasbank nezdindeki kayıtlar üzerinden doğrulanır; kayıp halinde Yatırımcı Tazmin Merkezi (SPK m.83) devreye girer.
5. **Sorumluluk ve yol:** Sözleşmeye aykırılık/haksız fiil (TBK m.112, m.49) ile SPK yükümlülükleri birlikte değerlendirilir; uyuşmazlıkta sözleşmesel tahkim, Kurul şikâyeti ve adli yargı yolları ayrıştırılır. İspatta talimat/işlem kayıtları esastır.

## Çıktı modülleri
- Hizmet ve yükümlülük haritası
- Uygunluk/yerindelik ve emir denetim notu
- Tazmin yolu (YTM/dava/tahkim) değerlendirmesi
- Yatırımcı talep iskeleti veya kuruluş savunma çerçevesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

