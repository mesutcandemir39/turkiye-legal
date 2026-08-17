---
argument-hint: ''
description: Deniz ticareti uyuşmazlığında dava açmadan veya savunma kurmadan önce
  görevli ve yetkili mahkemeyi, tahkim/yabancı hukuk şartının geçerliliğini, dava
  şartlarını ve kanun yollarını belirlemek için kull
name: dava-usul-gorev-yetki-tahkim
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


# Dava, Görev-Yetki ve Tahkim

## Görev
Deniz ticareti uyuşmazlığını doğru forumda (mahkeme veya tahkim) konumlandırmak; görevli/yetkili mahkemeyi, tahkim ve yabancı hukuk kayıtlarının geçerliliğini, dava şartlarını ve istinaf/temyiz yolunu belirlemek.

## Soğuk başlangıç (intake)
- Uyuşmazlık konusu nedir ve taraflar tacir mi (ticari dava niteliği)?
- Sözleşmede tahkim şartı, yetki kaydı veya yabancı hukuk seçimi var mı?
- Yabancılık unsuru var mı (yabancı bayrak, yabancı taraf, yurt dışı ifa)?
- Talep edilen geçici koruma var mı (ihtiyati haciz/tedbir)?

## Denetim şeması
1. **Görevli mahkeme**: Deniz ticaretine ilişkin uyuşmazlıklar mutlak ticari dava olup **asliye ticaret mahkemesi**nde görülür (TTK m.4, m.5); ticaret mahkemesi bulunmayan yerde asliye hukuk mahkemesi ticaret mahkemesi sıfatıyla bakar.
2. **Yetki**: HMK'nın genel yetki kurallarıyla birlikte deniz hukukuna özgü kuralları (örn. ihtiyati hacizde geminin bulunduğu yer; taşıma sözleşmesinde teslim/varış yeri) uygula; tacirler arası geçerli yetki sözleşmesini (HMK m.17) gözet.
3. **Tahkim ve yabancı hukuk şartı**: Çarter partilerdeki tahkim ve yabancı hukuk kayıtlarının geçerliliğini ve konişmentoya incorporation (atıf) yoluyla sirayetini değerlendir; milletlerarası tahkimde MTK (4686) ve yabancı hakem kararlarının tenfizini (New York Sözleşmesi) gözet.
4. **Dava şartları ve geçici koruma**: Hukuki yarar, husumet ve gerekirse dava şartı arabuluculuk (ticari alacaklarda 6325 sayılı HUAK) kontrolünü yap; ihtiyati haciz/tedbir talebini ayrı değerlendir.
5. **İspat ve kanun yolu**: İddiayı ileri süren ispatlar; belge ve sörvey raporları esastır. İlk derece sonrası **istinaf** (BAM) ve kesinlik sınırını aşan kararlarda **temyiz** (Yargıtay) yolunu ve sürelerini hesapla. Çıktıda forum ve süre haritasını netleştir.

## Çıktı modülleri
- Görev-yetki-forum karar tablosu
- Tahkim/yabancı hukuk kaydı geçerlilik notu
- Dava şartı ve kanun yolu süre takvimi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

