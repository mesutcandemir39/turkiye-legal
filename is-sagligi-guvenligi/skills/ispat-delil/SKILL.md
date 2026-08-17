---
argument-hint: ''
description: İSG uyuşmazlıklarında ispat yükünün dağılımını, delil türlerini ve bilirkişi-kusur
  raporlarının değerlendirilmesini ele almak için kullanılır.
name: ispat-delil
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
  - ad: İş Sağlığı ve Güvenliği Kanunu
    numara: '6331'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İspat ve Delil Yönetimi

## Görev
İSG dosyasında ispat yükünü doğru dağıtmak, hangi tarafın neyi ispatlayacağını netleştirmek ve delilleri (belge, tanık, bilirkişi/kusur raporu) stratejik biçimde örgütlemek.

## Soğuk başlangıç (intake)
- Hangi vakıa çekişmeli (kaza nitelendirmesi, önlem alınıp alınmadığı, kusur oranı, zarar miktarı)?
- İşverenin uyum belgeleri (risk değerlendirmesi, eğitim, muayene, KKD teslim tutanağı) mevcut mu, imzalı mı?
- Kaza anına ilişkin tutanak, kamera kaydı, tanık, kolluk/iş müfettişi raporu var mı?
- Bilirkişi/kusur raporu düzenlendi mi; itiraz edilecek nokta var mı?

## Denetim şeması
1. **İspat yükü dağılımı:** İşçi/hak sahibi kazayı, zararı ve illiyeti ortaya koyar; işveren ise gerekli İSG önlemlerini aldığını ve gözetme borcunu yerine getirdiğini ispatla yükümlüdür (TBK m.417/2, m.112 mantığı; TMK m.6). Bu dağılım dosyanın iskeletidir.
2. **Belge delilleri:** İmzalı ve tarihli risk değerlendirmesi, İSG eğitim katılım belgeleri, işe giriş/periyodik muayene, KKD zimmet tutanağı, onay/öneri defteri. İmzasız/tarihsiz belge ispat değeri düşüktür.
3. **Diğer deliller:** Tanık (iş arkadaşı, ustabaşı), kamera, makine bakım kayıtları, iş müfettişi ve kolluk tutanağı, ATK/sağlık raporu (maluliyet).
4. **Bilirkişi/kusur raporu:** Kusur dağılımı ve teknik illiyet bu raporla belirlenir. Rapor görevlendirme kapsamına uygun mu, yöntemi ve dayanağı somut mu, hesap ve maddi hata var mı, çelişki taşıyor mu? Gerekçeli itirazla ek rapor/yeni heyet istenebilir.
5. **Karine ve değerlendirme:** Risk değerlendirmesinin/eğitimin yokluğu, kusur aleyhine güçlü emaredir. **Ara sonuç:** Çekişmeli her vakıa için "ispat yükü → mevcut delil → eksik delil" tablosu çıkar.

## Çıktı modülleri
- Çekişmeli vakıa-ispat yükü-delil matrisi.
- Belge delili yeterlilik kontrol listesi.
- Bilirkişi raporuna itiraz gerekçeleri taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

