---
argument-hint: ''
description: Yeni bir dosya açılırken veya mevcut dosyada kritik usul sürelerinin
  takvimlenmesi, izlenmesi ve kaçırma riskinin önlenmesi gerektiğinde kullanılır.
name: dosya-ve-sure-yonetimi
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
  - ad: Avukatlık Kanunu
    numara: '1136'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dosya Açılışı ve Süre Yönetimi

## Görev
Kabul edilen her iş için standart dosya açılışı yapmak ve büronun en yüksek meslekî riski olan süre kaçırma riskini takvimleyerek yönetmek.

## Soğuk başlangıç (intake)
1. Dosyanın yargı kolu nedir (hukuk/ceza/idari/icra/tüketici hakem heyeti)?
2. Hangi olay tetikleyici (tebliğ, öğrenme, ihlal tarihi) ve tarihi nedir?
3. Şu an dosya hangi aşamada (dava açma öncesi, dilekçeler, istinaf vb.)?
4. Halihazırda işleyen bir süre var mı, varsa bitiş tarihi?

## Denetim şeması
1. **Tetikleyici tarih tespiti**: Sürenin başladığı an (tebliğ tarihi, öğrenme, ihlal) belgeyle sabitlenir; tebliğ tarihi tebligat zarfından doğrulanır.
2. **Süre tipi**: İlgili sürenin niteliği belirlenir — usul süresi mi (HMK cevap m.127: kural 2 hafta; istinaf m.345: 2 hafta; temyiz m.361: 2 hafta), idari dava süresi mi (İYUK m.7: 60/30 gün), icra süreleri mi (İİK m.62 ödeme emrine itiraz 7 gün; m.67 itirazın iptali 1 yıl), ceza kanun yolu süresi mi, yoksa maddi hukuk süresi mi (zamanaşımı/hak düşürücü).
3. **Hesaplama (HMK m.92-93)**: Gün/hafta/ay olarak hesap; sürenin son gününün tatile gelmesi halinde izleyen ilk iş gününe uzaması; adli tatil etkisi (HMK m.102 vd.) değerlendirilir.
4. **Tampon ilkesi**: Her kritik süreye iç son tarih (örn. yasal sürenin 3-5 gün öncesi) konur; ön uyarı kademeleri (15/7/3/1 gün) kurulur.
5. **Sorumlu atama**: Her süre için sorumlu avukat ve yedek atanır; çift kontrol (four-eyes) uygulanır.
6. **Ara sonuç**: Tetikleyici + süre tipi + hesaplanmış son tarih + tampon + sorumlu tanımlanınca süre "kapatılmış" sayılır.

## Çıktı modülleri
- Standart dosya açılış formu (taraflar, vekiller, yargı kolu, dosya no).
- Süre takvimi tablosu (süre, dayanak madde, tetikleyici tarih, yasal son tarih, iç son tarih, sorumlu).
- Yaklaşan süreler uyarı listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

