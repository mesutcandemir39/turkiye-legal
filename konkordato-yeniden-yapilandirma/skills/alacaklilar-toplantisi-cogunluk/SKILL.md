---
argument-hint: ''
description: Alacakların bildirimi, alacaklılar toplantısının yapılması ve konkordatonun
  kabulü için aranan çoğunlukların hesaplanması gerektiğinde kullanılır.
name: alacaklilar-toplantisi-cogunluk
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


# Alacaklıların Daveti, Toplantı ve Çoğunluk

## Görev
Alacaklıları davet, alacakların bildirimi ve incelenmesi (İİK m.299-301), alacaklılar toplantısı ve konkordatonun kabulü için aranan nitelikli çoğunluğun (m.302) doğru hesaplanması.

## Soğuk başlangıç (intake)
- Alacaklılar davet ilanı yapıldı mı, bildirim süresi içinde miyiz?
- Kaydedilen toplam alacak ve alacaklı sayısı nedir?
- Rehinle temin edilmiş ve imtiyazlı alacaklar çoğunluk hesabında nasıl dışlanıyor?
- Çekişmeli (ihtilaflı) alacaklar var mı?

## Denetim şeması
1. **Alacaklıları davet (m.299).** Komiser, alacaklıları alacaklarını bildirmeye ilanla davet eder; bildirim süresi ve usulü denetlenir.
2. **Alacakların incelenmesi (m.300-301).** Borçlu, bildirilen alacaklar hakkında beyana davet edilir; komiser alacakları inceleyip rapor hazırlar. Çekişmeli alacakların çoğunluğa etkisi mahkemece m.308/c çerçevesinde değerlendirilir.
3. **Çoğunluğun hesabı (m.302/3).** Konkordato şu hâllerden biriyle kabul edilmiş sayılır: (a) kaydedilmiş alacaklıların ve alacakların yarısını aşan çoğunluk; veya (b) kaydedilmiş alacaklıların dörtte birini ve alacakların üçte ikisini aşan çoğunluk. İspat: tutanak ve alacak cetveliyle.
4. **Hesaba katılmayanlar (m.302/4-6).** Rehinle tam karşılanan alacaklar ve İİK m.206/1. sıradaki imtiyazlı alacaklar çoğunluk hesabında dikkate alınmaz; borçlunun yakınlarının alacakları için özel kural. Bunların doğru dışlanması denetlenir.
5. **Toplantı ve imza süresi.** Konkordato projesinin kabulü için tanınan süre (m.302/1) içinde imza/kabul beyanları toplanır. Ara sonuç: çoğunluk sağlandı mı, tasdik talebine geçilebilir mi.

## Çıktı modülleri
- Çoğunluk hesap tablosu (kişi sayısı ve alacak miktarı bazında).
- Dışlanan alacaklar (rehinli/imtiyazlı/yakın) listesi.
- Çekişmeli alacak değerlendirme notu.
- Toplantı tutanağı kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

