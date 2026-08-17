---
argument-hint: ''
description: Davanın doğru görevli ve yetkili mahkemede açılıp açılmadığını, görevsizlik-yetkisizlik
  veya gönderme riskini denetlemek gerektiğinde kullan.
name: gorev-ve-yetki-kontrolu
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Görev ve Yetki Kontrolü

## Görev
Dosyanın görevli mahkeme (dava konusuna göre) ve yetkili mahkeme (yer itibarıyla) bakımından doğru yerde olup olmadığını denetlemek; görevsizlik/yetkisizlik ile zaman kaybı riskini erken yakalamak.

## Soğuk başlangıç (intake)
- Dava konusu ve türü ne (alacak, tazminat, tüketici, iş, ticari, aile)?
- Dava hangi mahkemede ve hangi yerde açılmış?
- Taraflar arasında yetki sözleşmesi veya tahkim şartı var mı?
- Kesin yetki gerektiren bir dava türü söz konusu mu?

## Denetim şeması
1. Görev: HMK m.1 gereği görev kamu düzenindendir ve re'sen incelenir. Genel görevli asliye hukuk (HMK m.2) ile özel görevli mahkemeleri ayırt et: tüketici mahkemesi (6502 TKHK m.73), iş mahkemesi (7036 m.5), ticari dava-asliye ticaret (TTK m.4-5), aile mahkemesi, FSHM. Yanlış görevli mahkeme → görevsizlik kararı ve gönderme.
2. Yetki: genel yetki davalının yerleşim yeri (HMK m.6); özel/kesin yetki halleri (taşınmazda taşınmazın yeri HMK m.12; sözleşmede ifa yeri HMK m.10; haksız fiilde HMK m.16). Kesin yetki re'sen gözetilir.
3. Yetki sözleşmesi/tahkim: tacir-kamu tüzel kişisi arasında yetki sözleşmesi (HMK m.17) geçerli mi; tahkim şartı varsa tahkim ilk itirazı (HMK m.116) riski.
4. İtiraz zamanı: yetki ilk itirazdır, cevap süresinde ileri sürülmezse düşer (HMK m.116, m.117, m.19); görev her aşamada gözetilir.
5. Ara sonuç: görev/yetki uygun mu, değilse hangi mahkemeye gönderme ve süre etkisi. Mevzuat dışı varsayım yapılmaz.

## Çıktı modülleri
- Görev/yetki değerlendirme notu (doğru mahkeme + dayanak madde).
- Görevsizlik/yetkisizlik riski ve gönderme senaryosu.
- İtiraz süresi ve usul uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

