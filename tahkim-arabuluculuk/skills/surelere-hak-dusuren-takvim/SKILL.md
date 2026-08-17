---
argument-hint: ''
description: Tahkim ve arabuluculuk süreçlerindeki iptal süresi, dava açma penceresi,
  tahkim süresi ve zamanaşımı durması gibi sert süreleri hesaplamak ve takvimlemek
  gerektiğinde kullanılır.
name: surelere-hak-dusuren-takvim
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
  - ad: Şehircilik ve Şehir Plancılarının Statüsü Hakkında Kanun
    numara: '4686'
    tur: kanun
  - ad: Hukuk Uyuşmazlıklarında Arabuluculuk Kanunu
    numara: '6325'
    tur: kanun
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler ve Hak Düşüren Takvim

## Görev
Bu alandaki en sık hak kaybı süre kaçırmadan doğar. Bu beceri iptal süresi, dava açma
penceresi, tahkim süresi ve zamanaşımı durması gibi sert süreleri tek takvimde toplar ve
hatırlatma kurar.

## Soğuk başlangıç (intake)
1. Hangi aşamadasınız (tahkim başlangıcı, hakem kararı sonrası, arabuluculuk son tutanak)?
2. Belirleyici tarih nedir (kararın bildirimi, son tutanak tarihi, başvuru tarihi)?
3. İç tahkim mi MTK mı, dava şartı arabuluculuk mu?
4. Asıl talebin zamanaşımı/hak düşürücü süresi ne durumda?

## Denetim şeması
1. **Hakem kararı iptal süresi**: İç tahkimde kararın bildiriminden itibaren **1 ay**
   (**HMK m.439/4**); MTK'da **30 gün** (**MTK m.15/A-4**). Geçirilirse karar kesinleşir.
2. **Tahkim süresi**: Hakem kararı kural olarak **1 yıl** içinde verilir (**HMK m.427**,
   **MTK m.10/B**); uzatma anlaşma/mahkeme kararıyla. Süre aşımı iptal sebebidir.
3. **Dava şartı arabuluculuk dava açma penceresi**: Anlaşmama son tutanağından itibaren
   **2 hafta** içinde dava açılır (**HUAK m.18/A**); aksi halde yeniden arabuluculuk.
4. **Zamanaşımı/hak düşürücü süre durması**: Arabuluculuk başvurusu **zamanaşımını durdurur,
   hak düşürücü süreyi işlemez kılar** (**HUAK m.18/A-15**); koruma son tutanağa kadar
   sürer. Tahkimde davanın açılmasıyla zamanaşımı kesilir.
5. **Tenfiz/tanıma**: Yabancı kararlarda özel bir hak düşürücü süre öngörülmese de icra
   takibi öncesi tenfiz şarttır; gecikme icra riskini artırır. Ara sonuç: tarih bazlı
   takvim.

## Çıktı modülleri
- Tarih bazlı süre takvimi (her süre için başlangıç, bitiş, dayanak madde).
- Hatırlatma/uyarı kutusu (kesin süreler kırmızı işaretli).
- Zamanaşımı durması-kesilmesi özet notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

