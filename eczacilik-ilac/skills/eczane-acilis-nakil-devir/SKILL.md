---
argument-hint: ''
description: Eczane açma, nakil, devir, mesul müdür ve ikinci eczacı işlemlerinde
  6197 sayılı Kanun ve Yönetmelik şartlarını, sayı sınırlaması ve muvazaa riskini
  denetlemek gerektiğinde kullanılır.
name: eczane-acilis-nakil-devir
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


# Eczane Açılışı, Nakli ve Devri

## Görev
Eczane açma, nakil ve devir başvurularında 6197 sayılı Kanun ve Eczaneler Yönetmeliği şartlarını adım adım denetlemek, ruhsat reddi/iptaline veya muvazaa iddiasına karşı savunma kurmak.

## Soğuk başlangıç (intake)
- İşlem türü: yeni açılış, nakil, devir, mesul müdür/ikinci eczacı atanması mı?
- Eczacının diploma, kayıt ve varsa mecburi hizmet durumu nedir?
- Yerleşim yeri nüfusu ve mevcut eczane sayısı; nüfusa göre kontenjan uygun mu?
- Devir varsa: devreden vefat/emeklilik mi, bedel ve cari nasıl belirlendi, muvazaa şüphesi var mı?

## Denetim şeması
1. **Eczacı şartları.** 6197 m.2-4: Türk vatandaşlığı, eczacılık diploması, mesleği yapmaya engel hâl bulunmaması. Ara sonuç: kişi ehliyeti tamam mı?
2. **Açılış ve kontenjan.** 6197 m.5 ve Yönetmelik: nüfusa göre eczane sayısı sınırlaması, mevcut eczanelere mesafe, bölge eczacı odası ve il sağlık müdürlüğü süreci. İl sağlık müdürlüğünün ruhsat işlemi idari işlemdir; reddi İYUK m.7 ile 60 günde idari yargıya taşınır.
3. **Nakil.** Yönetmelikteki nakil şartları (taşınılacak yerin kontenjana uygunluğu, asgari donanım). Sebep unsuru eksikse iptal sebebi doğar.
4. **Devir ve muvazaa.** Eczanenin gerçekte eczacı dışı kişi/sermaye tarafından işletilmesi muvazaadır; 6197 ve Yönetmelik muvazaayı yasaklar, tespitinde ruhsat iptali gündeme gelir. İspat: işletme defterleri, banka hareketleri, kira ve cari kayıtları. Devir bedeli ve alacak uyuşmazlığı ise adli yargıda (TBK genel hükümler).
5. **Mesul müdür/ikinci eczacı.** Belirli ciro/nüfus eşiklerinde ikinci eczacı veya yardımcı eczacı zorunluluğu; mesul müdürün sorumluluk kapsamı.

## Çıktı modülleri
- Başvuru/dava uygunluk kontrol listesi (eksik belge dahil).
- Ruhsat reddi/iptaline karşı iptal dilekçesi iskeleti [doldurulacak].
- Muvazaa savunması veya tespiti için delil planı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

