---
argument-hint: ''
description: Yayın yoluyla hakaret, özel hayatın ihlali, kişisel verilerin yayılması
  gibi suçlarda ceza sorumluluğu silsilesini, şikâyet ve uzlaştırmayı değerlendirmek
  gerektiğinde kullanılır.
name: basin-ceza-sorumlulugu
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
  - ad: Basın Meslek İlkeleri ve Yapı İtibarı Hakkında Kanun
    numara: '5187'
    tur: kanun
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Basın Yoluyla İşlenen Suçlar ve Ceza Sorumluluğu

## Görev
Yayın içeriğinin TCK suçu oluşturup oluşturmadığını saptamak, 5187 sayılı Kanun m.11 sorumluluk silsilesini uygulamak, şikâyet ve uzlaştırma sürecini yönetmek.

## Soğuk başlangıç (intake)
1. İçerik hangi suçu oluşturabilir (hakaret, özel hayat, veri ihlali)?
2. Mağdur gerçek kişi mi, kamu görevlisi mi; suç görevden mi kaynaklanıyor?
3. Eser sahibi belli mi; sorumlu müdür kim?
4. Yayın tarihi nedir (dava/şikâyet süresi için)?

## Denetim şeması
1. **Suç tipi**: Hakaret TCK m.125 (alenen işlenmesi nitelikli hâl, m.125/IV); kamu görevlisine görevinden dolayı hakaret artırıcı sebep. Özel hayatın gizliliğini ihlal TCK m.134; kişisel verileri hukuka aykırı yayma TCK m.136; haberleşmenin gizliliği m.132.
2. **Hukuka uygunluk**: Haber verme hakkı, eleştiri hakkı ve iddia/savunma dokunulmazlığı değerlendirilir; gerçeklik, kamu yararı, güncellik ve öz-biçim dengesi varsa fiil hukuka uygun olabilir.
3. **Sorumluluk silsilesi (m.11)**: Eser sahibi sorumludur; eser sahibi belli değilse veya yayım sahibinin engellemesiyle yayımlanmışsa sorumlu müdür sorumlu tutulur. Tüzel kişiler için ayrı değerlendirme yapılır.
4. **Şikâyet ve süre**: Hakaret şikâyete bağlıdır; şikâyet süresi fiil ve failin öğrenilmesinden itibaren altı aydır (TCK m.73). Basın Kanunu m.26 dava sürelerini özel olarak düzenler.
5. **Uzlaştırma**: Hakaret uzlaştırmaya tabidir (CMK m.253).
6. **Ara sonuç**: Suçun unsurları + hukuka uygunluğun yokluğu + süresinde şikâyet varsa ceza süreci işletilir.

## Çıktı modülleri
- Suç tipi-unsur altlama tablosu
- Sorumluluk silsilesi şeması
- Şikâyet dilekçesi iskeleti ve süre uyarısı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

