---
argument-hint: ''
description: İşleme dayalı veya bilgiye dayalı manipülasyon, fiyat-miktarda yapay
  görüntü oluşturma, yanlış/yanıltıcı bilgi yayma iddiaları ve SPK m.107 sorumluluğu
  değerlendirileceğinde kullanılır.
name: piyasa-dolandiriciligi-manipulasyon
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


# Piyasa Dolandırıcılığı (Manipülasyon)

## Görev
Piyasa dolandırıcılığı iddiasını SPK m.107'nin iki türü (işleme dayalı ve bilgiye dayalı) üzerinden çözümlemek; yapay fiyat/arz-talep görüntüsü veya yanıltıcı bilgi unsurlarını delillerle bağlayarak sorumluluk değerlendirmesi yapmak.

## Soğuk başlangıç (intake)
- İddia hangi türde: işlem/emir bazlı yapaylık mı, yoksa yanlış/yanıltıcı bilgi yayma mı?
- Hangi araçta, hangi dönemde; anormal fiyat/hacim hareketi var mı?
- İşlemleri yapan/koordine eden kim; bağlantılı hesaplar, eşleştirilmiş emirler söz konusu mu?
- Müvekkil şüpheli/sanık mı yoksa Kurul incelemesine yanıt mı hazırlıyor?

## Denetim şeması
1. **Tür ayrımı:** SPK m.107/1 işleme dayalı (alım-satım, emir, emir iptali yoluyla fiyat/arz-talep/değerde yapay görünüm); m.107/2 bilgiye dayalı (yalan, yanlış, yanıltıcı bilgi vererek, haber yayarak ya da yorumla fiyatı etkileme) olarak ayrıştırılır.
2. **İşleme dayalı unsurlar:** Fiyatı, değeri veya yatırımcı kararlarını etkilemek amacıyla yapay arz-talep/fiyat görüntüsü oluşturulması aranır; eşleştirilmiş emirler, wash trade, hesaplar arası bağlantı, emir-iptal örüntüleri incelenir.
3. **Bilgiye dayalı unsurlar:** Verilen bilginin yanlış/yanıltıcı niteliği, yayılma kanalı ve fiyat üzerindeki etkisi kurulur; gerçek bilgilendirme ile manipülatif yayma ayrılır. Ara sonuç: hangi tür ve seçimlik hareketin oluştuğu netleşir.
4. **Kast ve illiyet:** Yapaylık veya yanıltma kastı; işlem/emir kayıtları, hesap sahipliği, KAP-haber zamanlaması ve fiyat etkisi analiziyle bağlanır. İspat iddia makamında (CMK m.217).
5. **Yaptırım ve usul:** Ceza m.107; idari boyut m.103 vd.; menfaat iadesi m.104; soruşturma için Kurul mütalaası m.115; etkin pişmanlık m.109. İçtihat Yargıtay bankasından doğrulanır, künye `[DOĞRULANMADI]`.

## Çıktı modülleri
- Tür ve unsur analizi (m.107/1 ve /2)
- İşlem/emir örüntüsü ve fiyat-hacim kronolojisi
- Savunma/iddia stratejisi ve menfaat iadesi/etkin pişmanlık notu
- Kurul mütalaası ve usul yol haritası



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

