---
argument-hint: ''
description: Dosyada cevaplanmamış iddiaları, ibraz edilmemiş delilleri ve taraf beyanları
  arasındaki çelişkileri sistematik biçimde tespit etmek gerektiğinde kullan.
name: eksik-ve-celiski-listesi
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Eksik ve Çelişki Listesi

## Görev
Dosyadaki boşlukları (cevaplanmamış iddia, eksik evrak, ibraz edilmemiş delil) ve tutarsızlıkları (çelişen beyan, çelişen tarih/tutar) bir kalite-kontrol listesine dönüştürmek.

## Soğuk başlangıç (intake)
- Dava ve cevap dilekçeleri ile varsa replik-düplik elinde mi?
- Hangi iddialar karşı tarafça yanıtsız bırakılmış?
- Beyanlar, tutarlar veya tarihler arasında göze çarpan çelişki var mı?
- Hangi evrakın dosyada olması gerekirken olmadığını biliyor musun?

## Denetim şeması
1. Cevaplanmamış iddia: dava dilekçesindeki her vakıaya karşı cevap dilekçesinde açık/örtülü itiraz var mı? Cevapta açıkça inkâr edilmeyen vakıanın ikrar/çekişmesizlik etkisini (HMK m.128) işaretle.
2. Eksik evrak: dilekçelerde dayanılan ama dosyada bulunmayan belgeler; HMK m.121 ve m.129 gereği dilekçeye eklenmesi gereken delillerin eksikliği.
3. Çelişki taraması: aynı tarafın farklı evrakındaki çelişen beyanlar; taraflar arası çelişen tutar/tarih; bilirkişi raporu ile dosya arasındaki uyumsuzluk. Her çelişkiyi kaynak evrak + sayfa ile göster.
4. Usuli eksik: dava şartı (HMK m.114-115), ilk itiraz (HMK m.116) ve süresinde ileri sürülmeyen savunma genişletme yasağı (HMK m.141) açısından risk notları.
5. Ara sonuç: önceliklendirilmiş eksik/çelişki listesi (kritik / orta / düşük). Tespitler yalnızca evraka dayanır; varsayım eklenmez.

## Çıktı modülleri
- Eksik kalemler tablosu (ne eksik, dayanak, etki).
- Çelişki tablosu (çelişen ifadeler, kaynak evrak, sayfa).
- Önceliklendirilmiş aksiyon listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

