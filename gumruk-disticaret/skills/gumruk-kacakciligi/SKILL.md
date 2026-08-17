---
argument-hint: ''
description: Gümrük işlemleriyle bağlantılı kaçakçılık suç ve kabahatleri, 5607 sayılı
  Kanun kapsamında cezai sorumluluk ve etkin pişmanlık söz konusu olduğunda; idari
  yük ile cezai riski birlikte yönetmek için ku
name: gumruk-kacakciligi
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


# Gümrük Kaçakçılığı ve Cezai Sorumluluk

## Görev
Gümrük işlemleriyle bağlantılı eylemlerin 5607 sayılı Kaçakçılıkla Mücadele Kanunu kapsamında suç mu kabahat mi oluşturduğunu değerlendirmek; cezai sorumluluk, etkin pişmanlık ve idari yükümlülükle ilişkisini birlikte yönetmek.

## Soğuk başlangıç (intake)
- İddia edilen eylem nedir (eşyayı gümrük işlemine tabi tutmadan ithal, sahte belge, gerçeğe aykırı beyan, transit/antrepo eşyasının amacı dışı kullanımı)?
- Soruşturma/kovuşturma aşaması nedir; el koyma var mı?
- Eşyanın kıymeti/vergileri belirlenmiş mi; ödeme veya teminat yapıldı mı?
- Etkin pişmanlık veya idari uzlaşma imkânı kullanılabilir mi?

## Denetim şeması
1. Suç-kabahat ayrımı: Eylemin 5607 m.3'teki ithalat/ihracat kaçakçılığı suçlarından birini mi yoksa idari yaptırımlık kabahati mi oluşturduğu belirlenir. Aynı maddi olayın hem 4458 idari cezası hem 5607 suçu kapsamına girebileceği gözetilir.
2. Tipiklik: Eşyayı gümrük işlemlerine tabi tutmaksızın ithal, aldatıcı işlem/sahte belge ile vergi ödememe, transit/şartlı muafiyet eşyasını amacı dışında tasarruf gibi seçimlik hareketler ayrı ayrı denetlenir.
3. Kast: Kaçakçılık suçları kasten işlenir (TCK m.21); beyan hatası, sınıflandırma görüş ayrılığı gibi durumlarda kastın bulunup bulunmadığı kritiktir.
4. Etkin pişmanlık: 5607'de soruşturma/kovuşturma evresine göre kademeli etkin pişmanlık ve ödemeye bağlı indirim/ceza ilişkisi değerlendirilir; eşyanın gümrüklenmiş değerinin ödenmesi sonuca etki eder.
5. İdari-cezai paralellik: 4458 ek tahakkuk/uzlaşma ile 5607 soruşturması paralel yürüyebilir; non bis in idem ve idari-adli süreçlerin etkileşimi gözetilir.
6. İspat: Suçun maddi ve manevi unsurlarını iddia makamı ispatlar; savunma beyan hatasını, kast yokluğunu ve belge geçerliliğini ortaya koyar. Bu beceri ceza savunması üretmez; risk haritalar ve uzman ceza avukatına yönlendirir.
7. Ara sonuç: Eylemin nitelendirmesi, ceza riski ve etkin pişmanlık/uzlaşma seçenekleri belirlenir. İlkesel içtihat karararama.yargitay.gov.tr üzerinden doğrulanır [DOĞRULANMADI].

## Çıktı modülleri
- Suç-kabahat nitelendirme ve risk haritası
- İdari-cezai süreç paralellik notu
- Etkin pişmanlık/ödeme stratejisi değerlendirmesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

