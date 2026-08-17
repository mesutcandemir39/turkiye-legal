---
argument-hint: ''
description: Eczacının hatalı ilaç verme, danışmanlık, sır saklama ve oda disiplin
  sorumluluğu ile hastaya karşı tazminat sorumluluğu konularında kullanılır.
name: eczaci-meslek-disiplin-sorumluluk
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
  - ad: Hemşirelik Kanunu
    numara: '6197'
    tur: kanun
  - ad: Mimar ve Mühendisler Hakkında Kanun
    numara: '1262'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Eczacının Meslek, Disiplin ve Tazminat Sorumluluğu

## Görev
Eczacının mesleki kusurundan (yanlış ilaç/doz, danışmanlık eksikliği, reçeteye aykırı verme) doğan disiplin, hukuki ve cezai sorumluluğunu değerlendirmek.

## Soğuk başlangıç (intake)
- İddia: yanlış ilaç/doz verme, muadil değişimi, reçeteye aykırılık, danışmanlık eksikliği, sır ihlali mi?
- Hastada zarar doğdu mu; nedensellik kuruluyor mu?
- Süreç: hasta şikâyeti, eczacı odası disiplin, savcılık, tazminat davası?
- Reçete ve teslim kaydı (varsa kamera/İTS) mevcut mu?

## Denetim şeması
1. **Sorumluluk türleri.** Disiplin (eczacı odası/Türk Eczacıları Birliği mevzuatı), hukuki tazminat (TBK m.49 vd. haksız fiil veya hasta-eczane ilişkisinde sözleşmesel sorumluluk), cezai (taksirle yaralama TCK m.89 / öldürme m.85).
2. **Kusur ve özen.** Eczacının uzman özen yükümlülüğü: reçeteyi kontrol, etkileşim uyarısı, doğru ürün/doz teslimi, muadil kuralları. Ara sonuç: özen yükümlülüğü ihlal edildi mi (objektif özen ölçütü)?
3. **Nedensellik ve zarar.** Hatalı teslim ile zarar arasında uygun illiyet; hastanın kendi kusuru/araya giren etken müterafık kusur (TBK m.52) doğurabilir. İspat: kusuru/zararı davacı; özenli davranışı eczacı belgelemeye çalışır.
4. **Sır saklama ve veri.** Hasta sağlık verisi özel nitelikli kişisel veridir (KVKK m.6); ifşa hem disiplin hem tazminat hem ceza (TCK m.136) sorumluluğu doğurabilir.
5. **Süre.** Haksız fiilde TBK m.72 zamanaşımı; ceza zamanaşımı uzunsa o uygulanır.

## Çıktı modülleri
- Sorumluluk türü ve görevli mercilere göre ayrıştırma.
- Kusur-nedensellik-zarar altlama notu.
- Disiplin savunması / tazminat dava değerlendirmesi [doldurulacak].



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

