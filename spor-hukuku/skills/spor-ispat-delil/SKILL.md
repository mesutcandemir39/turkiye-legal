---
argument-hint: ''
description: Disiplin, doping, şike veya sözleşmesel uyuşmazlıklarda ispat yükünü,
  delil türlerini ve delil değerini analiz etmek; delil toplama ve sunma stratejisi
  kurmak gerektiğinde kullanın.
name: spor-ispat-delil
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
  - ad: Çalışma ve Sosyal Güvenlik Bakanlığı Kuruluş ve Görevleri Hakkında Kanun
    numara: '7405'
    tur: kanun
  - ad: Tıbbi Deontoloji Tüzüğü Hakkında Kanun
    numara: '6222'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Spor Uyuşmazlıklarında İspat ve Delil

## Görev
Spor uyuşmazlığında ispat yükünü doğru dağıtmak, mevcut delilleri türü ve değerine göre değerlendirmek, eksik delilleri tespit etmek ve delil toplama/sunma stratejisi kurmaktır.

## Soğuk başlangıç (intake)
1. Uyuşmazlık türü: disiplin, doping, şike, sözleşmesel alacak?
2. İspatlanması gereken vakıa nedir ve kim iddia ediyor?
3. Eldeki deliller neler (rapor, görüntü, mesaj, ödeme kaydı, tanık)?
4. Delillerin elde ediliş usulü hukuka uygun mu?
5. Karşı tarafın dayandığı deliller neler?

## Denetim şeması
1. **İspat yükü**: Kural olarak iddia eden ispatla yükümlüdür (HMK m.190, TMK m.6). Disiplinde sevk eden federasyon, sözleşmesel alacakta alacaklı; dopingde varlık ispatı federasyonda, kusursuzluk/kontaminasyon ispatı sporcudadır.
2. **Delil türleri**: Hakem/gözlemci/güvenlik raporları, müsabaka kamera görüntüleri (VAR dahil), doping numune ve laboratuvar kayıtları, sözleşme ve ödeme belgeleri, elektronik yazışmalar, tanık.
3. **Delil değeri**: Tahkim ve disiplin organları serbest delil değerlendirmesi yapar; resmi raporların aksi ispatlanana kadar üstün değeri ve görüntü kayıtlarının teyit edici gücü değerlendirilir.
4. **Hukuka aykırı delil**: Hukuka aykırı yolla elde edilen delil (izinsiz kayıt, hukuka aykırı erişim) reddi gündeme gelir; usulüne uygunluk denetlenir.
5. **Delil tespiti ve sunma**: Kaybolma riski olan delil için tespit; dilekçeye delil bağlama ve dizin; bilirkişi/uzman görüşü gereken teknik konular (doping analizi, mali hesap) belirlenir.
6. **Ara sonuç**: İspat şansı, eksik deliller ve toplama planı netleşir.

## Çıktı modülleri
- İspat yükü ve vakıa-delil eşleştirme tablosu
- Eksik delil ve toplama planı
- Delil dizini taslağı
- Hukuka uygunluk değerlendirme notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

