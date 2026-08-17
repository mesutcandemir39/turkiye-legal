---
argument-hint: ''
description: İptal veya tam yargı davası için İYUK m.3 ve m.5 unsurlarına uygun dilekçe;
  dava açma süresi, üst makama başvuru ve yürütmenin durdurulması talebini kurmak
  gerektiğinde kullanılır.
name: idari-dava-dilekcesi-iyuk
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İdari Dava Dilekçesi (İYUK)

## Görev
İptal veya tam yargı davası dilekçesini İYUK m.3 unsurlarına uygun kurmak; en kritik unsur olan dava açma süresini doğru hesaplamak ve gerektiğinde yürütmenin durdurulmasını istemek.

## Soğuk başlangıç (intake)
- Dava konusu idari işlemin tarihi ve tebliğ/öğrenme tarihi nedir?
- İptal davası mı, tam yargı (tazminat) mı, ikisi birlikte mi?
- Üst makama (ihtiyari/zorunlu) başvuru yapıldı mı (m.11)?
- Telafisi güç zarar ve açık hukuka aykırılık var mı (YD talebi)?

## Denetim şeması
1. Dilekçe unsurları (İYUK m.3): Mahkeme, taraflar, davanın konusu ve sebepleri, dava konusu işlemin yazılı bildirim tarihi, sonuç (talep), deliller. İdari işlemin örneği eklenir (m.3/3).
2. Dava açma süresi (m.7): Kural olarak Danıştay ve idare mahkemelerinde 60 gün, vergi mahkemelerinde 30 gün; süre yazılı bildirimi izleyen günden işler. Özel kanunlardaki farklı süreleri kontrol edin. Süre kamu düzeninden, re'sen incelenir.
3. Üst makama başvuru (m.11): İşlemin kaldırılması/değiştirilmesi için dava süresi içinde üst makama başvuru süreyi durdurur; cevap verilmez/red gelirse kalan süre işler.
4. İptal sebepleri: İdari işlemin beş unsuru — yetki, şekil, sebep, konu, maksat — üzerinden sakatlık iddialarını altlayın.
5. Yürütmenin durdurulması (m.27): İki şart birlikte — telafisi güç/imkânsız zarar ve açık hukuka aykırılık; talebi gerekçelendirip teminat hususunu belirtin. Tam yargıda zarar ve idari kusur/sorumluluk dayanağını kurun. Ara sonuç: süre içinde ve unsurlar tamsa dilekçe hazır.

## Çıktı modülleri
- İptal/tam yargı dava dilekçesi taslağı (İYUK m.3 başlıklı)
- Süre hesabı notu (tebliğ → son gün)
- Yürütmenin durdurulması gerekçeli talebi
- Ek listesi (işlem örneği, başvuru evrakı)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

