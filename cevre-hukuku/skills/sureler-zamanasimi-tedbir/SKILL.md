---
argument-hint: ''
description: Dava açma süreleri, idari para cezası tahsil/karar zamanaşımı, tazminatta
  zamanaşımı ile yürütmenin durdurulması ve ihtiyati tedbir taleplerinin zamanlamasında;
  telafisi güç zararın önlenmesi için aci
name: sureler-zamanasimi-tedbir
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
  - ad: Çevre Kanunu
    numara: '2872'
    tur: kanun
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler, Zamanaşımı ve İhtiyati Tedbir

## Görev
Çevresel uyuşmazlıkta tüm süre ve zamanaşımı eşiklerini hesaplamak; telafisi güç/imkânsız zararı önlemek için yürütmenin durdurulması ve ihtiyati tedbir taleplerini doğru zamanda hazırlamak.

## Soğuk başlangıç (intake)
1. Hangi işlem/karar/fiil söz konusu; tebliğ/ilan/öğrenme tarihi nedir?
2. Talep idari mi (iptal/tam yargı) yoksa özel hukuk mu (tazminat/el atma)?
3. Devam eden ve telafisi güç bir zarar (geri dönüşü olmayan tahribat) var mı?
4. Daha önce idari başvuru/itiraz yapıldı mı; süre durduran bir işlem var mı?

## Denetim şeması
1. **İdari dava süresi**: İptal ve tam yargı davalarında kural süre 60 gündür (2577 sayılı İYUK m.7); ÇED ve izin işlemlerinde ilan/askı ve öğrenme tarihinin tespiti kritiktir. İYUK m.11 kapsamında idari başvuru süreyi durdurabilir.
2. **İdari yaptırım zamanaşımı**: İdari para cezalarında 5326 sayılı Kabahatler Kanunu m.20 (soruşturma) ve m.21 (yerine getirme) zamanaşımı süreleri uygulanır; süre dolmuşsa ceza verilemez/tahsil edilemez.
3. **Özel hukuk zamanaşımı**: Haksız fiil tazminatında TBK m.72 — zarar ve failin öğrenilmesinden itibaren 2 yıl ve her hâlde 10 yıl; fiil aynı zamanda suç ise daha uzun ceza zamanaşımı uygulanır. Devam eden (sürekli) kirlilikte zamanaşımının başlangıcı tartışmalıdır, fiil devam ettikçe yeniden işlemeye başlayabilir.
4. **Acil koruma**: İdari yargıda yürütmenin durdurulması (İYUK m.27 — açıkça hukuka aykırılık + telafisi güç zarar); adli yargıda ihtiyati tedbir (HMK m.389) ve delil tespiti (HMK m.400). Çevresel tahribatın geri döndürülemezliği "telafisi güç zarar" ölçütünü güçlü kılar.
5. **Ara sonuç**: Tüm süreler tek takvimde toplanır; en yakın eşik ve acil tedbir ihtiyacı kırmızı işaretlenir.

## Çıktı modülleri
- Süre ve zamanaşımı takvimi (idari + özel hukuk)
- Süre başlangıcı/durması analizi
- Yürütmenin durdurulması / ihtiyati tedbir talebi taslağı
- Delil tespiti başvuru iskeleti



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

