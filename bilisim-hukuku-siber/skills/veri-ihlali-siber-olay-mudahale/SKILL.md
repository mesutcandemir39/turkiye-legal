---
argument-hint: ''
description: Yaşanan bir veri ihlali veya siber saldırı sonrası KVKK m.12 bildirim
  yükümlülüğü, kriz yönetimi ve hukuki müdahale adımlarını planlamak; bildirim sürelerini
  ve içeriklerini belirlemek gerektiğinde ku
name: veri-ihlali-siber-olay-mudahale
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Elektronik Ticaretin Düzenlenmesine Dair Kanun
    numara: '5651'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Veri İhlali ve Siber Olay Müdahalesi

## Görev
Gerçekleşmiş veya şüpheli bir veri ihlali/siber olayda hukuki müdahale akışını kurmak; KVKK bildirim yükümlülüklerini, içeriklerini ve eş zamanlı ceza/sözleşme adımlarını yönetmek.

## Soğuk başlangıç (intake)
1. Ne oldu ve ne zaman fark edildi? (sızıntı, fidye yazılımı, yetkisiz erişim?)
2. Hangi kişisel veriler ve kaç ilgili kişi etkilendi? (özel nitelikli veri var mı?)
3. Veri sorumlusu kim, yurt dışı aktarım/işleyen zinciri var mı?
4. Sistem hâlâ tehdit altında mı, loglar/imaj korundu mu?

## Denetim şeması
1. **Kapsam ve sınıflandırma.** Olayın KVKK m.12/5 anlamında bir "veri ihlali" (kişisel verilerin kanuni olmayan yollarla başkalarınca elde edilmesi) olup olmadığı belirlenir. İhlal yoksa salt güvenlik olayı olarak iç süreç işler.
2. **Bildirim yükümlülüğü (KVKK m.12/5).** Veri sorumlusu ihlali öğrendiği tarihten itibaren en kısa sürede Kurula bildirir; Kurul kararları uyarınca bu süre kural olarak **72 saat** olarak uygulanır. İlgili kişilere de makul en kısa sürede bildirim yapılır. Form ve içerik kvkk.gov.tr'deki ihlal bildirim usulüne göre hazırlanır (ihlalin niteliği, etkilenen veri/kişi sayısı, olası sonuçlar, alınan önlemler).
3. **Delil ve sistem güvenliği.** Adli bilişim için imaj/log korunur (bkz. dijital delil becerisi); müdahale ekibinin hareketleri kayda alınır. İz silmemek esastır.
4. **Ceza ekseni.** Fiil aynı zamanda TCK m.243-244 ve m.135-140 kapsamında suç olabilir; suç duyurusu seçeneği değerlendirilir. İspat yükü: KVKK uyumunda veri sorumlusu, m.12'deki teknik/idari tedbirleri aldığını ispatla yükümlüdür; aksi halde m.18 idari para cezası riski doğar.
5. **Sözleşme ve aktarım ekseni.** Veri işleyen/alt işleyen sözleşmeleri, yurt dışı aktarım şartları ve müşteri/iş ortağı bildirim yükümlülükleri kontrol edilir. **Ara sonuç:** Bildirim takvimi, sorumlu rolleri ve risk önceliklendirmesi netleştirilir.

## Çıktı modülleri
- 72 saatlik aksiyon takvimi ve sorumlu matrisi.
- Kurul ihlal bildirim formu taslağı ve ilgili kişi bilgilendirme metni.
- Ceza/sözleşme eksenli ek aksiyon listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

