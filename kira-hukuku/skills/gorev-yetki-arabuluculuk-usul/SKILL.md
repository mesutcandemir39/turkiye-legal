---
argument-hint: ''
description: Kira uyuşmazlığında hangi mahkemenin görevli ve yetkili olduğu, dava
  açmadan önce arabuluculuğa başvuru zorunluluğu, basit yargılama usulü veya süreler
  söz konusu olduğunda bu beceriyi kullan.
name: gorev-yetki-arabuluculuk-usul
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


# Görev, Yetki, Dava Şartı Arabuluculuk ve Usul

## Görev
Kira uyuşmazlığını doğru mahkeme önüne ve doğru usule oturtmak: görev (sulh hukuk), yetki, zorunlu arabuluculuk dava şartı ve uygulanacak yargılama usulünü belirlemek; usuli ön engelleri baştan elemek.

## Soğuk başlangıç (intake)
- Talep ne (tahliye, kira tespiti, alacak, depozito iadesi)?
- Taşınmaz nerede, taraflar nerede ikamet ediyor?
- Arabuluculuğa başvuruldu mu; son tutanak var mı?
- Sözleşmede yetki kaydı veya tahkim şartı var mı?

## Denetim şeması
1. **Görev (HMK m.4/1-a)**: Kira ilişkisinden doğan **alacak ve tahliye** davaları ile kira tespiti davalarında **sulh hukuk mahkemesi** görevlidir; değer ve miktara bakılmaz.
2. **Yetki (HMK m.6, m.10)**: Genel yetki davalının yerleşim yeri; sözleşmeden doğan davalarda **ifa yeri** mahkemesi de yetkilidir (m.10). Taşınmaza ilişkin ayni nitelik taşımadığından kira davalarında kesin yetki kural değildir; sözleşmesel yetki kaydı denetlenir.
3. **Dava şartı arabuluculuk (HUAK m.18/A)**: 1.9.2023'ten itibaren **kira ilişkisinden kaynaklanan uyuşmazlıklar** (tahliye dahil, taşınmazın aynına ilişkin olmayanlar) dava açmadan önce **arabuluculuğa başvuru** dava şartıdır. Son tutanak dilekçeye eklenmezse dava usulden reddedilir. İlamsız icra/ihtiyati tedbir bu şartın istisnasıdır.
4. **Yargılama usulü (HMK m.316)**: Kira ilişkisinden doğan tahliye dahil uyuşmazlıklar **basit yargılama usulüne** tabidir; dilekçeler tek, süreler kısa, ön inceleme ve tahkikat sıkışıktır.
5. **Süreler ve hak düşürücü kontrol**: Tahliye sebebine bağlı bir aylık dava süreleri (TBK m.353), tespit davası süre penceresi (m.345) baştan takvimlenir.
6. **Ara sonuç**: Görevli-yetkili mahkeme + arabuluculuk durumu + usul + kritik süreler.

## Çıktı modülleri
- Görev-yetki tespit notu.
- Arabuluculuk başvuru/uygunluk kontrol listesi.
- Usul ve süre takvimi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

