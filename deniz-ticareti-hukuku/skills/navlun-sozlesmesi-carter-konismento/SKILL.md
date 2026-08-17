---
argument-hint: ''
description: Deniz yoluyla yük taşıma sözleşmeleri (yolculuk çarteri, zaman çarteri,
  kırkambar) ve konişmento düzenlendiğinde; sözleşme tipini, tarafların borçlarını,
  starya/sürastarya ve konişmentonun ispat işlev
name: navlun-sozlesmesi-carter-konismento
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Navlun Sözleşmesi, Çarter Parti ve Konişmento

## Görev
Deniz yoluyla eşya taşıma ilişkisini sözleşme tipine göre çözümlemek; taşıyan ve taşıtanın borçlarını, navlun ve sürastarya alacaklarını belirlemek; konişmentonun düzenlenmesi, içeriği ve ispat gücünü denetlemek.

## Soğuk başlangıç (intake)
- Sözleşme yolculuk çarteri mi, zaman çarteri mi, yoksa kırkambar (parça yük) mü?
- Konişmento düzenlendi mi; nama, emre veya hamiline mi; "temiz" mi yoksa rezerv kayıtlı mı?
- Yükleme/boşaltma süreleri (starya) ve sürastarya kayıtları nasıl belirlenmiş?
- Navlun peşin mi (freight prepaid) yoksa varışta mı ödenecek; FIOST gibi kayıtlar var mı?

## Denetim şeması
1. **Sözleşme tipi**: Yolculuk çarteri/kırkambar ayrımını TTK m.1138 vd. çerçevesinde yap; zaman çarterinde geminin tahsisi ve işletme yükünün dağılımı farklıdır. Tip, riziko ve masraf dağılımını belirler.
2. **Tarafların borçları**: Taşıyanın gemiyi denize, yola ve yüke elverişli hale getirme borcu (TTK m.1141) ve yükü özenle yükleme/istif/boşaltma borcu; taşıtanın navlun ve doğru beyan borcu. İhlalleri tespit et.
3. **Starya/sürastarya**: Yükleme-boşaltma süresinin başlangıcı, hesabı ve sürastarya (demuraj) alacağını sözleşme kayıtlarına göre hesapla; "once on demurrage always on demurrage" gibi kayıtların etkisini değerlendir.
4. **Konişmento işlevi**: Konişmentonun düzenlenmesi, zorunlu içeriği ve üç işlevi — makbuz, taşıma sözleşmesinin ispatı, kıymetli evrak/temsil (TTK m.1228 vd.). Konişmentodaki rezervlerin (clausing) ispat değerine etkisini belirle; konişmento ile çarter parti arasındaki çatışmada hangisinin geçerli olacağını analiz et.
5. **İspat yükü ve ara sonuç**: Temiz konişmento, yükün iyi durumda teslim alındığına dair karine doğurur; aksini taşıyan ispatlar. Çıktıda kimin neyi ispatlayacağını ve sözleşmenin zayıf kayıtlarını işaretle.

## Çıktı modülleri
- Sözleşme tipi ve borç dağılımı tablosu
- Starya/sürastarya hesap taslağı
- Konişmento denetim notu (rezervler, çatışma, ispat değeri)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

