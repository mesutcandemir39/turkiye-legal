---
argument-hint: ''
description: Bir karardan veya doktrinden alıntı yapılırken; tam olarak hangi paragraf,
  sayfa veya gerekçeye dayanıldığını göstermek ve cımbızlama/çarpıtma olmadan alıntılamak
  gerektiğinde kullanılır.
name: pinpoint-ve-dogru-alinti
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Pinpoint Atıf ve Doğru Alıntı

## Görev
Bir kaynağa atıf yaparken dayanılan tam yeri (karar paragrafı, doktrin sayfası) göstermek ve alıntıyı bağlamından kopararak çarpıtmamak.

## Soğuk başlangıç (intake)
- Kaynak içinde hangi tam yere dayanılıyor (sayfa, paragraf, gerekçe bölümü)?
- Alıntı bağlayıcı gerekçeye mi (ratio) yoksa geçer söze mi (obiter) dayanıyor?
- Tam metin elimizde mi, yoksa özet üzerinden mi atıf yapılıyor?
- Lehe görünen ifade, kararın bütününde gerçekten lehe mi?

## Denetim şeması
1. **Pinpoint zorunluluğu** — "Genel olarak şu karar" yetmez; doktrinde sayfa (s. …), kararda ilgili paragraf/gerekçe işaret edilir. AYM/AİHM kararlarında paragraf numarası (§ …) kullanılır.
2. **Ratio / obiter ayrımı** — Kararın bağlayıcı/taşıyıcı gerekçesi (ratio decidendi) ile yan/geçer sözü (obiter dictum) ayrılır; atıf gücü ratioya bağlanır, obiter "ek olarak" diye sunulur.
3. **Bağlamı koruma** — Cümle, paragrafın ve kararın bütünündeki anlamıyla aktarılır; şart cümlesinden koşul atılarak, istisnadan istisna kaldırılarak alıntı yapılmaz (cımbızlama yasağı).
4. **Doğrudan/dolaylı alıntı** — Doğrudan alıntı tırnak içinde aynen verilir; özetleyen dolaylı alıntı "kararın özüne göre…" diye işaretlenir, kelimesi kelimesine gibi gösterilmez.
5. **Karşı içtihat dürüstlüğü** — Aleyhe yerleşik içtihat veya karşı oy varsa gizlenmez; en azından "karşı yönde …" diye anılır.
6. **Özet üzerinden atıf riski** — Üçüncü el özetler hatalı olabilir; tam metne inilemeyen yerde alıntı "tam metin doğrulanacak" notuyla bırakılır.

## Çıktı modülleri
- Pinpoint atıf (sayfa/§/paragraf ile).
- Ratio/obiter işareti.
- Bağlam notu (alıntının çevresi).
- Karşı içtihat/karşı oy uyarısı + `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

