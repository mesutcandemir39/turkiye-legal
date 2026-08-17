---
argument-hint: ''
description: Çevre Kanunu kapsamında verilen idari para cezaları, faaliyet durdurma
  ve mühürleme kararlarına karşı itiraz/dava yolunu, süreleri ve görevli mercii belirlemek
  gerektiğinde; ceza tutarının ve dayanağı
name: idari-para-cezasi-itiraz
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
  - ad: Çevre Kanunu
    numara: '2872'
    tur: kanun
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İdari Yaptırımlar ve İtiraz Yolu

## Görev
Çevre mevzuatı kapsamında uygulanan idari para cezası, faaliyet durdurma ve mühürleme kararlarının dayanağını ve tutarını denetlemek; doğru başvuru/dava yolunu ve süreyi belirleyerek iptalini sağlamak.

## Soğuk başlangıç (intake)
1. Hangi yaptırım: idari para cezası, faaliyet durdurma, mühürleme, lisans iptali?
2. Karar hangi madde/yönetmelik hükmüne dayandırılmış; tebliğ tarihi nedir?
3. Tutar nasıl hesaplanmış (tekerrür, kademe, çarpan uygulandı mı)?
4. Tutanak/tespit usulü düzgün mü; ölçüm/numune zinciri var mı?

## Denetim şeması
1. **Dayanak ve yetki**: Ceza 2872 m.20-23'teki cetvele ve ilgili yönetmeliğe uygun mu; kararı veren makam yetkili mi (Bakanlık/il müdürlüğü/belediye yetki devri)? Yetkisizlik iptal sebebidir.
2. **Tutar denetimi**: Maktu tutarlar her yıl yeniden değerleme oranıyla güncellenir; yanlış yıl/oran, hatalı tekerrür veya kademe uygulaması iptal/kısmi iptal nedenidir.
3. **Usul**: Tespit tutanağı, savunma hakkı ve ölçüm/numune usulü 5326 sayılı Kabahatler Kanunu ve alan yönetmeliklerine uygun olmalıdır; usule aykırı delil cezayı sakatlar.
4. **Yargı yolu ve süre**: Çevre Kanunu'na dayalı idari para cezalarında başvuru kural olarak idare mahkemesinedir (2577 sayılı İYUK, süre 60 gün); ancak dayanağa göre 5326 m.27 ile sulh ceza hâkimliği yolunun gündeme gelebileceği hallerde görev yolunu mutlaka kanun maddesi düzeyinde teyit et. Yanlış mercie başvuru süre kaybına yol açar.
5. **İspat ve ara sonuç**: İdare işlemin maddi ve hukuki sebebini ispatla yükümlüdür; tutanak ve ölçümdeki tek bir zincir kopukluğu dahi iptale yetebilir.

## Çıktı modülleri
- Yaptırım künyesi tablosu (madde, tutar, tarih, merci)
- Görev/yetki ve süre analizi
- İtiraz/iptal dilekçesi iskeleti
- Tutanak ve ölçüm usul denetimi listesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

