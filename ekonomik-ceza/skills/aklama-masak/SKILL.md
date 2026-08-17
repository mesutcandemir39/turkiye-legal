---
argument-hint: ''
description: Suçtan kaynaklanan malvarlığı değerlerini aklama (TCK m.282) iddiası,
  öncül suç tartışması, MASAK şüpheli işlem bildirimi ve yükümlü sorumluluğu söz konusu
  olduğunda; aklama soruşturmasında savunma ve
name: aklama-masak
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Kaçakçılıkla Mücadele Kanunu
    numara: '5549'
    tur: kanun
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Aklama (Kara Para) ve MASAK Yükümlülükleri

## Görev
TCK m.282 aklama suçunun unsurlarını öncül suç ekseninde denetlemek; 5549 sayılı Kanun kapsamında yükümlü (banka, aracı kurum, gerçek/tüzel kişi) sorumluluğunu ve MASAK sürecini ele almak.

## Soğuk başlangıç (intake)
- Öncül (kaynak) suç ne, sabit mi, yoksa iddia mı?
- Hangi malvarlığı değeri, hangi işlemle "akladı" iddia ediliyor?
- Müvekkil yükümlü mü (banka/aracı kurum) yoksa fail mi konumunda?
- MASAK/şüpheli işlem bildirimi veya elkoyma kararı var mı?

## Denetim şeması
1. **Öncül suç (TCK m.282/1)**: Aklamanın ön şartı, malvarlığı değerinin "suçtan kaynaklanması"dır. Öncül suçun varlığı/kanıtı tartışılır; öncül suç sabit değilse aklama da sakatlanır. Öncül suçun kesin mahkûmiyeti şart değildir, ancak suç teşkil eden bir kaynak ortaya konmalıdır.
2. **Fiil**: Değeri "yurt dışına çıkarma" veya "gayrimeşru kaynağını gizleme/niteliğini değiştirme" fiilleri. Salt elde bulundurma yetmez; aklama fiili (gizleme/dönüştürme/aklamaya yönelik işlem) aranır.
3. **Manevi unsur**: Kast; failin değerin suçtan kaynaklandığını bilmesi (TCK m.21).
4. **Nitelikli haller ve etkin pişmanlık**: TCK m.282/3 (kamu görevlisi/belli meslek) ve m.282/6 etkin pişmanlık (soruşturma başlamadan önce değerlerin teslimi) kontrol edilir.
5. **Yükümlü sorumluluğu**: 5549 sayılı Kanun — müşterini tanı, şüpheli işlem bildirimi (ŞİB), muhafaza-ibraz. İhlal idari para cezası doğurur; ŞİB'in gizliliği (ifşa yasağı) önemlidir.
6. **Elkoyma/müsadere**: CMK m.128 (taşınmaz, hak, alacak) ve TCK m.54-55 müsadere; aklama dosyalarının ekonomik ağırlığı buradadır.
7. **Ara sonuç**: Öncül suç-aklama bağı, aklama fiilinin gerçekliği, kast ve yükümlülük ihlali ayrı ayrı değerlendirilir.

## Çıktı modülleri
- Öncül suç-aklama bağ analizi
- Fiil tipi (gizleme/dönüştürme/yurt dışı) nitelendirmesi
- Yükümlü uyum/ihlal değerlendirmesi
- Elkoyma-müsadere risk notu
- Savunma veya etkin pişmanlık stratejisi taslağı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

