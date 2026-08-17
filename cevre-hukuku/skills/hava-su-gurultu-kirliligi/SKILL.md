---
argument-hint: ''
description: Emisyon, atıksu deşarjı, hava kalitesi ve çevresel gürültü kaynaklı kirlilik
  iddialarında, limit aşımı tespitinde ve komşuluk hukuku ile kesişen rahatsızlık
  uyuşmazlıklarında; ölçüm ve numune usulünün
name: hava-su-gurultu-kirliligi
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
  - ad: Çevre Kanunu
    numara: '2872'
    tur: kanun
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Hava, Su ve Gürültü Kirliliği

## Görev
Hava emisyonu, su deşarjı ve çevresel gürültü kaynaklı kirlilik iddialarını sınır değerler ve ölçüm usulü üzerinden denetlemek; idari yaptırım, faaliyet durdurma ve özel hukuk taleplerini birlikte ele almak.

## Soğuk başlangıç (intake)
1. Hangi unsur: hava emisyonu, atıksu deşarjı, içme/yüzey suyu, çevresel gürültü?
2. Limit aşımı iddiası hangi ölçüme dayanıyor; ölçümü kim, hangi yöntemle yaptı?
3. Etkilenen taraf var mı (komşu tesis, yerleşim, sulak alan)?
4. Talep idari yaptırım mı, faaliyet durdurma mı, tazminat/el atma mı?

## Denetim şeması
1. **Sınır değerler**: Sanayi Kaynaklı Hava Kirliliğinin Kontrolü ve Su Kirliliği Kontrolü Yönetmelikleri ile Çevresel Gürültü Yönetmeliği sektörel limitleri belirler; 2872 m.8 ve m.11 kirletme yasağı ve arıtma yükümlülüğünün dayanağıdır.
2. **Ölçüm/numune usulü**: Numunenin akredite laboratuvarca, usulüne uygun alınması ve zincirin korunması esastır; usulsüz ölçüm hem yaptırımı hem de iddiayı çürütür.
3. **İdari sonuç**: Limit aşımında 2872 m.20-23 idari para cezası ve m.15 faaliyet durdurma uygulanır; tekerrür ağırlaştırıcıdır.
4. **Özel hukuk kesişimi**: Sürekli kirlilik/rahatsızlık komşuluk hukukunda el atmanın önlenmesi (TMK m.683, m.737 katlanma sınırı) ve TBK m.49 vd. tazminat talebi doğurabilir; görevli mahkeme adli yargıdır.
5. **İspat ve ara sonuç**: Bilirkişi, keşif ve karşı ölçüm belirleyicidir; ölçümler arasındaki çelişki ek/yeniden bilirkişiyi gerektirir.

## Çıktı modülleri
- Limit aşımı tespit tablosu (parametre + sınır + ölçüm)
- Ölçüm/numune usul denetim notu
- İdari yaptırım ve özel hukuk talep ayrımı
- Bilirkişi/keşif delil planı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

