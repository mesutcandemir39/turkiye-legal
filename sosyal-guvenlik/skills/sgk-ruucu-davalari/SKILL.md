---
argument-hint: ''
description: SGK'nın iş kazası, meslek hastalığı, trafik kazası veya üçüncü kişinin
  haksız fiili sonucu yaptığı ödemeleri kusurlu işveren ya da üçüncü kişiden geri
  istemesi söz konusu olduğunda; işveren/sigorta şi
name: sgk-ruucu-davalari
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
  - ad: Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu
    numara: '5510'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# SGK Rücu Davaları

## Görev
SGK'nın bağladığı gelir ve yaptığı masrafları kusurlu işveren, üçüncü kişi veya sorumlu sigortacıdan geri alma davasını kurmak veya bu davaya karşı savunma stratejisi geliştirmek.

## Soğuk başlangıç (intake)
- Rücuya konu olay iş kazası/meslek hastalığı mı, trafik kazası mı, başka bir haksız fiil mi?
- SGK hangi edimleri ödedi (geçici/sürekli iş göremezlik geliri, ölüm geliri, sağlık masrafı)?
- Sorumlu kim: işveren mi, üçüncü kişi mi, trafik sigortacısı mı?
- Kusur oranı belirlendi mi; ceza/hukuk dosyası var mı?

## Denetim şeması
1. Dayanak — 5510 m.21 (iş kazası/meslek hastalığı için işverene/üçüncü kişiye rücu) ve m.39/trafik kazasında ilgili hükümler; genel hükümler bakımından TBK m.49 vd. (haksız fiil) ve halefiyet.
2. Sorumluluğun kapsamı: Rücu, Kurumun ilk peşin sermaye değeri (bağlanan gelirin sermayeye çevrilmiş tutarı) ile sınırlıdır; bağlanan gelir miktarının tamamı değil, sigortalının zararı ve kusur oranı süzgecinden geçer.
3. Kusur tespiti: İşverenin İSG ihlali (6331) veya üçüncü kişinin haksız fiili bilirkişiyle saptanır; müterafik kusur (sigortalının kusuru) indirim sebebidir.
4. Sigortacıya yöneltme: Trafik kazalarında Zorunlu Mali Sorumluluk Sigortası kapsamı ve teminat limiti gözetilir (2918 sayılı Kanun ile bağlantı).
5. Zamanaşımı: Rücu alacağında haksız fiil zamanaşımı ve özel hükümler birlikte değerlendirilir; başlangıç anı (gelirin bağlandığı/onay tarihi) tartışmalıdır, içtihat kontrol edilir [DOĞRULANMADI]. Ara sonuç: rücu edilebilir tutar ve sorumlu çevresi. İspat: ödeme/onay belgeleri, kusur raporu.

## Çıktı modülleri
- Rücu tutarı ve sorumluluk dağılımı tablosu.
- İşveren/sigortacı savunma argümanları (kusur, limit, peşin sermaye değeri).
- Dava/savunma dilekçesi iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

