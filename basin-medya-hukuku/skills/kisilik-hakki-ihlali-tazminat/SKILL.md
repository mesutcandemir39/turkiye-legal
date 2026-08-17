---
argument-hint: ''
description: Basın veya yayın yoluyla şeref, itibar veya özel hayatın ihlali nedeniyle
  tespit, durdurma (men) ve maddi-manevi tazminat taleplerini kurgulamak gerektiğinde
  kullanılır.
name: kisilik-hakki-ihlali-tazminat
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
  - ad: Basın Meslek İlkeleri ve Yapı İtibarı Hakkında Kanun
    numara: '5187'
    tur: kanun
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Basın Yoluyla Kişilik Hakkı İhlali ve Tazminat

## Görev
Yayından kaynaklanan kişilik hakkı saldırısında TMK m.24-25 davalarını ve TBK m.49/m.58 tazminat taleplerini unsurlarıyla kurmak, husumet ve hesabı belirlemek.

## Soğuk başlangıç (intake)
1. İhlal eden ifade tam olarak nedir, kim hakkındadır?
2. Yayın organı, sorumlu müdür, yazar/muhabir kim?
3. Somut zarar (manevi elem, ticari itibar kaybı, maddi kayıp) nedir?
4. İhlal devam ediyor mu (online erişilebilirlik)?

## Denetim şeması
1. **Saldırı ve hukuka aykırılık**: TMK m.24/I uyarınca kişiliğe saldırı; m.24/II'deki hukuka uygunluk sebepleri (üstün yarar, rıza, kanuni yetki) yoksa hukuka aykırılık sabittir.
2. **Davalar (TMK m.25)**: Tespit davası (devam eden/etkisi süren saldırı), durdurma/men davası (sürmekte olan saldırı), önleme davası (yakın tehlike). Düzeltme veya kararın ilanı da istenebilir.
3. **Tazminat**: Manevi tazminat TBK m.58; maddi tazminat TBK m.49-52 (kusur, hukuka aykırı fiil, zarar, illiyet). Tüzel kişi için ticari itibar zararı maddi tazminata konu olabilir.
4. **Husumet**: 5187 sayılı Kanun m.11 sorumluluk silsilesini düzenler; eser sahibi, sorumlu müdür ve yayın sahibi birlikte değerlendirilir. Tazminatta yayın sahibi ve ilgili kişiler müteselsil sorumlu olabilir.
5. **İspat yükü**: Saldırı ve zararı davacı, hukuka uygunluk sebebini davalı ispatlar (TMK m.6).
6. **Ara sonuç**: İhlal + hukuka uygunluk sebebinin yokluğu + zarar/illiyet varsa talep kabule değer.

## Çıktı modülleri
- Talep matrisi (tespit/men/önleme/tazminat)
- Husumet tablosu (yazar, sorumlu müdür, yayın sahibi)
- Manevi tazminat takdir gerekçesi taslağı (sınıf/derece, müdahale ağırlığı)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

