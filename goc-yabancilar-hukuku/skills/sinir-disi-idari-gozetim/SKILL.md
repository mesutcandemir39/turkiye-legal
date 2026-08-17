---
argument-hint: ''
description: Yabancı hakkında sınır dışı etme (deport) kararı veya idari gözetim kararı
  verildiğinde; kararın hukuka uygunluğunu, geri gönderme yasağını ve dava/itiraz
  sürelerini denetlemek için kullanılır.
name: sinir-disi-idari-gozetim
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
  - ad: Yabancılar ve Uluslararası Koruma Kanunu
    numara: '6458'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Sınır Dışı Etme ve İdari Gözetim

## Görev
Sınır dışı etme ve idari gözetim kararlarını YUKK çerçevesinde denetlemek, sınır dışı edilemeyecekler ve geri gönderme yasağı korumalarını tespit etmek, kısa dava/itiraz sürelerini kaçırmadan yürütmeyi durdurmak.

## Soğuk başlangıç (intake)
1. Sınır dışı kararının tebliğ tarihi ve gerekçesi (hangi YUKK m.54 fıkrası) nedir?
2. İdari gözetim kararı var mı; gözetim başlangıç tarihi ve geri gönderme merkezi neresi?
3. Yabancı koruma başvurusu yaptı mı, ailesi/çocuğu Türkiye'de mi, sağlık durumu nedir?
4. Geri dönüşte yaşam/işkence riski var mı (m.55 / AİHS m.3)?

## Denetim şeması
1. **Sınır dışı sebebi**: YUKK m.54 — hangi fıkraya dayanıldığı (kamu düzeni/güvenliği, vize-ikamet ihlali, çalışma izni olmadan çalışma, terör/örgüt irtibatı vb.) ve maddi dayanağı denetlenir.
2. **Sınır dışı edilemeyecekler**: m.55 — geri gönderildiğinde ölüm cezası/işkence/insanlık dışı muamele riski, ciddi sağlık/yaş/gebelik, insan ticareti veya şiddet mağduru durumu. Bu haller mutlak engel oluşturabilir.
3. **Karara karşı dava**: Sınır dışı kararına karşı idare mahkemesine dava — kısa hak düşürücü süre (m.53); dava açılması halinde kural olarak işlem yürütülmez (geri gönderme yasağının usulî güvencesi). Süre titizlikle hesaplanır.
4. **İdari gözetim**: m.57 — valilik kararıyla, geri gönderme merkezinde; süre sınırı ve uzatma rejimi, aylık değerlendirme. Gözetime karşı sulh ceza hâkimliğine itiraz (m.57/6); hâkim kararı kesindir, ancak şartlar değişirse yeniden başvuru mümkündür.
5. **Alternatif yükümlülükler**: m.57/A — gözetim yerine ikamet zorunluluğu, bildirim, teminat gibi tedbirler.
**İspat yükü**: Sınır dışı sebebinin varlığını idare ispatlar; m.55 koruması ve riski yabancı somut delil/anlatıyla ortaya koyar. Tereddütte geri gönderme yasağı lehe işler.

## Çıktı modülleri
- Süre hesap tablosu (tebliğ → dava/itiraz son günü).
- Sınır dışına karşı iptal davası ve YD/yürütülmeme talebi dilekçesi.
- İdari gözetime karşı sulh ceza hâkimliği itiraz dilekçesi iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

