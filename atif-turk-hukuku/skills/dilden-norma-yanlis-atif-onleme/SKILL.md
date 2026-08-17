---
argument-hint: ''
description: Bir metinde mevzuat veya içtihat doğru görünse de yanlış maddeye, mülga
  hükme, çarpıtılmış ilkeye veya alakasız karara dayanıldığı durumlarda; bu hataları
  yakalayıp düzeltmek için kullanılır.
name: dilden-norma-yanlis-atif-onleme
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


# Yanlış ve Yanıltıcı Atıf Önleme

## Görev
Görünüşte düzgün ama içerik olarak yanlış atıfları — yanlış madde, mülga hüküm, çarpıtılmış ilke, alakasız emsal — tespit edip düzeltmek; metnin dayanaklarını gerçekten taşır hâle getirmek.

## Soğuk başlangıç (intake)
- Atfedilen madde, ileri sürülen kuralı gerçekten içeriyor mu?
- Hüküm güncel mi, yoksa değişmiş/mülga mı?
- Atfedilen kararın ilkesi, metinde söylendiği gibi mi?
- Emsal kararın vakıası eldeki olaya benziyor mu?

## Denetim şeması
1. **Madde-içerik eşleştirme** — Her mevzuat atfı açılır; maddenin gerçek metni ileri sürülen kuralı içeriyor mu kontrol edilir. Sık hata: doğru kanun, yanlış madde; veya doğru madde, yanlış fıkra/bent.
2. **Yürürlük kontrolü** — Mülga/değişik hükme dayanılmış mı (mevzuat.gov.tr güncel metin)? Eski-yeni kanun karışıklığı (örn. eski BK/yeni TBK madde numaraları) ayıklanır.
3. **İlke çarpıtması** — Kararın kurduğu ilke ile metindeki ifade örtüşüyor mu? İstisna kural gibi, obiter ratio gibi sunulmuş olabilir; düzeltilir.
4. **Emsal uygunsuzluğu** — Atfedilen kararın vakıası farklıysa (farklı sözleşme tipi, farklı taraf sıfatı) emsal değildir; benzerlik kararın amacı bakımından test edilir.
5. **Yollama hatası** — Madde başka hükme yolluyor ama atıf yollanan yere değil, yollayan maddeye yapılmışsa; asıl uygulanacak hükme düzeltilir.
6. **Düzeltme ve gerekçe** — Her hata için doğru atıf + neden yanlış olduğu kısaca yazılır; doğrulanamayan kısım `[DOĞRULANMADI]` bırakılır.

## Çıktı modülleri
- Hatalı atıf → doğru atıf düzeltme tablosu.
- Yürürlük/madde uyumsuzluğu listesi.
- İlke çarpıtması / emsal uygunsuzluğu notları.
- Düzeltilmiş dayanak listesi + işaretler.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

