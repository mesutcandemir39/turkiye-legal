---
argument-hint: ''
description: Riziko gerçekleştikten sonra ihbar yükümlülüğü, teminat-istisna değerlendirmesi
  ve zarar/tazminat hesabı yapılması gerektiğinde kullanılır; eksik/aşkın sigorta
  ve muafiyet düşümlerini içeren tazminat
name: riziko-tazminat
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


# Rizikonun Gerçekleşmesi, İhbar ve Tazminatın Belirlenmesi

## Görev
Gerçekleşen olayın teminat kapsamına girip girmediğini, ihbar yükümlülüğünün yerine getirilip getirilmediğini ve ödenecek tazminatın miktarını (tazminat ilkesi, eksik/aşkın sigorta, muafiyet) belirlemek.

## Soğuk başlangıç (intake)
1. Riziko ne zaman, nerede ve nasıl gerçekleşti; olay teminat tanımına uyuyor mu?
2. Sigortacıya ihbar yapıldı mı, ne zaman?
3. Sigorta bedeli ile rizikoya konu malın gerçek değeri nedir (eksik/aşkın sigorta)?
4. Muafiyet, sovtaj (kurtarılan kıymet), eksper raporu var mı?

## Denetim şeması
1. **Riziko-teminat eşleştirmesi.** Olay, poliçe ve genel şartlardaki teminat tanımına giriyor mu? İstisna kapsamında mı (örn. kasko genel şartlarında alkollü araç kullanımı)? İspat: teminatı sigortalı, istisnayı sigortacı.
2. **İhbar yükümlülüğü.** TTK m.1446: sigorta ettiren, rizikonun gerçekleştiğini öğrendikten sonra gecikmeksizin sigortacıya bildirir. m.1447: ihbarın ihmali, sigortacının ödeyeceği tazminatı artırdığı ölçüde indirim sebebidir (kasıtta tam, kusurda artış oranında). Ara sonuç: ihbar zamanında mı?
3. **Tazminat ilkesi.** TTK m.1459: zarar sigortasında sigortalı, gerçek zararından fazlasını isteyemez (zenginleşme yasağı).
4. **Eksik/aşkın sigorta.** TTK m.1462 (eksik sigorta — sigorta bedeli değerden düşükse oranlama/nispet kuralı); m.1463 (aşkın sigorta — bedel değeri aşarsa aşan kısım geçersiz, kötüniyet halinde sonuçları). m.1461 birden çok sigorta.
5. **Düşümler.** Muafiyet (tenzili/entegral), sovtaj değeri, daha önce ödenen tazminat düşülür. Can sigortasında tazminat ilkesi uygulanmaz; sigorta bedeli ödenir (TTK m.1487 vd.).

## Çıktı modülleri
- Riziko-teminat-istisna eşleştirme tablosu.
- İhbar zamanlaması ve indirim değerlendirmesi.
- Tazminat hesabı (gerçek zarar / oranlama / muafiyet / sovtaj).
- Talep edilebilir net tutar ve dayanak maddeleri.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

