---
argument-hint: ''
description: Eser üzerindeki hangi mali ve manevi hakların söz konusu olduğunu, kapsamını
  ve sınırlarını çıkarmak gerektiğinde; ihlal iddiasını doğru hak kalemine oturtmak
  ve devre konu olabilecek hakları ayırmak
name: mali-manevi-haklar-haritasi
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
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Mali ve Manevi Hakların Haritalanması

## Görev
Somut eser üzerinde mevcut mali ve manevi hakları tek tek çıkarmak, ihlal/talep iddiasını doğru hak kalemine oturtmak ve hangi hakların devredilebilir olduğunu ayırt etmek.

## Soğuk başlangıç (intake)
- Eser ve sahibi netleşti mi; hangi kullanım/eylem tartışmalı?
- Eylem eserin kopyalanması mı, uyarlanması mı, çevrimiçi paylaşımı mı, sahnelenmesi mi?
- Eser sahibinin adı belirtilmiş mi; üzerinde değişiklik yapılmış mı?
- Hak halen sahibinde mi, devredilmiş/lisanslanmış mı?

## Denetim şeması
1. Mali hak tasnifi (m.20): İhlal eyleminin hangi mali hakka girdiğini belirle — işleme/uyarlama (m.21), çoğaltma (m.22, dijital kopya dâhil), yayma (m.23, ilk satışla yayma hakkının tükenmesi m.23/2), temsil/sahneleme (m.24), işaret-ses-görüntü nakline yarayan araçlarla umuma iletim ve erişilebilir kılma/internet (m.25). Her mali hak bağımsızdır; biri için verilen izin diğerini kapsamaz.
2. Manevi hak tasnifi (m.14-17): Umuma arz yetkisi (m.14), adın belirtilmesi/eser sahibi olarak tanıtılma (m.15), eserde değişiklik yapılmasını men (m.16), eser sahibinin malik ve zilyede karşı hakları (m.17). Manevi haklar devredilemez; yalnızca kullanımı yetkilendirilebilir (m.16/son, m.19).
3. Süre süzgeci: Mali haklar koruma süresiyle sınırlıdır (kural: sahibin ölümü + 70 yıl, m.27; m.26-29). Süre dolmuşsa eser kamuya mal olmuştur; manevi menfaatler m.19 kapsamında belirli kişilerce korunabilir.
4. İhlal-hak eşleştirme: Eylemi madde madde hangi hakkı çiğnediğine bağla; birden çok hakkın ihlali (ör. izinsiz uyarlama + ad belirtmeme) ayrı ayrı sayılır.
5. Ara sonuç: İhlal edilen hak(lar), bunların sahibi ve süresi belirlenir; talep türü (ref/men/tazminat) buna göre kurgulanır.

İspat yükü: hakkın kapsamını ve ihlali iddia eden ispatlar; izin/devir savunmasını ileri süren onu ispatlar (HMK m.190).

## Çıktı modülleri
- Hak haritası tablosu (mali/manevi hak kalemi — madde — sahip — süre — ihlal eylemi).
- Devredilebilir/devredilemez ayrımı.
- Talep türüne köprü notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

