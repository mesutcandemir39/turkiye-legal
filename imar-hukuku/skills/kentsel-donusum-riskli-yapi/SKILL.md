---
argument-hint: ''
description: 6306 sayılı Kanun kapsamında riskli yapı/alan tespiti, tahliye ve yıktırma,
  malik kararı çoğunluğu ve dönüşüm uyuşmazlıkları gündeme geldiğinde; riskli yapı
  tespitine itiraz ve 2/3 çoğunluk süreci sor
name: kentsel-donusum-riskli-yapi
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
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kentsel Dönüşüm ve Riskli Yapı (6306)

## Görev
6306 sayılı Kanun kapsamındaki riskli yapı/alan sürecini denetlemek; tespite itiraz, malik kararı ve tahliye-yıktırma adımlarında hukuki yolu kurmak.

## Soğuk başlangıç (intake)
- Riskli yapı tespiti mı, riskli/rezerv alan ilanı mı var?
- Tespit raporu hangi lisanslı kuruluşça düzenlendi, tebliğ tarihi ne?
- Maliklerin dönüşüm/anlaşma çoğunluğu sağlandı mı?
- Tahliye ya da yıktırma kararı çıktı mı, kira/taşınma yardımı talebi var mı?

## Denetim şeması
1. **Riskli yapı tespiti (6306 m.3)**: Tespit, Bakanlıkça lisanslandırılmış kuruluşlarca yapılır ve tapuya şerh edilir. Maliklere tebliğ edilir; teknik dayanağın ve usulün denetimi ilk adımdır.
2. **Tespite itiraz**: Riskli yapı tespitine, tebliğden itibaren kanunda öngörülen sürede (15 gün) idareye itiraz edilebilir; itiraz teknik heyetçe incelenir. İdari sürecin tüketilmesi sonraki dava için önemlidir.
3. **Tahliye ve yıktırma (m.5)**: Riskli yapı maliklerce tahliye/yıktırılmazsa idarece yıktırılır; süreler ve idari yaptırım kademeli işler. Tahliye işlemine karşı idari yargı yolu açıktır.
4. **Malik kararı çoğunluğu (m.6)**: Yıkılan yapının arsası üzerinde yapılacak uygulamada **maliklerin hisseleri çoğunluğu (en az 2/3) ile karar** alınır; karara katılmayan maliklerin hisseleri Bakanlık marifetiyle satışa konu olabilir. Çoğunluk hesabı ve azınlık malik hakları denetlenir.
5. **Yargı kolu ve uyuşmazlık**: Riskli yapı tespiti ve idari işlemler → idari yargı (iptal); malikler arası dönüşüm sözleşmesi, müteahhit ilişkisi → adli yargı. 6306 işlemlerinde yürütmenin durdurulmasına ilişkin özel sınırlamalar gözetilir.
6. **İspat ve ara sonuç**: Tespit raporu, statik veriler, malik kararı tutanakları, sözleşmeler delildir. Teknik dayanak/usul sakatsa tespitin iptali; çoğunluk veya azınlık hakkı ihlali varsa ilgili dava. Mülkiyet hakkı (Anayasa m.35) AYM denetimi açısından değerlendirilir; künyeler `[DOĞRULANMADI]`.

## Çıktı modülleri
- Riskli yapı süreç kronolojisi.
- Tespit raporu/usul denetim notu.
- Malik çoğunluğu (2/3) ve azınlık hakkı analizi.
- Tespit/tahliye iptali veya dönüşüm sözleşmesi değerlendirme taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

