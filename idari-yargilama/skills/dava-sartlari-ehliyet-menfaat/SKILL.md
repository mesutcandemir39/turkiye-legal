---
argument-hint: ''
description: Davacının dava açma ehliyetinin, iptal davasında menfaatinin veya tam
  yargıda kişisel hak ihlalinin, husumetin ve kesin işlem şartının incelenmesi gerektiğinde
  kullanılır; davanın ilk inceleme aşaması
name: dava-sartlari-ehliyet-menfaat
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


# Dava Şartları, Ehliyet ve Menfaat

## Görev
Davanın esasa girilmeden reddine yol açacak dava şartı eksikliklerini önceden tespit etmek: ehliyet, menfaat/kişisel hak, husumet, kesin-yürütülebilir işlem ve idari merci tecavüzü.

## Soğuk başlangıç (intake)
- Davacı gerçek/tüzel kişi mi; dava ehliyeti ve temsil yetkisi var mı?
- Davacının işlemle güncel, kişisel ve meşru bir menfaat ilişkisi nedir?
- Davalı olarak doğru idare gösterildi mi?
- İşlem kesin ve yürütülebilir mi, yoksa hazırlık işlemi mi?

## Denetim şeması
1. **Ehliyet** (İYUK m.31 yollamasıyla HMK m.50 vd.): Taraf ve dava ehliyeti aranır. Tüzel kişilerde organın temsil yetkisi ve dava açma kararı; kamu kurumu niteliğindeki meslek kuruluşlarında üyelerinin ortak menfaatini ilgilendiren işlemlere karşı dava ehliyeti gözetilir.
2. **Menfaat / kişisel hak** (İYUK m.2): İptal davasında **menfaat ihlali** yeterlidir; menfaat güncel, kişisel ve meşru olmalı (subjektif kamu hukuku ilişkisi). Düzenleyici işlemlere karşı menfaat daha geniş yorumlanır. Tam yargıda ise **kişisel hak ihlali** aranır.
3. **Husumet** (davalı idarenin doğru gösterilmesi): Yanlış idareye husumet yöneltilmesi tek başına ret sebebi değildir; mahkeme gerçek hasmı resen belirleyip dilekçeyi tebliğ ettirebilir (İYUK m.15/1-c uygulaması).
4. **Kesin ve yürütülebilir işlem** (İYUK m.14/3-d): İcrai olmayan görüş, mütalaa, hazırlık işlemleri dava edilemez. Zincir işlemde nihai/kesin işlem dava konusu yapılır.
5. **İdari merci tecavüzü** (İYUK m.15/1-e): Mevzuat zorunlu bir idari başvuru öngörmüşse, bu yol tüketilmeden açılan dava görev/merci yönünden reddedilip dilekçe ilgili mercie tevdi edilir.
6. **Ara sonuç**: İlk inceleme (İYUK m.14) sırrasında saptanan eksiklikler m.15 sonuçlarına bağlanır; bazıları (ehliyet, kesin işlem, süre) doğrudan ret, bazıları düzeltme/merci tayini ile sonuçlanır.

## Çıktı modülleri
- Dava şartı kontrol listesi (karşılandı/risk/eksik)
- Husumet ve kesin işlem tespiti
- Ret riskini azaltıcı düzeltme önerileri



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

