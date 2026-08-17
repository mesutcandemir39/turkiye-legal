---
argument-hint: ''
description: Belirli erişim eşiğini aşan sosyal ağ sağlayıcılarının temsilci atama,
  içerik kaldırma başvurularını sonuçlandırma, raporlama, veri yerelleştirme ve bant
  genişliği daraltma riskine ilişkin uyum ve sav
name: sosyal-ag-saglayici-uyum
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
  - ad: Telekomunikasyon Kanunu
    numara: '5809'
    tur: kanun
  - ad: Elektronik Ticaretin Düzenlenmesine Dair Kanun
    numara: '5651'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Sosyal Ağ Sağlayıcı Yükümlülükleri ve Uyum

## Görev
Bir platformun 5651 anlamında sosyal ağ sağlayıcı sayılıp sayılmadığını ve buna bağlı temsilci, raporlama, başvuru yanıtlama ve veri yükümlülüklerini denetleyerek uyum programı kurmak veya yaptırıma karşı savunma hazırlamak.

## Soğuk başlangıç (intake)
1. Platform Türkiye'den günlük erişim/kullanıcı eşiğini (ilgili düzenlemedeki sayısal eşik) aşıyor mu?
2. Türkiye'de temsilci (gerçek/tüzel kişi) atandı mı, BTK'ya bildirildi mi?
3. İçerik kaldırma/erişim engelleme başvuruları süresinde yanıtlanıyor mu?
4. Şeffaflık/uygulama raporları yayımlanıyor mu; bir BTK bildirimi/yaptırımı var mı?

## Denetim şeması
1. **Kapsam tespiti**: 5651 sosyal ağ sağlayıcı düzenlemesi (7253 s.K. ile getirilen rejim ve ek değişiklikler) — Türkiye'den belirli günlük erişim eşiğini aşan platformlar kapsamdadır. Ara sonuç: platform kapsamda mı (tarih kilidi: eşik ve yükümlülükler değişti).
2. **Temsilci yükümlülüğü**: Türkiye'de yetkili temsilci atama ve BTK'ya bildirme; temsilci atanmaması kademeli yaptırım (idari para cezası, reklam yasağı ve nihayetinde bant genişliği daraltma/erişim kısıtı) doğurur.
3. **Başvuru ve süre**: m.9 ve m.9/A kapsamındaki içerik kaldırma başvurularını yasal süre içinde (kural olarak 48 saat) yanıtlama ve gerekçeli cevap verme; reddedilen başvurularda yargı yolunun açık tutulması.
4. **Raporlama ve veri**: Düzenli şeffaflık/uygulama raporu; Türkiye'deki kullanıcı verilerinin yurt içinde barındırılmasına yönelik düzenleme ve KVKK aktarım kuralları (6698 m.9) birlikte değerlendirilir.
5. **Kademeli yaptırım ve savunma**: Yükümlülük ihlalinde BTK kademeli yaptırım uygular; her aşama ayrı idari işlemdir ve İYUK m.7 süresinde iptal davası ile m.27 yürütmenin durdurulması istemine konu edilir. Ölçülülük ve ifade özgürlüğü dengesi savunmada esastır.

İlkesel içtihat için BTK yaptırımlarında karararama.danistay.gov.tr, temel hak boyutunda kararlarbilgibankasi.anayasa.gov.tr taranır; künye [DOĞRULANMADI] işaretlenir.

## Çıktı modülleri
- Sosyal ağ uyum kontrol listesi (temsilci/raporlama/başvuru/veri).
- Yaptırıma karşı savunma ve iptal davası iskeleti.
- Başvuru yanıtlama akış ve süre takvimi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

