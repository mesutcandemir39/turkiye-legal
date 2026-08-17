---
argument-hint: ''
description: Özel hayatın ve aile yaşamının korunması, haberleşme ve konut gizliliği,
  kişisel veri, çevre etkisi ile ayrımcılık yasağı/eşitlik bağlamında müdahaleler
  iddia edildiğinde kullanılır.
name: ozel-hayat-aile-esitlik
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  - ad: Anayasa Mahkemesinin Kuruluşu ve Yargılama Usulü Hakkında Kanun
    numara: '6216'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Özel Hayat, Aile ve Eşitlik

## Görev
m.20 (özel hayatın ve haberleşmenin gizliliği), m.21 (konut), aile yaşamı ve m.10 (eşitlik) ile m.17 manevi bütünlük kesişimindeki müdahaleleri değerlendirmek.

## Soğuk başlangıç (intake)
- Müdahale neye dokundu (özel yaşam, itibar, kişisel veri, aile birliği, haberleşme, konut)?
- Müdahale bir kamu işlemi mi, yoksa Devletin koruma yükümlülüğünü yerine getirmemesi mi?
- Ayrımcılık iddiası varsa hangi statüye dayalı ve karşılaştırma grubu kim?
- Müdahalenin kanuni dayanağı ve güttüğü amaç nedir?

## Denetim şeması
1. Uygulanabilirlik — m.20: özel hayat geniş yorumlanır; kişisel veriler, itibar, mesleki-sosyal kimlik, beden bütünlüğü dahildir. Aile yaşamı fiilî yakın bağları kapsar.
2. Negatif/pozitif yükümlülük — Devlet hem müdahaleden kaçınmalı hem de üçüncü kişilere karşı koruma sağlamalıdır (örn. işyerinde izleme, sağlık verisi, çevresel zarar).
3. Müdahale denetimi — m.13: kanunilik, meşru amaç, demokratik toplumda gereklilik ve ölçülülük. Usuli güvenceler (kişinin görüşünü sunması, etkili itiraz) ölçülülüğün parçasıdır.
4. Haberleşme ve konut — iletişimin dinlenmesi, arama-el koyma, konuta müdahale hâkim kararı ve sınırlı istisna şartlarına bağlıdır; usulsüz tedbir ihlal doğurur.
5. Eşitlik/ayrımcılık (m.10) — benzer durumdakilere farklı muamele, objektif ve makul gerekçeye dayanmıyorsa ve ölçüsüzse ayrımcılık oluşur; ayrımcılık genellikle başka bir hakla BAĞLANTILI incelenir. Cinsiyet, doğum, din, dil gibi şüpheli kategorilerde denetim sıkılaşır.

İspat yükü: müdahaleyi/farklı muameleyi başvurucu; haklılığı kamu makamı gösterir. Ayrımcılıkta ilk görünüş ispatından sonra yük yer değiştirebilir.

Ara sonuç: ihlal edilen hak ve varsa eşitlik bağlantısı.

## Çıktı modülleri
- Hak nitelendirmesi (özel hayat/aile/haberleşme/konut/eşitlik).
- Negatif/pozitif yükümlülük ve ölçülülük altlaması.
- Ayrımcılık karşılaştırma analizi.
- İlke kararlarına atıf [DOĞRULANMADI].



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

