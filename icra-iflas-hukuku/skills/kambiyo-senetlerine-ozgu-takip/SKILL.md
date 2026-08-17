---
argument-hint: ''
description: Çek, bono veya poliçeye dayalı haciz/iflas yoluyla takip kurmak, ödeme
  emrine 5 gün içinde itiraz veya şikâyet etmek ve kambiyo vasfı denetimini yapmak
  gerektiğinde kullanılır.
name: kambiyo-senetlerine-ozgu-takip
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
  - ad: İcra ve İflas Kanunu
    numara: '2004'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kambiyo Senetlerine Özgü Takip

## Görev
Çek/bono/poliçeye dayanarak kambiyo senetlerine özgü haciz yolu (m.167 vd.) ile takip yapmak; senedin kambiyo vasfını ve takip yetkisini denetlemek; borçlu tarafında borca/imzaya itiraz ve şikâyet yollarını kullanmak.

## Soğuk başlangıç (intake)
- Senet çek mi, bono mu, poliçe mi; TTK'daki zorunlu unsurları (TTK m.671, m.776, m.692; çek için 5941 s.K. ve TTK m.780) taşıyor mu?
- Alacaklı meşru hamil mi; ciro silsilesi düzgün mü?
- Ödeme emri tebliğ tarihi nedir (itiraz/şikâyet 5 gün)?
- Çek için ibraz süresi/karşılıksız işlemi yapıldı mı?

## Denetim şeması
1. **Kambiyo vasfı (m.170/a)**: Senedin kambiyo senedi sayılması için zorunlu şekil şartları aranır; eksikse senet kambiyo vasfını taşımaz, takip iptal edilir. Bu husus süresiz şikâyet kapsamında değerlendirilir.
2. **Takip talebi ve ödeme emri (m.168)**: Borçluya 5 gün içinde borca/imzaya itiraz, 10 gün içinde ödeme veya mal beyanı bildirilir; itiraz icra mahkemesine yapılır ve kural olarak **takibi durdurmaz** (m.169, m.169/a — ancak teminatla durdurma mümkündür).
3. **İmzaya itiraz (m.170)**: 5 gün içinde icra mahkemesine; mahkeme inceleme yapar, haksız çıkan taraf aleyhine tazminat ve para cezası gündeme gelir.
4. **Borca itiraz (m.169, m.169/a)**: İtirazın esası icra mahkemesinde incelenir; itiraz yerinde görülürse takip durur.
5. **Yetki ve hamillik**: Senet bedeli, vade, faiz başlangıcı (TTK) ve hamilin müracaat hakkı (protesto/ibraz şartları) denetlenir.
6. **Ara sonuç**: Senedin geçerliliği, takibin durup durmayacağı ve teminat/tazminat riski belirlenir.

## Çıktı modülleri
- Senet vasfı kontrol listesi (zorunlu unsurlar + ciro).
- Kambiyo takip talebi taslağı / itiraz dilekçesi.
- Teminatla durdurma ve tazminat risk notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

