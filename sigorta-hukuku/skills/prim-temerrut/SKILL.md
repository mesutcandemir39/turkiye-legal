---
argument-hint: ''
description: Primin ödenmemesi nedeniyle teminatın askıya alınması, sözleşmenin feshi
  veya rizikonun primsiz dönemde gerçekleşmesi tartışıldığında kullanılır; prim temerrüdünün
  sigortacının sorumluluğuna etkisini
name: prim-temerrut
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  - ad: Bankalar Kanunu
    numara: '5684'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Prim Ödeme Borcu ve Temerrüt

## Görev
Primin (ilk veya takip eden taksit) zamanında ödenip ödenmediğini, ödenmemenin teminata ve sigortacının sorumluluğuna etkisini, fesih ve askı sonuçlarını belirlemek.

## Soğuk başlangıç (intake)
1. Hangi prim ödenmedi: ilk prim mi, takip eden taksit mi?
2. Ödeme tarihi ve vadesi ne; kısmi ödeme var mı?
3. Sigortacı ihtar/uyarı gönderdi mi, fesih iradesi açıklandı mı?
4. Riziko hangi tarihte gerçekleşti — prim borcu var iken mi?

## Denetim şeması
1. **Borcun niteliği.** TTK m.1430: prim, sözleşmede kararlaştırılan tutar ve vadede ödenir; götürülecek borçtur. Ara sonuç: hangi prim, hangi vade?
2. **İlk primde temerrüt.** TTK m.1430/3 ve genel şartlar: ilk taksit/peşin prim ödenmeden sigortacının sorumluluğu başlamaz; bu dönemde gerçekleşen riziko karşılanmaz.
3. **Takip eden primde temerrüt.** TTK m.1434: sigortacı, ödememe halinde sigorta ettirene noter aracılığıyla ya da iadeli taahhütlü mektupla on günlük süre vererek borcun ödenmesini ister. Süre sonunda ödeme yapılmazsa sözleşme feshedilmiş sayılır; ihtarda bu sonuç belirtilmelidir.
4. **Askı/sorumluluk boşluğu.** İhtar süresince ve fesihten sonra gerçekleşen rizikoda sigortacının sorumluluğu doğmaz. İstisna: usulüne uygun ihtar çekilmemişse fesih sonucu doğmaz; teminat devam eder.
5. **İspat.** Ödemeyi sigorta ettiren, usulüne uygun ihtarı ve feshi sigortacı ispatlar.

## Çıktı modülleri
- Prim ödeme/temerrüt zaman çizelgesi.
- İhtar usulü uygunluk kontrolü (m.1434).
- Riziko anında teminat durumu (var/askıda/fesihli).
- Sigortalı veya sigortacı için argüman seti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

