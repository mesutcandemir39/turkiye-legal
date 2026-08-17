---
argument-hint: ''
description: Tazminat davasının hangi mahkemede ve nerede açılacağı, dava şartlarının
  sağlanıp sağlanmadığı ve ispat yükünün nasıl dağılacağı belirlenmek istendiğinde
  kullanılır.
name: dava-gorev-yetki-ve-ispat
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dava, Görev-Yetki ve İspat Düzeni

## Görev
Haksız fiil tazminat davasında görevli ve yetkili mahkemeyi (HMK), dava şartlarını, ispat yükünün dağılımını ve delil rejimini belirlemek; talep sonucunu (belirsiz alacak/kısmi dava) doğru kurmak. Usuldeki hata, esasa girilmeden ret riski doğurur.

## Soğuk başlangıç (intake)
- Taraflar kim (gerçek/tüzel kişi, tacir mi); uyuşmazlık ticari mi?
- Fiil nerede işlendi, zarar nerede doğdu, davalının yerleşim yeri neresi?
- Zarar miktarı baştan belirlenebiliyor mu (belirsiz alacak ihtimali)?
- Eldeki deliller neler; ceza dosyası/bilirkişi raporu var mı?

## Denetim şeması
1. **Görev.** Kural olarak Asliye Hukuk Mahkemesi görevlidir (HMK m.2). Taraflar tacir ve uyuşmazlık ticari işten doğuyorsa Asliye Ticaret Mahkemesi (TTK m.4-5); trafik/sigorta gibi özel rejimlerde özel görev kuralları kontrol edilir.
2. **Yetki.** Genel yetki davalının yerleşim yeri (HMK m.6); haksız fiilde ek olarak fiilin işlendiği veya zararın meydana geldiği ya da gelme ihtimalinin bulunduğu yahut zarar görenin yerleşim yeri mahkemesi de yetkilidir (HMK m.16).
3. **Dava şartları ve türü.** Hukuki yarar, taraf/dava ehliyeti (HMK m.114) kontrol edilir. Miktar baştan tam belirlenemiyorsa belirsiz alacak davası (HMK m.107); aksi halde kısmi/tam eda davası tercih edilir; ıslah imkânı (HMK m.176) gözetilir.
4. **İspat yükü.** Genel kural: iddia eden ispatlar (TMK m.6, HMK m.190). Zarar gören fiil-zarar-illiyet ve kusuru; davalı hukuka uygunluk sebebini, kurtuluş kanıtını ve indirim sebeplerini ispatlar. Kusursuz sorumlulukta kusur aranmaz.
5. **Deliller.** Senet, tanık, bilirkişi (zarar/maluliyet/hesap), keşif; ceza mahkemesi kararının hukuk hâkimini bağlama sınırı (TBK m.74) değerlendirilir.
6. **Ara sonuç.** Görev-yetki-dava türü-ispat dağılımı netleştirilir; harç (nispi), faiz türü ve dava şartı arabuluculuk (ticari/uygulanan hallerde) kontrolü yapılır.

## Çıktı modülleri
- Görev-yetki gerekçe notu (dayanak maddelerle).
- Dava türü seçimi (belirsiz/kısmi/tam) ve ıslah notu.
- İspat yükü dağılım tablosu (taraf-unsur-delil).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

