---
argument-hint: ''
description: 3194 sayılı Kanun m.42 uyarınca verilen idari para cezalarına karşı dava
  açılacağında; ceza miktarının hesabı, ağırlaştırıcı katsayılar, ceza muhatabı, zamanaşımı
  ve usul denetimi sorulduğunda kullanı
name: imar-para-cezalari
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
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İmar Para Cezaları (m.42)

## Görev
İmar mevzuatına aykırılıktan verilen idari para cezasının hukuka uygunluğunu (muhatap, hesap, usul, süre) denetlemek ve iptal yolunu kurmak.

## Soğuk başlangıç (intake)
- Ceza hangi aykırılığa dayanıyor (ruhsatsız, ruhsata aykırı, yapı denetim eksiği)?
- Ceza kararının tarihi, miktarı ve hesaplama kalemleri neler?
- Muhatap kim (yapı sahibi, müteahhit, fenni mesul, yapı denetim)?
- Aynı fiile başka işlem (yıkım, başka ceza) uygulandı mı?

## Denetim şeması
1. **Cezanın dayanağı (3194 m.42)**: Ruhsatsız/ruhsata aykırı yapı ve mevzuata aykırı eylemler için idari para cezası; ceza yapının türü, yüzölçümü, sınıfı, kullanım amacı ve aykırılığın niteliğine göre belirlenen katsayılarla hesaplanır.
2. **Hesabın denetimi**: m.42'deki taban ceza ve **ağırlaştırıcı katsayılar** (yapının çevre ve görüntü kirliliğine etkisi, kullanım amacı değişikliği, kat ilavesi, hisseli/komşu parsele tecavüz vb.) tek tek incelenir; her katsayının somut gerekçesi aranır. Yanlış/dayanaksız katsayı kısmen iptal sebebidir.
3. **Ceza muhatabı**: Ceza ilgili yapı sahibine, ayrıca müteahhit ve fenni mesul/yapı denetim kuruluşuna ayrı ayrı kesilebilir; muhatabın doğru tespiti ve sorumluluk derecesi denetlenir. Yanlış muhatap iptal sebebidir.
4. **Usul ve yetki**: Cezayı belediye/il encümeni verir; karar gerekçeli, hesabı gösterir ve usulüne uygun tebliğ edilmiş olmalıdır. Eksik gerekçe/tebliğ şekil sakatlığı doğurur.
5. **Zamanaşımı ve ne bis in idem**: İdari yaptırımlarda 5326 sayılı Kabahatler Kanunu'nun genel hükümleri yardımcı kaynak olabilir; aynı fiile mükerrer ceza ve cezanın yıkımla ilişkisi (cezanın yıkıma engel olmaması) tartışılır.
6. **İspat ve dava**: Yapı tatil tutanağı ve teknik tespit idarenin delili; davacı hesap hatasını/aykırılığın yokluğunu somutlaştırır. İYUK m.7'de 60 gün içinde iptal davası; hesabın bir kısmı sakatsa kısmen iptal istenir.

## Çıktı modülleri
- Ceza hesabı kalem kalem denetim tablosu.
- Muhatap/sorumluluk değerlendirmesi.
- Usul ve gerekçe denetim notu.
- Kısmen/tamamen iptal talepli dilekçe iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

