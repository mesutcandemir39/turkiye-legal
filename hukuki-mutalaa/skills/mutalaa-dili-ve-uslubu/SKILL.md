---
argument-hint: ''
description: Hukuki görüşün tarafsız, gerekçeli ve ikna edici biçimde yazılmasını,
  olasılık dilinin ve atıf düzeninin doğru kullanılmasını sağlamak gerektiğinde kullanılır;
  mütalaayı dava dilekçesi üslubundan ayır
name: mutalaa-dili-ve-uslubu
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


# Mütalaa Dili ve Üslubu

## Görev
Mütalaa metnini analitik, dengeli ve ikna edici bir hukukçu diliyle kaleme almak; abartılı taraf-savunucu üsluptan ve sahte kesinlikten kaçınmak. Mütalaanın inandırıcılığı gerekçenin şeffaflığından gelir.

## Soğuk başlangıç (intake)
- Metin dava dosyasına mı girecek (HMK m.293 uzman görüşü), yoksa iç danışmanlık mı?
- Okuyucu hâkim/hukukçu mu, yoksa hukukçu olmayan müvekkil mi?
- İstenen uzunluk/derinlik seviyesi ne?
- Hassas/gizli bilgi içeriyor mu?

## Denetim şeması
1. Üslup seçimi: Dava içi uzman görüşünde tarafsız-bilimsel ton zorunludur; danışmanlık mütalaasında aleyhe senaryo açıkça tartılır. Her iki halde de "kazanırsınız" gibi kategorik vaatlerden kaçınılır.
2. Olasılık dili: Sonuçlar derecelendirilir — "kuvvetle muhtemel / tartışmalı / zayıf ihtimal / hâkimin takdirine bağlı". Belirsizlik gizlenmez, dürüstçe ifade edilir.
3. Gerekçe görünürlüğü: Her sonuç önermesi norm + altlama + (varsa) içtihada bağlanır; "kanaatimce" denip geçilmez, gerekçe yazılır.
4. Atıf düzeni: Mevzuat madde/fıkra/bent ile (ör. "TBK m.49/1", "HMK m.119/1-ğ"); içtihat künyesi doğrulanmadıysa `[DOĞRULANMADI]`; doktrin yazar-eser-sayfa. Model hafızasından karar numarası yazılmaz.
5. Yapı disiplini: Başlıklandırma, numaralı alt sorular, ara sonuçların belirginleştirilmesi; uzun paragraflar yerine izlenebilir akış.
6. Yer tutucu disiplini: Eksik bilgi `[doldurulacak: ...]`, doğrulanacak künye `[DOĞRULANMADI]` ile işaretlenir; uydurma veriyle boşluk kapatılmaz.

## Çıktı modülleri
- Üsluba uygun yazılmış değerlendirme metni
- Olasılık dili kontrol listesi
- Atıf formatı denetimi (mevzuat/içtihat/doktrin)
- Yer tutucu ve `[DOĞRULANMADI]` envanteri



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

