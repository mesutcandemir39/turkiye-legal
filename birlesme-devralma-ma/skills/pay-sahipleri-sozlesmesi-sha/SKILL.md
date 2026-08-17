---
argument-hint: ''
description: Devralma sonrası ortaklık ilişkisini, yönetim ve oy haklarını, çıkış
  mekanizmalarını (tag/drag, ön alım) ve azınlık korumalarını düzenleyen pay sahipleri
  sözleşmesini tasarlamak için kullanılır.
name: pay-sahipleri-sozlesmesi-sha
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  - ad: Rekabetin Korunması Hakkında Kanun
    numara: '4054'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Pay Sahipleri Sözleşmesi (SHA) ve Yönetişim

## Görev
İşlem sonrası ortaklık yapısını, yönetişimi ve çıkış mekanizmalarını TTK'nın emredici sınırları içinde sözleşmeyle düzenlemek.

## Soğuk başlangıç (intake)
- İşlem sonrası ortaklık yapısı nedir (çoğunluk/azınlık)?
- Yönetim kurulu kompozisyonu ve veto hakları nasıl olacak?
- Çıkış senaryoları (IPO, satış) ve süre öngörülüyor mu?
- SHA hükümleri esas sözleşmeye taşınacak mı?

## Denetim şeması
1. **Sözleşme-esas sözleşme ilişkisi**: SHA taraflar arası borçsal etki doğurur; üçüncü kişilere ve şirkete karşı etki için esas sözleşmeye (TTK m.340 tipiklik sınırı) yansıtılması gerekir.
2. **Yönetişim**: Yönetim kurulu üyeliği için aday gösterme, imtiyazlı pay (TTK m.478-479), veto/önemli işlem onay listesi.
3. **Oy sözleşmeleri**: Oy hakkının kullanımına ilişkin sözleşmeler geçerlidir; ancak TTK'nın emredici nisap ve eşit işlem ilkesi (TTK m.357) sınır oluşturur.
4. **Çıkış mekanizmaları**: Birlikte satma hakkı (tag-along), birlikte satışa zorlama (drag-along), ön alım (pre-emption), alım/satım opsiyonları (call/put); TTK m.493 bağlam sınırları gözetilir.
5. **Kilitlenme çözümü**: Deadlock için Texas shootout / Russian roulette gibi mekanizmalar; emredici hükümlere aykırılık denetimi.
6. **Yaptırım**: İhlalde cezai şart (TBK m.179) ve aynen ifa talebi sınırları.
7. **İspat yükü**: SHA ihlalini ileri süren taraf ispatlar.

## Çıktı modülleri
- SHA madde başlıkları iskeleti
- Yönetişim ve veto matrisi
- Tag/drag/ön alım klozları
- Esas sözleşmeye taşınacak hükümler listesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

