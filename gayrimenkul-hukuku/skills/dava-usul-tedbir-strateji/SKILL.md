---
argument-hint: ''
description: Taşınmaz davası açılmadan önce doğru mahkeme, dava şartları, harç-değer,
  süreler ve taşınmazın elden çıkmasını önleyici ihtiyati tedbir/şerh stratejisi belirlenmesi
  gerektiğinde kullanılır.
name: dava-usul-tedbir-strateji
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Gayrimenkulde Usul, Görev-Yetki, İhtiyati Tedbir ve Strateji

## Görev
Taşınmaz uyuşmazlığının usulî iskeletini kurmak: görevli ve yetkili mahkemeyi, dava şartlarını, harç ve değeri, süreleri ve karşı tarafın taşınmazı devretmesini önleyecek ihtiyati tedbir/şerh stratejisini belirlemek; davayı en etkili sıra ve biçimde kurgulamak.

## Soğuk başlangıç (intake)
- Talep türü ne (tapu iptali-tescil, satış vaadi ifası, el atma, ortaklığın giderilmesi, kamulaştırma bedeli, tüketici)?
- Uyuşmazlığın değeri ve taraf sıfatları (tüketici/tacir/idare) ne?
- Karşı tarafın taşınmazı üçüncü kişiye devretme veya kayıt değiştirme riski var mı?
- İşleyen süreler var mı (satış vaadi 10 yıl, İYUK 60 gün, tüketici/cayma süreleri)?

## Denetim şeması
1. **Yetki**: Taşınmazın aynına ilişkin davalarda (mülkiyet, tapu iptali-tescil, el atma, ortaklığın giderilmesi, irtifak) kesin yetki taşınmazın bulunduğu yer mahkemesidir (HMK m.12). Birden çok taşınmazda biri yeterlidir.
2. **Görev**: Kural asliye hukuk (HMK m.2). Ortaklığın giderilmesi ve kat mülkiyetinden doğan davalar sulh hukuk (HMK m.4; KMK Ek m.1). Tüketici sıfatı varsa tüketici mahkemesi (6502 m.73). İmar/kamulaştırma iptali idari yargı (İYUK). Görev kesindir, re'sen gözetilir.
3. **Dava şartları (HMK m.114-115)**: Hukuki yarar, taraf-dava ehliyeti, husumet; elbirliği mülkiyeti ve ortaklığın giderilmesinde zorunlu dava arkadaşlığı eksik husumet doğurabilir.
4. **İspat (TMK m.6; HMK m.190 vd.)**: Hakkı iddia eden ispatla yükümlüdür; tapu kaydı doğruluk karinesi taşır. Taşınmaz davalarında keşif ve bilirkişi (harita-fen, değerleme, inşaat) çoğunlukla zorunludur. Resmî senetle yapılan işlemler güçlü delildir; tanıkla aksinin ispatı sınırlıdır (HMK m.201).
5. **İhtiyati tedbir (HMK m.389 vd.)**: Taşınmazın devrini/üzerine işlem yapılmasını önlemek için tapuya tedbir şerhi istenir; yaklaşık ispat ve teminat gerekir. Satış vaadi/kişisel haklarda m.1010 (TMK) tasarruf kısıtlaması şerhi düşünülür.
6. **Harç ve değer**: Aynı ilişkin davalar nispi harca tabidir; dava değeri taşınmazın güncel değerine göre belirlenir; eksik harç dava şartı sorunu doğurur.
7. **Ara sonuç**: Doğru mahkeme + tam dava şartları + gerekiyorsa devri önleyici tedbir; talepler arasında terditli/kademeli kurgu.

## Çıktı modülleri
- Görev/yetki, yargı kolu ve harç-değer kontrol listesi.
- İhtiyati tedbir/şerh dilekçesi iskeleti (yaklaşık ispat, teminat).
- Süre ve husumet (zorunlu dava arkadaşlığı) uyarı notu ve dava kurgu planı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

