---
argument-hint: ''
description: Bir enerji uyuşmazlığında idari yargı mı adli yargı mı tahkim mi gerektiği,
  görevli mahkeme, dava açma süresi ve yürütmenin durdurulması belirsiz olduğunda
  kullanılır.
name: enerji-uyusmazlik-yargi-yol
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
  - ad: Elektrik Piyasası Kanunu
    numara: '6446'
    tur: kanun
  - ad: Mühendislik ve Mimarlık Meslek Kanunu
    numara: '4646'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Enerji Uyuşmazlıklarında Yargı Yolu ve Görev-Yetki

## Görev
Enerji uyuşmazlığını doğru yargı koluna, görevli/yetkili mahkemeye veya tahkime yönlendirmek; dava açma süresini ve yürütmeyi durdurma ihtiyacını net biçimde tespit etmek.

## Soğuk başlangıç (intake)
1. Uyuşmazlığın kaynağı EPDK işlemi mi, sözleşme mi, haksız fiil/alacak mı?
2. İlgili sözleşmede tahkim/yetki şartı var mı?
3. Tebliğ/öğrenme tarihi nedir; süre işliyor mu?
4. Acil koruma (yürütmenin durdurulması/ihtiyati tedbir) ihtiyacı var mı?

## Denetim şeması
1. **Yargı kolu ayrımı**: EPDK/idare işlemi → idari yargı (İYUK). Tarafların özel hukuk ilişkisinden doğan alacak/sözleşme → adli yargı; tahkim şartı varsa tahkim. Ara sonuç: hangi yargı kolu.
2. **İdari yargı**: İYUK m.2 iptal/tam yargı; m.7 dava açma süresi (kural 60 gün, özel kanun süresi varsa o); m.27 yürütmenin durdurulması (telafisi güç zarar + açık hukuka aykırılık). Görevli yer kural olarak idare mahkemesi; konuya göre Danıştay ilk derece.
3. **Adli yargı**: Ticari nitelikli enerji sözleşmelerinde asliye ticaret mahkemesi (TTK m.4-5); HMK m.6 yetki ve sözleşmedeki yetki şartı. İhtiyati tedbir HMK m.389 vd.
4. **Tahkim**: Geçerli tahkim şartında (HMK m.412 / 4686) hakem yargılaması; hakem kararının iptali (HMK m.439) ve milletlerarası unsurlu işlemde tenfiz.
5. **Süre disiplini**: İdari ve adli sürelerin ayrı işlediği, hak düşürücü süre/zamanaşımı karışıklığı en sık hata; süre takvimi sabitlenmeden dilekçe yazılmaz.

## Çıktı modülleri
- Yargı yolu ve görevli/yetkili merci tespiti.
- Süre takvimi ve YD/ihtiyati tedbir ihtiyaç notu.
- Yanlış mercie başvuru riski uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

