---
argument-hint: ''
description: Yeni işe alım, sözleşme türü seçimi, deneme süresi, belirli/belirsiz
  süreli ayrımı, rekabet yasağı ve gizlilik kayıtları ile iş sözleşmesi taslağı gerektiğinde
  kullanılır.
name: ise-alim-ve-is-sozlesmesi
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
  - ad: İş Kanunu
    numara: '4857'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İşe Alım ve İş Sözleşmesi Tasarımı

## Görev
İşverenin yeni çalışan istihdamında doğru sözleşme türünü seçmesini, emredici hükümlere uygun ve dava riski düşük bir iş sözleşmesi kurmasını sağlamak. Aşırı koruyucu ama geçersiz kayıtlar yerine ayakta kalacak, dengeli metin üretmek.

## Soğuk başlangıç (intake)
1. Pozisyon, görev tanımı ve aylık ücret (brüt/net, prim/yan haklar) nedir?
2. İhtiyaç süreklilik arz ediyor mu, yoksa proje/sezon bazlı objektif neden var mı (belirli süreli için şart)?
3. Çalışan gizli bilgiye/müşteri portföyüne erişecek mi (rekabet yasağı/gizlilik gereği)?
4. Deneme süresi öngörülüyor mu, uzaktan/hibrit mi?

## Denetim şeması
1. **Süre tipi (4857 m.11)**: Belirli süreli sözleşme ancak işin niteliği veya objektif neden varsa kurulabilir; aksi halde baştan **belirsiz süreli** sayılır ve zincirleme yenileme belirsiz süreliye döner. Objektif neden yoksa belirsiz süreli tasarla.
2. **Şekil (m.8)**: Bir yıl ve üzeri süreli sözleşme yazılı yapılır; yazılı olmasa bile işveren 2 ay içinde çalışma koşullarını gösteren belge vermek zorundadır.
3. **Deneme süresi (m.15)**: En çok 2 ay (TİS ile 4 aya çıkarılabilir); bu sürede iki taraf da bildirimsiz fesih yapabilir, ancak kıdem korunur.
4. **Rekabet yasağı (TBK m.444-447)**: Geçerlilik için işçinin müşteri çevresi/üretim sırlarına vakıf olması, **yer-zaman-konu** bakımından sınırlama ve hakkaniyet şarttır; süre kural olarak 2 yılı aşamaz (m.445). Aşırı kayıt hâkim tarafından sınırlanır → ölçülü yaz.
5. **Cezai şart**: Tek taraflı (yalnız işçi aleyhine) ve fahiş cezai şart geçersiz/indirilebilir (TBK m.182). Karşılıklı dengele.
6. **KVKK**: Aday ve çalışan verisi için işleme şartı (m.5) ve aydınlatma (m.10); sağlık/adli sicil özel nitelikli veri olup işleme sınırlıdır. İspat yükü: sözleşmenin yapıldığını ve içeriğini işveren ispatlar.

## Çıktı modülleri
- İş sözleşmesi taslağı (tür gerekçesi + esas kayıtlar + [doldurulacak] alanlar).
- Görev tanımı ve çalışma koşulları eki.
- Gizlilik/rekabet yasağı ve KVKK aydınlatma + ek protokol seti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

