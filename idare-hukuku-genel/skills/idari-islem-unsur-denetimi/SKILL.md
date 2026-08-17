---
argument-hint: ''
description: Bir idari işlemin hukuka uygunluğunu yetki-şekil-sebep-konu-maksat unsurları
  üzerinden denetlemek ve sakatlık (yokluk/iptal) hallerini tespit etmek için kullanılır;
  iptal davası gerekçesi kurarken baş
name: idari-islem-unsur-denetimi
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İdari İşlemin Unsurları ve Sakatlık Denetimi

## Görev
İdari işlemi beş unsur üzerinden adım adım denetleyerek hukuka aykırılıkları tespit etmek ve iptal sebeplerini somut dayanaklarla kurmak. Bu beceri iptal davasının maddi çekirdeğini üretir.

## Soğuk başlangıç (intake)
1. İşlemin tam metni, dayanağı (kanun/yönetmelik maddesi) ve gerekçesi elinde mi?
2. İşlemi tesis eden makam ve imza yetkisi/devri belli mi?
3. İşlemden önce alınması gereken görüş, savunma, kurul kararı var mıydı?
4. İşlemin maddi ve hukuki sebepleri dosyada gösterilmiş mi?

## Denetim şeması
1. **Yetki.** Kişi (doğru makam mı, yetki devri/imza devri usulüne uygun mu), yer, zaman ve konu bakımından yetki. Yetkisizlik ağırsa **yokluk**; aksi halde iptal sebebidir. Fonksiyon gaspı/yetki gaspı yokluk doğurur.
2. **Şekil.** Yazılılık, gerekçe gösterme, başvuru yollarının bildirilmesi, kurul ise toplantı/karar nisabı. Savunma alınması gereken hallerde (özellikle yaptırım işlemleri) savunma alınmamışsa esaslı şekil sakatlığı. Anayasa m.40 başvuru yollarının gösterilmesi.
3. **Sebep.** İşlemin dayandığı maddi olay ve hukuki neden gerçek, doğru ve ilgili kuralın aradığı nitelikte mi? Sebebin hiç bulunmaması veya yanlış nitelendirme iptal sebebidir; maddi olayın gerçekliği re'sen araştırılır (İYUK m.20).
4. **Konu.** İşlemin doğurduğu hukuki sonuç, kanunun öngördüğü sonuç mu? İmkânsız/kanuna aykırı konu sakatlık doğurur.
5. **Maksat (amaç).** İşlem kamu yararı amacıyla mı tesis edilmiş? Yetki saptırması (başka amaç, kişisel/siyasi saik) iptal sebebidir.
6. **Takdir yetkisi denetimi.** Bağlı yetki yoksa idarenin takdiri; ancak takdir eşitlik, ölçülülük (Anayasa m.13) ve kamu yararı ile sınırlıdır; sınır aşımı denetlenir.
7. **Ara sonuç ve ispat.** Her unsur için "uygun/sakat" ve dayanak. İspat yükü kural olarak işlemin hukuka uygunluğunu belgeleyecek idarededir; davacı somut aykırılık iddiasını ortaya koyar.

## Çıktı modülleri
- Beş unsur denetim tablosu (uygun/sakat + dayanak + delil).
- Yokluk/iptal nitelendirmesi.
- İptal dilekçesi için hukuki sebepler listesi.
- Eksik belge ve ek bilgi talebi notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

