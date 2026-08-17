---
argument-hint: ''
description: Halka açık ortaklığın sürekli kamuyu aydınlatma yükümlülükleri, özel
  durum açıklamaları, içsel bilginin ertelenmesi ve KAP açıklamalarından doğan sorumluluk
  değerlendirileceğinde kullanılır.
name: kamuyu-aydinlatma-ve-ozel-durumlar
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


# Kamuyu Aydınlatma ve Özel Durumlar

## Görev
İhraççının sürekli kamuyu aydınlatma yükümlülüklerini (özel durumlar, finansal raporlama) SPK m.14-15 ve özel durumlar tebliği çerçevesinde denetlemek; açıklama zamanlaması, erteleme ve sorumluluk (m.32) konularını yönetmek.

## Soğuk başlangıç (intake)
- Açıklanması tartışılan bilgi nedir; içsel bilgi (fiyat/yatırım kararı etkili) niteliği taşıyor mu?
- Bilgi ne zaman doğdu, kimler biliyor; açıklama yapıldı mı, ertelendi mi?
- Açıklama eksik/yanlış/gecikmeli mi yapıldı; yatırımcı zararı veya Kurul incelemesi var mı?
- İhraççı, yönetici/imza yetkilisi mi yoksa zarar gören yatırımcı mı danışıyor?

## Denetim şeması
1. **İçsel bilgi tespiti:** Bilginin henüz kamuya açıklanmamış, ortaklık/araçla ilgili, açıklandığında fiyatı veya yatırım kararını etkileyebilecek nitelikte olup olmadığı belirlenir (SPK m.15, m.106 tanımı ile uyumlu). Değilse özel durum açıklaması yükümlülüğü doğmaz.
2. **Açıklama zamanı:** İçsel bilgi oluştuğunda gecikmeksizin KAP üzerinden açıklama esastır; ara sonuç olarak yükümlülüğün doğduğu an tespit edilir.
3. **Erteleme rejimi:** Meşru menfaat, yatırımcının yanıltılmaması ve gizliliğin sağlanması koşullarıyla açıklamanın ertelenebileceği; erteleme kararının ve gerekçesinin belgelenmesi, içsel bilgiye erişenler listesinin tutulması aranır (m.15 ve tebliğ).
4. **Sorumluluk (m.32):** Kamuyu aydınlatma belgelerindeki yanlış/yanıltıcı/eksik bilgiden doğan zarardan ihraççı ve kusurlu yöneticiler sorumludur; ispatta bilginin yanlışlığı ve illiyet yatırımcıda, özen ispatı ihraççıdadır.
5. **Yaptırım ekseni:** İhlal hem idari yaptırım (m.103 vd.) hem -koşulları varsa- piyasa suçu (m.107/2 bilgiye dayalı piyasa dolandırıcılığı) doğurabilir; idari ve cezai süreç ayrıştırılır.

## Çıktı modülleri
- İçsel bilgi/özel durum nitelendirme notu
- Açıklama/erteleme karar ve belgeleme kontrol listesi
- Sorumluluk değerlendirmesi (m.32) ve muhatap analizi
- KAP açıklama taslağı iskeleti veya yatırımcı talep çerçevesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

