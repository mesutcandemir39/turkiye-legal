---
argument-hint: ''
description: Bir sözleşme maddesinin ya da irade beyanının anlamı taraflar arasında
  çekişmeliyse; lafza mı gerçek ortak iradeye mi üstünlük verileceğini ve boşlukların
  nasıl doldurulacağını çözmek için kullanılır.
name: sozlesme-yorumu
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
    madde: '1'
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Sözleşme ve İrade Beyanlarının Yorumu

## Görev
Çekişmeli bir sözleşme hükmünü ya da irade beyanını TBK m.19 ve güven ilkesi çerçevesinde yorumlamak, boşlukları tamamlamak ve geçersizlik/uyarlama ihtimallerini gözetmek.

## Soğuk başlangıç (intake)
- Hangi madde/ifade tartışmalı; tarafların ona yüklediği iki anlam ne?
- Sözleşme metni dışında yazışma, teamül, önceki ilişki var mı?
- Hüküm tip sözleşme/genel işlem koşulu mu, bireysel müzakere ürünü mü?
- Bu bir ticari iş mi (ticari teamül ağırlığı) yoksa tüketici işlemi mi?

## Denetim şeması
1. **Gerçek irade önce — TBK m.19** — Yorumda tarafların gerçek ve ortak iradesi esastır; yanlış yazılmış sözcük/deyim tarafları bağlamaz (*falsa demonstratio non nocet*). Lafız, iradenin tespitinde başlangıç noktasıdır, son söz değil.
2. **Güven ilkesi** — Gerçek ortak irade saptanamıyorsa, beyan, dürüst ve makul bir muhatabın anlayacağı şekilde (güven teorisi) yorumlanır.
3. **Yardımcı ölçütler** — Sözleşmenin amacı, bütünlüğü (maddeler birbirini açıklar), kuruluş öncesi/sonrası davranışlar, teamül ve ticari örf; tereddütte düzenleyenin aleyhine yorum (genel işlem koşullarında).
4. **Boşluk tamamlama** — Düzenlenmeyen nokta için önce yedek hukuk kuralı (tamamlayıcı emredici olmayan hükümler), yoksa TMK m.2 dürüstlük kuralıyla varsayımsal taraf iradesi.
5. **Geçerlilik süzgeci** — Yorumdan sonra: emredici hükümlere, kamu düzenine, ahlaka, kişilik hakkına aykırılık (TBK m.27) ve genel işlem koşullarında haksız şart denetimi (TBK m.20-25) yapılır.
6. **Uyarlama** — Aşırı ifa güçlüğü/öngörülemeyen değişiklikte TBK m.138 (işlem temelinin çökmesi) ile uyarlama/dönme değerlendirilir.

## Çıktı modülleri
- Tartışmalı madde + iki rakip okuma.
- Gerçek irade / güven ilkesi analizi.
- Boşluk varsa tamamlayıcı kural önerisi.
- Geçerlilik ve uyarlama uyarıları + `[DOĞRULANMADI]` içtihat.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

