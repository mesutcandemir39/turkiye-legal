---
argument-hint: ''
description: Bir işaretin tescil edilebilirliği tartışmalıysa veya TÜRKPATENT re'sen
  ret kararı verdiyse; ayırt edicilik, tasvirilik, yanıltıcılık ve şekil markası sınırlarını
  m.5 üzerinden denetlemek için kullanı
name: marka-olabilirlik-mutlak-ret
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
  version: 0.1.0
user-invocable: true
---


# Marka Olabilirlik ve Mutlak Ret Sebepleri

## Görev
İşareti SMK m.4 (marka olabilirlik) ve m.5 (mutlak ret) süzgecinden geçirmek. Mutlak ret sebepleri kamu yararına dayanır ve TÜRKPATENT tarafından re'sen incelenir; hükümsüzlükte de herkes ileri sürebilir. Kullanımla kazanılmış ayırt edicilik (m.5/2) tek kurtarıcı istisnadır.

## Soğuk başlangıç (intake)
- İşaret ne (kelime, şekil, renk, üç boyutlu, slogan)?
- Hangi mal/hizmet için tescil isteniyor?
- İşaret malın özelliğini/cinsini/kalitesini doğrudan anlatıyor mu?
- İşaret piyasada yoğun ve süreli kullanılmış mı (m.5/2 dayanağı)?

## Denetim şeması
1. **Ayırt edicilik (m.5/1-b).** İşaret, malı/hizmeti bir teşebbüsünkinden ayırt edebiliyor mu? Sıradan, vasıfsız işaret reddedilir.
2. **Tasviri işaret (m.5/1-c).** Cins, çeşit, vasıf, kalite, miktar, coğrafi kaynak, üretim zamanını gösteren işaretler. Doğrudan tasvir reddedilir; çağrıştırıcı (suggestive) işaret tescil edilebilir.
3. **Yaygın/jenerik işaret (m.5/1-d).** Ticarette herkesçe veya belirli meslek grubunca kullanılan işaretler.
4. **Şekil engeli (m.5/1-e).** Malın doğal yapısından doğan, teknik zorunluluk içeren veya mala asli değerini veren şekil — kullanımla dahi aşılamaz (m.5/2 dışında).
5. **Yanıltıcılık ve kamu düzeni (m.5/1-f, -i).** Mal/hizmetin niteliği-kaynağı konusunda yanıltıcı; kamu düzeni-genel ahlaka aykırı işaretler.
6. **Önceki aynı/ayırt edilemeyecek marka (m.5/1-ç).** Aynı/aynı tür mal-hizmet için aynı veya ayırt edilemeyecek benzer önceki tescil/başvuru re'sen ret sebebidir.
7. **İstisna (m.5/2).** İşaret başvuru tarihinden önce kullanımla ayırt edicilik kazandıysa b-c-d bentleri uygulanmaz; ispat yükü başvurana aittir (yoğun kullanım, pazar payı, tanıtım delilleri).

## Çıktı modülleri
- Ret sebebi-bent eşleştirme tablosu (var/yok/şüpheli).
- m.5/2 kullanımla ayırt edicilik delil listesi.
- Tescil şansı değerlendirmesi ve mal/hizmet daraltma önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

