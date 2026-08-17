---
argument-hint: ''
description: Edinilmiş mallara katılma rejiminin tasfiyesi, katılma alacağı ve değer
  artış payı hesabı, mal gruplarının ayrıştırılması ve sözleşmesel rejimlerin sonuçları
  gerektiğinde kullanılır; boşanmadan ayrı b
name: mal-rejimi-tasfiyesi
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
    numara: '4721'
    tur: kanun
  - ad: Ailenin Korunması ve Kadına Karşı Şiddetin Önlenmesine Dair Kanun
    numara: '6284'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Mal Rejimi Tasfiyesi ve Katılma Alacağı

## Görev
Sona eren mal rejimini tasfiye etmek; mal gruplarını ayırmak, katılma alacağı (TMK m.231, m.236) ve değer artış payını (m.227) hesaplamak, aile konutu ve tasfiyenin usulünü belirlemek.

## Soğuk başlangıç (intake)
1. Evlenme tarihi ve mal rejimi türü nedir (yasal/sözleşmesel)?
2. Rejim hangi tarihte ve nasıl sona erdi (dava tarihi, ölüm, sözleşme)?
3. Hangi mallar var: taşınmaz, araç, banka hesabı, şirket payı, SGK/birikim?
4. Mal alımları kişisel mi (miras/bağış) yoksa edinilmiş gelirle mi finanse edildi?

## Denetim şeması
1. **Rejim ve sona erme tarihi.** Yasal rejim edinilmiş mallara katılmadır (m.202). Tasfiyede mal varlıkları rejimin **sona erdiği andaki** durumlarına göre, değerleri ise **tasfiye/karar anına** göre belirlenir (m.225, m.227, m.235). Sona erme tarihi genellikle boşanma dava tarihidir (m.225/2).
2. **Mal gruplarının ayrılması.** Her eşin kişisel malları (m.220: miras/bağış yoluyla gelenler, manevi tazminat, kişisel kullanım eşyası) ile edinilmiş malları (m.219: çalışma karşılığı edinimler, sosyal güvenlik edimleri, kişisel malların gelirleri) ayrıştırılır. İspatlanamayan mal edinilmiş sayılır (m.222).
3. **Hesap kalemleri.** Eklenecek değerler (karşılıksız kazandırmalar, mal kaçırma — m.229), denkleştirme (m.230), değer artış payı (m.227: bir eşin diğerinin malına katkısı), artık değer ve **katılma alacağı = artık değerin yarısı** (m.231, m.236). Katılma alacağında zamanaşımı ve faiz başlangıcı (m.239) gözetilir.
4. **Aile konutu ve tasarruf.** Aile konutu şerhi ve eşin rızası (m.194); konutun/ev eşyasının sağ kalan veya hak sahibi eşe özgülenmesi (m.240, m.279).
5. **Ara sonuç.** Bilanço (kişisel/edinilmiş ayrımı) + katılma alacağı tutarı + dava türü (alacak/aynileştirme) raporlanır. Tasfiye boşanmadan **ayrı dava** olup boşanma kesinleşmeden hüküm kurulamaz (talep edilse de bekletici mesele).

## Çıktı modülleri
- Mal envanteri ve kişisel/edinilmiş tasnif tablosu.
- Katılma alacağı / değer artış payı hesap çizelgesi.
- Tasfiye dava dilekçesi için talep sonucu ve delil (tapu, banka, SGK kaydı) listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

