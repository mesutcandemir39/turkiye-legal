---
argument-hint: ''
description: Üretilmiş bir sade dil metnini kaynakla karşılaştırıp anlam kaybı, düşen
  hak/süre/şart ve yanıltıcı mutlaklaştırma açısından denetlemek; yayımdan önce risk
  kontrolü yapmak gerektiğinde kullanılır.
name: dogruluk-denetimi-risk
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


# Sadeleştirme Doğruluk Denetimi ve Risk Kontrolü

## Görev
Hazır bir sade dil metnini (özet, çeviri, bilgilendirme) kaynak hukuki belgeyle karşılaştırarak
denetlemek; anlam kaybı, düşen hak/süre/şart, yanıltıcı kesinlik ve kaynak hijyeni ihlali var mı
belirlemek. Bu beceri, metni yayımdan/iletmeden önceki son süzgeçtir.

## Soğuk başlangıç (intake)
1. Denetlenecek sade metin ve kaynağı elinizde mi (ikisi birlikte gerekir)?
2. Metin kime gidecek (risk eşiği okuyucuya göre değişir)?
3. Metinde tarih, tutar, süre, koşul gibi sayısal/şart içeren ifadeler var mı?

## Denetim şeması
1. SATIR KARŞILAŞTIRMA: Sade metnin her iddiası kaynaktaki karşılığına bağlanır; karşılığı
   olmayan ("uydurma") veya kaynakta olup metinden düşen unsur işaretlenir.
2. HAK/SÜRE/ŞART KAYBI (ispat yükü): Tüm süreler, tutarlar, koşullu ifadeler ("…hâlinde",
   "…koşuluyla", "…saklı kalmak kaydıyla") kaynakla birebir doğrulanır; mutlaklaştırma düzeltilir.
3. NÜANS DENETİMİ: Tehlikeli terimler (zamanaşımı/hak düşürücü süre, fesih/iptal/dönme,
   müteselsil/müşterek, def'i/itiraz) yanlış eşanlamlıyla değiştirilmiş mi kontrol edilir.
4. KAYNAK HİJYENİ: Atıflar madde/fıkra düzeyinde doğru mu; içtihat zikredilmişse künye
   (mahkeme/daire/esas-karar/tarih) doğrulanmış mı, uydurma numara var mı denetlenir; teyit için
   karararama.yargitay.gov.tr, karararama.danistay.gov.tr, mevzuat.gov.tr kullanılır.
5. YANILTICI KESİNLİK: "Kesinlikle kazanırsınız" gibi vaatler, hukuki tavsiye yerine geçen ifadeler
   ve eksik çekince taranır; beklenti yönetimi notu eklenir.
6. ARA SONUÇ: Bulgular düzeltildi mi; "[DOĞRULANMADI]"/"[doldurulacak]" yer tutucuları yerinde mi.

## Çıktı modülleri
- Denetim bulguları tablosu (düşen / eklenen / mutlaklaştırılan / yanlış terim).
- Düzeltilmiş sade metin veya düzeltme önerileri.
- Kaynak hijyeni kontrol satırı.
- Kalan belirsizlikler ve okuyucuya çekince notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

