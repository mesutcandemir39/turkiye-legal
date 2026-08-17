---
argument-hint: ''
description: İdari işleme karşı dava açma sürelerini, İYUK m.10-11-13 başvurularını,
  zımni ret rejimini ve sürelerin hesabını çıkarmak için kullanılır; süre kaçırma
  riskini önlemek üzere her dosyada erken başvurul
name: sureler-ve-basvuru-yollari
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler, Zamanaşımı ve İdari Başvuru Yolları

## Görev
Dosyadaki tüm idari süreleri ve başvuru yollarını çıkarıp bir takvime dökmek; zımni ret, dava açma süresi ve durdurucu başvuruları doğru hesaplamak. İdare hukukunda hak kaybının en sık sebebi süredir.

## Soğuk başlangıç (intake)
1. İşlemin tebliğ/ilan/öğrenme tarihi tam olarak nedir?
2. İşlem bireysel mi düzenleyici mi; vergi/genel idari mi?
3. İYUK m.11 (üst makam/işlemi yapan makam) başvurusu yapıldı mı, ne zaman?
4. İdareye bir talep yapıldı ve cevapsız mı kaldı (m.10 zımni ret)?

## Denetim şeması
1. **Genel dava açma süresi.** İYUK m.7: Danıştay ve idare mahkemelerinde **60 gün**, vergi mahkemelerinde **30 gün**; tebliğ/ilan/öğrenme tarihini izleyen günden başlar.
2. **Düzenleyici işlem.** İYUK m.7/4: düzenleyici işleme karşı süresi içinde dava açılabileceği gibi, uygulama işlemiyle birlikte de düzenlemeye karşı dava açılabilir.
3. **İdari başvuru ile durma (m.11).** İşlemin kaldırılması/değiştirilmesi için **üst makama veya işlemi yapan makama** başvuru, dava süresini **durdurur**. İdarenin cevabı üzerine kalan süre işler; 60 gün cevapsızlık talebin reddi sayılır.
4. **Zımni ret (m.10).** İlgililerin idareden bir talebine **60 gün** içinde cevap verilmezse talep reddedilmiş sayılır; dava süresi bu sürenin bitiminden işler. Sonradan gelen cevap dava süresini etkilemez (cevaba göre yeni dava hakkı doğabilir).
5. **Eylemde ön başvuru (m.13).** İdari eylemlerden doğan zararlarda dava açmadan önce idareye başvuru zorunludur; eylemin/zararın öğrenilmesinden itibaren **bir yıl** ve her halde **beş yıl** içinde.
6. **Sürelerin hesabı (m.8).** Süreler tebliğ/ilanı izleyen günden başlar, tatil günleri dâhildir; son gün tatile rastlarsa ilk iş günü sonuna uzar. Çalışmaya ara verme (adli tatil) süreyi uzatabilir (m.61).
7. **Ara sonuç.** Tüm süreler için başlangıç-bitiş tarihli takvim ve hangi başvurunun süreyi durdurduğu.

## Çıktı modülleri
- Süre takvimi tablosu (olay → tarih → son gün).
- Zımni ret / m.11 durma senaryosu hesabı.
- Eylemde m.13 ön başvuru uyarısı.
- Süre riskleri kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

