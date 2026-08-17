---
argument-hint: ''
description: Mütalaadaki hukuki görüşü Yargıtay/Danıştay/AYM içtihadı ve doktrinle
  desteklemek, içtihat eğilimini ve istikrar durumunu değerlendirmek gerektiğinde
  kullanılır; katı atıf hijyeniyle çalışır.
name: ictihat-doktrin-degerlendirmesi
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


# İçtihat ve Doktrin Değerlendirmesi

## Görev
Mütalaadaki hukuki kanaati yerleşik içtihat ve doktrinle desteklemek; içtihat eğilimini, varsa görüş ayrılıklarını ve içtihadı birleştirme kararlarını tespit etmek. İçtihat hâkimi bağlamasa da uygulamadaki gerçek eğilimi gösterir; mütalaanın gerçekçiliğini bu sağlar.

## Soğuk başlangıç (intake)
- Hangi alt soru için içtihat aranıyor?
- Konu hangi mahkeme/dairenin görev alanında? (Yargıtay HD/CD, Danıştay dava dairesi, AYM, BAM)
- İçtihadı birleştirme kararı veya AYM/AİHM kararı konuyu doğrudan etkiliyor mu?
- Doktrinde tartışmalı/çoğunluk-azınlık görüşü var mı?

## Denetim şeması
1. Doğru kaynak seçimi: Konuya göre karararama.yargitay.gov.tr, karararama.danistay.gov.tr veya kararlarbilgibankasi.anayasa.gov.tr; mülga/yürürlükteki mevzuat dönemine dikkat.
2. ATIF HİJYENİ (mutlak kural): Hiçbir esas/karar numarası hatırlanarak yazılmaz. Karara dayanılacaksa mahkeme + daire + esas/karar no + tarih kaynaktan doğrulanır. Doğrulanmamış her künye `[DOĞRULANMADI]` ile işaretlenir; sahte numara asla üretilmez. Doğrulanamıyorsa ilkesel atıf yapılır ("yerleşik Yargıtay içtihadına göre... [karararama.yargitay.gov.tr üzerinden doğrulanmalı]").
3. İçtihat eğilimi tespiti: Tek karar değil eğilim aranır; istikrarlı mı, daireler arası çelişki var mı, içtihadı birleştirme kararı (İBK) konuyu bağlayıcı şekilde çözmüş mü?
4. Hiyerarşi: AYM bireysel başvuru ve norm denetimi kararları ile AİHM kararları temel hak boyutunda üstün ağırlıklıdır; İBK Yargıtay daireleri için bağlayıcıdır.
5. Doktrin kullanımı: Yazar-eser-sayfa ile; çoğunluk ve azınlık görüşü ayrılır; mütalaa hangi görüşü neden benimsediğini gerekçelendirir.
6. Ara sonuç: Destekleyici içtihat/doktrin + karşı yöndeki görüş + bunların mütalaadaki sonuca etkisi.

## Çıktı modülleri
- İlkesel içtihat değerlendirmesi (eğilim + istikrar notu)
- Doğrulanacak künye listesi (`[DOĞRULANMADI]` işaretli)
- Doktrin görüş tablosu (çoğunluk/azınlık)
- Arama kaynağı ve sorgu önerisi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

