---
argument-hint: ''
description: Bir şirket uyuşmazlığında görevli mahkeme (asliye ticaret), yetki, ticari
  dava niteliği, arabuluculuk dava şartı, ihtiyati tedbir ve süreler belirlenirken;
  doğru usul rotasını ve süreleri kaçırmamak i
name: sirket-uyusmazligi-dava-gorev-yetki
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


# Şirket Uyuşmazlıklarında Dava, Görev ve Yetki

## Görev
Şirket kaynaklı uyuşmazlığı doğru usul rotasına oturtmak: ticari dava niteliği, görevli/yetkili mahkeme, dava şartı arabuluculuk, ihtiyati tedbir ve hak düşürücü süreler.

## Soğuk başlangıç (intake)
1. Uyuşmazlık türü ne (genel kurul iptali, sorumluluk, pay devri, fesih, alacak)?
2. Taraflar tacir mi; uyuşmazlık mutlak ticari dava mı (TTK m.4)?
3. Konusu para alacağı mı (dava şartı arabuluculuk gerekir mi)?
4. Hak düşürücü/zamanaşımı süresi işliyor mu (ör. iptal 3 ay)?
5. Acil koruma (ihtiyati tedbir, kararın icrasının ertelenmesi) gerekiyor mu?

## Denetim şeması
1. Ticari dava niteliği: TTK m.4 (mutlak ticari davalar — TTK'dan doğanlar dâhil) ve m.5 (görev). Şirketler hukuku uyuşmazlıkları kural olarak ticari davadır.
2. Görev: Asliye ticaret mahkemesi (TTK m.5; 6102/6335 düzenlemeleri). Tek hâkim/heyet ayrımı parasal sınıra göre.
3. Yetki: Genel kurul iptali ve birçok şirket davası için şirket merkezi mahkemesi (ör. m.445/2). Genel yetki HMK m.6; sözleşmeden doğan alacakta HMK m.10.
4. Dava şartı arabuluculuk: Ticari davalarda konusu bir miktar para olan alacak/tazminat talepleri için dava açmadan önce arabuluculuk zorunlu (TTK m.5/A; 6325 sayılı HUAK ve ilgili düzenlemeler). İptal/tespit davaları kural olarak kapsam dışı — talebin niteliğini denetle.
5. Süreler: Genel kurul iptali 3 ay (m.445); sorumlulukta m.560 zamanaşımı; pay devrine bağlı talepler ilgili özel sürelere tabi. Süreyi en başta takvimle.
6. İhtiyati tedbir/koruma: HMK m.389 vd. tedbir; genel kurul kararının icrasının ertelenmesi m.449 (teminat).
7. İspat ve dava şartları: HMK m.114-115 dava şartları (görev, yetki kesin değilse ilk itiraz, arabuluculuk dava şartı); HMK m.190 ispat yükü.

## Çıktı modülleri
- Usul rotası kararı (görev-yetki-arabuluculuk-süre tablosu).
- Süre takvimi ve hak düşürücü süre uyarıları.
- İhtiyati tedbir/erteleme talebi taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

