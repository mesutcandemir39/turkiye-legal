---
argument-hint: ''
description: Bir markanın izinsiz kullanımı, taklit ürün, karıştırılma ihtimali veya
  tanınmış markadan haksız yararlanma iddiasında tecavüzün varlığını SMK m.7 ve m.29
  çerçevesinde adım adım değerlendirmek gerekti
name: marka-tecavuzu-denetimi
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Marka Hakkına Tecavüz Denetimi

## Görev
Tescilli marka hakkına tecavüz iddiasını SMK m.7 (hakkın kapsamı) ve m.29 (tecavüz sayılan fiiller) çerçevesinde denetlemek; karıştırılma ihtimalini ve tanınmışlık korumasını altlamak.

## Soğuk başlangıç (intake)
- Markanın tescil numarası, sınıfı (Nice) ve tescilli işaret nedir?
- İhlal iddia edilen işaret/ürün hangi mal-hizmette, hangi biçimde kullanılıyor?
- Markalar/işaretler aynı mı, benzer mi; mallar/hizmetler aynı mı, benzer mi?
- Marka tanınmış mı; kullanmama def'i (m.19/2) gündeme gelir mi?

## Denetim şeması
1. Hakkın kapsamı: Tescilli marka sahibi izinsiz kullanımı önleme hakkına sahiptir (SMK m.7/2). Aynı işaret + aynı mal/hizmet halinde karıştırılma aranmaz (m.7/2-a).
2. Karıştırılma ihtimali: İşaret benzer ve mal/hizmet benzer ise halk nezdinde karıştırılma ihtimali (ilişkilendirme dahil) değerlendirilir (m.7/2-b). Bütünsel izlenim, ortalama tüketici, ayırt edicilik düzeyi ölçütleri uygulanır.
3. Tanınmış marka: Farklı mal/hizmette dahi haksız yarar, itibara/ayırt ediciliğe zarar varsa koruma genişler (m.7/2-c). Tanınmışlık davacıya ispat yükü.
4. Tecavüz fiilleri: Taklit, iltibas yaratacak kullanım, ambalaj/etiket, ticari belge ve internet kullanımı SMK m.29'da sayılıdır. Marka olarak kullanım şartı ve dürüst kullanım istisnaları (m.7/5) tartılır.
5. Savunmalar: Kullanmama def'i (m.19/2 — son 5 yıl ciddi kullanım), önceki hak, hakkın kötüye kullanılması; süre yönünden sessiz kalma (m.25/6).
6. Ara sonuç: Tecavüz sabitse SMK m.149 talepleri (tespit, durdurma, giderme, tazminat, el koyma, imha) açılır.

## Çıktı modülleri
- İşaret/mal-hizmet karşılaştırma tablosu.
- Karıştırılma ihtimali altlama notu.
- Talep listesi (SMK m.149 atıflı) ve savunma haritası.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

