---
argument-hint: ''
description: Eşyanın menşeinin belirlenmesi, tercihli/tercihsiz menşe, GTİP sınıflandırması,
  menşe ispat belgeleri ve ek mali yükümlülük ihtilaflarında; menşe ve tarife eksenli
  ek tahakkuk ve önlemleri analiz etme
name: mense-ve-tarife
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
  - ad: Gümrük Müsait Müşterek Gümrük Bölgeleri Hakkında Kanun
    numara: '4458'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Menşe, Tarife Sınıflandırma ve Tercihli Ticaret

## Görev
Eşyanın menşeini ve tarife pozisyonunu (GTİP) doğru saptamak; tercihli menşe iddialarını, menşe ispat belgelerini ve menşe/sınıflandırma kaynaklı ek tahakkuk ile ticaret politikası önlemlerini (antidamping, EMY, korunma) değerlendirmek.

## Soğuk başlangıç (intake)
- Beyan edilen menşe ülke ve GTİP nedir; hangi ispat belgesi sunuldu (EUR.1, A.TR, menşe şahadetnamesi, fatura beyanı)?
- Tercihli tarife mi talep edildi; uygulanan anlaşma hangisi?
- Eşya antidamping, ek mali yükümlülük veya korunma önlemi kapsamında mı?
- İdarenin tespiti menşe değişikliği mi, GTİP değişikliği mi, belge geçersizliği mi?

## Denetim şeması
1. Tercihsiz menşe (m.18-21): Tamamen bir ülkede elde edilen eşya o ülke menşelidir; birden çok ülke katkısı varsa "son esaslı, ekonomik bakımdan haklı işçilik veya işlem" ölçütü uygulanır (m.19). Bu ölçüt antidamping/EMY için belirleyicidir.
2. Tercihli menşe: İlgili STA/Gümrük Birliği kuralları ve menşe protokolleri uygulanır. A.TR Gümrük Birliği'nde serbest dolaşım belgesidir, menşe ispatı değildir; EUR.1/EUR-MED ve fatura beyanı tercihli menşe ispatıdır. Belge geçerli, süresinde ve usulüne uygun olmalı.
3. Sonradan kontrol: Menşe belgelerinin doğruluğu ihracatçı ülke idaresi nezdinde sonradan kontrole tabidir; olumsuz/teyitsiz sonuç tercihli oranın geri alınmasına ve ek tahakkuka yol açar.
4. Tarife sınıflandırma: GTİP, Armonize Sistem İzahnamesi ve Genel Yorum Kuralları ile belirlenir. Tereddütte BTB (Bağlayıcı Tarife Bilgisi) başvurusu yapılır; BTB sahibini ve idareyi bağlar.
5. İspat yükü: Tercihli oran iddiasında bulunan yükümlü geçerli menşe ispat belgesini ve menşe kurallarına uygunluğu ortaya koyar; idare reddini somut sonradan kontrol sonucu veya teknik tespitle gerekçelendirir.
6. Ara sonuç: Doğru menşe, GTİP ve uygulanacak oran ile önlem belirlenir; ek tahakkuk ve ceza riskinin hukuki dayanağı saptanır. İlkesel içtihat için Danıştay 7. Daire kararlarına bakılabilir [DOĞRULANMADI].

## Çıktı modülleri
- Menşe/GTİP analiz notu ve belge geçerlilik kontrolü
- Sonradan kontrol cevabına itiraz taslağı
- BTB başvuru taslağı (gerekirse)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

