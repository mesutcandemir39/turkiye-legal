---
argument-hint: ''
description: Yabancı müvekkile süreç, riskler ve adımların sade anlatılması veya idari
  makama/mahkemeye resmî yazışma hazırlanması gerektiğinde kullanılır.
name: muvekkil-iletisimi
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
  - ad: Yabancılar ve Uluslararası Koruma Kanunu
    numara: '6458'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Müvekkil ve Makam İletişimi

## Görev
Yabancı müvekkile süreci, riskleri ve sorumlulukları sade ve doğru biçimde aktarmak; Göç İdaresi, Bakanlık ve mahkemeyle yürütülen yazışmaları usulüne uygun hazırlamak.

## Soğuk başlangıç (intake)
1. İletişim kime yönelik (müvekkil bilgilendirmesi mi, makama resmî yazı mı)?
2. Müvekkilin dil ihtiyacı ve hukuki bilgisi düzeyi nedir?
3. Hangi konu aktarılacak (mevcut durum, risk, yapılması gerekenler, sonuç)?
4. Süreye bağlı, müvekkilin acil yapması gereken bir iş var mı?

## Denetim şeması
1. **Bilgilendirmenin doğruluğu**: Statü, işlem ve süreler madde dayanağıyla; abartısız, ne fazla iyimser ne yıldırıcı. Sonuç garantisi verilmez.
2. **Sade dil**: Hukuki terimler (idari gözetim, geri gönderme yasağı, yürütmenin durdurulması) gündelik dile çevrilir; müvekkilin yapması gereken somut adımlar (belge temini, randevu, imza, son gün) listelenir.
3. **Makam yazışması**: Resmî üslup, doğru makam adı, dosya/başvuru numarası `[doldurulacak]`, dayanak madde; bilgi/belge talebi ve süreye atıf net yazılır.
4. **Riziko ve sorumluluk paylaşımı**: Müvekkilin verdiği eksik/yanlış bilginin sonucu (ret, iptal, sahte belge ile vatandaşlığın iptali) açıkça hatırlatılır; belge teyidi vurgulanır.
5. **Gizlilik**: Müvekkilin korunma/aile bilgileri hassas veri olarak işlenir; üçüncü kişilere paylaşımda dikkat.
**Ara sonuç**: Anlaşılır, eyleme dönük bir bilgilendirme veya usulüne uygun bir makam yazısı.

## Çıktı modülleri
- Müvekkile sade bilgilendirme notu (durum, risk, yapılacaklar, son gün).
- Makama/mahkemeye resmî yazı/dilekçe taslağı.
- Müvekkilden istenecek belge ve onay listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

