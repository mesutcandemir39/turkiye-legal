---
argument-hint: ''
description: İkamet/çalışma/vatandaşlık başvuru dilekçesi, idari itiraz veya iptal
  dava dilekçesi hazırlanacağında; yer tutucu disiplini ve doğru madde atıflarıyla
  taslak üretmek için kullanılır.
name: dilekce-basvuru-taslagi
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
  - ad: Yabancılar ve Uluslararası Koruma Kanunu
    numara: '6458'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dilekçe ve Başvuru Taslağı

## Görev
Göç ve yabancılar alanında idari başvuru, idari itiraz ve idari dava dilekçelerini doğru biçim, madde atfı ve yer tutucu disipliniyle üretmek; her belgenin makamına ve süresine uygun olmasını sağlamak.

## Soğuk başlangıç (intake)
1. Hangi belge hazırlanacak (başvuru, uzatma, itiraz, iptal davası dilekçesi)?
2. Muhatap makam kim (Göç İdaresi il müdürlüğü, Bakanlık, Komisyon, idare mahkemesi)?
3. Eldeki belgeler ve dayanılacak vakıalar nelerdir?
4. Süre durumu nedir (son gün)?

## Denetim şeması
1. **Belge-makam eşleşmesi**: Başvuru/uzatma → Göç İdaresi/Bakanlık; ret kararına itiraz → öngörülmüşse ilgili komisyon; iptal davası → idare mahkemesi (İYUK m.3'teki dilekçe unsurları); idari gözetim itirazı → sulh ceza hâkimliği.
2. **İdari dava dilekçesi unsurları**: İYUK m.3 — tarafların kimliği, dava konusu işlem ve tebliğ tarihi, açıklama (vakıalar), hukuki sebepler, deliller, sonuç-talep ve YD talebi. Sınır dışı/gözetimde aciliyet vurgusu.
3. **Madde atıf disiplini**: Talep YUKK/6735/5901'in ilgili maddesine; geri gönderme yasağı için m.4/m.55 ve AİHS m.3'e; usul için İYUK m.2/7/27'ye bağlanır.
4. **Yer tutucu disiplini**: Bilinmeyen tarih, sayı, ad ve tutar `[doldurulacak]` ile işaretlenir; uydurma karar/işlem numarası yazılmaz. İçtihat ihtiyacı varsa ilkesel atıf + `[DOĞRULANMADI]`.
**Ara sonuç**: Eksiksiz, makamına ve süresine uygun, doğrulanabilir kaynaklı bir taslak.

## Çıktı modülleri
- Hedef belgenin tam taslağı (başlık, taraf, vakıa, hukuki sebep, talep).
- Ek belge/delil listesi ve sunulacak suret sayısı notu.
- İmza-tebliğ-harç ve son gün hatırlatması.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

