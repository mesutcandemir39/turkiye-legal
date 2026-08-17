---
argument-hint: ''
description: Konkordato komiserinin görev ve yetkilerini, alacaklılar kurulunun oluşumunu
  ve işleyişini, organların kararlarına karşı başvuru yollarını ele almak gerektiğinde
  kullanılır.
name: komiser-ve-alacaklilar-kurulu
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
  - ad: İcra ve İflas Kanunu
    numara: '2004'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Konkordato Komiseri ve Alacaklılar Kurulu

## Görev
Sürecin organlarını yönetmek: komiserin görevlendirilmesi, görev ve yetkilerinin (İİK m.290) denetimi, alacaklılar kurulunun oluşturulması (m.289/3) ve işleyişi, organların işlem ve raporlarına karşı denetim/şikâyet yollarının kullanımı.

## Soğuk başlangıç (intake)
- Komiser atandı mı, sayısı ve nitelikleri uygun mu (komiserlik yönetmeliği)?
- Alacaklılar kurulu kuruldu mu, kaç üyeli, hangi alacaklı gruplarını temsil ediyor?
- Komiserin/kurulun bir işlemine itiraz mı var?
- Komiser ücreti ve depo durumu nedir?

## Denetim şeması
1. **Komiser görevlendirme.** Mahkeme, geçici mühletle birlikte bir veya birden fazla geçici komiser atar; nitelikler Adalet Bakanlığı konkordato komiserliği yönetmeliği ile belirlenir. Bilirkişilik/komiserlik listesine kayıt şartı denetlenir.
2. **Komiserin görevleri (m.290).** Projenin tamamlanmasına katkı, defter ve belgelerin incelenmesi, malların korunması, alacaklılar kurulunca verilen görevler, mahkemeye dönemsel rapor. İspat: komiser raporunun gerekçeli ve belgeye dayalı olması aranır.
3. **Alacaklılar kurulu (m.289/3, m.290).** Mahkeme, alacaklı sayısı/alacak miktarı ve niteliği gözetilerek bir alacaklılar kurulu oluşturabilir; farklı alacaklı sınıflarının (rehinli, imtiyazlı, adi) temsili sağlanır. Kurul komiserin işlemlerini denetler, görüş bildirir.
4. **Organların kararlarına karşı (m.290/son, m.297).** Komiserin tasarruf onayı, kurulun kararları ve raporlar; ilgililer mahkemeye şikâyet/itiraz edebilir. Süre ve usul denetlenir.
5. **Komiser ücreti.** Adalet Bakanlığı ücret tarifesi esas alınır; tasdik şartı olarak depo (m.305) gözetilir. Ara sonuç: organ yapısı usule uygun mu, müdahale gerekir mi.

## Çıktı modülleri
- Komiser/alacaklılar kurulu görev-yetki tablosu.
- Komiser raporu değerlendirme notu.
- Organ kararına itiraz/şikâyet dilekçesi taslağı (yer tutuculu).
- Ücret ve depo kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

