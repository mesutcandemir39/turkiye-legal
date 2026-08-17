---
argument-hint: ''
description: Genel kurulda toplanti ve karar yetersayilari, agirlastirilmis nisaplar,
  oyda imtiyaz, oydan yoksunluk ve toplantinin ertelenmesi konularinda hesap ve denetim
  yapilacaksa kullanilir.
name: nisap-oy-ve-karar-alma
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


# Toplantı Nisabı, Oy ve Karar Alma

## Görev
Genel kurulda toplantı ve karar yetersayılarını doğru hesaplamak; ağırlaştırılmış nisapları, oyda imtiyazı ve oydan yoksunluğu denetleyerek kararın geçerli alınıp alınmadığını belirlemek.

## Soğuk başlangıç (intake)
1. Karar konusu olağan bir karar mı, esas sözleşme değişikliği mi, m.421'in özel nisap gerektiren hâllerinden biri mi (tür değiştirme, tabiiyet değişikliği, pay senetleri devrinin sınırlanması vb.)?
2. Esas sözleşmede ağırlaştırılmış nisap var mı?
3. Oyda imtiyazlı pay veya oydan yoksunluk doğuran ilişki (m.436) söz konusu mu?
4. İlk toplantıda nisap sağlandı mı; ikinci toplantı yapıldı mı?

## Denetim şeması
1. **Genel nisap:** Kanun veya esas sözleşmede aksi öngörülmedikçe GK, sermayenin **en az dörtte birini** karşılayan payların sahipleriyle toplanır; bu nisap toplantı süresince korunur. İlk toplantıda sağlanamazsa ikinci toplantıda nisap aranmaz (m.418). Kararlar, toplantıda hazır bulunan oyların çoğunluğuyla alınır.
2. **Ağırlaştırılmış nisaplar:** m.421 belirli esas sözleşme değişiklikleri için özel nisaplar getirir; örneğin bilanço zararlarının kapatılması için ek ödeme/yükümlülük, tabiiyet/merkez değişikliği gibi hâllerde **oybirliği** veya nitelikli çoğunluk aranır. Konu hangi fıkraya giriyorsa o fıkranın nisabı uygulanır; yanlış nisap iptal sebebidir.
3. **Oyda imtiyaz ve yoksunluk:** Oyda imtiyaz m.479 sınırları içinde geçerlidir (esas sözleşme değişikliği, ibra ve sorumluluk davasında imtiyaz kullanılamaz — m.479/3). Pay sahibi, kendisi/eşi/alt-üstsoyu ile şirket arasındaki kişisel nitelikli işlerde ve ibra/sorumlulukta oy kullanamaz (m.436).
4. **Erteleme:** Finansal tabloların müzakeresi, azlığın talebiyle bir ay sonraya ertelenir (m.420); bu hak gündeme bağlılıktan bağımsızdır.
5. **İspat yükü/ara sonuç:** Nisabın varlığı hazır bulunanlar listesi (m.415) ve tutanakla (m.422) ispatlanır. Nisap hatası, oydan yoksun payların oya katılması veya imtiyazın yasak alanda kullanılması kararı iptale açar; bazı temel ihlaller (sermayenin korunması) butlana gidebilir.

## Çıktı modülleri
- Nisap hesap tablosu (toplantı + karar nisabı, ilk/ikinci toplantı).
- m.421 konu-nisap eşleştirme cetveli.
- Oydan yoksunluk/imtiyaz uygunluk notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

