---
argument-hint: ''
description: Göç dosyasında ispat yükünün kimde olduğu, hangi belge ve delillerin
  gerektiği veya risk anlatısının nasıl belgeleneceği değerlendirileceğinde kullanılır.
name: ispat-delil
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


# İspat ve Delil Yönetimi

## Görev
Göç ve yabancılar uyuşmazlığında ispat yükünü doğru dağıtmak, gereken belge ve delilleri toplamak, risk/koruma anlatısını doğrulanabilir biçimde belgelemek ve idarenin tespitlerine karşı delil üretmek.

## Soğuk başlangıç (intake)
1. İspatlanacak temel iddia nedir (şart sağlandı, risk var, çalışma izinsiz değil vb.)?
2. Eldeki belgeler nelerdir (pasaport, ikamet, evlilik, gelir, sigorta, tıbbi rapor)?
3. İdarenin dayandığı tespit/tutanak/istihbarat var mı, içeriği biliniyor mu?
4. Yabancı dildeki belgeler için yeminli tercüme/apostil yapıldı mı?

## Denetim şeması
1. **İspat yükü dağılımı**: İdari yargıda re'sen araştırma ilkesi geçerli olsa da, lehe şartların varlığını (ikamet süresi, evlilik birliği, geçim, koruma riski) yabancı; işlemin maddi dayanağını ve kamu düzeni-güvenliği gerekçesini idare ortaya koyar.
2. **Belge delili**: Resmî belgeler (nüfus, tapu, sigorta, banka), yabancı resmî belgelerde apostil/konsolosluk onayı ve yeminli tercüme; sahtelik iddiası ayrıca incelenir.
3. **Koruma riskinin ispatı**: Uluslararası korumada güncel ülke menşe bilgisi, raporlar, tıbbi/psikolojik değerlendirme; standart inandırıcı kılma + tereddütte lehe yorum.
4. **İdarenin gizli/istihbari dayanağı**: Kamu düzeni-güvenliği gerekçeli işlemlerde dayanak çoğu kez soyut kalır; savunmaya esas teşkil eden somut maddi vakıa talep edilir, soyut nitelendirme yeterli sayılamaz (silahların eşitliği/AİHS m.6-13 ekseni).
5. **Delil tespiti/ara karar**: Mahkemeden işlem dosyasının (idari işlem dayanak belgeleri) celbi istenir.
**Ara sonuç**: İddia-delil eşleştirme tablosu ve eksik delil için toplama planı.

## Çıktı modülleri
- İddia/ispat yükü/delil eşleştirme matrisi.
- Eksik belge ve tercüme/apostil yapılacaklar listesi.
- Mahkemeye ara karar/işlem dosyası celbi talep metni.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

