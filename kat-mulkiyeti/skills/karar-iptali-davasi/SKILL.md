---
argument-hint: ''
description: Kat malikleri kurulunun bir kararı kanuna, yönetim planına veya dürüstlük
  kuralına aykırı bulunduğunda ya da kurul kararı eksik/gereken kararı almaktan kaçındığında;
  KMK m.33 kapsamında iptal ya da hâ
name: karar-iptali-davasi
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
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kurul Kararının İptali ve Eksikliğin Giderilmesi

## Görev
Kanuna, yönetim planına veya dürüstlük kuralına aykırı kat malikleri kurulu kararının iptalini sağlamak; ayrıca kurulun karar almaktan kaçındığı veya yönetimin işlemediği hâllerde hâkimin müdahalesini (m.33) istemek. Süre ve husumetin doğru kurulması bu davada belirleyicidir.

## Soğuk başlangıç (intake)
- İptali istenen karar hangi toplantıda, hangi gündem maddesiyle alındı; tutanak var mı?
- Müvekkil toplantıya katıldı/aykırı oy kullandı mı, yoksa katılmadı mı (süre buna göre değişir)?
- Karar ne yönden sakat: usul (çağrı/nisap) mu, içerik (kanuna/plana/dürüstlüğe aykırılık) mı?
- Karar tarihinden bu yana ne kadar süre geçti?

## Denetim şeması
1. **Hukuki dayanak (KMK m.33/1)**: Kat malikleri kurulunca verilen karara razı olmayan veya kanuna/yönetim planına aykırı karar alındığını ileri süren her kat maliki, anagayrimenkulün bulunduğu yer **sulh hukuk mahkemesine** başvurabilir.
2. **Dava açma süreleri (m.33/1)**: Toplantıya katılıp karara **aykırı oy kullanan** malik karar tarihinden başlayarak **bir ay** içinde; **toplantıya katılmayan** malik kararı öğrenmesinden başlayarak bir ay ve **her hâlde karar tarihinden başlayarak altı ay** içinde dava açabilir. Süreler hak düşürücüdür, re'sen gözetilir.
3. **İptal sebepleri**: (a) Usul sakatlığı — çağrı eksikliği, yetersiz nisap, gündem dışı karar; (b) içerik sakatlığı — KMK'nın emredici hükmüne (örn. oybirliği gereken konuda çoğunlukla karar), yönetim planına veya TMK m.2 dürüstlük kuralına aykırılık.
4. **Yokluk/butlan ayrımı**: Hiç toplantı yapılmadan veya çağrısız "karar" görüntüsü yoklukla maluldür ve süreye bağlı olmaksızın ileri sürülebilir; bu hâlde tespit istenir. Süreye bağlı iptal ile sürekli ileri sürülebilen yokluk ayrımına dikkat et [ilkeler için karararama.yargitay.gov.tr].
5. **Hâkimin müdahalesi (m.33/2-3)**: Kurul, kanunen alması gereken kararı almaktan kaçınır veya yönetim işlemezse, hâkim kat malikinin istemiyle gerekli tedbiri alır ve eksikliği giderir; aykırı davranan malike idari para cezası benzeri yaptırım uygulanabilir (m.33/son).
6. **Husumet**: Dava, kararı uygulayan/yöneten sıfatıyla diğer kat maliklerine veya temsilci olarak yöneticiye yöneltilir; toplu yapıda ilgili kurul esas alınır.
7. **Ara sonuç**: Süre içindeyse iptal/tespit; süre geçmiş ama yokluk varsa tespit; karar eksikliği varsa hâkimin müdahalesi.

## Çıktı modülleri
- İptal davası dilekçesi iskeleti (karar künyesi, sakatlık sebebi, talep, süre beyanı).
- Süre hesap tablosu (katılan/katılmayan; 1 ay / 6 ay).
- Yokluk-iptal ayrım notu ve tedbir (kararın icrasının durdurulması) talebi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

