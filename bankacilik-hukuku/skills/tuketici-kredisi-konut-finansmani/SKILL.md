---
argument-hint: ''
description: Tüketici kredisi, konut finansmanı, kredili mevduat veya kredi kartı
  sözleşmesinde tüketici lehine emredici hükümlerin (cayma, erken ödeme, haksız ücret,
  faiz tavanı) uygulanıp uygulanmadığını denetle
name: tuketici-kredisi-konut-finansmani
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
  - ad: Bankacılık Kanunu
    numara: '5411'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tüketici Kredisi, Konut Finansmanı ve Kart Sözleşmeleri

## Görev
Tüketici nitelikli kredi ve kart ilişkilerinde TKHK ve 5464 sayılı Kanun'un emredici koruma hükümlerini uygulamak; haksız ücret/komisyon iadesi, cayma, erken ödeme ve haksız şart taleplerini hukuki dayanağıyla kurmak.

## Soğuk başlangıç (intake)
- Ürün: belirli süreli tüketici kredisi, konut finansmanı, kredili mevduat hesabı (KMH), kredi kartı mı?
- Müşteri gerçek kişi ve ticari/mesleki amaç dışı mı (tüketici tanımı, TKHK m.3)?
- Talep konusu: dosya masrafı/komisyon iadesi, faiz/asgari ödeme itirazı, cayma, erken kapatma indirimi, haksız şart iptali?
- Uyuşmazlık tutarı tüketici hakem heyeti parasal sınırı içinde mi?

## Denetim şeması
1. **Tüketici sıfatı ve kapsam**: TKHK m.3 tüketici tanımı doğrulanır. Tüketici kredisi TKHK m.22-31, konut finansmanı m.32-39, kart ilişkisi 5464 ve TKHK genel hükümlerine tabidir.
2. **Sözleşme şekli ve ön bilgilendirme**: Yazılı/kalıcı veri saklayıcısıyla düzenlenme, sözleşme örneğinin verilmesi, ön bilgilendirme formu yükümlülüğü kontrol edilir; eksiklik tüketici lehine sonuç doğurur.
3. **Cayma ve erken ödeme**: Tüketici kredisinde 14 gün cayma hakkı (TKHK m.24); erken ödemede faiz ve maliyet indirimi (TKHK m.27); konut finansmanında erken ödeme tazminatı sınırları (TKHK m.37).
4. **Ücret/komisyon ve haksız şart**: Yalnızca ürün/hizmetin zorunlu maliyetini yansıtan, tüketiciden açık onay alınan ücretler tahsil edilebilir; dayanaksız dosya masrafı, komisyon ve hesap işletim ücretleri TKHK m.5 ve ilgili tebliğ uyarınca haksız şart olup iadeye tabidir. Bu yöndeki Yargıtay/HGK uygulaması istikrarlıdır [doğrulanacak — karararama.yargitay.gov.tr].
5. **Faiz ve asgari ödeme**: Kredi kartında akdi/gecikme faizi TCMB azami oranlarıyla, asgari ödeme oranı ilgili düzenlemeyle sınırlıdır; aşan tahsilatlar fazlaya ilişkin talep oluşturur. Ara sonuç olarak iade/iptal edilebilir kalemleri ve dayanağını yaz.

## Çıktı modülleri
- İade edilebilir ücret/komisyon kalemleri ve hesap tablosu.
- Tüketici hakem heyeti / tüketici mahkemesi yol seçimi notu.
- Başvuru/dava dilekçesi iskeleti ([doldurulacak] yer tutucularıyla).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

