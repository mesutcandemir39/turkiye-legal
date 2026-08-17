---
argument-hint: ''
description: Arsa sahibi ile yüklenici arasında daire/bağımsız bölüm karşılığı inşaat
  anlaşması yapılması, ihlali veya tasfiyesi söz konusu olduğunda; sözleşmenin kuruluşu,
  gecikme/ayıp, fesih-dönme ve üçüncü kişi
name: kat-karsiligi-insaat
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kat Karşılığı (Arsa Payı Karşılığı) İnşaat Sözleşmesi

## Görev
Karma (atipik) nitelikteki kat karşılığı inşaat ilişkisini kurmak ve uyuşmazlığını çözmek: yüklenicinin inşa ve devir borçları ile arsa sahibinin arsa payı devri borcunu dengelemek; gecikme, ayıp ve eksik iş hâllerinde dönme/fesih ile tazminat yollarını belirlemek; daire alan üçüncü kişilerin durumunu çözmek.

## Soğuk başlangıç (intake)
- Sözleşme noterde resmî şekilde mi yapıldı; arsa payları/bağımsız bölüm paylaşımı net mi?
- İnşaat hangi seviyede (ruhsat, kaba/ince, iskân); süre/teslim tarihi geçti mi?
- Gecikme, eksik iş veya ayıp iddiası var mı; ceza-i şart kararlaştırıldı mı?
- Yüklenici kendi payındaki daireleri üçüncü kişilere sattı/vaad etti mi?

## Denetim şeması
1. **Hukuki nitelik ve şekil**: Sözleşme, eser (TBK m.470 vd.) ile taşınmaz devri (satış vaadi) unsurlarını birleştiren karma sözleşmedir; taşınmaz devri içerdiğinden resmî şekle tabidir (noterde düzenleme; TBK m.29, m.237). Şekle aykırılık kural olarak hükümsüzlük doğurur (TBK m.27); fakat inşaatın önemli ölçüde tamamlanması hâlinde şekil eksikliğini ileri sürmek dürüstlük kuralına aykırı olabilir (TMK m.2).
2. **Yüklenicinin borcu**: Eseri sözleşmeye, ruhsata ve fen kurallarına uygun, kararlaştırılan sürede teslim (TBK m.470, m.473). Gecikmede temerrüt hükümleri ve varsa cezai şart (TBK m.179) işler.
3. **Ayıp ve eksik iş**: Ayıba karşı tekeffül (TBK m.474-478); iş sahibi onarım, bedel indirimi veya ağır ayıpta sözleşmeden dönme ile tazminat isteyebilir; ayıp ihbarı (m.474) ve süreler gözetilir.
4. **Dönme/fesih**: Yüklenicinin temerrüdünde TBK m.123-125 (süre verme/dönme) ile m.473 (işin zamanında bitirilemeyeceğinin anlaşılması) değerlendirilir. Geriye etkili dönme ile ileriye etkili fesih ayrımı, ifa derecesine göre belirlenir; kısmen ifada tasfiye ilişkisi kurulur.
5. **Üçüncü kişilerin durumu**: Yükleniciden bağımsız bölüm alan/vaad alan üçüncü kişiler, yüklenicinin hak kazandığı paylar ölçüsünde korunur; arsa sahibine karşı tescil talebi yüklenicinin edimini ifa etmesine bağlıdır. Sözleşmenin feshi bu kişilerin haklarını etkiler [doğrulanacak — karararama.yargitay.gov.tr].
6. **Ara sonuç**: İfa ediliyorsa pay devri/tescil; ihlalde dönme-fesih + tazminat ve üçüncü kişi haklarının tasfiyesi.

## Çıktı modülleri
- Kat karşılığı inşaat sözleşmesi ana hat taslağı (paylaşım tablosu, süre, ceza-i şart, teslim) [doldurulacak].
- Temerrüt/dönme veya ayıp ihtarı taslağı (süre verme, talepler).
- Üçüncü kişi (daire alan) hak durumu analizi ve tasfiye notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

