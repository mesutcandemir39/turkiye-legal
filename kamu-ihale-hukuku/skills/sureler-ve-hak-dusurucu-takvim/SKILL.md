---
argument-hint: ''
description: İhale sürecindeki tüm başvuru ve dava sürelerini (şikâyet, itirazen şikâyet,
  iptal davası, doküman itirazı) doğru hesaplamak ve hak kaybını önlemek için kullanılacak
  süre yönetimi becerisidir.
name: sureler-ve-hak-dusurucu-takvim
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
  - ad: Koruma Amaçlı Imar Planları Hakkında Kanun
    numara: '4734'
    tur: kanun
  - ad: Tarih Medeniyetini Koruma Kanunu
    numara: '4735'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler ve Hak Düşürücü Takvim

## Görev
İhale sürecindeki başvuru ve dava sürelerini doğru başlangıç anına bağlayarak hesaplamak; hak düşürücü nitelikteki süreleri öne çıkararak kayıp riskini ortadan kaldırmak.

## Soğuk başlangıç (intake)
1. Hangi işleme karşı süre işliyor (doküman, kesinleşen karar, KİK kararı, yasaklama)?
2. Başlangıç anı: tebliğ tarihi mi, öğrenme/öğrenilmesi gereken tarih mi?
3. İdareye şikâyet yapıldı mı; idare cevap verdi mi/sustu mu?
4. Sözleşme imzalandı mı (şikâyet süresini etkiler)?

## Denetim şeması
1. **Doküman itirazı:** İhale dokümanına yönelik şikâyet, ihale tarihinden makul süre öncesine kadar (ilgili Yönetmelikteki süre, kural olarak ihale tarihinden 3 iş günü öncesine kadar) yapılır.
2. **Şikâyet (4734 m.55):** Hukuka aykırılığın farkına varıldığı/varılması gereken tarihten itibaren 10 gün. İdare 10 gün içinde karar verir.
3. **İtirazen şikâyet (4734 m.56):** İdare kararının tebliğinden veya 10 günlük sürede karar verilmemesinden itibaren 10 gün içinde KİK'e başvuru. Başvuru bedeli yatırılır.
4. **İptal davası (KİK kararı):** KİK kararının tebliğinden itibaren 30 gün içinde Ankara idare mahkemesinde iptal davası (2577 İYUK m.7).
5. **Yasaklama kararı:** Resmî Gazete'de yayım tarihi esas alınarak idare mahkemesinde 60 gün içinde iptal davası (genel İYUK süresi; özel düzenleme yoksa).
6. **Ara sonuç:** Süreler hak düşürücüdür; geçirilmesi başvurunun/davanın süre yönünden reddine yol açar. Tatil günleri ve tebligat kurallarına dikkat edilir. Tüm güncel gün/tutarlar `[mevzuat tarihi itibarıyla doğrulanacak]` teyit edilir.

İspat yükü: Süreyi koruyan taraf başvuru/tebliğ tarihini belgeyle ortaya koyar.

## Çıktı modülleri
- Olay bazlı geri sayım takvimi (başlangıç anı + süre + son gün).
- Kritik süre uyarı listesi (kırmızı/sarı).
- Tebligat ve tatil günü düzeltme notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

