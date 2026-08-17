---
argument-hint: ''
description: Verilen bir hakem kararına karşı iptal davası açmak veya gelen iptal
  talebine karşı koymak; iptal sebeplerini, süreyi ve yetkili mahkemeyi belirlemek
  gerektiğinde kullanılır.
name: hakem-karari-iptal-davasi
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


# Hakem Kararının İptali Davası

## Görev
Hakem kararına karşı tek kanun yolu olan iptal davasını yönetmek: iptal sebeplerinin
sınırlı listesi içinde dayanak bulmak, sert süreye uymak ve yetkili mahkemede doğru
talep kurmak. İptal davası kararın esasının yeniden incelenmesi DEĞİLDİR.

## Soğuk başlangıç (intake)
1. Karar iç tahkim (HMK) mi milletlerarası (MTK) mi kararı?
2. Karar tarafa ne zaman bildirildi (süre hesabı için)?
3. Hangi sakatlık iddia ediliyor (yetki yokluğu, usul, kamu düzeni)?
4. Karşı taraf mısınız yoksa iptal mi istiyorsunuz?

## Denetim şeması
1. **Yetkili mahkeme ve süre**: İç tahkimde **bölge adliye mahkemesi**, kararın
   bildiriminden itibaren **1 ay** (**HMK m.439/1, /4**). MTK'da **asliye ticaret
   mahkemesi**, **30 gün** (**MTK m.15/A-4**). Süre kesindir; geçirilirse karar
   kesinleşir.
2. **İptal sebepleri (sınırlı/numerus clausus)**: **HMK m.439/2** / **MTK m.15/A** —
   tahkim sözleşmesinin geçersizliği, hakem seçimi/usul aykırılığı, sürenin aşılması,
   talep dışına çıkılması, eşitlik ve hukuki dinlenilme hakkı ihlali. **Re'sen**
   incelenenler: uyuşmazlığın tahkime elverişsizliği ve **kamu düzenine aykırılık**.
3. **İspat yükü**: Sözleşme geçersizliği, usul aykırılığı gibi sebepleri **iptal isteyen**
   ispatlar; elverişlilik ve kamu düzenini mahkeme kendiliğinden gözetir.
4. **Esasa girme yasağı**: Mahkeme kararın maddi/hukuki isabetini denetlemez; yalnızca
   sınırlı sebepleri inceler. Bu sınır talep dilekçesinde gözetilmelidir.
5. **Ara sonuç**: Dayanılabilir iptal sebepleri, süre durumu ve başarı şansı notu.

## Çıktı modülleri
- İptal sebebi-dayanak eşleştirme tablosu (madde atıflı).
- İptal davası dilekçesi taslağı veya iptal talebine cevap taslağı.
- Süre ve yetki uyarı kutusu; ilkesel içtihat atfı `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

