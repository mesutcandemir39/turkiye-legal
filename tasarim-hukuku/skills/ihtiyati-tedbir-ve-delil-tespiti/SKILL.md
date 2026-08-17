---
argument-hint: ''
description: Tasarım uyuşmazlıklarında tecavüzün durdurulması/önlenmesi için ihtiyati
  tedbir ve delillerin kaybolmadan tespiti taleplerinin hazırlanması; hızlı müdahale,
  fuar baskını veya ürünün piyasadan çekilmes
name: ihtiyati-tedbir-ve-delil-tespiti
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İhtiyati Tedbir ve Delil Tespiti

## Görev
Esas dava açılmadan veya dava sürerken hakkı korumak: tecavüz fiilini durduran/önleyen ihtiyati tedbir ile, kaybolması/değişmesi muhtemel delillerin tespitini sağlamak. Fuar, ihale, sezon ürünü gibi zaman-kritik durumlarda belirleyicidir.

## Soğuk başlangıç (intake)
1. Acil tehlike ne (fuarda sergileme, toplu satış, ihaleye teklif, ürünün tükenmesi)?
2. Korunan hakkın geçerliliği ve sicil durumu güçlü mü (tedbirde yaklaşık ispat gerekir)?
3. Hangi delil kaybolabilir (numune, üretim kayıtları, stok, dijital kayıt)?
4. Karşı tarafın adresi/ürünü tespit edilebilir mi (keşif/bilirkişi için)?

## Denetim şeması
1. İhtiyati tedbir dayanağı (SMK m.159, HMK m.389 vd.): Tasarım sahibi, tecavüz veya yakın tehlike hâlinde üretimin/satışın durdurulması, ürünlere el konulması, teminat gibi tedbirler isteyebilir. Yaklaşık ispat (HMK m.390/3) yeterlidir; hakkın varlığı ve tecavüz/tehlike yaklaşık olarak gösterilir.
2. Teminat (HMK m.392): Tedbir kural olarak teminata bağlanır; haksız tedbir tazminat sorumluluğu doğurur (HMK m.399). Teminat tutarı ve istisnaları değerlendirin.
3. Tedbirin kapsamı: Üretim/satış/ithalat yasağı, gümrükte durdurma (SMK m.159 ve gümrük mevzuatı), ürünlere/araçlara el koyma, fuarda standdan çekme. Orantılılığı gerekçelendirin.
4. Esas dava süresi (HMK m.397/1): Dava açılmadan alınan tedbirde, tedbir kararının uygulanmasından itibaren 2 hafta içinde esas dava açılmalı; aksi hâlde tedbir kendiliğinden kalkar.
5. Delil tespiti (HMK m.400 vd.): Numune alma, üretim/stok/defter incelemesi, bilirkişiyle keşif; ileride elde edilmesi zorlaşacak deliller için ayrı veya tedbirle birlikte talep edilir.
6. Görev/yetki: FSHHM; tedbir esas davaya bakacak veya en yakın/uygun mahkemeden istenir (HMK m.390/1).

## Çıktı modülleri
- İhtiyati tedbir dilekçesi iskeleti (yaklaşık ispat, talep, teminat görüşü).
- Delil tespiti talebi ve tespit edilecek delil listesi.
- 2 haftalık esas dava süresi takvimi ve haksız tedbir riski notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

