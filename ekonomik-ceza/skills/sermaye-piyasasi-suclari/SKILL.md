---
argument-hint: ''
description: Bilgi suistimali/içeriden öğrenenlerin ticareti (SPK m.106), piyasa dolandırıcılığı/manipülasyon
  (SPK m.107) ve sermaye piyasası araçlarıyla işlenen güveni kötüye kullanma/sahtecilik
  (m.110) iddiaları
name: sermaye-piyasasi-suclari
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


# Sermaye Piyasası Suçları (Manipülasyon ve İçsel Bilgi)

## Görev
6362 sayılı SPK m.106-107-110 suçlarını unsurlarına göre denetlemek; SPK'nın şikâyet/mütalaa şartını (m.115) ve idari yaptırımla ceza yargısı arasındaki ilişkiyi yönetmek.

## Soğuk başlangıç (intake)
- İddia hangi fiile dayanıyor? (içsel bilgiyle işlem, fiyat/işlem hacmi manipülasyonu, yanıltıcı bilgi/yalan haber)
- Failin pozisyonu: yönetici/ortak/aracı kurum çalışanı/yatırımcı?
- SPK incelemesi/raporu ve şikâyeti/mütalaası var mı (m.115)?
- İdari para cezası ayrıca uygulandı mı?

## Denetim şeması
1. **Bilgi suistimali — insider (SPK m.106)**: Henüz kamuya açıklanmamış, açıklandığında araç fiyatını/yatırımcı kararını etkileyebilecek nitelikteki içsel bilgiyi kullanarak işlem yapma/yaptırma/aktarma. Failin bilgiye erişim kaynağı (organ, çalışan, meslek/görev) ve bilginin "içsel/önemli" niteliği tespit edilir.
2. **Piyasa dolandırıcılığı (SPK m.107)**: (1) işlem bazlı manipülasyon — fiyat/talep/arz konusunda yanlış izlenim veren alım-satım; (2) bilgi bazlı manipülasyon — yalan, yanlış, yanıltıcı bilgi verme, dedikodu yayma. İşlem örüntüsü (wash trade, layering vb.) ve yanıltma kastı incelenir.
3. **m.110 suçları**: Sermaye piyasası araçlarıyla güveni kötüye kullanma, izinsiz halka arz/faaliyet, belge sahteciliği — ilgili fıkraya göre ayrılır.
4. **Şikâyet/mütalaa şartı (SPK m.115)**: Bu suçlarda soruşturma SPK'nın Cumhuriyet başsavcılığına yazılı başvurusuna (şikâyet) bağlıdır; SPK'nın mütalaası alınmadan kovuşturma yürütülemez. İlk kontrol budur.
5. **İdari yaptırımla ilişki**: SPK idari para cezası ve işlem yasakları ayrıca uygulanabilir; ceza ve idari yaptırımın paralelliği ile non bis in idem tartışması not edilir.
6. **Ara sonuç**: Fiil tipi (m.106/107/110), içsel bilgi veya manipülasyon kastının kanıtı, şikâyet şartı ve idari süreç netleşir.

## Çıktı modülleri
- Fiil-madde eşleştirme (m.106/107/110)
- İçsel bilgi/önemlilik veya manipülasyon örüntüsü analizi
- m.115 şikâyet/mütalaa şartı kontrolü
- İdari yaptırım-ceza paralel notu
- Savunma stratejisi taslağı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

