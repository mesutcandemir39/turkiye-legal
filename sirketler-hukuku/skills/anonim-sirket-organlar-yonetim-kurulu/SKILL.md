---
argument-hint: ''
description: Anonim şirkette yönetim kurulunun oluşumu, görev-yetki dağılımı, temsil,
  devredilemez yetkiler, toplantı ve karar nisapları ile iç yönerge konuları gündeme
  geldiğinde; yönetim ve temsil ilişkilerini d
name: anonim-sirket-organlar-yonetim-kurulu
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# AŞ Organları ve Yönetim Kurulu

## Görev
Anonim şirkette yönetim ve temsil yapısını TTK'ya uygun kurmak: YK oluşumu, devredilemez yetkiler, yetki devri (iç yönerge), temsil ve bağlayıcılık, toplantı/karar usulü.

## Soğuk başlangıç (intake)
1. YK kaç üyeli; tüzel kişi üye var mı (m.359/2)?
2. Yetki devri/iç yönerge mevcut mu; murahhas üye/müdür atandı mı?
3. Somut işlem hangi yetkiye giriyor (olağan yönetim mi, devredilemez yetki mi)?
4. Temsil yetkisi nasıl düzenlenmiş (çift imza, münferit, sınırlama)?
5. Karar fiziki toplantıyla mı, elden dolaştırmayla mı (m.390/4) alındı?

## Denetim şeması
1. Oluşum: YK en az bir üye (m.359); üyelerin tescil-ilanı m.359-360; tüzel kişi üyenin gerçek kişi temsilcisi m.359/2.
2. Devredilemez görev ve yetkiler: m.375 (üst gözetim, muhasebe-finans denetim düzeni, müdürlerin atanması, genel kurulun hazırlanması vb.) — bunlar devredilemez.
3. Yetki devri: Yönetim yetkisi iç yönergeyle murahhaslara/üçüncü kişilere devredilebilir (m.367); en az bir üyenin temsil yetkisi kalmalı (m.370/1).
4. Temsil: m.370-371; şirket, temsilcilerin işletme konusu dışındaki işlemleriyle de bağlanır, iyiniyetli üçüncü kişiye karşı konu sınırı ileri sürülemez (m.371/2 ultra vires'in yumuşatılması). Temsil yetkisinin sınırlandırılması iyiniyetli üçüncü kişiye karşı geçersiz (m.371/3), ancak merkez/şube ve birlikte imza tescil edilmişse geçerli (m.371/3).
5. Toplantı ve nisap: Aksi esas sözleşmede yoksa üye tam sayısının çoğunluğuyla toplanır, toplantıda hazır üyelerin çoğunluğuyla karar alınır (m.390/1); oyların eşitliği m.390/3; elden dolaştırma m.390/4.
6. Menfaat çatışması/işlem yasakları: m.393 (müzakereye katılma yasağı), m.395 (şirketle işlem/borçlanma yasağı), m.396 (rekabet yasağı).
7. İspat: Geçerli karar ve yetki, kararı dayanak yapan tarafça; usulsüzlük iddiası iddia edence ispatlanır.

## Çıktı modülleri
- YK kararı/iç yönerge taslağı.
- Temsil ve imza sirküleri uyum notu.
- Devredilemez yetki ve menfaat çatışması kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

