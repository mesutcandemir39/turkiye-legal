---
argument-hint: ''
description: Kıdem ve ihbar tazminatına hak kazanma şartları ile tutarın hesaplanması
  gerektiğinde; hizmet süresi, giydirilmiş ücret, kıdem tavanı, ihbar öneli ve fesih
  sebebine göre tazminatları kalem kalem belir
name: kidem-ihbar-tazminati
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
  - ad: İş Kanunu
    numara: '4857'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kıdem ve İhbar Tazminatı Hesabı

## Görev
Kıdem (mülga 1475 m.14) ve ihbar (İş K. m.17) tazminatına hak kazanma şartlarını denetlemek ve giydirilmiş ücret üzerinden tutarı hesaplamak.

## Soğuk başlangıç (intake)
1. İşe giriş ve çıkış tarihleri; fasılalı çalışma var mı?
2. Fesheden taraf ve fesih sebebi nedir?
3. Son brüt çıplak ücret ve düzenli ekler (yol, yemek, ikramiye, prim) nelerdir?
4. Fesih tarihi hangi yıla ait (kıdem tavanı için)?

## Denetim şeması
1. **Kıdeme hak kazanma (1475 m.14):** En az **1 yıl** kıdem ve hak kazandıran fesih: işveren feshi (m.25/II hariç), işçinin haklı feshi (m.24), erkek için muvazzaf askerlik, kadın için evlilik (1 yıl içinde), emeklilik/yaşlılık aylığı şartlarını sağlama, ölüm. İstifa kural olarak kıdeme hak kazandırmaz.
2. **Kıdem hesabı:** Her tam yıl için **30 günlük** giydirilmiş brüt ücret; artan süreler oranlanır. Giydirilmiş ücrete düzenli ve süreklilik arz eden sosyal yardımlar dahil; arızi ödemeler hariç. **Kıdem tavanı** uygulanır (en yüksek devlet memuruna ödenen bir yıllık emekli ikramiyesi tutarı) — güncel tavan [DOĞRULANMADI]. Kıdem tazminatından yalnızca damga vergisi kesilir, gelir vergisi kesilmez.
3. **İhbar (m.17):** Belirsiz süreli sözleşmede öneller: 0-6 ay → 2 hafta, 6 ay-1,5 yıl → 4 hafta, 1,5-3 yıl → 6 hafta, 3 yıldan fazla → 8 hafta. Önele uymayan taraf, önel süresine ait ücret tutarında ihbar tazminatı öder. İşçinin haklı feshinde (m.24) işçi ihbara hak kazanmaz; işverenin haklı feshinde (m.25) ihbar doğmaz.
4. **Ara sonuç:** Kıdem giydirilmiş ücret + tavan; ihbar giydirilmiş ücret üzerinden, tavansız. İhbar tazminatından gelir ve damga vergisi kesilir.
5. **Faiz:** Kıdeme **fesih tarihinden** en yüksek banka mevduat faizi; ihbara temerrüt/dava tarihinden yasal faiz.

## Çıktı modülleri
- Hak kazanma değerlendirmesi (kıdem ve ihbar ayrı ayrı).
- Giydirilmiş ücret tablosu (kalem kalem).
- Tutar hesabı + tavan kontrolü + faiz başlangıcı.
- Vergi kesintisi notu ve [DOĞRULANMADI] güncel tavan.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

