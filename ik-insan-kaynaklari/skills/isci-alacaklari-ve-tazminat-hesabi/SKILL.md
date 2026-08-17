---
argument-hint: ''
description: Kıdem, ihbar, yıllık izin, fazla mesai, UBGT ve diğer işçilik alacaklarının
  hesabı, fesih sonrası yükümlülüklerin belirlenmesi veya karşı hesap çıkarılması
  gerektiğinde kullanılır.
name: isci-alacaklari-ve-tazminat-hesabi
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İşçilik Alacakları ve Tazminat Hesap Şeması

## Görev
Fesih sonrası işverenin ödeyeceği (veya dava edilebilecek) işçilik alacaklarını kalem kalem hesaplamak, hak ediş/zamanaşımı süzgecinden geçirmek ve bordro/SGK kayıtlarıyla tutarlı bir karşı hesap üretmek.

## Soğuk başlangıç (intake)
1. İşe giriş-çıkış tarihleri, son giydirilmiş brüt ücret ve yan haklar (yol, yemek, prim) nedir?
2. Fesih kim tarafından, hangi sebeple yapıldı (kıdem/ihbar hak ediş belirler)?
3. Kullandırılmayan yıllık izin, fazla mesai ve UBGT iddiası var mı, kayıt var mı?
4. Daha önce ödeme/ibraname/avans verildi mi?

## Denetim şeması
1. **Kıdem tazminatı (1475 m.14, yürürlükte)**: 1 yıl+ kıdem ve hak kazandıran fesih (işveren m.25/II hariç fesih, işçinin haklı feshi vb.) şartı; her tam yıl için 30 günlük **giydirilmiş brüt** ücret, kıdem tavanı sınırıyla. m.25/II ile fesihte kıdem yok.
2. **İhbar tazminatı (4857 m.17)**: Bildirim sürelerine (2-8 hafta, kıdeme göre) uymadan fesihte; haklı fesihte (m.25) işveren ihbar ödemez.
3. **Yıllık izin ücreti (m.59)**: Kullandırılmayan izin, fesihte **son ücret** üzerinden ödenir; zamanaşımı fesihten işler.
4. **Fazla çalışma (m.41)**: Haftalık 45 saati aşan süre %50 zamlı; ispatı kural olarak işçide, ancak işyeri kayıt tutmuşsa kayda bakılır. Yıllık 270 saat sınırı.
5. **UBGT/hafta tatili (m.44, 46-47)**: Çalışılan genel tatil ve hafta tatili ücreti zamlı.
6. **Zamanaşımı**: Kıdem, ihbar, yıllık izin alacaklarında **5 yıl** (m.32/8 ve geçiş hükümleri); fazla mesai/UBGT gibi ücret alacaklarında 5 yıl.
7. **İndirim/mahsup**: İbraname (TBK m.420 — yazılı, fesihten 1 ay sonra, banka ödemesi), avans ve önceki ödemeler düşülür. Ara sonuç: net işveren yükü.

## Çıktı modülleri
- Kalem kalem alacak hesap tablosu (hak ediş + zamanaşımı + mahsup).
- Bordro/SGK ile çelişki notu.
- Karşı hesap / sulh teklifi taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

