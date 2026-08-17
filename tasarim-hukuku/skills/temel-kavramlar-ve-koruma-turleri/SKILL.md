---
argument-hint: ''
description: Tescilli/tescilsiz tasarım, FSEK ve marka kümülasyonu ayrımının yapılması,
  koruma türünün ve uygulanacak rejimin belirlenmesi; bir görünümün hangi sınai mülkiyet
  hakkıyla korunacağını netleştirmek ger
name: temel-kavramlar-ve-koruma-turleri
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


# Temel Kavramlar ve Koruma Türleri

## Görev
Önündeki uyuşmazlık veya danışma için doğru koruma rejimini belirlemek: tescilli tasarım, tescilsiz tasarım, FSEK eser koruması ve marka korumasından hangisinin (veya hangilerinin birlikte) devreye girdiğini tespit etmek.

## Soğuk başlangıç (intake)
1. Korunması istenen şey bir ürünün veya parçanın görünümü mü, teknik bir işlevi mi, yoksa bir ayırt edici işaret mi?
2. Tasarım TÜRKPATENT'te tescilli mi; tescilliyse başvuru/tescil tarihi nedir?
3. Tasarım ilk kez kamuya ne zaman ve nasıl sunuldu (fuar, satış, katalog, internet)?
4. Görünüm özgün bir sanatsal/estetik yaratım mı (FSEK eseri ihtimali)?
5. Olay 10/01/2017 öncesi mi sonrası mı (554 KHK / 6769 SMK ayrımı)?

## Denetim şeması
1. Konu tanımı (SMK m.55): "Tasarım" ürünün tümü veya bir parçasının görünümüdür; "ürün" geniş tanımlıdır (bileşik ürün parçaları, ambalaj, grafik semboller dâhil). Görünüm değil işlev korunuyorsa tasarım yolu kapanır, patent/faydalı model'e yönelin.
2. Koruma türü ayrımı:
   - Tescilli (SMK m.55/4, m.69): TÜRKPATENT tescili ile doğar, 5'er yıllık yenilemeyle azami 25 yıl. Yenilik ve ayırt edicilik için aynı ölçütler aranır ama korumanın kapsamı geniştir (kötü niyet/kopyalama aranmaz).
   - Tescilsiz (SMK m.55/4, m.57/2): Kamuya ilk sunmadan itibaren 3 yıl; yalnızca taklit/kopyalamaya karşı koruma.
3. Kümülasyon kontrolü: Görünüm aynı zamanda özgün eserse FSEK m.1/B-4 (güzel sanat eseri) kümülatif korunabilir (SMK m.58/5'in kümülasyona engel olmadığı). Ürün şekli ayırt edici işaret işlevi görüyorsa 6769 marka hükümleri (m.4-5) ayrıca incelenir.
4. Zaman bakımından uygulama: Koruma 10/01/2017 öncesi doğmuşsa 554 KHK'nın ilgili hükümleri esas alınır; ara sonuç olarak hangi metnin uygulanacağı net yazılır.
5. Ara sonuç: Korunan değer (görünüm), koruma türü, süre ve uygulanacak metin tek cümlede sabitlenir.

## Çıktı modülleri
- Koruma türü karar tablosu (tescilli/tescilsiz/FSEK/marka) ve gerekçe.
- Tarih hattı (kamuya sunma, başvuru, rüçhan, koruma bitişi).
- Uygulanacak mevzuat ve madde listesi; eksik bilgi için [doldurulacak] notları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

