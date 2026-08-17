---
argument-hint: ''
description: Bir kusurun ek raporla giderilebilir mi yoksa yeni bilirkişi/heyet mi
  gerektirdiği ayrımını yapmak ve bu doğrultuda en isabetli usulî talebi gerekçelendirmek
  istendiğinde kullanılır.
name: ek-rapor-yeni-bilirkisi
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  - ad: Sağlık Turizmi Kanunu
    numara: '6754'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Ek Rapor ve Yeni Bilirkişi Talebi Stratejisi

## Görev
Tespit edilen her kusur için "tamamlama mı, ikame mi" kararını vermek: eksik/belirsizlik ek raporla; yöntem hatası, esaslı çelişki veya tarafsızlık kusuru yeni bilirkişi/heyetle ele alınır (HMK m.281).

## Soğuk başlangıç (intake)
- Kusur eksiklik/belirsizlik mi, yoksa yöntem/tarafsızlık temelli mi?
- Aynı bilirkişi düzeltirse güven verir mi, yoksa yenisi mi gerekli?
- Dosyada birden fazla çelişen rapor var mı (üçüncü heyet ihtiyacı)?
- Talebin yargılamayı uzatma maliyeti kabul edilebilir mi?

## Denetim şeması
1. **Eksiklik/belirsizlik testi (HMK m.281):** Hususlar eksik/belirsizse veya tamamlanması gerekiyorsa, kural olarak aynı bilirkişiden **ek rapor** istenir. Hesap hataları, yanıtsız sorular ve tamamlanabilir veriler bu kapsamdadır.
2. **Yöntem/güven testi:** Kusur yöntemin temelinde veya bilirkişinin objektifliğindeyse (6754 s.K. m.3), tamamlama yetmez; **yeni bilirkişi/heyet** seçimi istenir.
3. **Çelişki yoğunluğu:** Birden fazla rapor esaslı ve giderilemez biçimde çelişiyorsa, çelişkiyi giderecek **yeni/üçüncü heyet** talebi gerekçelendirilir; hâkim raporları serbestçe takdir eder (HMK m.282).
4. **Maliyet-fayda:** Yeni heyet yargılamayı uzatır ve gider doğurur; bu nedenle ikame talebi yalnızca tamamlama yetersizse tercih edilir, gerekçesi güçlü tutulur.
5. **Ara sonuç:** Her kusur "ek rapor / yeni heyet / üçüncü heyet" etiketiyle ve dayanağıyla sınıflandırılır; karma talep (bazı kalemlerde ek rapor, bir kalemde yeni heyet) mümkündür.

## Çıktı modülleri
- Kusur-yol eşleştirme tablosu (ek rapor / yeni heyet / üçüncü heyet + gerekçe).
- Ek rapor için bilirkişiye sorulacak ilave sorular listesi.
- Yeni bilirkişi talebinin gerekçe paragrafı.
- Yargılama süresi ve gider etkisine ilişkin kısa risk notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

