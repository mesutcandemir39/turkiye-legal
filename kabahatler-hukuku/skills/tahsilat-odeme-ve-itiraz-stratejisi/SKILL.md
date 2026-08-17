---
argument-hint: ''
description: İdari para cezasının kesinleşmesi, 6183 sayılı Kanuna göre tahsili, ödeme
  emri, peşin ödeme indirimi ve başvuru-ödeme arasındaki tercih stratejisini kurmak
  gerektiğinde kullanılır.
name: tahsilat-odeme-ve-itiraz-stratejisi
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
  - ad: Kabahatler Kanunu
    numara: '5326'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tahsilat, Ödeme ve İtiraz Stratejisi

## Görev
Cezanın kesinleşme ve tahsil sürecini yönetmek; peşin ödeme indirimi ile başvuru arasında maliyet-risk dengesi kurmak ve tahsilata karşı hukuki yolları belirlemek.

## Soğuk başlangıç (intake)
- Ceza kesinleşti mi, ödeme emri tebliğ edildi mi?
- Peşin ödeme süresi (5326 m.17/6) hâlâ açık mı?
- Tahsilat 6183 sayılı Kanuna göre mi yürütülüyor (haciz, ödeme emri)?
- Başvuru yapıldı mı, sonucu bekleniyor mu?

## Denetim şeması
1. **Tahsil rejimi (5326 m.17):** İdari para cezaları 6183 sayılı Amme Alacaklarının Tahsil Usulü Hakkında Kanuna göre tahsil edilir. Kesinleşmeden cebri tahsil yapılamaz.
2. **Peşin ödeme indirimi (5326 m.17/6):** Tebliğden itibaren süresinde ödenirse cezanın 1/4'ü indirilir. Bu hak, başvuru yapma hakkını ortadan kaldırmaz; ancak ödeme ile başvuru ilişkisini somut olayda doğru kur (ödenen kısmın iadesi/talep stratejisi).
3. **Başvuru-ödeme tercihi:** Başvuruda esaslı şans varsa ve tutar yüksekse başvuru; sübut güçlü ve tutar düşükse indirimli ödeme öne çıkar. Risk haritasıyla karar ver.
4. **Ödeme emrine karşı (6183 m.58):** Ödeme emrinin esasına (borcun yokluğu, zamanaşımı, ödenmiş olma) karşı görevli yargı yolunda dava; idari para cezalarında genel başvuru yolu (5326 m.27) ile ödeme emrine itiraz yolunu ayırt et.
5. **Yerine getirme zamanaşımı (5326 m.21):** Tahsil süresi geçmişse cezanın infaz edilemeyeceğini ileri sür.
6. **Ara sonuç:** Ödeme yapılacaksa indirim süresini koru; itiraz yolu seçilecekse cebri tahsil riskini ve teminat/tedbir ihtimalini değerlendir.

## Çıktı modülleri
- Ödeme vs. başvuru maliyet-risk matrisi.
- Tahsilata karşı hukuki yol notu (6183 m.58 / 5326 m.27 ayrımı).
- Zamanaşımı ve indirim süresi uyarı kartı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

