---
argument-hint: ''
description: İdari davada 30/60 günlük genel süreler, m.11 başvurusunun durdurucu
  etkisi, m.13 ön başvurusu ve özel kanun süreleri hesaplanırken kullanılır; sürenin
  başlangıcı, durması ve kaçırılıp kaçırılmadığı t
name: dava-acma-sureleri
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
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dava Açma Süreleri ve Sürenin Hesabı

## Görev
İdari davanın süresinde açılıp açılmadığını; başlangıç anını, durma/uzama hâllerini ve özel kanun sürelerini dikkate alarak kesin biçimde hesaplamak. Süreler kamu düzenindendir ve resen incelenir.

## Soğuk başlangıç (intake)
- İşlem ilgilisine tebliğ mi edildi, ilan mı edildi, yoksa başka yolla mı öğrenildi; tarih nedir?
- İşleme karşı m.11 kapsamında üst makama başvuruldu mu; başvuru tarihi ve cevabı?
- Uyuşmazlık vergiyle mi ilgili (30 gün), genel idari mi (60 gün)?
- Özel bir kanun (kamulaştırma, ihale, YUKK vb.) farklı bir süre öngörüyor mu?

## Denetim şeması
1. **Genel süre** (İYUK m.7): Danıştay ve idare mahkemelerinde **60 gün**, vergi mahkemelerinde **30 gün**. Süre, yazılı bildirimin (tebliğ) yapıldığı tarihi izleyen günden başlar. İlanı gereken işlemlerde ilan süresinin bitimini izleyen günden işler.
2. **İdari başvuru ile durma** (İYUK m.11): İlgililer, dava açma süresi içinde işlemi yapan makama veya üst makama başvurarak işlemin kaldırılmasını/değiştirilmesini isteyebilir. Bu başvuru **işlemeye başlamış süreyi durdurur**. İdarenin cevabı veya 30 günlük zımni ret süresinin dolmasıyla kalan süre yeniden işlemeye başlar (durmuş olan süre kaldığı yerden devam eder).
3. **Tam yargı ön başvurusu** (İYUK m.13): İdari eylem zararlarında 1 yıl / 5 yıl sınırı (bkz. tam yargı becerisi).
4. **İptal sonrası tam yargı** (İYUK m.12): İptal davasıyla birlikte veya iptal kararının/temyizde onanmasının tebliğinden itibaren 60 gün içinde tam yargı açılabilir.
5. **Özel kanun süreleri**: 2942 sayılı Kamulaştırma K., 4734/4735 sayılı ihale mevzuatı, 6458 sayılı YUKK, 6183 sayılı AATUHK ödeme emri (7 gün/15 gün gibi) süreleri saklıdır ve genel süreye önceliklidir.
6. **Ara sonuç — son gün**: Sürenin son günü çalışmaya ara verme (adli tatil — İYUK m.61) veya resmî tatile rastlarsa, süre tatili izleyen ilk iş gününün mesai bitiminde sona erer (İYUK m.8). Adli tatilde biten süreler tatilin bitiminden itibaren 7 gün uzar.

## Çıktı modülleri
- Süre hesap tablosu (başlangıç, durma, son gün)
- m.11 başvurusu yapılmışsa durma/devam analizi
- Süre aşımı riski ve önerilen ivedi adımlar



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

