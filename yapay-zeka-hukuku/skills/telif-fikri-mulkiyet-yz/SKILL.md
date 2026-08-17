---
argument-hint: ''
description: Üretken yapay zekânın eğitiminde eser kullanımı, ürettiği içeriğin eser/tasarım/marka
  sahipliği, telif ihlali iddiası veya açık kaynak lisans uyumu gündeme geldiğinde
  FSEK ve SMK çerçevesinde değerlen
name: telif-fikri-mulkiyet-yz
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yapay Zekâ ve Fikri Mülkiyet

## Görev
Yapay zekâ ile eser/içerik ilişkisini iki yönden çözmek: girdi tarafında eğitim verisi olarak eser kullanımının telif boyutu; çıktı tarafında üretilen içeriğin hak sahipliği ve ihlal değerlendirmesi.

## Soğuk başlangıç (intake)
1. Sorun girdi tarafında mı (eğitim verisinde eser kullanımı) yoksa çıktı tarafında mı (üretilen içerik)?
2. Üretilen çıktı esere benzer mi; somut bir eserin kopyası/işlemesi iddiası var mı?
3. Modelin lisansı/açık kaynak bileşenleri ve kullanım koşulları neler?
4. Müvekkil hak sahibi mi, kullanıcı mı, geliştirici mi?

## Denetim şeması
1. **Çıktıda eser sahipliği**: FSEK m.1/B ve m.8 — eser, sahibinin hususiyetini taşıyan fikrî üründür ve sahibi gerçek kişidir. Tamamen otomatik üretilen çıktı, insan hususiyeti yoksa "eser" sayılmayabilir; insanın yaratıcı katkısı oranında koruma tartışılır. Ara sonuç: çıktı korunan eser mi.
2. **Eğitim verisinde kullanım**: Korunan eserlerin izinsiz model eğitiminde çoğaltılması (m.22) ve işlenmesi (m.21) mali hakları ilgilendirir; FSEK istisnaları (m.30 vd.) dar yorumlanır, genel "metin-veri madenciliği" istisnası Türk hukukunda açıkça düzenlenmemiştir.
3. **İhlal değerlendirmesi**: Çıktı somut bir eserin kopyası/işlemesi ise tecavüz; benzerlik ve esinlenme ayrımı yapılır. Tecavüzde ref/men (FSEK m.66-67) ve tazminat (m.68 — üç kata kadar) gündeme gelir.
4. **Marka/tasarım/buluş**: SMK kapsamında YZ üretimi tasarım/markada gerçek hak sahipliği; buluşta mucit gerçek kişi olmalıdır.
5. **Lisans uyumu**: Açık kaynak ve veri seti lisans şartlarına uyum sözleşmesel ve telifsel olarak ayrı denetlenir.

FSHM uygulaması için karararama.yargitay.gov.tr; AB ve ABD'deki davalar yalnız karşılaştırmalı kaynaktır, künye [DOĞRULANMADI].

## Çıktı modülleri
- Girdi/çıktı telif risk haritası.
- Eser/koruma değerlendirme notu.
- İhlal iddiasına karşı savunma veya hak talebi taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

