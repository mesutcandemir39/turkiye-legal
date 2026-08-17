---
argument-hint: ''
description: Pay sahibinin genel kurulda vekille temsili, organ temsilcisi, tevdi
  eden ve bagimsiz temsilci, hazir bulunanlar listesi ve katilma hakki konularinda
  taslak veya denetim gerektiginde kullanilir.
name: temsil-vekalet-ve-katilim
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
  version: 0.1.0
user-invocable: true
---


# Temsil, Vekâlet ve Katılım

## Görev
Pay sahibinin genel kurula bizzat veya temsilci aracılığıyla katılımını düzenlemek; temsil belgelerini hazırlamak ve hazır bulunanlar listesinin doğruluğunu denetlemek.

## Soğuk başlangıç (intake)
1. Pay sahibi gerçek kişi mi, tüzel kişi mi; temsilci pay sahibi olmak zorunda mı (esas sözleşme şartı)?
2. Halka açık şirket mi (kurumsal temsilci/organın temsilcisi düzenlemeleri farklılaşır)?
3. Paylar bir bankaya/aracı kuruma mı tevdi edilmiş (tevdi eden temsilcisi)?
4. Temsil belgesi yazılı ve usulüne uygun mu; çıkar çatışması var mı?

## Denetim şeması
1. **Temsil ilkesi:** Pay sahibi paylarını GK'de temsilci aracılığıyla da kullandırabilir; temsilcinin pay sahibi olması şart değildir; esas sözleşmedeki aksine hüküm temsilci yönünden geçersizdir (m.425). Temsil için yazılı yetki belgesi gerekir.
2. **Özel temsilci türleri:** Organın temsilcisi, bağımsız temsilci ve kurumsal temsilci için çağrıda öneri yapılır ve şirketin internet sitesinde duyurulur (m.428); tevdi eden temsilcisi, payları tevdi eden adına oyu talimata uygun kullanır (m.429-430). Bu temsilciler talimat ve açıklama yükümlülüğüne tabidir.
3. **Hazır bulunanlar listesi:** Toplantıya katılanların ad, pay miktarı, oy sayısı ve temsil bilgileri listede gösterilir; liste YK ve toplantı başkanlığınca imzalanır (m.415, m.417). Liste, nisap ve oy hesabının temel ispat aracıdır.
4. **Çıkar çatışması:** Temsilcinin m.436 kapsamına giren işlerde oy kullanması yasaktır; vekâletin bu sınırı aşması iptal sebebi yaratır.
5. **İspat yükü/ara sonuç:** Temsil yetkisinin varlığını temsilci/pay sahibi belgeyle ispatlar. Geçersiz temsille kullanılan oylar nisap dışı bırakılır; sonuç değişiyorsa karar iptale açıktır.

## Çıktı modülleri
- Vekâletname/temsil belgesi taslağı (yetki kapsamı ve talimatlı).
- Hazır bulunanlar listesi şablonu.
- Temsil geçerlilik kontrol listesi ve çıkar çatışması uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

