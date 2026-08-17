---
argument-hint: ''
description: Müvekkil veya karşı tarafın freight forwarder/taşıma işleri komisyoncusu
  olduğu, taşımanın organizasyonu üstlenildiği ilişkilerde komisyoncunun sorumluluk
  rejiminin ve taşıyıcı gibi sorumlu sayılma ha
name: tasima-isleri-komisyonculugu
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
  version: 0.1.0
user-invocable: true
---


# Taşıma İşleri Komisyonculuğu (Forwarder)

## Görev
Taşıma işleri komisyoncusunun (freight forwarder) borçlarını, özen ve sorumluluk ölçüsünü belirlemek; hangi hallerde taşıyıcı gibi tam sorumlu sayılacağını saptamak.

## Soğuk başlangıç (intake)
1. Müvekkil taşımayı kendi mi üstleniyor, yoksa taşıyıcılarla sözleşip organizasyonu mu sağlıyor?
2. Ücret nasıl belirlenmiş: sabit/maktu (kapsamlı) ücret mi, yoksa komisyon mu?
3. Eşya başkalarının yüküyle birlikte toplu (gruppage) taşımaya mı verildi?
4. Komisyoncu bizzat taşımayı (kendi aracıyla) üstlendi mi?

## Denetim şeması
1. **Tanım ve borç:** TTK m.917 — komisyoncu, ücret karşılığı kendi adına ve müvekkil hesabına eşya taşıtmayı üstlenir. Taşıma sözleşmelerini yapma, gönderme ve özen borcu vardır.
2. **Özen ve sorumluluk:** TTK m.918 — komisyoncu işleri tedbirli bir tacir özeniyle görmekle yükümlüdür; kendi kusurundan ve seçtiği kişilerden sorumludur.
3. **Taşıyıcı gibi sorumluluk halleri:** 
   - **Sabit ücret (m.926):** Komisyoncu müvekkille maktu/sabit bir taşıma ücreti kararlaştırmışsa, yalnızca taşıyıcının hak ve borçlarına sahip olur ve taşıyıcı gibi sorumlu olur.
   - **Toplu yük/gruppage (m.927):** Eşyayı başkalarının eşyasıyla birlikte toplu taşımaya verirse taşıyıcı gibi sorumlu tutulur.
   - **Bizzat taşıma (m.928):** Komisyoncu taşımayı kendisi yaparsa taşıyıcının hak ve yükümlülüklerine de sahip olur.
4. **Sorumluluk sınırı:** Taşıyıcı gibi sorumlu sayılan komisyoncu, TTK m.882 sınırından yararlanır; m.886 halinde sınır kalkar.
5. **Zamanaşımı:** TTK m.855 (1/3 yıl) komisyonculuk istemleri için de esas alınır.
6. **Ara sonuç:** Komisyoncunun özen sorumluluğu mu yoksa taşıyıcı gibi objektif sorumluluğu mu söz konusu.

## Çıktı modülleri
- Sıfat ve ücret yapısına göre sorumluluk rejimi tablosu (m.917/926/927/928).
- Taşıyıcı gibi sorumluluk tetiklenip tetiklenmediği değerlendirmesi.
- Rücu ve zincir sorumluluk (alt taşıyıcı) haritası.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

