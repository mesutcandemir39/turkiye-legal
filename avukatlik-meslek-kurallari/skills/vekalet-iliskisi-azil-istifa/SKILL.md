---
argument-hint: ''
description: Vekâletnamenin kapsamı, avukatın özen ve sadakat borcu, müvekkilin azil
  hakkı ile avukatın istifası ve bunların ücret-sorumluluk sonuçları söz konusu olduğunda
  kullanılır.
name: vekalet-iliskisi-azil-istifa
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
  - ad: Avukatlık Kanunu
    numara: '1136'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Vekâlet İlişkisinin Kurulması, Azil ve İstifa

## Görev
Avukat-müvekkil vekâlet ilişkisinin kurulması, kapsamı ve sona ermesini; azil/istifanın
haklılığını ve ücret-sorumluluk sonuçlarını belirlemek.

## Soğuk başlangıç (intake)
1. Vekâletname var mı; özel yetki gerektiren işlemler (sulh, feragat, kabul) kapsamda mı?
2. İlişki nasıl sona erdi (azil, istifa, işin bitmesi)?
3. Azil/istifanın somut sebebi haklı mı?
4. Devam eden süre/duruşma riski ve dosya teslimi durumu ne?

## Denetim şeması
1. **Kuruluş ve kapsam.** Vekâlet ilişkisi avukatlık sözleşmesiyle kurulur; temsil yetkisinin
   sınırı vekâletnamedir. Sulh, feragat, kabul, davadan vazgeçme, ibra gibi tasarruflar için
   vekâletnamede özel yetki şarttır (HMK m.74; TBK m.504/3). Ara sonuç: yapılan işlem yetki
   kapsamında mı?
2. **Özen ve sadakat.** Avukat işi özenle ve müvekkil yararına yürütür, talimatlara uyar,
   gelişmelerden bilgilendirir, hesap verir (Av. K. m.34; TBK m.506-508). Süre kaçırma,
   bildirim yapmama özen ihlali ve tazminat sebebidir (TBK m.502 vd., m.49).
3. **Azil.** Müvekkil avukatı her zaman azledebilir; ancak azil haksızsa ücretin tamamı
   muaccel olur, haklıysa indirim/iade gündeme gelir (Av. K. m.174/1; TBK m.512). Uygun
   olmayan zamanda azil tazminat doğurabilir.
4. **İstifa.** Avukat haklı sebeple istifa edebilir; istifa, müvekkilin zarar görmemesi için
   uygun zamanda yapılmalı, istifadan sonra da on beş gün süreyle (Av. K. m.41 anlamında
   işten çekilmenin sonuçları) gerekli önlemleri alma yükümü gözetilmelidir. Haksız/uygunsuz
   zamanda istifa ücret hakkını ve tazminat sorumluluğunu etkiler.
5. **Sona ermenin sonuçları.** Dosya ve belgelerin iadesi, hesap verme, hapis hakkı (Av. K.
   m.166), karşı tarafa yüklenen vekâlet ücretinin akıbeti ve zamanaşımı (TBK m.147/5)
   değerlendirilir.

## Çıktı modülleri
- Azil/istifanın haklılık ve ücret sonucu değerlendirmesi.
- Vekâletname kapsam denetimi (özel yetki kontrolü).
- İstifa/azil bildirimi ve dosya teslim tutanağı taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

