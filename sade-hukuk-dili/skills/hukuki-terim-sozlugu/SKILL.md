---
argument-hint: ''
description: Bir metindeki hukuki ve Latince terimleri, kalıpları ve kısaltmaları
  müvekkile açıklayan sözlük üretmek; terimin yanlış eşanlamlıyla değiştirilmeden
  doğru karşılığını ve anlam farkını vermek gerektiği
name: hukuki-terim-sozlugu
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Hukuki Terim Açıklama ve Sözlük

## Görev
Bir belgedeki hukuki terimleri, Latince ifadeleri ve kısaltmaları okuyucuya açıklayan, anlam
nüanslarını koruyan bir sözlük/açıklama listesi üretmek. Amaç terimi yok etmek değil, doğru
anlamını yalın bir cümleyle vermek.

## Soğuk başlangıç (intake)
1. Hangi belge ve hangi hukuk alanı (terimlerin anlamı bağlama göre değişir)?
2. Okuyucunun seviyesi (hiç bilmeyen / temel bilen)?
3. Tüm terimler mi, yoksa işaretli olanlar mı açıklanacak?

## Denetim şeması
1. TERİM AVI: Metindeki teknik terimler, Latince kalıplar (inter alia, prima facie, per se, ex nunc/
   ex tunc) ve kısaltmalar (TBK, HMK, İİK, BAM/BİM, ATK) çıkarılır.
2. BAĞLAMA GÖRE TANIM: Her terim, kullanıldığı hukuk dalına göre tanımlanır; aynı kelime farklı
   alanda farklı anlam taşıyabilir ("ifa", "zilyetlik", "def'i").
3. NÜANS AYRIMI (anlam yükü): Karıştırılan çiftler ayrı ayrı açıklanır — zamanaşımı (borç durur
   ama def'i gerekir, TBK m.146 vd.) ≠ hak düşürücü süre (hak kendiliğinden düşer); fesih ≠ iptal
   ≠ dönme ≠ cayma; itiraz ≠ def'i; müteselsil ≠ müşterek sorumluluk; tazminat ≠ ceza.
4. YANLIŞ EŞANLAMLI YASAĞI: Hiçbir terim, hukuki sonucu değiştiren bir günlük kelimeyle eşitlenmez;
   tanım açıklayıcıdır, eşitleyici değildir.
5. ATIF: Terimin dayandığı temel madde varsa parantezle verilir (ör. muacceliyet — TBK m.90 vd.).
6. ARA SONUÇ: Açıklamalar bağlama uygun ve nüans koruyor mu denetlenir.

## Çıktı modülleri
- Alfabetik veya metin sırasına göre terim listesi.
- Her terim için: yalın tanım + (varsa) madde atfı + karıştırılan terimden farkı.
- "Aynı kelime başka anlamda" uyarı kutusu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

