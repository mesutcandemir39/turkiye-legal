---
argument-hint: ''
description: 6563 kapsamında idari para cezası, ETBİS kayıt yükümlülüğü, ETAHS lisansı
  veya Ticaret Bakanlığı denetim/yaptırımına ilişkin bir durumun değerlendirilmesi
  ya da itiraz hazırlanması gerektiğinde kullan
name: idari-yaptirim-etbis-uyum
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
  - ad: Elektronik Ticaretin Düzenlenmesi Hakkında Kanun
    numara: '6563'
    tur: kanun
  - ad: Tüketicinin Korunması Hakkında Kanun
    numara: '6502'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İdari Yaptırım, ETBİS ve Lisans Uyumu

## Görev
6563 sayılı Kanun ve yönetmelikleri kapsamında ETBİS kaydı, ETAHS lisansı ve idari para cezalarına ilişkin uyumu denetlemek; verilen idari yaptırıma karşı itiraz/dava stratejisini kurmak.

## Soğuk başlangıç (intake)
- Müvekkil ETBİS'e kayıtlı mı; faaliyet türü kayıt kapsamında mı?
- Bir idari yaptırım kararı tebliğ edildi mi; dayanağı hangi madde?
- ETAHS ise net işlem hacmi lisans eşiğini aşıyor mu, lisans alındı mı?
- Tebliğ tarihi ve itiraz süresi ne durumda?

## Denetim şeması
1. ETBİS (6563 m.11): hizmet sağlayıcı ve aracı hizmet sağlayıcılar, Bakanlıkça belirlenen kapsamda Elektronik Ticaret Bilgi Sistemi'ne kayıt ve bildirim yapar; kayıtsızlık idari yaptırım sebebidir.
2. Lisans (ETAHS): belirli net işlem hacmi eşiğini aşan elektronik ticaret aracı hizmet sağlayıcılar Bakanlıktan lisans almak ve lisans bedeli ödemekle yükümlüdür; reklam/indirim bütçesi sınırlarına uyulur.
3. İdari para cezaları (6563 m.12): bilgi verme, ticari ileti, ETBİS, aracı yükümlülükleri ve lisans ihlallerine bağlı kademeli idari para cezaları ile faaliyet durdurma/erişim engelleme tedbirleri öngörülür; ceza miktarları her yıl yeniden değerleme oranıyla güncellenir.
4. Yaptırıma karşı yol: idari yaptırım kararının niteliğine göre başvuru mercii belirlenir; idari para cezası niteliğindeki kararlara karşı 2577 sayılı İYUK uyarınca idari yargı yolu (iptal davası) ya da ilgili özel başvuru yolu değerlendirilir; süreler kaçırılmaz.
5. Savunma ekseni: yetki-şekil-sebep-konu-maksat denetimi; tebligat usulü, oransızlık ve maddi hata itirazları.
İspat yükü: yükümlülüğün yerine getirildiğini müvekkil belgelerle ortaya koyar.

## Çıktı modülleri
- ETBİS/lisans uyum kontrol listesi.
- Yaptırım risk ve süre takvimi.
- İtiraz/iptal dilekçesi iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

