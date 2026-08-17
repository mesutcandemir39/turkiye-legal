---
argument-hint: ''
description: Tıbbi müdahaleden doğan ölüm veya yaralanmada hekimin taksirle öldürme/yaralama
  bakımından cezai sorumluluğunu ve soruşturma rejimini değerlendirmek için kullanılır.
name: ceza-sorumlulugu
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
  - ad: Banka Muhasebe Sistemi Hakkında Kanun
    numara: '1219'
    tur: kanun
  - ad: Gayrimenkul Ek Vergisi Hakkında Kanun
    numara: '3359'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Hekimin Cezai Sorumluluğu

## Görev
Ölüm veya bedensel zararla sonuçlanan tıbbi müdahalede taksirle öldürme/yaralama suçlarının oluşup oluşmadığını ve usuli rejimi (soruşturma izni, ATK) belirlemek.

## Soğuk başlangıç (intake)
1. Sonuç ölüm mü, yaralanma mı, kalıcı sakatlık mı?
2. Hekim kamu görevlisi mi (kamu hastanesi) yoksa özel sektörde mi?
3. Şikâyet/soruşturma başladı mı; ATK raporu var mı?
4. Birden fazla sağlık çalışanı zincirleme mi sorumlu (ekip)?

## Denetim şeması
1. **Suç tipi**: Taksirle öldürme (TCK m.85) veya taksirle yaralama (TCK m.89). Yaralama şikâyete bağlıdır (basit hâl); bilinçli taksir ceza artırıcıdır (TCK m.22/3).
2. **Taksirin unsurları**: Dikkat ve özen yükümlülüğüne aykırılık + öngörülebilir sonuç + uygun illiyet. Standart sapması ATK/bilirkişi ile tespit edilir.
3. **İhmali davranış**: Hareketsizlikle (takipsizlik, sevk etmeme) gerçekleşen netice için TCK m.83.
4. **Hukuka uygunluk**: Endikasyonlu, rızaya dayalı, lege artis müdahale hukuka uygundur; rıza TCK m.26. Aydınlatma/onam eksikliği ayrıca tartışılır.
5. **Usul ve izin**: Kamu görevlisi hekim hakkında soruşturma kural olarak 4483 sayılı Kanun ve 3359 Ek m.18 çerçevesinde izne tabidir (yürürlükteki son hâl doğrulanmalı). Görevli yargı: asliye ceza.
6. **Ara sonuç**: Taksir + illiyet + zarar varsa suç oluşur; rıza ve lege artis icra cezai sorumluluğu kaldırabilir. Müterafik kusur ceza miktarına etki edebilir.

## Çıktı modülleri
- Suç unsuru değerlendirmesi (TCK m.85/89/83)
- Soruşturma izni ve görevli yargı notu
- ATK/bilirkişi raporuna itiraz noktaları
- İlkesel içtihat atfı (Yargıtay 12. CD; karararama.yargitay.gov.tr) [DOĞRULANMADI]



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

