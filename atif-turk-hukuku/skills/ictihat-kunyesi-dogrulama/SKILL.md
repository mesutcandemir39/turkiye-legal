---
argument-hint: ''
description: Bir karara atıf yapılacağında ya da metinde geçen bir karar künyesinin
  gerçekliği şüpheliyse; mahkeme-daire-esas-karar-tarih bilgisini doğru biçimde kurmak
  ve resmî kaynaktan doğrulamak için kullanılı
name: ictihat-kunyesi-dogrulama
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


# İçtihat Künyesi ve Doğrulama

## Görev
Bir yargı kararına usulüne uygun, eksiksiz ve doğrulanmış bir künye ile atıf yapmak; doğrulanamayan künyeyi uydurmak yerine açıkça işaretlemek.

## Soğuk başlangıç (intake)
- Hangi mahkeme/daire/kurul (Yargıtay HGK mı, 11. HD mi, Danıştay mı, AYM mi)?
- Elimizde karar metni var mı, yoksa yalnızca ikinci el bir atıf mı?
- Karar tarihi ve E./K. numaraları tam mı, eksik mi?
- Bu karar lehe mi, yoksa karşı tarafın dayanağı mı?

## Denetim şeması
1. **Tam künye şablonu** — Yargıtay: "Yargıtay [Daire/HGK/İBK], E. …/…, K. …/…, T. gg.aa.yyyy". Danıştay: "Danıştay [Daire/İDDK/VDDK], E. …, K. …, T. …". AYM: norm denetimi "AYM, E. …/…, K. …/…, T. …"; bireysel başvuru "AYM, B. No: …/…, T. …". AİHM: "Taraflar/Türkiye, B. No: …, T. …".
2. **Doğrulama zorunluluğu** — Künye yalnızca karar metni görüldüğünde veya resmî bankadan teyit edildiğinde yazılır: karararama.yargitay.gov.tr, karararama.danistay.gov.tr, kararlarbilgibankasi.anayasa.gov.tr, hudoc.echr.coe.int. **E./K. numarası, daire ve tarih model hafızasından ASLA üretilmez.**
3. **Eksik/şüpheli künye** — Numaranın bir kısmı eksikse veya teyit edilemiyorsa, sayı uydurulmaz; künye `[DOĞRULANMADI]` ile, varsa yalnızca ilke özeti yazılır: "Yargıtay'ın yerleşik içtihadına göre … [künye doğrulanacak]".
4. **İkinci el atıf uyarısı** — Bir dilekçe/makaledeki künye doğrudan kopyalanmaz; asıl metne inilir, çünkü ikinci el atıflarda numara/tarih hatası sıktır.
5. **Künye-içerik tutarlılığı** — Atfedilen ilke, kararın gerçekten kurduğu ilke mi? Vakıası benzer mi? Uyuşmuyorsa karar emsal gösterilmez.

## Çıktı modülleri
- Doldurulmuş künye şablonu (mahkeme türüne göre).
- Doğrulama durumu: teyit edildi / `[DOĞRULANMADI]`.
- Arama sorgusu önerisi (banka adı + anahtar kelime).
- İçerik-künye tutarlılık notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

