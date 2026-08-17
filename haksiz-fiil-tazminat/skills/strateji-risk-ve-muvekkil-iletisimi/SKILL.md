---
argument-hint: ''
description: Tazminat dosyasında dava açma, sulh veya bekleme arasında karar verirken;
  pozisyonun gücünü, maliyet-faydayı ve tahsil riskini değerlendirip müvekkile sade
  bir yol haritası sunmak için kullanılır.
name: strateji-risk-ve-muvekkil-iletisimi
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Strateji, Risk ve Müvekkil İletişimi

## Görev
Haksız fiil dosyasında pozisyonu değerlendirmek, dava/sulh/bekleme seçeneklerini maliyet-fayda ve tahsil riski üzerinden tartmak ve müvekkile sade Türkçe ile gerekçeli bir yol haritası sunmak. Kesin kazanç vaadi verilmez; varsayımlar açıkça yazılır.

## Soğuk başlangıç (intake)
- Müvekkilin hedefi ne (tazminat tahsili, ilkesel sonuç, hızlı çözüm)?
- Delillerin gücü ve karşı tarafın muhtemel savunması (hukuka uygunluk, müterafik kusur, zamanaşımı)?
- Zaman baskısı (yaklaşan zamanaşımı/öğrenme süresi)?
- Karşı tarafın ödeme gücü ve müvekkilin risk-bütçe iştahı?

## Denetim şeması
1. **Pozisyon analizi.** Beş unsuru ve indirim sebeplerini delil gücüyle altla; zayıf halkayı (örn. illiyet ispatı, öğrenme tarihi belirsizliği) belirginleştir. Kusursuz sorumluluk normunun varlığı pozisyonu güçlendirir.
2. **Senaryo matrisi.** En iyi/orta/en kötü sonuç ve kazanma olasılığı kaba bant (yüksek/orta/düşük) olarak; kesin oran vaadinden kaçınılır. İndirim ve müterafik kusur etkisi tahmini tutara yansıtılır.
3. **Maliyet-fayda.** Nispi harç, bilirkişi/aktüer gideri, yargılama süresi (istinaf/temyiz), tahsil kabiliyeti (karşı tarafın/sigortanın ödeme gücü). Düşük tutarlı/yüksek belirsizlikli işte sulh öne alınır.
4. **Süre ve usul riski.** Yakın zamanaşımı (m.72), görev-yetki hatası, dava türü seçimi gibi riskler önceliklenir; gerekirse ihtiyati haciz/tedbir (İİK m.257; HMK m.389) değerlendirilir.
5. **Strateji seçimi.** İhtarname → müzakere/sulh → dava sıralaması; sigortacıya doğrudan başvuru imkânı; delil tespiti ihtiyacı (HMK m.400). Sulh için makul aralık ve kozlar belirlenir.
6. **Müvekkil iletişimi.** Hukuki sonuç sade Türkçe ile; seçeneklerin artı/eksisi, önerilen adım ve varsayımlar açık yazılır; `[DOĞRULANMADI]` veriler ve kesin kazanç taahhüdü verilmediği belirtilir. Ara sonuç: önerilen yol + gerekçe + sonraki adımlar.

## Çıktı modülleri
- Risk haritası (unsur-delil-zayıflık tablosu).
- Senaryo ve maliyet-fayda özeti (sulh aralığı dahil).
- Müvekkile sade bilgilendirme notu ve aksiyon planı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

