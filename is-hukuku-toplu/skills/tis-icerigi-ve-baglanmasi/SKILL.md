---
argument-hint: ''
description: Toplu is sozlesmesinin normatif ve borc dogurucu hukumlerini, suresini,
  duzeyini, yararlanma-dayanisma aidati rejimini ve sozlesmenin sona ermesini ele
  alir; TIS metni hazirlama, yorumlama veya uygula
name: tis-icerigi-ve-baglanmasi
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
  - ad: Sendikalar ve Toplu İş Sözleşmesi Kanunu
    numara: '6356'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# TİS İçeriği, Düzeyi ve Bağıtlanması

## Görev
TİS'in hukuki yapısını çözümlemek: hangi hükümler normatif (iş sözleşmesine doğrudan etki eden), hangileri borç doğurucu (taraflar arası); yararlanma rejimi, süre ve sona erme. TİS metni okuma, kaleme alma ve yorumlama işidir.

## Soğuk başlangıç (intake)
- Hangi düzeyde TİS (işyeri/işletme/grup)?
- TİS imzalandı mı, süresi ve yürürlük tarihi nedir?
- Talepte bulunan işçi sendika üyesi mi, değilse dayanışma aidatı ödüyor mu?
- Sorun bir hükmün yorumu mu yoksa boşluğu mu?

## Denetim şeması
1. **TİS'in niteliği:** 6356 m.36 — TİS'in **normatif hükümleri** (ücret, ikramiye, çalışma süreleri) iş sözleşmesinin yerini alır, doğrudan ve emredici etki gösterir; **borç doğurucu hükümler** sadece tarafları bağlar.
2. **Art etki (ardçıl etki):** 6356 m.36/2 — TİS sona erse de, yeni TİS yapılana kadar normatif hükümler iş sözleşmesi hükmü olarak devam eder.
3. **Düzey kuralı:** 6356 m.34 — bir işyerinde aynı dönem için yalnızca bir TİS uygulanabilir; işletme düzeyinde toplu sözleşme bütünlüğü esastır.
4. **Süre:** 6356 m.35 — TİS en az **1**, en çok **3** yıl süreli yapılır; süre sonradan değiştirilemez (faaliyet/işletme TİS'lerinde özel istisnalar saklı).
5. **Yararlanma:** 6356 m.39 — kural olarak TİS'ten taraf işçi sendikasının üyeleri yararlanır. Üye olmayanlar **dayanışma aidatı** ödeyerek yararlanabilir; üyelikten farklı olarak grev kararına katılma gibi sonuçlar doğmaz.
6. **Teşmil:** 6356 m.40 — Cumhurbaşkanı, bir işkolundaki TİS'i o işkolundaki üye olmayan işyerlerine teşmil edebilir (sınırlı, istisnai yol).

Ara sonuç: Sorun normatif hükmün uygulanması ise hak uyuşmazlığı → yargı; metin oluşturma ise pazarlık/taslak çalışması yapılır.

## Çıktı modülleri
- TİS hüküm ayrıştırması (normatif / borç doğurucu).
- Yararlanma ve dayanışma aidatı değerlendirmesi.
- Taslak madde önerileri ([doldurulacak] yer tutucularıyla).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

