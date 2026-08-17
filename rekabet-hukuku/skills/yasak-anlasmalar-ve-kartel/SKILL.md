---
argument-hint: ''
description: Fiyat tespiti, bölge/müşteri paylaşımı, ihalede danışıklılık, bilgi paylaşımı
  veya teşebbüs birliği kararı gibi rekabeti sınırlayıcı koordinasyon iddialarını
  4054 m.4 çerçevesinde değerlendirmek isten
name: yasak-anlasmalar-ve-kartel
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
  - ad: Rekabetin Korunması Hakkında Kanun
    numara: '4054'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yasak Anlaşmalar, Uyumlu Eylem ve Kartel (m.4)

## Görev
Teşebbüsler arası bir anlaşma, uyumlu eylem veya teşebbüs birliği kararının 4054 m.4 kapsamında rekabeti sınırlayıp sınırlamadığını; amaç mı yoksa etki bakımından mı ihlal oluşturduğunu ve muafiyet ihtimalini değerlendirmek.

## Soğuk başlangıç (intake)
- Taraflar yatay (rakip) mı, dikey (sağlayıcı-alıcı) mı?
- Koordinasyon konusu: fiyat, miktar, pazar/müşteri paylaşımı, ihale, ortak satınalma, bilgi değişimi?
- Yazılı bir anlaşma mı var, yoksa paralel davranış/temas mı söz konusu?
- Bir dernek/birlik kararı veya tavsiyesi var mı?

## Denetim şeması
1. **Çoklu irade unsuru (m.4)** — anlaşma, uyumlu eylem veya teşebbüs birliği kararı tespit edilir. Uyumlu eylemde doğrudan irade beyanı aranmaz; bilinçli paralellik + rasyonel açıklama yokluğu yeterli olabilir. Uyumlu eylem karinesi piyasa koşullarına dayalı ispatı kolaylaştırır.
2. **Rekabeti sınırlama** — açık/sert ihlaller (kartel: fiyat tespiti, bölge-müşteri paylaşımı, arz kısıtlama, ihalede danışıklı teklif) **amaç bakımından** ihlaldir; ayrıca etki analizi gerekmez. Diğer kısıtlamalarda ilgili pazarda fiili/olası etki gösterilmelidir.
3. **Dikey ilişki süzgeci** — dikey anlaşmalarda Dikey Anlaşmalara İlişkin Grup Muafiyeti Tebliği'ne (2002/2) bakılır; pazar payı eşiği aşılmıyor ve ağır kısıtlama (yeniden satış fiyatının tespiti vb.) yoksa grup muafiyeti uygulanır.
4. **De minimis** — De Minimis Tebliği kapsamında pazar payı eşiklerinin altında ve açık ihlal niteliği taşımayan anlaşmalar soruşturma dışı bırakılabilir; kartel buna dâhil değildir.
5. **Muafiyet (m.5)** — grup muafiyeti dışında kalan anlaşmada dört şart birlikte aranır; ispat yükü teşebbüstedir.
6. **Yaptırım ve pişmanlık** — kartel ihlalinde ciro üzerinden idari para cezası (m.16); Pişmanlık (Kartel) Yönetmeliği ile ilk başvurana ceza muafiyeti/indirimi imkânı; özel hukukta üç kat tazminat (m.57-58).

## Çıktı modülleri
- Anlaşma/eylem nitelendirmesi ve amaç-etki ayrımı notu.
- Grup muafiyeti / de minimis / bireysel muafiyet kontrol listesi.
- Risk ve ceza tahmini; pişmanlık başvurusu uygunluk değerlendirmesi.
- Delil zayıflık/güçlülük haritası ve doğrulanacak Kurul kararı atıfları `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

