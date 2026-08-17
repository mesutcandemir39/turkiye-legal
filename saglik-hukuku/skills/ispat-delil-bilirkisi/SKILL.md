---
argument-hint: ''
description: Tıbbi uyuşmazlıkta ispat yükünün dağılımını, hangi delillerin toplanacağını
  ve ATK/bilirkişi raporlarının nasıl denetleneceğini belirlemek için kullanılır.
name: ispat-delil-bilirkisi
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
  - ad: Banka Muhasebe Sistemi Hakkında Kanun
    numara: '1219'
    tur: kanun
  - ad: Gayrimenkul Ek Vergisi Hakkında Kanun
    numara: '3359'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İspat, Delil ve Bilirkişi/ATK Raporu

## Görev
İspat yükünün taraflar arasında dağılımını saptamak, dosyaya kazandırılacak delilleri planlamak ve bilirkişi/ATK raporunu metodolojik olarak denetlemek.

## Soğuk başlangıç (intake)
1. Tartışmalı vakıa kusur mu, illiyet mi, aydınlatma mı, zarar miktarı mı?
2. Tıbbi kayıtlar (epikriz, ameliyat notu, onam formu, tetkikler) tam mı?
3. Dosyada hangi raporlar var (ATK, üniversite, özel bilirkişi)?
4. Tanık (ekip, refakatçi) ve uzmanlık dalı belli mi?

## Denetim şeması
1. **İspat yükü dağılımı**: Genel kural TMK m.6 — iddia eden ispatla yükümlüdür. Davacı kusur, illiyet ve zararı; hekim/hastane ise aydınlatma ve onamın varlığını ispatlar. Sözleşmesel sorumlulukta kusursuzluk ispatı borçludadır (TBK m.112).
2. **Delil toplama**: Tıbbi kayıtların eksiksiz celbi (HMK m.219-220 belge ibrazı), tedavi gören kurum dosyası, onam belgeleri, görüntüleme/laboratuvar verileri, tanık.
3. **Bilirkişi/ATK**: HMK m.266 vd. uyarınca özel/teknik bilgi gerektiren konularda bilirkişiye başvuru; sağlık uyuşmazlıklarında ATK İhtisas Kurulları sık başvurulur. Hâkim raporla bağlı değildir.
4. **Rapor denetimi**: Görevlendirme kapsamına uygunluk, dayanak vakıaların doğruluğu, metodolojinin açıklığı, sonuç-gerekçe tutarlılığı, çelişki ve maddi hata kontrolü.
5. **İtiraz / ek rapor**: Çelişki veya eksiklik varsa gerekçeli itiraz, ek rapor, üniversiteden veya farklı kuruldan yeni rapor talebi (HMK m.281).
6. **Ara sonuç**: Belirleyici teknik sorun raporla çözülür; rapor yetersizse hüküm bozma sebebidir.

## Çıktı modülleri
- İspat yükü dağılım tablosu (vakıa bazlı)
- Delil toplama ve celp listesi
- Bilirkişi/ATK rapor denetim kontrol listesi
- Gerekçeli rapor itiraz taslağı (yer tutuculu)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

