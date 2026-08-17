---
argument-hint: ''
description: Boşanma, nafaka, velayet, mal rejimi tasfiyesi dava dilekçeleri ile anlaşmalı
  boşanma protokolü ve 6284 başvurusu gibi belgeleri HMK formatında taslaklaştırmak
  gerektiğinde kullanılır.
name: dilekce-ve-protokol-taslagi
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
  - ad: Ailenin Korunması ve Kadına Karşı Şiddetin Önlenmesine Dair Kanun
    numara: '6284'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dava Dilekçesi ve Anlaşmalı Boşanma Protokolü Taslağı

## Görev
Aile hukuku belgesini (dava/cevap dilekçesi, anlaşmalı boşanma protokolü, 6284 başvurusu) HMK m.119 mimarisine ve [doldurulacak] yer tutucu disiplinine uygun taslaklaştırmak.

## Soğuk başlangıç (intake)
1. Hangi belge isteniyor (dava dilekçesi, protokol, başvuru, cevap)?
2. Taraflar, çocuklar ve talep kalemleri (boşanma, nafaka türü ve miktarı, velayet, tazminat, tasfiye) net mi?
3. Hangi deliller mevcut (tanık, mesaj, rapor, tapu, banka kaydı)?
4. Anlaşmalı ise taraflar tüm mali ve çocuk konularında mutabık mı?

## Denetim şeması
1. **Dava dilekçesi iskeleti (HMK m.119).** Mahkeme; taraf ve vekil bilgileri; konu; **açık talep sonucu** (boşanma + her bir fer'i ayrı ayrı ve miktarlı); vakıalar (sebep ve kusur olgularının kronolojisi); hukuki sebepler (TMK m.166/166/3 vd., m.174, m.175, m.182, m.169); **deliller her vakıaya bağlanarak** (tanık, isticvap, sosyal/ekonomik araştırma, uzman raporu); harç ve imza. Eksik bilgiler [doldurulacak] ile işaretlenir, uydurulmaz.
2. **Anlaşmalı boşanma protokolü (TMK m.166/3).** Şartlar: evlilik en az 1 yıl; tarafların özgür iradesi; hâkimce uygun bulunma. Protokol mutlaka şunları içermeli: boşanma iradesi, yoksulluk/iştirak nafakası (tür-miktar-artış), velayet ve kişisel ilişki takvimi, maddi/manevi tazminat, mal rejimi/ev eşyası paylaşımı, ziynet, soyadı; hâkim çocuğun yararına aykırı düzenlemeyi değiştirebilir (m.166/3 son cümle).
3. **6284 başvurusu.** Sade dille olay anlatımı + talep edilen tedbirler (m.5 önleyici / m.3-4 koruyucu) + aciliyet beyanı; harç muafiyeti notu.
4. **Tutarlılık denetimi.** Talep sonucu ile vakıa ve hukuki sebepler örtüşüyor mu; nafaka türleri karışmış mı; tasfiye talebi ayrı davaya mı bırakılacak; süre/hak düşürücü süre dilekçede gözetilmiş mi?
5. **Ara sonuç.** Belge taslağı + eksik veri (yer tutucu) listesi + ekler dizini.

## Çıktı modülleri
- İlgili belgenin HMK uyumlu tam taslağı (yer tutuculu).
- Talep-vakıa-hukuki sebep-delil eşleme kontrolü.
- Ekler ve delil dizini ile imza/harç notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

