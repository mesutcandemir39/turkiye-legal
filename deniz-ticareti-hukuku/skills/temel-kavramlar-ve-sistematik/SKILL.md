---
argument-hint: ''
description: Deniz ticareti hukukunun temel kavramlarını (gemi, donatan, taşıyan,
  navlun, konişmento) ve TTK Beşinci Kitap sistematiğini ilk kez bir dosyaya çerçevelerken;
  uyuşmazlığın hangi alt alana girdiğini ve
name: temel-kavramlar-ve-sistematik
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
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Sistematik

## Görev
Deniz ticaretine ilişkin bir olayı doğru vasıflandırmak, ilgili tarafları ve sözleşme/kaza ilişkisini tanımlamak, TTK Beşinci Kitap içinde hangi rejimin uygulanacağını ve hangi milletlerarası kaynakların devreye gireceğini belirlemek.

## Soğuk başlangıç (intake)
- İlişki bir taşıma mı (navlun/konişmento), bir deniz kazası mı (çatma/kurtarma/avarya), yoksa ayni hak/icra meselesi mi (gemi ipoteği/ihtiyati haciz)?
- Geminin bayrağı, sicili ve adı; taraflar tacir mi; sözleşmede tahkim veya yabancı hukuk kaydı var mı?
- Elinizde hangi belgeler var (konişmento, çarter parti, sörvey raporu, gemi jurnali)?
- Olayın tarihi ve zarar/ihbar tarihleri nedir (zamanaşımı için kritik)?

## Denetim şeması
1. **Gemi ve ticaret gemisi nitelendirmesi**: Aracın TTK m.931 anlamında gemi ve ticaret gemisi olup olmadığını belirle; sicile tescilli olup olmadığı (TTK m.954 vd.) ayni hak ve ipotek sonuçlarını etkiler.
2. **Tarafların belirlenmesi**: Donatan (TTK m.1061), gemi işletme müteahhidi (TTK m.1065), taşıyan ve taşıtan, gönderilen; konişmentoda kimin "taşıyan" olduğunu lafza göre tespit et. Donatanın adamlarının kusurundan sorumluluğu (TTK m.1062) kapsamını not et.
3. **İlişki tipinin vasıflandırılması**: Navlun sözleşmesi (yolculuk çarteri / kırkambar — TTK m.1138 vd.) mı, yolcu taşıma mı, yoksa kaza ilişkisi mi? Vasıflandırma, sorumluluk rejimini ve süreyi belirler.
4. **Uygulanacak norm katmanı**: TTK Beşinci Kitap esas; konişmentolu taşımada Lahey-Visby kaynaklı hükümler (TTK m.1178 vd.), müşterek avaryada York-Anvers Kuralları (TTK m.1272 vd.), ihtiyati hacizde 1952 Sözleşmesi ile uyumlu TTK m.1352 vd. Ara sonuç olarak uygulanacak madde setini sabitleyin.
5. **İspat yükü ve ara sonuç**: Kural olarak zararı ve ilişkiyi ileri süren ispatlar; taşıyanın özen borcunun ihlali bakımından ispat yükünün yer değiştirdiği özel haller (denize elverişlilik, m.1141) ayrıca incelenir. Çıktıda hangi rejimin neden seçildiğini gerekçelendirin.

## Çıktı modülleri
- İlişki haritası (taraflar, sıfatlar, sözleşme/kaza zinciri)
- Uygulanacak normlar tablosu (TTK maddeleri + milletlerarası kaynak)
- Vasıflandırma notu ve bir sonraki uzman beceriye yönlendirme



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

