---
argument-hint: ''
description: İhale uyuşmazlığında hangi belgenin ne için delil olduğunu, EKAP ve ihale
  işlem dosyasından hangi kayıtların temin edileceğini ve ispat yükünün kimde olduğunu
  belirlemek gerektiğinde kullanılır.
name: ispat-delil-ve-dosya
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


# İspat, Delil ve İhale Dosyası

## Görev
İhale uyuşmazlığında iddiayı destekleyecek belge ve kayıtları (ihale işlem dosyası, EKAP kayıtları, teklif zarfı, tutanaklar) belirlemek; ispat yükünün dağılımını ve delil temin yollarını ortaya koymak.

## Soğuk başlangıç (intake)
1. İddianın özü ne (yeterlik, değerlendirme, aşırı düşük, eşit muamele ihlali)?
2. Elinde hangi belgeler var; eksik olan kritik belge hangisi?
3. İhale işlem dosyasına/EKAP kayıtlarına erişim sağlandı mı?
4. Karşı tarafın/diğer isteklilerin teklif bilgisine ihtiyaç var mı?

## Denetim şeması
1. **Delil türleri:** İhale dokümanı, teklif mektubu ve eki belgeler, geçici teminat, ihale komisyon kararı, kesinleşen ihale kararı bildirimi, tutanaklar (zarf açma, değerlendirme), zeyilname, açıklama yazıları temel yazılı delillerdir.
2. **EKAP ve işlem dosyası:** Elektronik Kamu Alımları Platformu (EKAP) üzerindeki kayıtlar ve ihale işlem dosyası temin edilir; idareden bilgi/belge talebi (saydamlık ilkesi, m.5) ve gerekirse mahkemece celp yoluna gidilir.
3. **İspat yükü:** Kural olarak işlemi tesis eden idare dayandığı sebebi ve belgeyi ortaya koyar; yeterliğini/teklifinin uygunluğunu iddia eden istekli ise ilgili belgeyi sunmuş olmalıdır. Aşırı düşük açıklamasında ispat yükü açıklamayı sunan isteklidedir.
4. **Gizlilik dengesi (m.5, m.61):** Diğer isteklilerin ticari sır niteliğindeki bilgileri korunur; itirazen şikâyette KİK dosya üzerinden inceleme yapar.
5. **Ara sonuç:** İddia-delil eşleştirmesi yapılır; eksik delil için temin yolu (idareden talep, EKAP, mahkeme celbi) planlanır.

İspat yükü: Yukarıdaki dağılıma göre her iddia somut belgeye bağlanır.

## Çıktı modülleri
- İddia-delil eşleştirme tablosu.
- Eksik belge ve temin yolu listesi.
- EKAP/işlem dosyası kayıt dizini.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

