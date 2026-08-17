---
argument-hint: ''
description: Çevresel etki değerlendirmesi zorunluluğu, ÇED Olumlu veya ÇED Gerekli
  Değildir kararlarının hukuka uygunluğu ve iptali, EK-1/EK-2 listelerine tabilik
  ve katılım hakkı sorunlarında kullan; ÇED dava ve
name: ced-sureci-ve-iptali
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
  - ad: Çevre Kanunu
    numara: '2872'
    tur: kanun
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# ÇED Süreci ve ÇED Kararının İptali

## Görev
Bir projenin ÇED'e tabi olup olmadığını, ÇED sürecinin usulüne uygunluğunu ve ÇED kararının iptal edilebilirliğini denetlemek; yatırımcı veya itiraz eden taraf için strateji kurmak.

## Soğuk başlangıç (intake)
1. Proje türü ve kapasitesi nedir; ÇED Yönetmeliği EK-1 mi yoksa EK-2 mi kapsamında?
2. Hangi karar verilmiş: "ÇED Olumlu", "ÇED Gerekli", "ÇED Gerekli Değildir"? Tarihi ve ilanı?
3. Halkın katılımı toplantısı yapıldı mı; inceleme-değerlendirme komisyonu süreci işledi mi?
4. İtiraz eden tarafın menfaat bağı (komşuluk, yöre halkı, dernek) nedir?

## Denetim şeması
1. **Tabilik**: 2872 m.10 ÇED zorunluluğunu kurar; projenin EK-1 (ÇED zorunlu) veya EK-2 (seçme-eleme, proje tanıtım dosyası) listesinde yer alıp almadığı yürürlükteki ÇED Yönetmeliği üzerinden tespit edilir. Kapasite/parçalama (proje bölme) yoluyla ÇED'den kaçınma iptal sebebidir.
2. **Usul denetimi**: Halkın katılımı toplantısı, bilgilendirme ve İDK sürecinin yönetmeliğe uygunluğu; eksiklik şekil sakatlığı doğurur.
3. **Esas denetimi**: ÇED raporunun bilimsel-teknik yeterliliği, alternatiflerin ve kümülatif etkilerin değerlendirilmesi; eksik/yanıltıcı veri esas yönünden sakatlık yaratır.
4. **Yargı yolu ve süre**: İptal davası idari yargıda açılır (2577 sayılı İYUK m.7 — kural olarak 60 gün; ilan/öğrenme tarihi önem taşır). Yürütmenin durdurulması (m.27) telafisi güç zarar nedeniyle erken talep edilir.
5. **İspat yükü ve ara sonuç**: Hukuka aykırılığı iddia eden davacı somut sakatlığı, idare ise işlemin sebep ve maksat unsurlarını ortaya koyar; bilirkişi/keşif belirleyicidir. ÇED dosyasındaki tek bir esaslı eksik dahi iptale yetebilir.

## Çıktı modülleri
- Tabilik analizi (EK-1/EK-2 eşleştirmesi)
- Usul ve esas sakatlık kontrol listesi
- İptal dilekçesi iskeleti + yürütmenin durdurulması talebi
- Bilirkişi/keşif delil planı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

