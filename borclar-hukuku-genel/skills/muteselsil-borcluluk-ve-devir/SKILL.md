---
argument-hint: ''
description: Birden çok borçlunun aynı borçtan birlikte sorumlu olduğu, alacağın temlik
  edildiği veya borcun başkasına geçtiği durumlarda taraflar arası ilişkiyi çözmek
  için kullanılır.
name: muteselsil-borcluluk-ve-devir
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


# Müteselsil Borçluluk, Alacağın Devri ve Borcun Üstlenilmesi

## Görev
Birden çok borçlu/alacaklı arasındaki teselsül ilişkisini, iç-dış ilişki ve rücuyu çözmek; alacağın devri ve borcun üstlenilmesinin geçerlilik ve sonuçlarını belirlemek.

## Soğuk başlangıç (intake)
- Borçlular birden çok mu; teselsül kararlaştırıldı mı yoksa kanundan mı doğuyor?
- Alacaklı kime, ne kadar başvurdu; ödeyen borçlunun rücu hakkı ne?
- Alacak bir başkasına devredildi mi; yazılı temlik var mı?
- Borç bir üçüncü kişiye mi geçti; alacaklının rızası alındı mı?

## Denetim şeması
1. Müteselsil borçluluğun kaynağı: TBK m.162 — teselsül ya borçluların beyanıyla ya kanunla doğar (örn. ortak haksız fiil m.61, adi şirket). Aksi belirtilmedikçe bölünebilir borçlarda teselsül karinesi yoktur.
2. Dış ilişki: m.163 — alacaklı borcun tamamını dilediği borçludan isteyebilir; biri ifa edince hepsi borçtan kurtulur. Borçluların def'ileri: ortak def'iler herkese, kişisel def'iler yalnız ilgiliye ait (m.164-165).
3. İç ilişki ve rücu: m.167 — aksi kararlaştırılmadıkça borçlular eşit pay taşır; fazlasını ödeyen, payları oranında diğerlerine rücu eder; ödeyemeyenin payı paylaştırılır. Halefiyet (m.168) ile alacaklının teminatlarına girer.
4. Alacağın devri (temlik): m.183-194 — kural olarak borçlunun rızası gerekmez; geçerlilik için yazılı şekil (m.184). Devirden önce borçluya yöneltilen def'iler yeni alacaklıya karşı da ileri sürülebilir (m.188); iyiniyetli borçlunun eski alacaklıya ifası (m.186).
5. Borcun üstlenilmesi: m.195-201 — iç üstlenme + dış üstlenme; borçlunun değişmesi alacaklının kabulüne bağlıdır (m.196). Kabule kadar iç ilişki, ret hâlinde sonuçlar; teminatların akıbeti (m.198-199).
6. İspat yükü: Teselsülü/temliki ileri süren yazılı dayanağı; rücu ve payları ödeyen borçlu ispatlar.

## Çıktı modülleri
- Teselsül haritası (dış ilişki/iç ilişki/rücu).
- Temlik veya borç üstlenme sözleşmesi taslağı iskeleti.
- Def'i ve teminat akıbeti kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

