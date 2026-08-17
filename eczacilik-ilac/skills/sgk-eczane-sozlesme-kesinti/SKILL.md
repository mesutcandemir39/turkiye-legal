---
argument-hint: ''
description: Eczane ile SGK arasındaki protokol, reçete kesintileri, cezai şart, MEDULA
  provizyonu ve sözleşme feshi uyuşmazlıklarında itiraz kademeleri ve dava yolunu
  kurmak için kullanılır.
name: sgk-eczane-sozlesme-kesinti
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
  - ad: Hemşirelik Kanunu
    numara: '6197'
    tur: kanun
  - ad: Mimar ve Mühendisler Hakkında Kanun
    numara: '1262'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# SGK-Eczane Protokolü ve Kesinti Uyuşmazlıkları

## Görev
Eczacı-SGK arasındaki ilaç temin protokolünden doğan kesinti, cezai şart ve fesih uyuşmazlıklarında doğru itiraz kademesini ve yargı yolunu belirlemek.

## Soğuk başlangıç (intake)
- Uyuşmazlık reçete kesintisi mi, cezai şart mı, sözleşmenin feshi/sözleşme dışı bırakma mı?
- Eczacı ile SGK arasında imzalanan protokol/sözleşme yürürlükte mi; protokoldeki itiraz kademeleri kullanıldı mı?
- Kesinti gerekçesi: reçete/fatura uyumsuzluğu, mükerrer, MEDULA/provizyon hatası, kural ihlali mi?
- Tebliğ/kesinti tarihi ve itiraz süreleri?

## Denetim şeması
1. **İlişkinin niteliği.** SGK-eczacı protokolü idari sözleşme tartışmalıdır; uygulamada kesinti ve cezai şart uyuşmazlıklarında görevli yargı yeri içtihatla şekillenir — güncel görev içtihadı karararama.danistay.gov.tr ve karararama.yargitay.gov.tr üzerinden teyit edilmelidir [DOĞRULANMADI].
2. **İtiraz kademesi.** Önce protokolde öngörülen itiraz komisyonu/kademesi tüketilir. Ara sonuç: idari/sözleşmesel başvuru yolu tamamlandı mı?
3. **Esas denetimi.** Kesintinin dayanağı SUT ve protokol kuralı; reçete-fatura örneklemi, MEDULA kayıtları delil olur. İspat: SGK kesinti sebebini; eczacı reçetenin usulüne uygunluğunu (hekim onayı, ICD, doz) gösterir.
4. **Cezai şart.** Protokoldeki cezai şartın TBK m.182 vd. çerçevesinde fahiş olup olmadığı, tenkis imkânı (sözleşmesel ilişki kabul edilirse) değerlendirilir.
5. **Fesih/sözleşme dışı bırakma.** Süreli/süresiz fesih sebebi, ölçülülük ve eczacının savunma hakkı; iptal/menfi tespit veya alacak davası seçimi ilişkinin niteliğine göre yapılır.

## Çıktı modülleri
- İtiraz kademesi ve görevli yargı yolu notu.
- Kesinti kalemi bazında itiraz/dava cetveli.
- İtiraz dilekçesi veya dava dilekçesi iskeleti [doldurulacak].



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

