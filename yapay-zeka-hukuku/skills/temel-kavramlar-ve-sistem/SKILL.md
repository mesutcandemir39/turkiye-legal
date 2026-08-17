---
argument-hint: ''
description: Yapay zekâ içeren bir dosyayı katman (veri-KVKK, sözleşme, sorumluluk,
  fikri mülkiyet, sektörel), sistemin rolü (karar destek, tam otomatik karar, üretken
  model, profilleme) ve tarafların sıfatı eksen
name: temel-kavramlar-ve-sistem
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yapay Zekâ Hukuku Temel Kavramlar ve Sistematik

## Görev
Yapay zekâ unsuru içeren dosyayı doğru hukuki katmana oturtmak; Türkiye'de yatay bir YZ kanunu bulunmadığını dikkate alarak uygulanacak norm setini (KVKK 6698, TBK 6098, FSEK/SMK, sektörel) ve görevli mercii hızlıca tespit ederek sonraki uzman becerilere giriş kapısını açmak.

## Soğuk başlangıç (intake)
1. Sistem ne yapıyor: karar destek mi, tam otomatik karar mı, üretken model (metin/görüntü) mü, profilleme/skorlama mı?
2. Müvekkilin sıfatı: model geliştiren/sağlayan, sistemi kullanan (deployer), veri sorumlusu/işleyen, zarar gören/ilgili kişi mi?
3. Coğrafi erişim: sistem AB'deki kişilere ürün/hizmet sunuyor mu (AB Tüzüğü/GDPR riski)?
4. Uyuşmazlık türü: veri/KVKK uyumu mu, sözleşmesel mi, tazminat mı, fikri mülkiyet mi, kamu işlemi mi?

## Denetim şeması
1. **Katman tespiti**: Kişisel veri işleniyorsa KVKK (m.4 ilkeler, m.5-6 şartlar) devrede; otomatik kararla aleyhe sonuç varsa m.11/1-g; sözleşmesel ilişki varsa TBK 6098; zarar varsa haksız fiil (TBK m.49 vd.) veya kusursuz sorumluluk (m.66, m.71); içerik/eser üretimi varsa FSEK/SMK. Ara sonuç: hangi norm seti baskın.
2. **Sistemin rolü**: Tam otomatik karar mı (insan denetimi yok), insan onaylı karar destek mi? Bu ayrım KVKK m.11 itiraz hakkını ve sorumluluk dağılımını belirler.
3. **Yer/uygulama**: AB pazarına dokunuyorsa AB Yapay Zekâ Tüzüğü 2024/1689 ve GDPR m.22 doğrudan; yalnız Türkiye ise bu metinler karşılaştırmalı kaynaktır, bağlayıcı değildir. Müvekkile bunu açıkça belirt.
4. **Görevli merci**: KVKK ihlalinde Kurul (m.14) ve sulh/asliye hukuk; tüketici işleminde tüketici mahkemesi/hakem heyeti; kamu otomatik işleminde idari yargı (İYUK); fikri hakta FSHM.
5. **Tarih kilidi**: KVKK m.9 aktarım rejimi ve ceza tutarları değişti; olay tarihini sabitle.

## Çıktı modülleri
- Dosya konumlandırma notu (katman + sistemin rolü + norm seti).
- Uygulanır/karşılaştırmalı norm ayrımı (KVKK/TBK vs. AB Tüzüğü).
- Görevli merci ve hangi uzman beceriye geçileceğine dair yönlendirme.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

