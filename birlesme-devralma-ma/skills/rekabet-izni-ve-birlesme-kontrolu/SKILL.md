---
argument-hint: ''
description: Bir devralma işleminin 4054 sayılı Kanun m.7 kapsamında Rekabet Kurulu
  iznine tabi olup olmadığını ciro eşiklerine göre değerlendirmek, bildirim hazırlamak
  ve gun-jumping riskini yönetmek için kullanı
name: rekabet-izni-ve-birlesme-kontrolu
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  - ad: Rekabetin Korunması Hakkında Kanun
    numara: '4054'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Rekabet İzni ve Birleşme Kontrolü

## Görev
İşlemin 4054 sayılı Kanun m.7 ve 2010/4 sayılı Tebliğ uyarınca bildirime/izne tabi olup olmadığını saptamak, bildirimi kurgulamak ve izin alınmadan kapanış (gun-jumping) riskini bertaraf etmek.

## Soğuk başlangıç (intake)
- Tarafların Türkiye ve dünya ciroları nedir (son mali yıl)?
- İşlem kontrol değişikliği yaratıyor mu (tek/ortak kontrol)?
- Taraflar aynı pazarda yatay/dikey örtüşüyor mu?
- Kapanış için izin kapanış şartı (CP) olarak kurgulandı mı?

## Denetim şeması
1. **Kontrol testi**: 4054 m.7 — bir teşebbüsün kontrolünde kalıcı değişiklik yaratan devralma/birleşme. Azınlık pay alımı tek başına kontrol vermiyorsa kural olarak bildirime tabi değildir.
2. **Eşik testi**: 2010/4 sayılı Tebliğ m.7'deki ciro eşikleri aşılıyorsa bildirim **zorunludur**. Eşikler periyodik güncellendiği için yürürlükteki güncel tutarlar rekabet.gov.tr'den teyit edilir `[DOĞRULANMADI]`.
3. **Teknoloji teşebbüsü istisnası**: Tebliğde teknoloji teşebbüslerinin devralınmasında yerel eşik aranmaması düzenlemesi gözetilir (güncel metinden teyit).
4. **Bildirim ve askı**: İzin alınmadan işlem hukuken **geçerlilik kazanmaz** (m.7) ve gun-jumping idari para cezası (4054 m.16) doğurur. Kapanış izne bağlanır.
5. **Esasa ilişkin değerlendirme**: Etkilenen pazarlarda hâkim durum yaratma/güçlendirme analizi; gerekirse taahhüt (remedy) önerisi.
6. **İspat/dayanak**: Ciro hesabı bağlı teşebbüsler dahil yapılır; bildirim formu belgeyle desteklenir.
7. **Ara sonuç**: Bildirim gerekli/gereksiz kararı ve izin takvimi (yaklaşık süre) belirlenir.

## Çıktı modülleri
- Bildirim gerekliliği değerlendirme notu (eşik hesabı)
- Rekabet Kurulu bildirim formu taslağı kontrol listesi
- Gun-jumping risk uyarısı ve closing condition lafzı
- İzin takvimi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

