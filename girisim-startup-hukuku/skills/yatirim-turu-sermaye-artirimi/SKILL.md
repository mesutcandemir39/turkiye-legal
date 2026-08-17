---
argument-hint: ''
description: Bir yatırım turunda yeni yatırımcıya doğrudan pay verilirken (equity
  round); bedelli sermaye artırımı, rüçhan hakkının yönetimi, pay ihracı, kapanış
  ön şartları ve fonun şirkete girişi adım adım kurgu
name: yatirim-turu-sermaye-artirimi
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yatırım Turu ve Bedelli Sermaye Artırımı

## Görev
Equity yatırım turunu hukuken icra etmek: yeni payların ihracı için sermaye artırımını, rüçhan yönetimini, kapanış ön şartlarını ve fonun şirkete girişini doğru sıralamak.

## Soğuk başlangıç (intake)
1. Tur büyüklüğü, değerleme ve yatırımcıya verilecek pay oranı nedir?
2. Şirket kayıtlı sermaye sisteminde mi (YK ile artırım) yoksa esas sermaye sisteminde mi (GK)?
3. Mevcut pay sahiplerinin rüçhan hakkı kullandırılacak mı, sınırlanacak mı?
4. Yatırımcıya imtiyazlı pay mı veriliyor (tasfiye tercihi, oy, veto)?
5. Kapanış için hangi ön şartlar (DD, onaylar, rekabet izni) var?

## Denetim şeması
1. Artırım türü: Esas sermaye artırımı GK kararı + esas sözleşme değişikliği (TTK m.456-458); kayıtlı sermayede tavan içinde YK kararı (m.460). Önceki sermayenin tamamen ödenmiş olması kural (m.456/1).
2. Rüçhan hakkı: m.461 — mevcut pay sahiplerine oranları kadar; yatırımcı girişi için bu hak sınırlanır (m.461/2: haklı sebep + nitelikli nisap + eşit işlem). Sınırlama gerekçesi GK kararında belgelenmeli.
3. İmtiyazlı pay ihracı: Yatırımcı payı imtiyazlıysa (m.478-479) esas sözleşmede pay grubu/imtiyaz tanımlanmalı; imtiyazlı pay sahipleri özel kurulu (m.454) ilerideki değişikliklerde devreye girer.
4. Bedel ve ödeme: Nominal üstü çıkış primli ihraçta emisyon primi; nakdî sermaye ödeme kuralı m.344; primli payda bedelin tescilden önce ödenmesi.
5. Kapanış ön şartları: DD'nin tamamlanması, kurumsal kararlar (GK/YK), gerekiyorsa rekabet izni (4054 m.7) ve üçüncü kişi onayları; eş zamanlı SHA imzası.
6. Tescil ve hüküm: Artırım tescille hüküm ifade eder (m.456 vd.); pay defterine kayıt (m.499).
7. İspat/şekil: Nisap ve ödeme belgeleri şirkette; rüçhan sınırlamasının haklı sebebi şirketçe ortaya konur.

## Çıktı modülleri
- Tur kapanış adım planı (DD → karar → ödeme → tescil).
- GK/YK karar taslakları (rüçhan sınırlama gerekçeli).
- Pay alım/iştirak (SSA) sözleşmesi iskeleti ve kapanış checklist'i.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

