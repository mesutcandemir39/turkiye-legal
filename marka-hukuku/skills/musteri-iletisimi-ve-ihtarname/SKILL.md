---
argument-hint: ''
description: Karşı tarafa ihtarname gönderilecek, müvekkile risk anlatılacak veya
  tecavüz iddiasına cevap verilecekse; iletişimi yönetmek ve dengeli, geri tepmeyen
  ihtarname kurmak için kullanılır.
name: musteri-iletisimi-ve-ihtarname
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


# Müvekkil İletişimi ve İhtarname Yönetimi

## Görev
Marka uyuşmazlığında taraflar arası iletişimi yönetmek: tecavüz edene ihtarname (cease and desist) hazırlamak, müvekkile riski sade dille anlatmak ve gelen ihtarnameye/iddiaya stratejik cevap kurmak. İhtarname hem caydırıcı hem de aşırıya kaçıp haksız tehdit/geri tepme yaratmayacak biçimde dengeli olmalıdır.

## Soğuk başlangıç (intake)
- İhtarname gönderen taraf mı, cevap veren taraf mı?
- Markanın tescil/hak durumu sağlam mı (ihtardan önce teyit edildi mi)?
- Amaç durdurma mı, tazminat mı, sulh/lisans mı?
- Karşı tarafla ticari ilişki sürdürülecek mi?

## Denetim şeması
1. **Hak teyidi (ön kontrol).** İhtar göndermeden önce kendi markanın geçerliliği, kullanım durumu ve kapsamı doğrulanır; zayıf hakka dayalı ihtar karşı dava (menfi tespit) riski doğurur.
2. **İhtarname içeriği.** Hak sahipliği ve tescil bilgisi, tecavüz fiilinin somut tarifi, dayanak maddeler (m.7, m.29), talep (durdurma, ürün toplama, taahhüt), makul süre ve sonuç ihtarı (dava/tazminat). Abartılı/asılsız tehditten kaçınılır.
3. **Müvekkile bilgilendirme.** Riskin gerçekçi anlatımı (kazanma ihtimali, maliyet, süre); en iyi/en kötü senaryo; karar müvekkilindir.
4. **Gelen ihtara cevap.** İddianın dayanağı denetlenir (gerçek tescil mi, kullanmama def'i mümkün mü, dürüst kullanım/önceye dayalı hak savunması var mı); ölçülü cevap veya sulh önerisi.
5. **Delil ve kayıt.** Tüm yazışmalar tarih/teslim kanıtıyla saklanır; ihtar, ileride zamanaşımı/temerrüt ve kusur tartışmasında dayanak olur.
6. **Sulh kapısı.** Koexistence sözleşmesi, lisans veya sınırlı kullanım gibi çözümler erken masaya konur.

## Çıktı modülleri
- İhtarname taslağı ([doldurulacak] yer tutucularla, dayanak madde listeli).
- Müvekkile sade dilli risk-özet notu (senaryolu).
- Gelen ihtara cevap iskeleti ve savunma kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

