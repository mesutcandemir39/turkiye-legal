---
argument-hint: ''
description: Avukatın bilgi-belge isteme, dosya inceleme, örnek alma yetkileri ile
  büro/üst aramasına ilişkin güvenceler ve görevden doğan dokunulmazlık söz konusu
  olduğunda kullanılır.
name: avukatin-yetkileri-guvenceleri
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
  - ad: Avukatlık Kanunu
    numara: '1136'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Avukatın Yetkileri, Güvenceleri ve Büro Dokunulmazlığı

## Görev
Avukatın görevini yerine getirirken sahip olduğu yetki ve güvenceleri somut duruma
uygulamak; engellenme veya hukuka aykırı arama hallerinde başvuru yolunu göstermek.

## Soğuk başlangıç (intake)
1. Talep bir kurumdan bilgi/belge/dosya inceleme mi reddedildi?
2. Avukat görevi sırasında mı, görevi nedeniyle mi bir işleme maruz kaldı?
3. Büroda/konutta arama-elkoyma mı söz konusu?
4. İşleme baro temsilcisi katıldı mı; karar var mı?

## Denetim şeması
1. **Bilgi ve belge isteme.** Avukat, işini görmek için gerekli bilgi ve belgeleri kurum ve
   kuruluşlardan isteyebilir; bu talepler kanunda öngörülen istisnalar dışında reddedilemez
   (Av. K. m.2/3). Reddin gerekçesi ve dayanağı sorgulanır.
2. **Dosya inceleme ve örnek.** Avukat, görevli olduğu işlerde ilgili dosyaları inceleyebilir,
   örnek/suret alabilir (Av. K. m.46; CMK m.153 soruşturma dosyası için özel rejim ve
   kısıtlama kararı koşulları). Ara sonuç: kısıtlama kararı var mı, kapsamı ne?
3. **Görevden doğan güvenceler.** Avukatın görevi nedeniyle işlediği iddia edilen suçlarda
   soruşturma usulü ve yetkili merciler özeldir (Av. K. m.58-59); görevi sırasında ve görevden
   dolayı işlenen fiillerde ağırlaştırıcı koruma söz konusudur. Avukata karşı görevi
   dolayısıyla işlenen suçlar hâkime karşı işlenmiş gibi cezalandırılır (Av. K. m.57).
4. **Büro araması.** Avukat bürosu ancak mahkeme kararıyla, kararda yazılı olayla sınırlı
   aranır; arama sırasında baro başkanı/temsilcisi hazır bulunur; sır kapsamı iddia edilen
   şey mühürlenip hâkime gönderilir (CMK m.130). Bu güvencelere aykırı arama hukuka aykırı
   delil sorununu doğurur (CMK m.206/2-a, m.217/2).
5. **Engellenme.** Yetkinin engellenmesi tutanakla belgelenir; idari işleme karşı dava,
   ceza boyutunda suç duyurusu ve baroya bildirim seçenekleri değerlendirilir.

## Çıktı modülleri
- Yetki/engel değerlendirmesi ve dayanak maddeler.
- Arama anı kontrol listesi (karar, baro temsilcisi, mühürleme).
- Engellenmeye karşı başvuru/tutanak taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

