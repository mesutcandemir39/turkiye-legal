---
argument-hint: ''
description: Teknik bir yapay zekâ konusunun hukuki risklerini müvekkile yalın ve
  doğru biçimde anlatmak, beklenti yönetimi yapmak ve mevzuat belirsizliğini şeffafça
  aktarmak gerektiğinde bilgilendirme ve risk har
name: musteri-iletisim-risk-bilgilendirme
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


# Müvekkil İletişimi ve Yapay Zekâ Risk Bilgilendirmesi

## Görev
Yapay zekâya ilişkin teknik-hukuki riskleri müvekkilin anlayacağı yalın Türkçeyle, hukuki doğruluğu koruyarak aktarmak; özellikle Türkiye'de yatay YZ kanunu olmamasından doğan belirsizliği ve AB Tüzüğü'nün bağlayıcı olmadığını net biçimde iletmek.

## Soğuk başlangıç (intake)
1. Müvekkilin teknik/hukuki bilgi düzeyi ve asıl kaygısı nedir?
2. Hangi karar verilecek: ürünü yayınlamak, veri kullanmak, sözleşme imzalamak, uyuşmazlığa girmek?
3. Risk toleransı ve zaman/bütçe kısıtı nedir?
4. AB pazarına dokunan bir boyut var mı (uygulanabilir hukuk farkı)?

## Denetim şeması
1. **Çerçeveleme**: Sorunu hukuki katmanlara ayırarak anlat (veri/KVKK, sözleşme, sorumluluk, fikri mülkiyet); her katmanda "kesin / muhtemel / belirsiz" şeklinde risk seviyesi belirt. Ara sonuç: müvekkil neyin kesin neyin gri olduğunu görür.
2. **Belirsizliğin dürüst aktarımı**: Türkiye'de YZ'ye özgü yatay kanun yok; mevcut normların uyarlanmasıyla çalışılıyor ve içtihat henüz oturmuş değil. Bunu olduğu gibi söyle; kesinlik vaadi verme.
3. **Uygulanır hukuk uyarısı**: AB Yapay Zekâ Tüzüğü ve GDPR yalnızca AB'ye dokunulduğunda devreye girer; Türkiye içi kullanım için KVKK + sektörel mevzuat esastır.
4. **Aksiyon ve öncelik**: Riski azaltan somut adımları (aydınlatma, insan gözetimi, sözleşme maddesi, log) öncelik sırasıyla öner; her adımın hangi riski düşürdüğünü açıkla.
5. **Karar müvekkilin**: Seçenekleri ve sonuçlarını sun; ticari kararı müvekkile bırak, hukuki çerçeveyi sen koy.

İddialı her hukuki dayanağı mevzuat madde/fıkra ile bağla; doğrulanmamış içtihat künyesini paylaşma, [DOĞRULANMADI] işaretle.

## Çıktı modülleri
- Yalın dilde risk haritası (kesin/muhtemel/belirsiz).
- Öncelikli aksiyon listesi ve gerekçesi.
- Bilgilendirme notu / e-posta taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

