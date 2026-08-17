---
argument-hint: ''
description: Vergi uyuşmazlığında dava-uzlaşma-ödeme seçeneklerini kazanma olasılığı,
  maliyet, nakit akışı ve ceza riskine göre tartıp müvekkile bütüncül strateji önerisi
  hazırlamak için kullanılır.
name: risk-strateji-ve-musavirlik
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
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk Değerlendirmesi ve Vergi Uyuşmazlık Stratejisi

## Görev
Uyuşmazlığın bütününü değerlendirerek dava, uzlaşma, indirimli ödeme veya bekleme seçeneklerini kazanma olasılığı, maliyet, süre, nakit akışı ve olası adli (VUK m.359) risk bakımından tartmak; müvekkile gerekçeli strateji önerisi sunmak.

## Soğuk başlangıç (intake)
1. Toplam mali risk ne (vergi aslı + ceza + faiz) ve müvekkilin ödeme kapasitesi nedir?
2. Uyuşmazlığın çekirdeği hukuki yorum mu, maddi/hesap meselesi mi?
3. Sahte belge / kaçakçılık iddiası var mı (adli boyut riski)?
4. Müvekkilin önceliği maliyeti minimize etmek mi, esastan haklılığı tescil ettirmek mi, hızlı kapanış mı?

## Denetim şeması
1. **Hukuki güç analizi.** Tarhiyat ve cezaların her bir kalemi için iptal şansı (zayıf/orta/güçlü) ilgili madde ve içtihat eğilimiyle (Danıştay daire kararları, `[DOĞRULANMADI]`) işaretlenir.
2. **Maliyet-fayda.** Dava harcı/vekâlet, gecikme faizi (VUK m.112) ve gecikme zammı (AATUHK m.51) birikimi, uzlaşma/indirim (VUK m.376) ile dava sonucu beklentisi karşılaştırılır.
3. **Nakit akışı ve tahsilat baskısı.** İYUK m.27/4 otomatik durma var mı; haciz riski varsa teminat/tecil (AATUHK m.48) ile YD seçenekleri tartılır.
4. **Adli risk köprüsü.** Sahte belge düzenleme/kullanma iddiası varsa VUK m.359 kapsamında ayrı bir ceza yargılaması riski; idari dava ile ceza davası arasındaki etkileşim ve mütalaa şartı (VUK m.367) not edilir. Ara sonuç: idari uyuşmazlık stratejisi adli riski ağırlaştırmayacak şekilde kurgulanır.
5. **Senaryolar.** En iyi / beklenen / en kötü senaryolar tutarsal olarak sunulur; her senaryo için tavsiye edilen eylem ve son tarih belirlenir.

## Çıktı modülleri
- Kalem bazlı kazanma olasılığı ve risk matrisi.
- Seçenek karşılaştırması (dava / uzlaşma / indirimli ödeme) — maliyet, süre, sonuç.
- Müvekkile gerekçeli strateji önerisi ve karar takvimi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

