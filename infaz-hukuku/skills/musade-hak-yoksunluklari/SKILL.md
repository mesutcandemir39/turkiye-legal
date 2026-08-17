---
argument-hint: ''
description: Müsadere, belli hakları kullanmaktan yoksun bırakma ve diğer güvenlik
  tedbirlerinin infazı ile bu yoksunlukların sona ermesini değerlendirmek gerektiğinde
  kullanılır.
name: musade-hak-yoksunluklari
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
  - ad: Ceza ve Güvenlik Tedbirlerinin İnfazı Hakkında Kanun
    numara: '5275'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Güvenlik Tedbirleri, Müsadere ve Hak Yoksunluklarının İnfazı

## Görev
Hapis/para cezası yanında hükmedilen güvenlik tedbirlerinin (müsadere, hak yoksunlukları) infazını ve bunların ne zaman sona ereceğini TCK ve 5275 çerçevesinde belirlemek.

## Soğuk başlangıç (intake)
- Hükümde hangi güvenlik tedbiri var (müsadere, hak yoksunluğu, sınır dışı, tedavi)?
- Müsadere eşya mı kazanç mı; üçüncü kişi hakkı söz konusu mu?
- Hak yoksunlukları mahkûmiyetin kanuni sonucu mu, ayrıca hükmedilmiş mi?
- Koşullu salıverilme/erteleme yoksunlukların süresini etkiliyor mu?

## Denetim şeması
1. Hak yoksunlukları: TCK m.53 kasten işlenen suçtan mahkûmiyetin kanuni sonucu olarak belirli hakları kullanmaktan yoksunluğu öngörür; kural olarak cezanın infazı tamamlanıncaya kadar sürer, belirli istisnalarda farklı süre uygulanır. Ara sonuç: yoksunluğun kapsamı ve süresi.
2. Müsadere: eşya müsaderesi (TCK m.54) ve kazanç müsaderesi (TCK m.55) ayrı denetlenir; iyiniyetli üçüncü kişiye ait eşya korunur, müsadere konusu mülkiyet ilişkisi araştırılır. İspat: malın suçla bağlantısı ve mülkiyet durumu.
3. Diğer tedbirler: akıl hastalarına özgü tedavi/koruma tedbirleri (TCK m.57), tüzel kişiler hakkında güvenlik tedbirleri (TCK m.60), yabancılarda sınır dışı (TCK m.59).
4. İnfaz usulü: güvenlik tedbirleri 5275 genel hükümlerine ve ilgili yönetmeliklere göre Cumhuriyet savcılığınca infaz edilir.
5. Sona erme/iade: hak yoksunlukları infazın tamamlanmasıyla; yasaklanmış hakların geri verilmesi için ayrı bir karar gerekebilir (5352 sayılı Adli Sicil Kanunu m.13/A çerçevesinde). Müsadere edilen ancak iadesi gereken eşya için iade usulü işletilir.
6. İtiraz: müsadere/iade ve yoksunluk uygulamasına karşı hükmü veren mahkeme veya infaz hâkimliği yolu; ilkesel içtihat karararama.yargitay.gov.tr, künye `[DOĞRULANMADI]`.
7. Ara sonuç: tedbir kapsamı + süre/sona erme + başvuru mercii.

## Çıktı modülleri
- Güvenlik tedbiri envanteri ve süre tablosu.
- Üçüncü kişi hakkı/iade kontrol listesi.
- Yasaklanmış hakların geri verilmesi veya iade talebi dilekçesi tetiği.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

