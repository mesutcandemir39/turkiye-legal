---
argument-hint: ''
description: Tacirler arasi cerceve/mal alim/hizmet sozlesmesi, cari hesap sozlesmesi,
  fatura itiraz veya temerrut ihtarnamesi ile ticaret sicili basvurusu gibi belgelerin
  TTK emredici hukumlerine uygun taslagini
name: ticari-sozlesme-ve-belge-taslagi
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


# Ticari Sözleşme, İhtarname ve Başvuru Taslağı

## Görev
Ticari işletme hukuku alanında işleme uygun, TTK emredici hükümlerine ve uygulama gerçeğine uygun belge taslağı üretmek: sözleşme, ihtarname veya sicil başvurusu. Belge, yer tutucu disipliniyle hazırlanır.

## Soğuk başlangıç (intake)
1. Hangi belge isteniyor (sözleşme türü / ihtarname / sicil başvurusu)?
2. Taraflar kim; tacir sıfatları ve unvanları ne?
3. Konu, bedel, vade, faiz ve teminat parametreleri belli mi?
4. Müvekkil hangi tarafta; risk toleransı ve pazarlık gücü ne?

## Denetim şeması
1. **Belge tipini ve zorunlu içeriği belirle:** Sözleşmede taraf kimlikleri (unvan + sicil no), konu, edim, bedel/faiz (TTK m.8 serbestisi), teslim/ifa, ayıp ve temerrüt, fesih, uygulanacak hukuk ve uyuşmazlık çözümü (yetki/tahkim — HMK m.17/tahkim şartı). İhtarnamede: muaccel borç, dayanak, verilen süre, sonuç ihtarı; tebliğ usulü TTK m.18/3'e uygun (noter/iadeli taahhütlü/KEP).
2. **Emredici süzgeç:** TTK ve TBK emredici hükümleri (örn. cezai şart indirimi — tacir m.22 ile indirim isteyemez; bunu sözleşmede aleyhe kullan/lehte koru), genel işlem koşulları denetimi (TBK m.20-25; haksız rekabet m.55/1-f), tüketici işlemiyse TKHK önceliği. Geçersiz/asimetrik şartları işaretle.
3. **Faiz ve süre fıkraları:** Ticari temerrüt faizi/avans faizi (3095 m.2) ve fatura itiraz süresine (TTK m.21: 8 gün) atıf; cari hesapta yazılı şekil (TTK m.89) ve dönem sonu bakiye (m.94) hükümleri.
4. **Yer tutucu disiplini:** Bilinmeyen her veri `[doldurulacak: ...]` olarak bırakılır; varsayım yapılmaz, varsayım yapılmışsa açıkça not düşülür.
5. **Ara sonuç:** Taslak, zorunlu unsurlar + emredici süzgeç + müvekkil lehine dengeli risk dağılımı ile tamamlanır; karşı tarafın değiştirmek isteyeceği maddeler ayrıca işaretlenir.

## Çıktı modülleri
- Belge taslağı (madde başlıkları ve yer tutucularla).
- Riskli/müzakere edilecek madde notları (lehte/aleyhte).
- Tebliğ ve süre takip uyarıları (TTK m.18/3, m.21, zamanaşımı).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

