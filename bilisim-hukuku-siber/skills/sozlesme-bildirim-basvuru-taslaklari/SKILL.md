---
argument-hint: ''
description: Veri işleyen sözleşmesi, gizlilik/güvenlik eki, ihlal bildirimi, içerik
  kaldırma başvurusu, suç duyurusu gibi bilişim hukukuna özgü metinlerin taslağını
  üretmek gerektiğinde kullanılır.
name: sozlesme-bildirim-basvuru-taslaklari
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Elektronik Ticaretin Düzenlenmesine Dair Kanun
    numara: '5651'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Sözleşme, Bildirim ve Başvuru Taslakları

## Görev
Bilişim/siber alanına özgü hukuki metinleri (sözleşme ekleri, bildirimler, başvurular, dilekçeler) doğru hukuki çerçeveyle ve yer tutucu disiplinine uygun taslamak.

## Soğuk başlangıç (intake)
1. Hangi belge? (veri işleyen sözleşmesi/eki, ihlal bildirimi, içerik kaldırma, suç duyurusu, ihtar?)
2. Taraflar ve sıfatları kim? (veri sorumlusu/işleyen, mağdur, sağlayıcı?)
3. Hangi olgular sabit, hangileri eksik?
4. Muhatap mercі ve dil resmiyeti ne düzeyde olmalı?

## Denetim şeması
1. **Belge tipi ve dayanağı.** Her metin dayanağına bağlanır: veri işleyen sözleşmesi (KVKK m.12 müşterek sorumluluk, aktarım şartları), ihlal bildirimi (KVKK m.12/5 ve Kurul formu), içerik kaldırma (5651 m.9/m.9/A), suç duyurusu (TCK m.243-245; CMK soruşturma), ihtar/tazminat talebi (TBK m.49/m.112).
2. **Zorunlu unsurlar.** Dilekçelerde taraf/mercі, olay özeti, hukuki sebep ve talep sonucu net ayrılır (HMK m.119 mantığı esas alınır). İhlal bildiriminde ihlalin niteliği, etkilenen veri/kişi, olası sonuçlar ve alınan tedbirler yer alır. Sözleşmede güvenlik taahhütleri, denetim, alt işleyen, ihlal bildirim yükümlülüğü ve sorumluluk dağılımı düzenlenir.
3. **Risk ve emredici hüküm süzgeci.** Sorumluluğu tümüyle kaldıran kayıtların TBK m.115 (ağır kusur/kasıtta geçersizlik) ve tüketici/emredici hükümler karşısında geçerliliği denetlenir; KVKK yükümlülükleri sözleşmeyle bertaraf edilemez.
4. **Yer tutucu disiplini.** Doğrulanmamış olgular `[doldurulacak]`, doğrulanmamış içtihat künyesi `[DOĞRULANMADI]` olarak bırakılır; uydurma veri/numara yazılmaz.
5. **Ara sonuç.** Belgenin iskeleti, eksik bilgi listesi ve risk uyarıları birlikte sunulur.

## Çıktı modülleri
- Talep edilen belgenin tam taslağı (başlık, gövde, talep/sonuç).
- Eksik bilgi/olgu listesi ([doldurulacak] dökümü).
- Risk ve müzakere notu (geçerlilik, emredici hüküm uyarıları).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

