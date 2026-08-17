---
argument-hint: ''
description: Yabancı bir hakem kararını Türkiye'de icra ettirmek veya tenfiz talebine
  itiraz etmek; New York Sözleşmesi ve MÖHUK çerçevesinde ret sebeplerini denetlemek
  gerektiğinde kullanılır.
name: yabanci-hakem-karari-tenfiz
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


# Yabancı Hakem Kararının Tanınması ve Tenfizi

## Görev
Yurt dışında verilmiş bir hakem kararının Türkiye'de hüküm ifade etmesini sağlamak veya
karşı tarafsanız tenfizi engelleyecek ret sebeplerini ortaya koymak. Tenfiz, esasın
yeniden yargılanması değil, sınırlı bir denetimdir.

## Soğuk başlangıç (intake)
1. Karar hangi ülkede, hangi kurum/ad hoc tahkimde verildi?
2. Karar kesinleşti/bağlayıcı mı, taraflara usulüne uygun tebliğ edildi mi?
3. Türkiye veya tahkim yeri New York Sözleşmesi'ne taraf mı?
4. Kararın aslı/onaylı örneği ve tahkim sözleşmesi mevcut mu, yeminli çevirileri var mı?

## Denetim şeması
1. **Uygulanacak rejim**: Türkiye'nin tarafı olduğu **New York Sözleşmesi (1958)** ve
   tamamlayıcı olarak **MÖHUK m.60-63**. Görevli mahkeme asliye (ticaret) mahkemesidir,
   yetki **MÖHUK m.60** uyarınca belirlenir.
2. **Şekli şartlar**: Karar ve tahkim sözleşmesinin aslı/onaylı örneği ve yeminli tercümesi
   sunulur (**NY Sözleşmesi m.IV**, **MÖHUK m.61**).
3. **Ret sebepleri (sınırlı)**: **NY Sözleşmesi m.V** / **MÖHUK m.62** — tahkim
   sözleşmesinin geçersizliği, savunma hakkının ihlali (usulüne uygun bildirim yokluğu),
   hakemlerin yetki aşımı, heyet oluşumunun aykırılığı, kararın bağlayıcı olmaması veya
   iptal edilmesi. **Re'sen** incelenen: uyuşmazlığın Türk hukukuna göre tahkime
   elverişsizliği ve **kamu düzenine açık aykırılık**.
4. **İspat yükü**: m.V/1 (m.62/1) sebeplerini **tenfize itiraz eden** ispatlar; m.V/2
   (elverişlilik, kamu düzeni) mahkemece re'sen gözetilir. Revizyon yasağı (esasa girme
   yasağı) geçerlidir.
5. **Ara sonuç**: Tenfiz edilebilirlik değerlendirmesi ve itiraz dayanakları.

## Çıktı modülleri
- Belge kontrol listesi (aslı/örnek/tercüme).
- Tenfiz dilekçesi taslağı veya tenfize itiraz dilekçesi taslağı (madde atıflı).
- Ret sebebi-ispat yükü tablosu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

