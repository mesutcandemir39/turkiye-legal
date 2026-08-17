---
argument-hint: ''
description: Dava öncesi üst makama başvuru, zorunlu idari başvuru yolları, zımni
  ret kavramı ve idari merci tecavüzü değerlendirilirken kullanılır; bir işleme doğrudan
  dava açılabilir mi yoksa önce idareye başvur
name: idari-basvuru-ve-merci-tecavuzu
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
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İdari Başvuru, Zımni Ret ve Merci Tecavüzü

## Görev
Dava açılmadan önce idareye başvurunun zorunlu mu ihtiyari mi olduğunu, zımni ret sürelerini ve merci tecavüzünün sonuçlarını belirleyerek davanın usulden reddini önlemek.

## Soğuk başlangıç (intake)
- İlgili mevzuat, dava öncesi zorunlu bir idari başvuru (itiraz) öngörüyor mu?
- İlgili idareye yapılmış bir başvuru var mı; başvuru tarihi ve cevap durumu?
- İdare hiç cevap vermedi mi (zımni ret) yoksa açık ret mi verdi?
- Başvuru dava açma süresi içinde mi yapıldı?

## Denetim şeması
1. **İhtiyari başvuru ve sürenin durması** (İYUK m.11): İlgililer dava açma süresi içinde, işlemi yapan veya üst makama başvurarak işlemin kaldırılması/geri alınması/değiştirilmesini isteyebilir. Bu başvuru işlemeye başlamış dava süresini **durdurur**.
2. **Zımni ret** (İYUK m.10): İlgililerin idareye yaptıkları başvurulara **60 gün** içinde cevap verilmezse istek reddedilmiş (zımni ret) sayılır; bu sürenin bitiminden itibaren dava açma süresi işler. İdare 60 gün geçtikten sonra cevap verirse, cevap tarihinden itibaren dava süresi yeniden işlemeye başlar.
3. **m.11 zımni reddi**: m.11 başvurusuna 30 gün (özel kanunda farklı süre yoksa) içinde cevap verilmezse istek reddedilmiş sayılır ve durmuş olan dava süresi kaldığı yerden işlemeye devam eder.
4. **Zorunlu idari başvuru / merci tecavüzü** (İYUK m.15/1-e): Mevzuat dava açmadan önce tüketilmesi zorunlu bir başvuru yolu öngörmüşse (ör. bazı vergi/gümrük itirazları, kamu ihalesinde KİK'e itirazen şikâyet), bu yol tüketilmeden açılan dava **merci tecavüzü** nedeniyle reddedilir ve dilekçe ilgili mercie tevdi olunur.
5. **İspat yükü**: Başvuru ve tebliğ tarihlerini ispat ilgilidedir; başvurunun kayıtlı/iadeli yapılması önerilir.
6. **Ara sonuç**: Başvurunun ihtiyari mi zorunlu mu olduğu ayrımı, hem süre hesabını hem de merci tecavüzü riskini doğrudan etkiler; tereddütte zorunlu yol varsayımıyla hareket güvenlidir.

## Çıktı modülleri
- Başvuru türü (ihtiyari/zorunlu) tespiti
- Zımni ret ve süre etkisi hesabı
- Merci tecavüzü riski ve gerekli başvuru taslağı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

