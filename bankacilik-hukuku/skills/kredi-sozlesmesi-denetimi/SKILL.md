---
argument-hint: ''
description: Genel kredi sözleşmesi, tüketici/konut kredisi veya ticari kredi metnini
  emredici hükümler, genel işlem koşulu ve haksız şart açısından madde madde denetlemek,
  geçersiz/yazılmamış sayılan kayıtları te
name: kredi-sozlesmesi-denetimi
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
  - ad: Bankacılık Kanunu
    numara: '5411'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kredi Sözleşmesi ve Genel Kredi Sözleşmesi Denetimi

## Görev
Bir kredi sözleşmesini (genel kredi sözleşmesi, tüketici kredisi, konut finansmanı veya ticari kredi) emredici hukuk, genel işlem koşulu denetimi ve haksız şart süzgecinden geçirerek geçerli, sakat ve yazılmamış sayılacak kayıtları ayırmak; risk ve müzakere noktalarını çıkarmak.

## Soğuk başlangıç (intake)
- Kredi türü: nakdi/gayrinakdi, rotatif genel kredi, taksitli tüketici kredisi, konut finansmanı, ticari işletme kredisi?
- Müşteri tüketici mi, tacir mi? Sözleşme matbu/standart mı, müzakere edilmiş mi?
- Faiz tipi: sabit/değişken; akdi ve temerrüt faizi oranları ne, bileşik faiz var mı?
- Talep edilen masraf/komisyon/sigorta kalemleri neler; teminat yapısı (kefalet/ipotek/rehin) nasıl?

## Denetim şeması
1. **Standart koşul tespiti**: Sözleşme tek tarafça hazırlanıp dayatılmışsa genel işlem koşulu denetimine tabidir (TBK m.20-25). Diğer tarafın menfaatine aykırı, beklenmeyen, dürüstlüğe aykırı kayıtlar yazılmamış sayılır (TBK m.21-22); değiştirme yasağı (TBK m.24) ve aleyhe yorum (TBK m.23) uygulanır.
2. **Tüketici ise haksız şart denetimi**: TKHK m.5 ve Haksız Şartlar Yönetmeliği uyarınca dürüstlüğe aykırı, dengesizlik yaratan şartlar kesin hükümsüzdür. TKHK m.22-31 emredici hükümleri (sözleşmenin yazılı şekli, ön bilgilendirme, cayma hakkı 14 gün, erken ödeme indirimi) karşılanmış mı?
3. **Faiz ve eklentiler**: Akdi faiz oranı, temerrüt faizi (TBK m.120 — sözleşmede kararlaştırılmamışsa kanuni temerrüt faizi), bileşik faiz yasağı ve TTK m.8-9 istisnaları kontrol edilir. Tüketici kredisinde değişken faizde tavan/referans şartları (TKHK m.25) aranır. Haksız komisyon/masraf kalemleri iadeye tabidir.
4. **Teminat zinciri**: Kefalet varsa TBK m.583 (yazılı şekil, azami miktar-tarih el yazısı şartı) ve m.584 (eşin rızası) sağlanmış mı; sağlanmamışsa kefalet geçersizdir. İpotek/rehinde tesis usulü ayrıca denetlenir.
5. **Muacceliyet ve fesih kayıtları**: Tek taksit temerrüdüyle tüm borcun muaccel olması koşulu tüketici kredisinde TKHK m.27 sınırlamasına (en az iki taksit, 30 gün önel) tabidir. Ara sonuç olarak her kayıt için geçerli/sakat/yazılmamış nitelendirmesi yap.

## Çıktı modülleri
- Madde madde risk tablosu (geçerli / yazılmamış sayılır / hükümsüz / müzakere).
- Önerilen redline ve alternatif lafızlar.
- İade/itiraz konusu faiz-masraf kalemleri listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

