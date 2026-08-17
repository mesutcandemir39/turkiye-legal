---
argument-hint: ''
description: SGK uyuşmazlıklarında görevli mahkeme (iş mahkemesi), yetki, idari başvuru/itiraz
  zorunluluğu ve dava açma süresi belirlenmesi gerektiğinde; davanın usulden reddini
  önlemek için ilk kontrol olarak kul
name: gorev-yetki-ve-idari-asama
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
  - ad: Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu
    numara: '5510'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Görev, Yetki ve İdari Aşama

## Görev
SGK uyuşmazlığında doğru yargı yolunu, görevli/yetkili mahkemeyi, idari başvuru zorunluluğunu ve süreleri saptayarak davanın usulden reddini önlemek.

## Soğuk başlangıç (intake)
- Uyuşmazlık SGK ile mi (sigortalılık, prim, aylık), işveren ile mi (rücu, alacak)?
- SGK'nın yazılı bir işlemi/red kararı var mı; tebliğ tarihi nedir?
- İdari itiraz/başvuru yapıldı mı; süresi geçti mi?
- Sigortalının ikametgâhı ve işyeri hangi yer mahkemesi çevresinde?

## Denetim şeması
1. Yargı yolu: Sigortalılık, prim, gelir/aylık ve hizmet tespiti adli yargıda; SGK'nın bazı genel düzenleyici/idari işlemleri idari yargıda görülebilir — işlemin niteliği ayrılır.
2. Görev — 7036 sayılı İş Mahkemeleri Kanunu m.5: SGK ile sigortalı/işveren arasındaki sosyal güvenlik uyuşmazlıkları iş mahkemelerinde görülür.
3. İdari aşama — 5510 m.101 ve İş Mahkemeleri Kanunu m.4: Kurumca verilen kararlara karşı dava açmadan önce SGK'ya itiraz/başvuru ve cevap beklenmesi koşulu; bu dava şartı niteliğindedir, atlanırsa dava usulden reddedilir.
4. Süre: İdari başvurunun reddi veya zımni red üzerine dava açma süresi (İş Mahkemeleri Kanunu m.4'teki süreler) hesaplanır.
5. Yetki — HMK m.6 ve özel kurallar: Genelde davalının yerleşim yeri; sosyal güvenlikte sigortalının ikametgâhı/işyeri yer mahkemesi de yetkili olabilir. Ara sonuç: yargı yolu + görev + yetki + süre haritası. İspat: SGK tebliğ ve başvuru belgeleri.

## Çıktı modülleri
- Yargı yolu/görev/yetki tespit notu.
- İdari başvuru ve süre takvimi (tebliğ-başvuru-red-dava).
- Usul riski uyarı listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

