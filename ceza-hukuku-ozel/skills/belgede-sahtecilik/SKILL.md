---
argument-hint: ''
description: Resmî/özel belgede sahtecilik, resmî belgenin düzenlenmesinde yalan beyan
  ve bunların dolandırıcılık gibi suçlarla içtimaı gündeme geldiğinde kullanılır.
name: belgede-sahtecilik
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kamu Güvenine Karşı Suçlar (Belgede Sahtecilik)

## Görev
Sahtecilik suçlarında belgenin niteliğini (resmî/özel), sahteciliğin türünü (maddi/fikrî) ve diğer suçlarla içtima ilişkisini madde metniyle belirlemek.

## Soğuk başlangıç (intake)
- Belge resmî belge mi (kamu görevlisinin görevi gereği düzenlediği) yoksa özel belge mi?
- Sahtecilik belgenin tümüyle uydurulması mı, üzerinde değişiklik mi, yoksa gerçeğe aykırı beyanın belgeye geçirilmesi mi?
- Sahte belge kullanıldı mı; kullanılarak ayrıca bir yarar sağlandı mı?
- Belge aldatma kabiliyetine (iğfal kabiliyeti) sahip mi?

## Denetim şeması
1. Resmî belgede sahtecilik (TCK m.204): Resmî belgeyi sahte düzenleme, değiştirme veya sahte belgeyi kullanma + kast. Belgenin kanunen kesin delil oluşturması nitelikli hal (m.204/3). Kamu görevlisi tarafından işlenmesi ağırlaştırıcı (m.204/2).
2. Özel belgede sahtecilik (TCK m.207): Özel belgeyi sahte düzenleme/değiştirme ve kullanma; tamamlanması için belgenin kullanılması da unsurdur.
3. Maddi/fikrî sahtecilik ayrımı: Belgenin fiziksel olarak tahrif edilmesi maddi sahtecilik; içeriğin gerçeğe aykırı olması fikrî sahteciliktir. Resmî belgenin düzenlenmesinde yalan beyan (TCK m.206) ile resmî belgede fikrî sahteciliği ayır.
4. Iğfal (aldatma) kabiliyeti: Sahteciliğin suç oluşturması için belgenin nesnel olarak aldatıcı olması gerekir; bilirkişi/kriminal inceleme bu unsuru belirler. Aldatma kabiliyeti yoksa tipiklik gerçekleşmez.
5. İçtima: Sahte belge bir dolandırıcılığın aracı olarak kullanıldıysa, sahtecilik ve dolandırıcılık (TCK m.157-158) gerçek içtima kurallarına göre ayrı ayrı değerlendirilir; tek fiille birden çok suç söz konusuysa fikrî içtima (m.44) tartışılır.
6. Ara sonuç: Belge türü + sahtecilik türü + uygulanacak madde + iğfal kabiliyeti tespiti + diğer suçlarla içtima sonucu.

## Çıktı modülleri
- Belge/sahtecilik nitelendirme tablosu (madde atıflı).
- İğfal kabiliyeti için bilirkişi sorusu önerisi.
- İçtima değerlendirme notu (sahtecilik + dolandırıcılık vb.).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

