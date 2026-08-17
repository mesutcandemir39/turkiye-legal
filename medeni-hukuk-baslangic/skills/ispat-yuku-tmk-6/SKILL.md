---
argument-hint: ''
description: Bir davada hangi tarafın hangi vakıayı ispatla yükümlü olduğu, karinelerin
  ve aksini ispat yükünün nasıl dağılacağı tartışıldığında TMK m.6 ve HMK m.190 ile
  ispat yükü haritasını çıkarmak için kullanı
name: ispat-yuku-tmk-6
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İspat Yükünün Dağılımı (TMK m.6)

## Görev
Uyuşmazlıktaki her çekişmeli vakıa için ispat yükünün hangi tarafta olduğunu TMK m.6 ve HMK m.190 temel kuralı ile karineler çerçevesinde belirlemek; ispatsız kalan vakıanın sonucunu göstermek.

## Soğuk başlangıç (intake)
- Çekişmeli (ispat gerektiren) vakıalar nelerdir; çekişmesiz/ikrar edilen hangileri?
- Talep eden hangi hak doğurucu vakıaları ileri sürüyor; davalı hangi hak engelleyici/düşürücü/bozucu itirazları?
- Olayda yasal bir karine var mı (ör. iyiniyet TMK m.3/1, tapu/sicil TMK m.7, m.1023)?
- Kanunda ispat yükünü tersine çeviren özel bir hüküm var mı?

## Denetim şeması
1. **Temel kural** — TMK m.6 / HMK m.190/1: kanunda aksine hüküm bulunmadıkça, taraflardan her biri *hakkını dayandırdığı olguların* varlığını ispatla yükümlüdür. Hak doğurucu vakıaları talep eden, karşı (engelleyici/bozucu/düşürücü) vakıaları ileri süren ispatlar.
2. **Vakıa türüne göre dağılım** — Davacı: hakkın doğumunun şartları. Davalı: ödeme, ibra, zamanaşımı, irade sakatlığı, sözleşmenin geçersizliği gibi savunma vakıaları.
3. **Karinelerin etkisi** — Yasal karine (ör. iyiniyet TMK m.3/1, resmî sicil/senedin doğruluğu TMK m.7) lehine olan taraf ispat yükünden kurtulur; aksini iddia eden *aksini ispat* yükü altına girer. Fiilî karineler (hayatın olağan akışı) yükü tersine çevirmez, sadece takdiri etkiler.
4. **Aksine hüküm** — Kanun bazı hâllerde yükü çevirir (ör. kusursuzluğu ispat, ayıptan sorumlulukta bazı varsayımlar). Bu özel hükümler m.6'nın temel kuralının önüne geçer.
5. **İspat ölçüsü ve sonuç** — Çekişmeli vakıa tam ispat (HMK) ölçüsünde kanıtlanamazsa, o vakıa *gerçekleşmemiş* sayılır ve ispat yükü kimde ise aleyhine sonuç doğar (ispat yükünün "son sözü").
6. **Senetle ispat sınırı** — HMK m.200-201: belirli tutarın üzerindeki hukuki işlemler kural olarak senetle ispatlanır; tanıkla ispat sınırı ve istisnaları gözetilir.

## Çıktı modülleri
- Çekişmeli vakıa listesi (davacı/davalı yükü ayrımı).
- Karine tablosu ve aksini ispat yükü.
- "Aksine hüküm" kontrolü (yük çevrildi mi).
- İspatsız vakıanın sonucu + ilkesel içtihat `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

