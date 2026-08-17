---
argument-hint: ''
description: Yetki belgesinden TIS imzasina veya uyusmazlik tutanagina kadar olan
  toplu gorusme surecini, cagri usulunu, surelerini ve 6356 m.50 kapsaminda resmi
  arabuluculugu ele alir; pazarlik takvimi ve uyusmaz
name: toplu-gorusme-ve-arabuluculuk
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


# Toplu Görüşme ve Resmî Arabuluculuk

## Görev
Toplu görüşmenin başlatılması, sürdürülmesi ve tıkanması halinde resmî arabuluculuğa geçişin usul-süre yönetimi. Menfaat uyuşmazlığının barışçıl çözüm hattıdır.

## Soğuk başlangıç (intake)
- Yetki belgesi tebliğ edildi mi, tarihi nedir?
- Çağrı yapıldı mı; ilk toplantı gerçekleşti mi?
- Görüşmeler kaç gündür sürüyor; uyuşmazlık tutanağı tutuldu mu?
- Hangi konularda anlaşmazlık var?

## Denetim şeması
1. **Çağrı:** 6356 m.46 — yetki belgesini alan taraf, **15 gün** içinde karşı tarafı toplu görüşmeye çağırır; çağrı tarihinden itibaren **30 gün** içinde toplanılmazsa veya görüşmeye başlanmazsa yetki düşebilir (m.46/2-3 kontrol edilir).
2. **Görüşme süresi:** 6356 m.47 — toplu görüşme süresi, ilk toplantı tarihinden itibaren **60 gün**dür.
3. **Uyuşmazlık tutanağı:** Anlaşma sağlanamaz veya taraflardan biri görüşmeye gelmezse uyuşmazlık tutanağı tutulur; bu, arabuluculuk ve grev sürecinin tetikleyicisidir.
4. **Resmî arabuluculuk:** 6356 m.50 — uyuşmazlığın görevli makama (görevli birim) bildirilmesi üzerine resmî listeden bir arabulucu görevlendirilir; arabulucu **15 gün** (gerekirse 6 işgünü uzatmayla) içinde tarafları uzlaştırmaya çalışır, sonuçta tutanak düzenler.
5. **Ara sonuç:** Arabuluculukta anlaşma olursa TİS imzalanır. Anlaşma olmazsa menfaat uyuşmazlığı grev/lokavt veya (kamu hizmeti gibi yasak hallerde) yüksek hakem yoluna açılır.

Not: Toplu menfaat uyuşmazlığında **6325 sayılı HUAK dava şartı arabuluculuk uygulanmaz**; 6356'nın kendi resmî arabuluculuk rejimi işler.

## Çıktı modülleri
- Toplu görüşme süre/aşama takvimi (15-30-60 gün eşikleri).
- Çağrı yazısı ve uyuşmazlık tutanağı iskeleti.
- Arabuluculuk sonrası yol haritası (grev / yüksek hakem / imza).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

