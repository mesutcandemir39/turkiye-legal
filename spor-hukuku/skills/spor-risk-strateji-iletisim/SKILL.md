---
argument-hint: ''
description: Spor uyuşmazlığında kazanç-kayıp ihtimalini değerlendirmek, sportif/mali/itibari
  riskleri tartmak, çözüm seçeneklerini sıralamak ve müvekkili (sporcu, kulüp, federasyon)
  bilgilendirmek gerektiğinde ku
name: spor-risk-strateji-iletisim
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
  - ad: Çalışma ve Sosyal Güvenlik Bakanlığı Kuruluş ve Görevleri Hakkında Kanun
    numara: '7405'
    tur: kanun
  - ad: Tıbbi Deontoloji Tüzüğü Hakkında Kanun
    numara: '6222'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk Değerlendirmesi, Strateji ve Müvekkil İletişimi

## Görev
Spor uyuşmazlığında olası sonuçları, sportif-mali-itibari riskleri ve çözüm seçeneklerini (mücadele, uzlaşma, geri çekilme) tartmak; müvekkile sade ve dürüst bir risk-strateji bilgilendirmesi sunmaktır.

## Soğuk başlangıç (intake)
1. Müvekkil kim ve nihai hedefi ne (cezanın kalkması, transfer, alacak, itibar koruması)?
2. Uyuşmazlığın bulunduğu aşama ve eldeki güçlü/zayıf yönler?
3. Zaman baskısı var mı (müsabaka takvimi, transfer dönemi, lisans tarihi)?
4. Mali ve itibari hassasiyetler neler?
5. Uzlaşma/sulh seçeneği masada mı?

## Denetim şeması
1. **Olasılık değerlendirmesi**: Hukuki argümanların gücüne ve emsal uygulamaya göre kazanma/hafifletme ihtimali gerçekçi biçimde belirlenir; kesin sonuç vaadi verilmez.
2. **Çok boyutlu risk**: Hukuki sonucun yanında sportif (men, puan silme, transfer yasağı), mali (para cezası, tazminat, bonservis kaybı) ve itibari (kamuoyu, sponsor) etkiler birlikte tartılır.
3. **Zaman ve takvim baskısı**: Müsabaka/transfer/lisans takvimi, tedbir talebi gerekliliği ve sürelerle çakışma değerlendirilir; acil tedbir seçeneği öne çekilir.
4. **Seçenek sıralaması**: Tam mücadele, kısmi itiraz, uzlaşma/sulh, geri çekilme seçenekleri maliyet-fayda ve süreyle birlikte sıralanır.
5. **İletişim ilkesi**: Müvekkile sade dille, en kötü-en iyi-olası senaryo üçlüsüyle ve net karar noktalarıyla bilgi verilir; karar müvekkilindir, kararın temeli yazılı bırakılır.
6. **Ara sonuç**: Önerilen strateji, gerekçesi ve müvekkilden istenen kararlar listelenir.

## Çıktı modülleri
- Risk haritası (hukuki/sportif/mali/itibari)
- Senaryo tablosu (en iyi/olası/en kötü)
- Strateji önerisi ve gerekçe
- Müvekkil bilgilendirme notu (sade dil)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

