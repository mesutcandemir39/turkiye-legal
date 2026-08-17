---
argument-hint: ''
description: Konut/iş yeri/üst aramasının, el koymanın ve iletişimin/teknik araçlarla
  izlemenin hukuka uygunluğunu denetlemek ve buradan elde edilen delillerin geçerliliğini
  değerlendirmek gerektiğinde kullanılır.
name: arama-el-koyma-iletisim
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
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Arama, El Koyma ve İletişimin Denetlenmesi

## Görev
Arama, el koyma ve iletişim denetimi tedbirlerinin karar, kapsam ve usul yönünden hukuka uygunluğunu denetlemek; bu yolla elde edilen delillerin kullanılabilirliğini değerlendirmek.

## Soğuk başlangıç (intake)
- Arama nerede yapıldı (konut, iş yeri, üst, araç) ve karar var mıydı?
- Arama gece mi gündüz mü; ihtiyar heyeti/komşu tanık hazır mıydı (m.119)?
- Neye el konuldu; el koymaya hâkim onayı alındı mı?
- İletişim denetimi/teknik takip kararı hangi suçtan ve hangi süreyle verildi?
- Elde edilen delil dosyada hükme esas mı alınıyor?

## Denetim şeması
1. **Arama kararı.** Kural olarak hâkim kararı; gecikmesinde sakınca varsa savcı, savcıya ulaşılamıyorsa kolluk amirinin yazılı emriyle yapılır (CMK m.116, m.119). Karar/emir aramanın konusunu, kapsamını ve sebebini içermelidir.
2. **Usul güvenceleri.** Konut ve iş yeri araması kural olarak gündüz; gece sınırlamaları ve hazır bulunacaklar m.118-120'de düzenlenir. İlgilinin gösterdiği belge müsadereye tabi değilse aleyhe kullanılamaz.
3. **El koyma.** Suç delili eşyaya el konulur; hâkim kararı esastır, gecikmesinde sakınca olan halde savcı/kolluk el koyar ve 24 saat içinde hâkim onayına sunar, hâkim 48 saat içinde karar verir (m.123-127). Avukat bürosu (m.130), basılı eser, postada el koyma için özel rejim vardır.
4. **İletişimin denetlenmesi.** Sadece katalog suçlarda, başka yolla delil elde imkânı yoksa, kuvvetli şüphe sebepleri varsa hâkim/gecikmede savcı kararıyla, azami sürelerle uygulanır (m.135). Tesadüfen elde edilen deliller m.138 sınırına tabidir.
5. **Yaptırım.** Hukuka aykırı arama/el koyma/dinleme ile elde edilen delil hükme esas alınamaz (m.206/2-a, m.217/2; Anayasa m.38/6). Zehirli ağacın meyvesi tartışması burada yürütülür.
6. **Ara sonuç.** Karar/onay/kapsam eksikse delil dışlanması talebi; geçerliyse delilin içeriği değerlendirmesine geçilir.

## Çıktı modülleri
- Tedbir başına hukuka uygunluk denetim tablosu (karar-kapsam-süre-onay).
- Delilin hükümden çıkarılması (dışlama) talebi gerekçesi.
- El konulan eşyanın iadesi talebi taslağı (m.131).
- İhlal tespit edilen güvencelerin maddeyle eşlenmiş listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

