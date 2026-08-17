---
argument-hint: ''
description: Bir karara dayanılırken onun mahkemeleri ne ölçüde bağladığı tartışıldığında;
  içtihadı birleştirme kararı, genel kurul, daire ve AYM kararlarının bağlayıcılık
  hiyerarşisini belirlemek için kullanılır.
name: ictihat-baglayiciligi-ibk-ve-aym
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# İçtihat Bağlayıcılığı (İBK, HGK, AYM)

## Görev
Bir yargı kararının somut uyuşmazlıkta ne kadar ağırlık taşıdığını — bağlayıcı mı yoksa yalnızca ikna edici mi olduğunu — doğru sınıflandırmak ve buna göre güç atfetmek.

## Soğuk başlangıç (intake)
- Karar hangi merciden: İBK, HGK/İDDK/VDDK, daire, BAM/BİM mi?
- Konu AYM norm denetimi veya bireysel başvuru kararına mı dayanıyor?
- Karşı tarafın dayandığı içtihat ile çatışan başka karar var mı?
- Karardan sonra mevzuat veya içtihat değişmiş mi?

## Denetim şeması
1. **AYM kararları** — Anayasa m.153/son: bağlayıcı (herkesi bağlar). Norm denetimi kararı iptal ettiği hükmü ortadan kaldırır; bireysel başvuruda ihlal kararı yeniden yargılama yolu açabilir. En üst değer.
2. **İçtihadı Birleştirme Kararı (İBK)** — Yargıtay Kanunu m.45: benzer hukuki konularda Yargıtay genel kurullarını, dairelerini ve mahkemeleri bağlar. Daireler arası çelişkiyi giderir; daire kararından üstündür.
3. **Genel Kurul (HGK / Ceza GK / İDDK / VDDK)** — Bağlayıcı değil ama daire kararından ağır basan, yön gösterici emsal; direnme kararlarında belirleyici.
4. **Daire kararı** — İkna edici emsal (Anayasa m.138/1: hâkim yalnız hukuka bağlı). "Yerleşik içtihat" demek için birden çok, istikrarlı, güncel karar gerekir.
5. **BAM/BİM (istinaf)** — Bölgesel emsal değeri; ülke çapında bağlayıcılığı yoktur, daireler arasında farklılaşabilir.
6. **Çatışma ve güncellik** — Çelişen kararlarda hiyerarşi (İBK > GK > daire) ve tarih gözetilir; eski karar, sonraki kanun değişikliği veya İBK ile aşılmış olabilir.

## Çıktı modülleri
- Karar → bağlayıcılık sınıfı eşlemesi.
- "Yerleşik içtihat" iddiası için yeterlilik kontrolü.
- Çatışan içtihat varsa öncelik/tarih analizi.
- Güç atfı önerisi (bağlar / güçlü emsal / tek görüş) + `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

