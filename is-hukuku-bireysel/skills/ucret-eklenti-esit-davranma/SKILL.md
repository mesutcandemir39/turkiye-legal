---
argument-hint: ''
description: Ödenmeyen ücret, prim, ikramiye, AGİ ve eşit davranma (ayrımcılık) tazminatı
  tartışıldığında; ücretin tespiti, gecikme faizi, ücret kesintisi sınırları ve eşitlik
  ilkesi ihlalini değerlendirmek için k
name: ucret-eklenti-esit-davranma
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
  - ad: İş Kanunu
    numara: '4857'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Ücret, Ücret Ekleri ve Eşit Davranma

## Görev
Ücret ve eklerinin ödenip ödenmediğini, miktarını ve eşit davranma ilkesine aykırılığı denetlemek; doğan alacak ve tazminatları belirlemek.

## Soğuk başlangıç (intake)
1. Kararlaştırılan ve fiilen ödenen ücret nedir; bordro ile banka kaydı uyuşuyor mu?
2. Prim, ikramiye, sosyal yardım gibi ekler düzenli mi?
3. Ücret kesintisi/avans mahsubu yapıldı mı?
4. Aynı işi yapan emsallere kıyasla farklı muamele iddiası var mı?

## Denetim şeması
1. **Ücretin korunması (m.32):** Ücret en geç ayda bir, kural olarak banka aracılığıyla ödenir. Ücret nitelikli alacaklarda zamanaşımı **5 yıl**. Ödenmeyen ücret işçiye haklı fesih hakkı verir (m.24/II-e) ve gününde ödenmezse iş görmekten kaçınma hakkı doğabilir (m.34).
2. **Ücretin ispatı:** Bordro imzalı ve ihtirazi kayıtsızsa aksini işçi yazılı delille çürütmelidir. Miktar çekişmeliyse meslek odası/sendika emsal ücret araştırması yapılır.
3. **Ücret kesintisi sınırları (m.38):** İşveren disiplin cezası dışında ücretten kesinti yapamaz; toplu sözleşme/sözleşme dayanağı ve ayda iki günlük ücreti aşmama sınırı vardır.
4. **Asgari ücret ve AGİ:** Ücret asgari ücretin altında olamaz; AGİ ayrı kalemdir (güncel mevzuat ve uygulama değişiklikleri [DOĞRULANMADI]).
5. **Eşit davranma (m.5):** İşveren biyolojik/cinsiyet, dil, ırk, din vb. sebeplerle ayrım yapamaz; esaslı sebep olmadıkça tam-kısmi süreli ve belirli-belirsiz süreliyi farklı işleme tabi tutamaz. İhlalde işçi, dört aya kadar ücreti tutarında **ayrımcılık tazminatı** ve yoksun bırakıldığı haklar talep edebilir. İhlali işçi ortaya koyar, ayrım olmadığını işveren ispatlar.

## Çıktı modülleri
- Ücret/ek tespit tablosu ve eksik ödeme kalemleri.
- Faiz ve zamanaşımı değerlendirmesi.
- Eşit davranma ihlali değerlendirmesi ve tazminat öngörüsü.
- İspat stratejisi notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

