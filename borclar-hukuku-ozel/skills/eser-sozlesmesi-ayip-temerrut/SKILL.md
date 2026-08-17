---
argument-hint: ''
description: İnşaat, imalat, tadilat veya yazılım gibi bir eserin ayıplı, geç veya
  eksik teslim edilmesi halinde iş sahibinin haklarını ve yüklenicinin sorumluluğunu
  denetlemek gerektiğinde kullanılır.
name: eser-sozlesmesi-ayip-temerrut
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


# Eser Sözleşmesi — Ayıp, Teslim ve Temerrüt

## Görev
Eserin (inşaat, imalat, tadilat, yazılım) ayıbı, gecikmesi veya bedel uyuşmazlığında tarafların haklarını TBK m.470-486 çerçevesinde denetlemek; ayıba karşı tekeffül ile temerrüt rejimini ayırmak.

## Soğuk başlangıç (intake)
- Eserin konusu ve teslim durumu (teslim edildi/edilmedi, kabul var mı)?
- Ayıp türü (gizli/açık, ağır/önemli); gözden geçirme yapıldı mı?
- Ücret götürü mü, yaklaşık mı; ek iş/imalat var mı?
- Gecikme varsa kesin vade/ihtar durumu?

## Denetim şeması
1. **Yüklenicinin özen ve sadakat borcu (m.471).** Malzeme yüklenicininse ayıba karşı satıcı gibi sorumlu; iş sahibininse uygun olmayan malzeme/talimatı bildirme yükü (m.472).
2. **Eseri gözden geçirme ve bildirim (m.477).** İş sahibi teslimden sonra imkân bulunca gözden geçirip ayıpları uygun sürede bildirir; aksi halde kabul edilmiş sayılır. Açıkça/örtülü kabul yüklenicinin sorumluluğunu (kasten gizlenen ayıp hariç) kaldırır.
3. **İş sahibinin seçimlik hakları (m.475).** Eser ayıplı ve kullanılamaz/kabul beklenemezse dönme; ayıbın giderilmesini isteme (aşırı masraf gerektirmiyorsa); bedelden indirim. Ayrıca yüklenicinin kusuru varsa tazminat.
4. **Ayıp sorumluluğu zamanaşımı (m.478).** Teslimden itibaren 2 yıl; taşınmaz yapılarda 5 yıl; yüklenicinin ağır kusuru varsa 20 yıl. Süreler kabul tarihiyle bağlantılı işletilir.
5. **Ücret ve ek iş (m.480-481).** Götürü bedelde kural olarak artırılamaz; olağanüstü hâl/aşırı ifa güçlüğünde hâkim uyarlayabilir (m.480/2; TBK m.138 ile birlikte). Yaklaşık bedel aşımında iş sahibinin dönme hakkı (m.481).
6. **Temerrüt/erken dönme (m.473).** İşe zamanında başlamama veya gecikme açıkça öngörülüyorsa iş sahibi süre vermeden dönebilir. İş sahibinin tazminatla fesih hakkı m.484. İspat: ayıbı iş sahibi, ayıbın iş sahibi malzeme/talimatından kaynaklandığını yüklenici ispatlar. Ara sonuç: hak-süre matrisi.

## Çıktı modülleri
- Ayıp bildirim ve onarım talebi yazısı.
- Bedelden indirim/dönme dava iskeleti.
- Götürü-yaklaşık bedel uyarlama notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

