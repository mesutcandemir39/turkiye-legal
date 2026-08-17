---
argument-hint: ''
description: Şirket ve yöneticiler için ekonomik suç riskinin haritalanması, etkin
  pişmanlık-uzlaşma-kamu davasının ertelenmesi gibi seçeneklerin tartılması, kurum
  içi uyum (MASAK/SPK/vergi) zafiyetlerinin gideril
name: risk-yonetimi-uyum-savunma-stratejisi
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
  - ad: Kaçakçılıkla Mücadele Kanunu
    numara: '5549'
    tur: kanun
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kurumsal Ceza Riski, Uyum ve Savunma Stratejisi

## Görev
Şirket ve yöneticilerin ekonomik suç riskini bütüncül haritalamak; soruşturma öncesi uyum tedbirleri ile soruşturma/kovuşturma aşamasındaki savunma ve hafifletme seçeneklerini tartmak.

## Soğuk başlangıç (intake)
- Risk hangi başlıkta? (aklama/MASAK, vergi, sermaye piyasası, dolandırıcılık, görev suçları)
- Henüz soruşturma yok mu, var mı, kovuşturmaya mı dönüştü?
- Şirket içinde sorumluluğu kim taşıyor (imza yetkisi, görev dağılımı)?
- Etkin pişmanlık/iade/ödeme penceresi açık mı?

## Denetim şeması
1. **Risk haritası**: Her suç tipi için (aklama TCK m.282/5549, vergi VUK m.359, SPK m.106-107, dolandırıcılık m.158, zimmet/rüşvet m.247/252) failin sıfatı, fiil, manevi unsur ve elkoyma/müsadere riski ayrı satırda değerlendirilir.
2. **Tüzel kişi-gerçek kişi ayrımı**: Tüzel kişiye ceza verilmez (TCK m.20/2); risk gerçek kişi yöneticide yoğunlaşır. Görev dağılımı, imza sirküleri ve karar defterleri sorumluluğu kime bağladığını gösterir — savunmada görevin devri/fiili durum ileri sürülür.
3. **Önleyici uyum**: MASAK uyum programı (yükümlüler için), vergi uyumu (e-fatura/karşıt inceleme disiplini), SPK içsel bilgi/işlem yasakları politikası; ihlal tespit edilince düzeltici adım ve gönüllü bildirim seçenekleri tartılır.
4. **Hafifletme seçenekleri**: Etkin pişmanlık (zimmette m.248, rüşvette m.254, malvarlığı suçlarında m.168, aklamada m.282/6), vergi pişmanlığı (VUK m.371) ve ödeme; suç tipine göre zaman penceresi ve indirim oranı farklıdır. Erken iade/ödeme genelde en güçlü kozdur.
5. **Savunma kurgusu**: Suç tipinin bir unsurunu (kast yokluğu, hile yokluğu, öncül suç eksikliği, mütalaa şartı eksikliği) hedef alan ana savunma ekseni seçilir; usul itirazları (görev, yetki, delil yasağı, iddianame iadesi) paralel hazırlanır.
6. **Ara sonuç**: Risk derecesi, sorumluluk taşıyıcısı, uyum boşluğu ve en uygun hafifletme/savunma hattı netleşir.

## Çıktı modülleri
- Suç tipi bazlı risk matrisi
- Sorumluluk (yönetici/imza) haritası
- Uyum boşluğu ve düzeltici eylem planı
- Etkin pişmanlık/ödeme senaryo karşılaştırması
- Ana savunma ekseni ve usul itirazları notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

