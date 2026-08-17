---
argument-hint: ''
description: Eşya hukuku ile borçlar hukuku ayrımının (in rem / in personam) Roma
  temelini açıklamak; mutlak-nispi hak, herkese karşı ileri sürülebilirlik ve actio
  tipi tartışmalarında dogmatik derinlik gerektiğin
name: ayni-sahsi-hak-eskidogmatik
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


# Ayni ve Şahsi Hak Dogmatiğinin Roma Temeli

## Görev
Türk özel hukukunun en temel ayrımı olan ayni hak (eşya hukuku) – şahsi/alacak hakkı (borçlar hukuku) ikilisini Roma'daki actio in rem / actio in personam ayrımına dayandırarak dogmatik olarak temellendirmek.

## Soğuk başlangıç (intake)
- Tartışma mutlak/nispi hak ekseninde mi yoksa eşya-borç sistematiği ekseninde mi?
- Somut kurum hangisi (mülkiyet, sınırlı ayni hak, alacak, satış vaadi)?
- Çıktı akademik açıklama mı, yorum argümanı mı?

## Denetim şeması
1. Modern ayrımı sabitle: ayni haklar herkese karşı ileri sürülür (mutlak), TMK eşya hukuku (m.683 vd., sınırlı ayni haklar m.779 vd. rehin, m.794 vd. intifa, m.779 irtifak çerçevesi). Alacak hakkı belirli borçluya karşıdır (nispi), TBK borç ilişkisi.
2. Roma kökenini kur: ayni hakkı koruyan actio in rem (rei vindicatio, actio negatoria, actio confessoria); borç ilişkisini koruyan actio in personam. Roma'da hak değil dava merkezlidir; korumayı sağlayan actio'nun tipi, hakkın mutlak mı nispi mi olduğunu belirler.
3. Numerus clausus ilkesini bağla: ayni hakların sınırlı sayıda ve tipte olması (TMK eşya hukuku sistematiği) Roma'daki sınırlı ayni hak kataloğuna (servitutes, usus fructus, pignus, hypotheca, superficies, emphyteusis) dayanır. Borç ilişkilerindeki tip serbestisi (TBK m.26 sözleşme özgürlüğü) ile karşıtlığını göster.
4. Sınır kuralını uygula: nemo plus iuris ad alium transferre potest quam ipse haberet — kimse sahip olduğundan fazla hak devredemez; bu, ayni hak devrinin (TMK m.683 vd., tasarruf yetkisi) ve yolsuz tescilin (TMK m.1023-1024 iyiniyetli üçüncü kişi istisnası) dogmatik çerçevesini açıklar.
5. Karma/sınır kurumları ayrıştır: kişisel hakkın güçlendirilmesi (şerhle ayni etki, TMK m.1009; satış vaadinin şerhi) tarihî olarak ayni-şahsi sınırının yumuşamasıdır; bu istisnayı işaretle.
6. Ara sonuç: somut kurumu doğru kategoriye yerleştir; koruma davasının tipini (ayni dava / alacak davası) belirle.

İspat/dayanak: modern norm madde ile (TMK m.683, m.1023; TBK m.26); Roma actio'ları ve maxim fragmanla; doktrin [DOĞRULANMADI].

## Çıktı modülleri
- Ayrım tablosu: ayni hak / şahsi hak — koruma davası, etki alanı, Roma karşılığı.
- Numerus clausus ile tip serbestisi karşılaştırması.
- nemo plus iuris uygulama notu (güncel madde bağlantısıyla).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

