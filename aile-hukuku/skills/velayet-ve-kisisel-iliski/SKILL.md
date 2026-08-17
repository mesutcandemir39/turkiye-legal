---
argument-hint: ''
description: Velayetin hangi tarafa verileceği, kişisel ilişki (görüş) düzeninin kurulması,
  velayetin değiştirilmesi veya kaldırılması ve çocuğun üstün yararının somutlaştırılması
  gerektiğinde kullanılır.
name: velayet-ve-kisisel-iliski
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  - ad: Ailenin Korunması ve Kadına Karşı Şiddetin Önlenmesine Dair Kanun
    numara: '6284'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Velayet ve Çocukla Kişisel İlişki

## Görev
Çocuğun üstün yararı ölçütüyle velayetin tevdii (TMK m.182, m.336), kişisel ilişki düzeninin (m.182-183, m.323-324) kurulması ve velayetin değiştirilmesi/kaldırılması şartlarının denetlenmesi.

## Soğuk başlangıç (intake)
1. Çocuğun yaşı, sağlık/eğitim durumu ve kiminle, nerede yaşadığı nedir?
2. Ebeveynlerin bakım kapasitesi, çalışma düzeni ve çocukla bağı nasıl?
3. İhmal, şiddet, bağımlılık, çocuğun kaçırılması gibi bir risk var mı?
4. İstenen kişisel ilişki sıklığı (hafta içi/sonu, yarıyıl, yaz, dini bayram) nedir?

## Denetim şeması
1. **Velayetin tevdii.** Evlilik içinde velayet ana-baba tarafından birlikte kullanılır (m.336/1); boşanmada hâkim çocuğu velayeti kendisine bırakılmayan taraf ile kişisel ilişki dahil düzenler (m.182). Ölçüt münhasıran **çocuğun üstün yararıdır**; ekonomik üstünlük tek başına belirleyici değildir. İdrak çağındaki çocuğun görüşü alınır (BM Çocuk Hakları Sözleşmesi m.12; uygulamada pedagog/uzman raporu).
2. **Kişisel ilişki düzeni.** m.182-183, m.323: velayet kendisinde olmayan taraf ile çocuk arasında somut, uygulanabilir bir takvim kurulur; ana-babadan başka kişilerle (örn. büyükanne-baba) kişisel ilişki m.325.
3. **Değiştirme/kaldırma.** Durumun değişmesi (m.183) — örn. velayet sahibinin ağır ihmali, başka yere yerleşmesi, çocuğun yararının zedelenmesi — velayetin değiştirilmesini gerektirebilir. Ağır hallerde velayetin kaldırılması (m.348) ve çocuğun korunmasına ilişkin tedbirler (m.346-347).
4. **İcra ve uluslararası boyut.** Kişisel ilişki kararlarının yerine getirilmesinde teslim/kişisel ilişki tesisi ADM (Adalet Bakanlığı/müdürlük) ve 5395 sK. ile ilgili mekanizmalar; çocuk kaçırma hallerinde 1980 Lahey Sözleşmesi.
5. **Ara sonuç.** Velayet önerisi + kişisel ilişki takvimi + risk/koruma tedbiri değerlendirmesi.

## Çıktı modülleri
- Üstün yarar değerlendirme matrisi (bakım, istikrar, bağ, risk).
- Somut kişisel ilişki takvimi taslağı.
- Velayetin değiştirilmesi/kaldırılması için dayanak ve delil listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

