---
argument-hint: ''
description: Tapusuz ya da malik kaydı belirsiz/ölü taşınmazın uzun süreli zilyetlikle
  kazanılarak adına tescili istendiğinde; olağan (m.712) ve olağanüstü (m.713) kazandırıcı
  zamanaşımı şartları, süre, zilyetlik
name: kazandirici-zamanasimi-tescil
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
  - ad: Tapu Kanunu
    numara: '3402'
    tur: kanun
  - ad: Kat Özel Koşulu Olmak Üzere Yapılan Satış Mukavelelerine Dair Kanun
    numara: '2644'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kazandırıcı Zamanaşımı ve Tescil (TMK m.712-713)

## Görev
Zilyetliğe dayalı mülkiyet kazanımının şartlarını denetlemek ve uygun olduğunda tescil davasını kurmak; olağan ve olağanüstü zamanaşımı ile kadastro zilyetliğini (3402 m.14) ayırt etmek.

## Soğuk başlangıç (intake)
- Taşınmaz tapulu mu (kim adına) yoksa tapusuz mu; tapu varsa malik ölü/gaip/belirsiz mi?
- Zilyetlik kaç yıldır, kesintisiz ve davasız mı; malik sıfatıyla mı kullanılıyor?
- Taşınmazın niteliği (tarım, orman, mera, kıyı, kamu) ve yüzölçümü nedir?
- Zilyetlik miras/satış yoluyla devralındıysa önceki zilyetlikle birleştirme mümkün mü?

## Denetim şeması
1. **Olağan zamanaşımı (TMK m.712).** Bir taşınmaza tapuda malik görünen ancak tescili yolsuz olan kişi; davasız, aralıksız ve iyiniyetle 10 yıl zilyet kalırsa kazanımı geçerli sayılır. İyiniyet (TMK m.3) ve geçerli tescil görünüşü şarttır.
2. **Olağanüstü zamanaşımı (TMK m.713).** Tapuda kayıtlı olmayan veya maliki 20 yıl önce ölmüş/gaipliğine karar verilmiş ya da kim olduğu belirlenemeyen taşınmazda; davasız, aralıksız, malik sıfatıyla 20 yıl zilyetlik → mahkemeden tescil istenebilir. İyiniyet aranmaz; ilan ve itiraz prosedürü işletilir.
3. **İstisna arazileri ele.** Orman (kadastro/orman mevzuatı), kıyı (Kıyı Kanunu), mera/yaylak, kamu malları ve özel kanunla tescili yasak yerler zamanaşımıyla kazanılamaz. Nitelik tespiti dava şartı gibidir.
4. **Zilyetliği birleştir.** Zilyetlik, önceki zilyetten devren (miras/satış) geçmişse süreler eklenir (TMK m.996, m.700); ancak nitelik ve davasızlık tüm dönem için aranır.
5. **Husumet ve usul.** Davalı Hazine ve/veya ilgili idare; tapulu ise malik/mirasçıları. Tescil davasında ilan, keşif, yerel bilirkişi-tanık ve fen incelemesi yapılır.
6. **Kadastro paraleli.** Kadastro sırasında aynı zilyetlik 3402 m.14 ile tespit konusu olur; süre ve sınırlar (40 dönüm, vergi kaydı) burada uygulanır.
7. **Ara sonuç.** Hangi madde (712/713/3402-14), süre tamam mı, taşınmaz tescile elverişli mi.

## Çıktı modülleri
- Şart kontrol listesi (süre / davasızlık / malik sıfatı / iyiniyet / nitelik).
- Tescil davası dilekçe iskeleti (husumet, ilan talebi, keşif/bilirkişi talebi).
- Tescile engel nitelik (orman/kıyı/mera) risk notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

