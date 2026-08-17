---
argument-hint: ''
description: Bir hukuki görüş veya mütalaa hazırlanması istendiğinde işin türünü (dava
  içi uzman görüşü, danışmanlık görüşü, kurumsal risk mütalaası) belirleyip iskeletini
  kurmak için kullanılır; mütalaanın dava d
name: mutalaa-temel-yapi-ve-tur
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Mütalaa Temel Yapısı ve Türü

## Görev
Talep edilen metnin gerçekten hukuki mütalaa mı, dava dilekçesi mi, yoksa bir bilgilendirme notu mu olduğunu ayırt etmek; doğru türü seçip standart mütalaa iskeletini kurmak. Mütalaa analitik ve dengeli yazılır; dava dilekçesi taraf-savunucudur (bkz. Dava Dilekçesi Atölyesi), bilirkişi raporu maddi vakıayı inceler, mütalaa ise hukuki nitelendirme yapar.

## Soğuk başlangıç (intake)
- Bu görüş ne için kullanılacak? (Mahkemeye HMK m.293 uyarınca uzman görüşü olarak mı, dava öncesi karar vermek için mi, sözleşme/işlem yapısı için mi?)
- Talep eden kim ve hangi sıfatla? (Müvekkil / karşı taraf / nötr danışan)
- Yanıtlanması istenen somut hukuki soru(lar) nedir?
- Hangi belge ve vakıalar veriliyor; eksik olan ne?

## Denetim şeması
1. Tür tayini: Dava içi uzman görüşü HMK m.293 kapsamına girer ve karşı tarafça incelenir; tarafsız-bilimsel üslup gerektirir. Danışmanlık mütalaası iç kullanım içindir, aleyhe senaryoyu açıkça tartabilir. Bu ayrım dil ve kapsamı belirler.
2. Kapsam ve sınır: Mütalaa yalnızca sunulan vakıa çerçevesiyle bağlıdır; bu sınır metnin başına yazılır ("İşbu görüş tarafıma iletilen ... belgelerine dayanmaktadır"). Eksik bilgi varsayımları işaretlenir.
3. İskelet kurulumu — standart altı bölüm: (a) Sorunun konusu ve kapsam, (b) Maddi olay özeti, (c) Hukuki çerçeve (mevzuat), (d) Hukuki değerlendirme (altlama), (e) İçtihat-doktrin desteği, (f) Sonuç ve öneriler.
4. Tarafsızlık testi: Metin, hasım bir hukukçunun eline geçtiğinde çürütülemeyecek kadar dengeli mi? Aleyhe argümanlar tartılmış mı? (Mütalaanın ikna gücü dürüstlüğünden gelir.)
5. Ara sonuç: Tür + iskelet + kapsam sınırı netleştiğinde içerik üretimine geçilir.

## Çıktı modülleri
- Mütalaa türü ve gerekçesi (tek paragraf)
- Doldurulmuş altı bölümlü iskelet (başlıklar + her başlık altında 1-2 cümlelik yönerge)
- Kapsam/sınır beyanı taslağı
- Eksik bilgi ve varsayım listesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

