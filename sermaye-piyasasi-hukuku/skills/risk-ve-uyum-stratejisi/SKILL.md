---
argument-hint: ''
description: İhraççı, yönetici veya yatırım kuruluşu için sermaye piyasası mevzuatına
  uyum, yaptırım/cezai risk haritası, içsel bilgi yönetimi ve önleyici politika tasarımı
  gerektiğinde kullanılır.
name: risk-ve-uyum-stratejisi
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
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk Değerlendirmesi ve Uyum Stratejisi

## Görev
İhraççı/yönetici/yatırım kuruluşu için sermaye piyasası risklerini haritalamak; idari ve cezai sorumluluk olasılıklarını tartmak; önleyici uyum politikaları önermek.

## Soğuk başlangıç (intake)
- Müvekkil kim: ihraççı, yönetim kurulu üyesi, yatırım kuruluşu, ortak mı?
- Risk konusu: kamuyu aydınlatma, içsel bilgi yönetimi, çağrı, ilişkili taraf işlemleri mi?
- Geçmişte Kurul incelemesi/yaptırımı veya devam eden işlem var mı?
- Amaç önleyici uyum mu, devam eden bir riske müdahale mi?

## Denetim şeması
1. **Risk envanteri:** Faaliyet türüne göre yükümlülükler listelenir: özel durum açıklamaları (SPK m.15), finansal raporlama (m.14), içsel bilgi erişen listesi, ilişkili taraf/örtülü kazanç aktarımı (m.21), geri alım (m.22), çağrı (m.25-26).
2. **Olasılık-etki tartımı:** Her risk için ihlal olasılığı ve sonucu (idari para cezası m.103, menfaat iadesi m.104, tedbir m.96-99, cezai sorumluluk m.106-107) değerlendirilir; ölçülülük ve tekerrür etkisi gözetilir. Ara sonuç: öncelikli riskler sıralanır.
3. **İçsel bilgi yönetimi:** Bilgi bariyerleri, içsel bilgiye erişen listesi, açıklama/erteleme prosedürü ve işlem yasağı pencereleri tasarlanır; yöneticilerin kişisel işlemleri için kurallar konur.
4. **Sözleşmesel dağıtım:** Aracılık, danışmanlık ve M&A işlemlerinde sorumluluk ve tazminat klozları (TBK çerçevesinde) ile bilgi/beyan yükümlülükleri dengelenir.
5. **Belgeleme:** Tüm karar ve gerekçelerin yazılı/iz bırakacak şekilde tutulması; ispat ve savunma için bu kayıtların kritikliği vurgulanır.

## Çıktı modülleri
- Risk haritası (olasılık-etki matrisi)
- İçsel bilgi yönetim politikası iskeleti
- Uyum kontrol listesi ve sorumluluk dağıtım önerisi
- Öncelikli eylem planı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

