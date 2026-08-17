---
argument-hint: ''
description: 6183 sayılı Kanun kapsamında düzenlenen ödeme emrine, hacze, e-hacze
  ve ihtiyati haciz/tahakkuk işlemlerine karşı tahsil aşamasındaki uyuşmazlıkları
  çözmek için kullanılır.
name: odeme-emri-ve-tahsilat
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
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Ödeme Emri ve Tahsilat İşlemlerine Karşı Dava

## Görev
Kesinleşmiş ya da kesinleştiği varsayılan kamu alacağının tahsili için çıkarılan ödeme emri ve takip işlemlerine karşı, AATUHK'nın sınırlı itiraz sebepleri çerçevesinde dava kurmak; tahsil aşamasının hukuka uygunluğunu denetlemek.

## Soğuk başlangıç (intake)
1. Ödeme emri size ne zaman tebliğ edildi? Üzerindeki alacağın türü ve dönemi ne?
2. Bu alacağın aslına ilişkin daha önce ihbarname tebliğ edildi mi, dava açıldı mı?
3. İtiraz sebebiniz hangisi: böyle bir borç yok / kısmen ödedim / borç zamanaşımına uğradı?
4. Halihazırda haciz, e-haciz, banka bloke veya ihtiyati haciz uygulandı mı?

## Denetim şeması
1. **Süre — kritik.** AATUHK m.58 — ödeme emrine karşı dava **tebliğden itibaren 7 gün** içinde vergi mahkemesinde açılır. Bu süre, 30 günlük genel vergi davası süresinden farklıdır; karıştırma en sık hata.
2. **Sınırlı itiraz sebepleri.** m.58 — yalnızca "böyle bir borcun olmadığı", "borcun kısmen ödendiği" veya "borcun zamanaşımına uğradığı" ileri sürülebilir. Tarhiyatın esasına (matrah/ceza) ödeme emri aşamasında girilemez; o aşama ihbarname davasında tüketilir.
3. **Önceki aşamayı sorgula.** Ödeme emrinin dayanağı kesinleşmiş mi? İhbarname usulüne uygun tebliğ edilmemişse "böyle bir borç yoktur" kapsamında tarhiyat aşaması canlanabilir; tebligatın geçerliliği (VUK m.93 vd.) denetlenir.
4. **Zamanaşımı.** AATUHK m.102 — tahsil zamanaşımı 5 yıl; m.103 kesilme, m.104 durma halleri kontrol edilir.
5. **Yürütmenin durdurulması.** Ödeme emrine karşı davada İYUK m.27/4'ün otomatik durma etkisi yoktur; teminat ve YD talebi (İYUK m.27) ayrıca istenir. İhtiyati haciz/tahakkuk (AATUHK m.13-20) için ayrı dava ve YD değerlendirilir. Ara sonuç: haciz baskısı varsa teminat gösterilerek YD önceliklendirilir.
6. **Tecil-taksit.** AATUHK m.48 tecil talebi ile dava paralel yürütülebilir; ödeme güçlüğü varsa not düşülür.

## Çıktı modülleri
- 7 günlük süre uyarısı ve itiraz sebebi seçim tablosu.
- Ödeme emrine itiraz dilekçesi iskeleti.
- Teminat + YD talep stratejisi notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

