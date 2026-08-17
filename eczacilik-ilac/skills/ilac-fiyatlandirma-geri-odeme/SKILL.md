---
argument-hint: ''
description: İlaç fiyat kararları, referans fiyat, kâr marjları ile SGK geri ödeme
  listesi, SUT ve Ödeme Komisyonu kararlarına ilişkin uyuşmazlıklarda kullanılır.
name: ilac-fiyatlandirma-geri-odeme
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
  - ad: Hemşirelik Kanunu
    numara: '6197'
    tur: kanun
  - ad: Mimar ve Mühendisler Hakkında Kanun
    numara: '1262'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İlaç Fiyatlandırma ve Geri Ödeme

## Görev
Bir ilacın fiyatlandırma (TİTCK) ve geri ödeme (SGK/SUT) süreçlerini ayrıştırmak, fiyat veya listeye alma/çıkarma işlemine karşı hukuki yolu kurmak.

## Soğuk başlangıç (intake)
- Sorun fiyatla mı (referans fiyat, depocu/eczacı kâr marjı, KDV), geri ödeme ile mi (EK-4 listesi, SUT koşulu) ilgili?
- İşlem: fiyat onayının reddi/düşürülmesi mi, listeye alınmama mı, listeden çıkarılma mı, eşdeğer grup/fiyat kırılması mı?
- Avro kuru/referans fiyat dönemi hangi karara tabi; hangi tebliğ yürürlükte?
- Ürün hayat kurtarıcı/alternatifi yok mu (ölçülülük argümanı için)?

## Denetim şeması
1. **Fiyat rejimi.** Farmasötik Müstahzarların/Beşeri İlaçların Fiyatlandırılmasına Dair Karar ve TİTCK fiyat tebliği: referans fiyat sistemi, avro değeri, depocu ve eczacı kâr oranları. İşlem idari işlemdir → idari yargı, İYUK m.7 (60 gün).
2. **Geri ödeme rejimi.** 5510 m.63 ve SUT; Ödeme Komisyonu Çalışma Usul ve Esasları; EK-4/A, EK-4/B listeleri. Listeye alma/çıkarma ve SUT koşulları idari düzenleyici işlem/birel işlem niteliğinde; iptal davası açılabilir.
3. **Ayrım kapısı.** Fiyat TİTCK’nın, geri ödeme SGK/Komisyonun yetkisindedir; doğru muhatap ve doğru işlem seçilmezse husumet/ehliyet sorunu doğar. Ara sonuç: dava hangi işleme, kime karşı?
4. **Esas denetimi.** Düzenleyici işlemde normlar hiyerarşisi ve ölçülülük; birel işlemde sebep ve gerekçe. İspat: idare fiyat/listenin dayanağını; davacı eşit muamele ihlali, hesaplama hatası veya ölçüsüzlüğü gösterir.
5. **Yürütmenin durdurulması.** Listeden çıkarma gibi hastayı doğrudan etkileyen işlemlerde telafisi güç zarar somutlaştırılarak İYUK m.27 talep edilir.

## Çıktı modülleri
- Fiyat/geri ödeme ayrım ve muhatap tespiti.
- İptal + yürütmeyi durdurma dilekçe iskeleti [doldurulacak].
- Kâr marjı/referans fiyat hesap denetimi tablosu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

