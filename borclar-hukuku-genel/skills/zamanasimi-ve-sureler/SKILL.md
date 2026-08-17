---
argument-hint: ''
description: Bir alacağın zamanaşımına uğrayıp uğramadığı, sürenin başlangıcı, kesilmesi-durması
  ve def'i olarak ileri sürülmesi söz konusu olduğunda kullanılır.
name: zamanasimi-ve-sureler
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Zamanaşımı ve Süreler

## Görev
Alacağa uygulanacak zamanaşımı süresini, başlangıcını, kesilme/durma hâllerini saptamak ve def'i olarak doğru zamanda ileri sürülmesini sağlamak.

## Soğuk başlangıç (intake)
- Alacağın türü ne (genel sözleşme alacağı, dönemsel edim, özel kanun alacağı)?
- Alacak ne zaman muaccel oldu (sürenin başlangıcı)?
- Arada dava, icra takibi, ikrar veya başka kesen işlem oldu mu?
- Tarafların biri tacir/şirket mi; özel süre öngören kanun var mı?

## Denetim şeması
1. Genel süre: TBK m.146 — kanunda aksi öngörülmedikçe her alacak 10 yıllık zamanaşımına tabidir.
2. Beş yıllık süre: m.147 — kira bedelleri, anapara faizleri, dönemsel edimler; vekâlet/komisyon/eser sözleşmesinden doğan bazı alacaklar; serbest meslek ve esnaf alacakları. Liste dikkatle uygulanmalı.
3. Başlangıç: m.149 — alacağın muaccel olduğu an. Kesin vade yoksa muacceliyet için ihtar gerekebilir.
4. Kesilme: m.154 — borçlunun ikrarı (taksit, faiz ödeme, rehin/kefil verme), dava/def'i, icra takibi, iflas masasına başvuru; kesilmeyle yeni süre işlemeye başlar (m.156).
5. Durma: m.153 — belirli kişisel ilişkiler ve hukuki engeller süresince durur; engel kalkınca kaldığı yerden işler.
6. Sonuç ve usul: m.161 — zamanaşımından önceden feragat edilemez; hâkim resen dikkate alamaz, mutlaka def'i olarak ileri sürülmelidir (HMK çerçevesinde cevap dilekçesi/ilk fırsatta). Zamanaşımına uğramış borç eksik borçtur; ifa edilirse geri istenemez.
7. İspat yükü: Süreyi ve başlangıcı zamanaşımını ileri süren; kesilme/durmayı buna dayanan taraf ispatlar.

## Çıktı modülleri
- Süre hesap tablosu (başlangıç, kesilme, kalan süre).
- Zamanaşımı def'i metni taslağı (usule uygun aşama uyarısıyla).
- Karşı tarafça kesilme iddiasına savunma notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

