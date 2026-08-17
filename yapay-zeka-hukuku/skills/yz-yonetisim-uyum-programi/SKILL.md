---
argument-hint: ''
description: Bir kurumda yapay zekâ sistemlerinin geliştirilmesi veya kullanılması
  için iç politika, etki değerlendirmesi, envanter, insan gözetimi ve sorumluluk yapısı
  kurulması istendiğinde proaktif uyum program
name: yz-yonetisim-uyum-programi
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kurumsal Yapay Zekâ Yönetişimi ve Uyum Programı

## Görev
Bir kurumun yapay zekâ kullanımını hukuki riske karşı yöneten iç yönetişim programını tasarlamak: envanter, politika, etki değerlendirmesi, insan gözetimi ve sorumluluk dağılımı.

## Soğuk başlangıç (intake)
1. Kurum YZ'yi nerede kullanıyor: İK, müşteri hizmeti, kredi/risk, pazarlama, üretim?
2. Sistemler iç geliştirme mi, üçüncü taraf (kapalı API) mi?
3. Kişisel veri ve özel nitelikli veri işleniyor mu; VERBİS kaydı var mı?
4. Mevcut KVKK uyum altyapısı (envanter, aydınlatma, saklama-imha) ne durumda?

## Denetim şeması
1. **Envanter ve sınıflandırma**: Tüm YZ sistemlerini, işledikleri veriyi ve karar etkisini envantere alın; her sistemi risk düzeyine göre ayırın (AB Tüzüğü sınıflandırması yön gösterici). Ara sonuç: yüksek etkili sistemler önceliklendirilir.
2. **KVKK uyumu**: m.4 ilkeler, m.5-6 işleme şartı, m.10 aydınlatma (otomatik karar açıklaması), m.11 hak süreçleri, m.12 güvenlik ve gerekirse VERBİS güncellemesi; etki değerlendirmesi (DPIA benzeri) yüksek riskte zorunlu pratik.
3. **İnsan gözetimi ve karar yetkisi**: Münhasıran otomatik kararı önlemek için anlamlı insan denetimi, itiraz mekanizması ve karar gerekçesi loglama tasarlanır (m.11/1-g riski yönetimi).
4. **Sözleşmesel zincir**: Üçüncü taraf modellerde veri işleyen sözleşmeleri, sorumluluk ve tazmin maddeleri (bkz. YZ sözleşmeleri becerisi).
5. **İç politika ve eğitim**: Kabul edilebilir kullanım politikası, gizli bilgi/halüsinasyon riski uyarıları, olay müdahale ve veri ihlali bildirimi (m.12) akışı.

Kurul rehberlerini kvkk.gov.tr'den güncel takip et; doğrulanmamış kaynağı [DOĞRULANMADI] işaretle.

## Çıktı modülleri
- YZ envanteri ve risk sınıflandırma tablosu.
- Uyum boşluğu raporu ve aksiyon planı.
- İç politika ve insan gözetimi prosedürü taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

