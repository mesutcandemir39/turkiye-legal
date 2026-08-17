---
argument-hint: ''
description: Bir hukuki görüşü yargı kararlarıyla desteklemek ya da güncel içtihat
  eğilimini saptamak gerektiğinde; karara ulaşma, bağlayıcılık derecesini tartma ve
  emsal olarak kullanma için kullanılır.
name: ictihat-arama-ve-degerlendirme
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
  - ad: Türk Medeni Kanunu
    madde: '1'
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İçtihat Arama ve Değerlendirme

## Görev
Bir hukuki sorunun yargı kararlarıyla nasıl çözüldüğünü doğrulanabilir kaynaklardan tespit etmek, kararın bağlayıcılık/ikna değerini tartmak ve emsal olarak güvenli biçimde kullanmak.

## Soğuk başlangıç (intake)
- Aranan ilke nedir; hangi kanun maddesi etrafında dönüyor?
- Hangi yargı kolu (Yargıtay/Danıştay/AYM/BAM-BİM) ve hangi daire ilgili?
- Lehe mi, aleyhe mi karar arıyoruz; karşı içtihat var mı?
- Karar güncel mi; sonradan değişen mevzuat/içtihat var mı?

## Denetim şeması
1. **Kaynaktan arama** — Resmî bankalar: karararama.yargitay.gov.tr, karararama.danistay.gov.tr, kararlarbilgibankasi.anayasa.gov.tr. Karar metni görülmeden künye yazılmaz; **karar numarası asla model hafızasından uydurulmaz.**
2. **Bağlayıcılık derecesi** — (a) İçtihadı Birleştirme Kararları: benzer konularda mahkemeleri bağlar, en yüksek değerdedir. (b) AYM kararları (norm denetimi ve bireysel başvuru): bağlayıcı (Anayasa m.153). (c) Daire/Genel Kurul kararları: emsal/ikna edici, kural olarak bağlamaz ama yerleşik içtihat ağırlık taşır. (d) BAM/BİM kararları: bölgesel emsal değeri.
3. **Karar okuma** — Olay örgüsünü (vakıa) eldeki olayla karşılaştır; benzemiyorsa karar emsal olmaz. *Ratio decidendi* (bağlayıcı gerekçe) ile *obiter dictum* (geçer söz) ayrılır. Karşı oy ayrıca not edilir.
4. **Güncellik denetimi** — Karardan sonra kanun değişti mi, içtihat birleştirme/değişikliği oldu mu, AYM iptal etti mi? Eski içtihat güncel mevzuata sözcü kılınmaz.
5. **Çelişkili içtihat** — Daireler arası çelişki varsa hiyerarşi (HGK, İBK) ve tarih gözetilir; eğilim tek cümlede dürüstçe özetlenir, lehe karar seçilip aleyhe karar gizlenmez.

## Çıktı modülleri
- Aranan ilke + arama sorgusu (banka adıyla).
- Karar künyesi şablonu: Mahkeme/Daire, E. .../..., K. .../..., T. gg.aa.yyyy `[DOĞRULANMADI]`.
- Bağlayıcılık ve güncellik notu.
- Olay benzerliği ve ratio/obiter ayrımı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

