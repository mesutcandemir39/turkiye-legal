---
argument-hint: ''
description: Lafzen açık kuralın uygulamada nasıl farklı sonuç verdiği, içtihat istikrarsızlığı
  veya yargıcın takdirini etkileyen kurum-dışı etkenler tartışıldığında; Amerikan/İskandinav
  realizmi ve menfaatler içt
name: hukuki-realizm-ve-yargi-davranisi
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


# Hukuki Realizm ve Yargısal Karar Davranışı

## Görev
"Kitaptaki hukuk" ile "uygulamadaki hukuk" arasındaki farkı çözümlemek; içtihadın neden
sapabildiğini, yargıcın takdir alanını ve karar gerekçesinin gerçek belirleyicilerini realist
araçlarla incelemek. Amaç gerekçeyi küçümsemek değil, öngörülebilirliği artırmaktır.

## Soğuk başlangıç (intake)
- Lafzen açık görünen kural pratikte neden farklı uygulanıyor — somut bir karar serisi var mı?
- Daireler/mahkemeler arasında içtihat çelişkisi mi gözleniyor?
- Soru "norm ne der" mi, yoksa "mahkeme fiilen ne yapar/yapacak" mı (tahmin sorusu)?
- Takdir yetkisinin (TMK m.4) devrede olduğu bir alanda mıyız?

## Denetim şeması
1. **Realist ayrımı kur.** Kâğıt üstündeki kural (rule in books) ile fiilî karar pratiği
   (rule in action) ayrımını yap; realizm, kuralın değil yargıcın davranışının sonucu
   belirlediğini ileri sürer. Bunu mutlak değil, tahmin gücü artıran bir merceğe çevir.
2. **Takdir alanını haritalandır.** TMK m.4 (hâkimin hukuka ve hakkaniyete göre takdiri),
   TBK m.51 (tazminatın belirlenmesi), m.52 (indirim) gibi takdir tanıyan normlarda sonucun
   öngörülemezliği yapısaldır; burada realist analiz en güçlüdür.
3. **Menfaat dengesini oku.** Menfaatler içtihadı (Heck) ışığında, kararın hangi çatışan
   menfaati hangi gerekçeyle üstün tuttuğunu çıkar; yargıcın "gerçek gerekçesi" çoğu zaman
   menfaat tartımıdır. Bunu lafzî gerekçeyle karşılaştır.
4. **İstikrar/sapma analizi.** İçtihat çelişkisi varsa, içtihadı birleştirme kararı (HMK m.;
   Yargıtay Kanunu ilgili hükümleri) yolunu ve birleştirme kararının bağlayıcılığını işaretle;
   somut karar serisini künyeleriyle ele al, doğrulanmadıkça [DOĞRULANMADI]. Ara sonuç:
   öngörülebilirlik tahmini.
5. **Strateji çıktısı.** Realist analiz, müvekkile "kazanma olasılığı" sunarken normatif
   argümanın yerine değil yanına konur; etik sınır (uydurma değil, gözlemlenen eğilim) korunur.

## Çıktı modülleri
- Kâğıt-pratik fark notu.
- Takdir alanı haritası (madde atıflarıyla).
- Menfaat tartımı çözümlemesi.
- Öngörülebilirlik/strateji değerlendirmesi (içtihat künyeleri [DOĞRULANMADI]).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

