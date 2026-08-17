---
argument-hint: ''
description: Tasarımcının kim olduğu, çalışan/sipariş üzerine yapılan tasarımlarda
  hakkın kime ait olduğu ve gerçek hak sahipliği davasının SMK m.70-73 çerçevesinde
  çözülmesi; tasarım üzerindeki mülkiyetin ihtilaf
name: hak-sahipligi-ve-calisan-tasarimlari
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Hak Sahipliği ve Çalışan Tasarımları

## Görev
Tasarım üzerindeki hakkın gerçek sahibini belirlemek: tasarımcı kimdir, çalışan/sipariş/ortaklık ilişkisinde hak kime aittir ve gerçek hak sahipliği davası nasıl kurulur.

## Soğuk başlangıç (intake)
1. Tasarımı fiilen kim yaptı (gerçek kişi tasarımcı)?
2. Tasarım bir iş/hizmet sözleşmesi kapsamında mı, sipariş üzerine mi, bağımsız mı yapıldı?
3. Sicilde kim hak sahibi görünüyor; başvuruyu kim yaptı?
4. Tasarımcının adının belirtilme (manevi) hakkı talep ediliyor mu?

## Denetim şeması
1. Tasarımcı ilkesi (SMK m.70): Tasarım hakkı, tasarımı yapan tasarımcıya veya halefine aittir. Birden fazla tasarımcı varsa hak müştereken doğar.
2. Çalışan tasarımları (SMK m.73): İşçinin işini görürken veya işverenin talimatıyla yaptığı tasarımların hakkı, aksi sözleşmede kararlaştırılmadıkça işverene aittir. İşçinin bedel/manevi hak talepleri (ad belirtilmesi) saklıdır; SMK ve yönetmelikteki bildirim/karşılık esaslarını uygulayın.
3. Sipariş/vekâlet ilişkisi: Sipariş üzerine yapılan tasarımlarda hak, sözleşmeye göre belirlenir; sözleşme yoksa SMK m.73 mantığı ve TBK eser/vekâlet hükümleri birlikte değerlendirilir.
4. Gerçek hak sahipliği davası (SMK m.71): Tasarım, hak sahibi olmayan kişi tarafından tescil ettirilmişse, gerçek hak sahibi tasarımın kendisine devrini veya hükümsüzlüğünü dava edebilir. Bu sebebi yalnız gerçek hak sahibi/halefi ileri sürebilir (m.77/1-b ile bağlantılı).
5. Manevi hak (SMK m.72): Tasarımcının, tasarımcı olarak belirtilme hakkı vardır; bu hak devredilemez.
6. Ara sonuç: Gerçek hak sahibi, sicil durumu, dava yolu (devir/hükümsüzlük) ve manevi hak durumu net yazılır.

## Çıktı modülleri
- Hak sahipliği zinciri (tasarımcı → işveren/sipariş veren → sicil) tablosu.
- Çalışan/sipariş sözleşmesi madde önerileri (hak devri, bedel, ad belirtme).
- Gerçek hak sahipliği davası iskeleti ve talep türü.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

