---
argument-hint: ''
description: Tıbbi uyuşmazlıkta hangi mahkemenin görevli ve yetkili olduğunu, hangi
  dava türünün açılacağını ve dava şartlarını belirlemek için kullanılır; adli/idari
  yargı ayrımını çözer.
name: dava-usul-gorev-yetki
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
  - ad: Banka Muhasebe Sistemi Hakkında Kanun
    numara: '1219'
    tur: kanun
  - ad: Gayrimenkul Ek Vergisi Hakkında Kanun
    numara: '3359'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dava, Usul ve Görev-Yetki

## Görev
Tıbbi uyuşmazlıkta doğru yargı kolu, görevli/yetkili mahkeme, dava türü ve dava şartlarını (özellikle arabuluculuk) saptamak.

## Soğuk başlangıç (intake)
1. Davalı kim: hekim, özel hastane, kamu idaresi, sigorta?
2. Müdahale kamu mu özel sağlık kuruluşunda mı yapıldı?
3. Talep tazminat mı, şikâyet mi, hizmet kusuru mu?
4. Zarar tarihi ve varsa öğrenme tarihi?

## Denetim şeması
1. **Yargı kolu**: Özel hastane/muayenehane → adli yargı. Kamu hastanesi → idari yargı (tam yargı davası, İYUK m.2, m.12-13). Hekime karşı kişisel dava 3359 Ek m.18 nedeniyle kural olarak idareye yöneltilir.
2. **Görevli mahkeme (adli)**: Hasta-özel hastane ilişkisi çoğu kez tüketici işlemi sayılır → Tüketici Mahkemesi (6502). Tacir/şirket taraf veya tüketici niteliği yoksa Asliye Hukuk. Ceza yönü için Asliye Ceza.
3. **Dava şartı arabuluculuk**: Tüketici ve ticari uyuşmazlık niteliğine göre 6325/6502 kapsamında zorunlu arabuluculuk gündeme gelir; idari davada uygulanmaz.
4. **İdari yolun ön şartı**: Tam yargı davasından önce İYUK m.13 uyarınca idareye başvuru ve süreler.
5. **Yetki**: HMK m.6 (davalı yerleşim yeri), haksız fiilde HMK m.16 (haksız fiilin işlendiği/zararın doğduğu yer). İdari davada İYUK m.33 vd.
6. **Dava şartları**: HMK m.114-115 (görev, yetki kesin ise, hukuki yarar, taraf ehliyeti). Ara sonuç: yanlış yargı kolunda açılan dava görevsizlik/yargı yolu reddi ile sonuçlanır.

## Çıktı modülleri
- Yargı kolu ve görevli/yetkili mahkeme tespiti
- Dava türü ve dava şartı kontrol listesi
- Arabuluculuk zorunluluğu değerlendirmesi
- Husumet (doğru davalı) tablosu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

