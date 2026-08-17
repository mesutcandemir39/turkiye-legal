---
argument-hint: ''
description: Bir işçilik dosyasında kazanç ihtimali, alacak büyüklüğü, işe iade ile
  alacak davası arasında seçim ve müzakere/sulh stratejisi belirlenmesi gerektiğinde;
  işçi veya işveren tarafında risk haritası ve
name: risk-strateji-iscilik-davasi
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
  - ad: İş Kanunu
    numara: '4857'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk ve Strateji — İşçilik Davası Değerlendirmesi

## Görev
Dosyayı uçtan uca tartarak kazanç olasılığı, beklenen alacak/maruz kalınan risk ve en uygun yol haritasını (dava/sulh/işe iade) belirlemek.

## Soğuk başlangıç (intake)
1. Tarafını temsil ettiğin kim (işçi mi işveren mi) ve önceliği nedir?
2. Fesih nitelendirmesinde zayıf/güçlü noktalar neler?
3. Belgesel delil durumu lehte mi aleyhte mi?
4. İşçi tekrar çalışmak istiyor mu, yoksa tazminat odaklı mı?

## Denetim şeması
1. **Fesih zemini riski:** Fesih haklı/geçerli/usulsüz ekseninde nerede? İşveren m.19 usulüne uymamışsa geçerli sebep dahi zayıflar; m.26 süresini kaçırdıysa haklı fesih düşer.
2. **İşe iade vs. alacak tercihi:** Güvence kapsamı varsa: işe iade kazanılırsa boşta geçen (≤4 ay) + başlatmama (4-8 ay) tazminatı doğar, ancak kıdem/ihbar mahsubu ve işe başlatma riski hesaplanmalı. Alacak davası daha kesin nakit sonuç verir ama güvence tazminatlarını içermez. İkisi birlikte/sırayla kurgulanabilir.
3. **Alacak büyüklüğü tahmini:** Kıdem + ihbar + fazla çalışma + tatil + izin kalemlerinin kaba aralığı; takdiri indirim ve zamanaşımı süzgeci uygulanır.
4. **İspat riski:** Tanığa bağlı kalemler (fazla çalışma) belirsizlik taşır; belgeyle desteklenmeyen iddialarda indirim beklenmeli. İşveren tarafında ibraz edilmeyen kayıt riski not edilir.
5. **Sulh/müzakere analizi:** Arabuluculuk aşaması zorunlu olduğundan, beklenen yargılama maliyeti, faiz ve süresi karşısında erken sulh aralığı hesaplanır. İşveren için itibar ve emsal etkisi; işçi için nakit-zaman dengesi tartılır.
6. **Ara sonuç:** Lehe/aleyhe faktör matrisi ve önerilen yol.

## Çıktı modülleri
- Güçlü/zayıf yön (SWOT benzeri) matrisi.
- Beklenen sonuç aralığı (alacak / tazminat tahmini).
- İşe iade-alacak-sulh karar önerisi ve gerekçesi.
- Müzakere taban-tavan aralığı ve sonraki adım listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

