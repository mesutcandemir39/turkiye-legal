---
argument-hint: ''
description: Karşılıksızdır işlemi yapılan çekte adli para cezası ve çek düzenleme/hesap
  açma yasağı (5941 s. Çek Kanunu m.5), şikâyet süresi ve etkin pişmanlıkla yaptırımın
  kaldırılması söz konusu olduğunda kulla
name: karsiliksiz-cek-kambiyo
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


# Karşılıksız Çek ve Kambiyo Suçları

## Görev
5941 sayılı Çek Kanunu m.5 çerçevesinde karşılıksız çek yaptırımını (adli para cezası ve çek düzenleme yasağı) denetlemek; şikâyet, süre ve etkin ödemeyle düşme imkânını değerlendirmek.

## Soğuk başlangıç (intake)
- Çekin üzerinde "karşılıksızdır" işlemi yapıldı mı, tarihi ne?
- Çek hesabı sahibi kim, çeki düzenleyen/temsilci kim?
- Hamil kim, şikâyet süresi (suçun/işlemin öğrenilmesinden itibaren) işliyor mu?
- Çek bedeli + faiz ödenip yaptırımın kaldırılması (m.5/10) gündemde mi?

## Denetim şeması
1. **Yaptırımın niteliği**: 5941 s. Kanun m.5 — üzerinde karşılıksızdır işlemi yapılmış çekin hamili şikâyette bulunursa, çek bedeli kadar adli para cezası ve çek düzenleme/çek hesabı açma yasağı uygulanır. Bu, şikâyete bağlı bir yaptırımdır.
2. **Fail-sorumlu tespiti**: Çek hesabı tüzel kişiye aitse, çeki düzenleyen yetkili gerçek kişi sorumlu olur (temsil ilişkisi ve imza yetkisi kontrol edilir).
3. **Şikâyet ve süre**: Yaptırım şikâyete bağlıdır; şikâyet süresi ve usulü kontrol edilir. Yetkili mahkeme (icra ceza/asliye ceza) ve görev belirlenir.
4. **Etkin ödeme — yaptırımın kaldırılması (m.5/10)**: Çek bedelinin işleyen faiziyle birlikte ödenmesi halinde, soruşturma/kovuşturma/infaz aşamasına göre yaptırım kaldırılır veya çek düzenleme yasağı kalkar; aşama ve ödeme zamanı belirleyicidir.
5. **Hukuk-ceza paralelliği**: Çek aynı zamanda kambiyo senedidir; İİK kapsamında kambiyo takibi (icra) paralel yürür. Ceza yaptırımı ile alacağın icra takibini ayrı yönet.
6. **Ara sonuç**: Karşılıksızdır işleminin geçerliliği, sorumlu sıfatı, şikâyet süresi ve ödeme ile düşme imkânı netleşir.

## Çıktı modülleri
- Karşılıksızdır işlemi/şikâyet süresi kontrolü
- Sorumlu (düzenleyen/temsilci) tespiti
- Etkin ödeme ile yaptırımı kaldırma senaryosu
- İcra (kambiyo takibi) ile koordinasyon notu
- Şikâyet veya savunma dilekçesi taslağı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

