---
argument-hint: ''
description: İdari yargıda ispat yükünün dağılımı, resen araştırma ilkesi, ara karar
  ile belge getirtme, bilirkişi ve keşif kullanımı değerlendirilirken kullanılır;
  idarenin işlem dayanaklarını sunmaması veya deli
name: ispat-delil-ve-resen-arastirma
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
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İspat, Delil ve Resen Araştırma

## Görev
İdari yargılamanın resen araştırma ilkesi çerçevesinde ispat yükünü dağıtmak, eksik delilleri ara kararla tamamlatmak ve bilirkişi/keşif gibi araçları doğru kullanmak.

## Soğuk başlangıç (intake)
- İşlemin sebebine/dayanağına ilişkin belgeler kimde (idarede mi, davacıda mı)?
- Çekişmeli maddi olgular neler; teknik/hesap bilirkişisi gerekli mi?
- İdare savunmasında dayanak belgeleri sundu mu?
- Hangi olgu ispatlanamazsa dava aleyhe sonuçlanır?

## Denetim şeması
1. **Resen araştırma ilkesi** (İYUK m.20): İdari yargıda hâkim, davanın çözümü için gerekli her türlü bilgi ve belgeyi taraflardan ve ilgili yerlerden **resen** isteyebilir; tahkikatı kendisi yürütür. Bu, dispozitif ilkenin yumuşatılmış hâlidir.
2. **İspat yükünün dağılımı**: İptal davasında işlemin sebep ve maddi dayanağını ortaya koymak kural olarak idareye düşer; idare işleminin hukuka uygunluğunu belgelendirmelidir. Tam yargıda zararın varlığı ve miktarını ispat kural olarak davacıdadır.
3. **Belge getirtme / ara karar**: Mahkeme idareden işlem dosyasının tamamını ister; idare belgeleri sunmaktan kaçınırsa bu durum işlem aleyhine değerlendirilebilir (idarenin savunma hakkıyla dengeli).
4. **Bilirkişi ve keşif** (İYUK m.31 yollamasıyla HMK ilgili hükümleri): Çözümü özel/teknik bilgi gerektiren hâllerde bilirkişi; mahallinde inceleme gerektiren hâllerde keşif yapılır. Bilirkişi raporu hâkimi bağlamaz, denetlenir.
5. **Delil yasakları ve gizlilik**: Devlet sırrı/ticari sır içeren belgelerde özel rejim gözetilir; hukuka aykırı elde edilen delil değerlendirilmez.
6. **Ara sonuç**: Resen araştırma, davacının ispat külfetini tümüyle kaldırmaz; davacı somut iddiasını ve başlangıç delilini sunmalı, mahkeme bunu tamamlatmalıdır.

## Çıktı modülleri
- İspat yükü dağılım tablosu (olgu / yük / delil)
- Ara karar talep listesi (getirtilecek belgeler)
- Bilirkişi/keşif gerekçesi taslağı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

