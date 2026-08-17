---
argument-hint: ''
description: Poliçenin kurulup kurulmadığı, teminatın ne zaman başladığı, genel/özel
  şartların bağlayıcılığı ve sözleşmenin geçerliliği tartışıldığında kullanılır; teminat
  kapsamı ve sigortalanabilir menfaat sorgu
name: sigorta-sozlesmesi-denetimi
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
  - ad: Bankalar Kanunu
    numara: '5684'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Sigorta Sözleşmesinin Kuruluşu ve Geçerlilik Denetimi

## Görev
Sigorta sözleşmesinin geçerli kurulup kurulmadığını, teminatın başlangıç anını ve genel/özel şartların bağlayıcılığını tespit ederek teminat kapsamını netleştirmek.

## Soğuk başlangıç (intake)
1. Teklifname/başvuru ile poliçe arasında fark var mı; poliçe sigortalıya verildi mi?
2. İlk prim ödendi mi, ne zaman ödendi?
3. Sigortalanan menfaat kime ait, riziko anında mevcut muydu?
4. Genel şartlara ek özel şart/klozlar var mı (çek kloz, abonman, blok poliçe)?

## Denetim şeması
1. **Sözleşmenin kurulması.** TTK m.1401, 1405: icap ve kabul; poliçe verme yükümlülüğü TTK m.1424. Sigortacı, başvurudan itibaren makul sürede red etmezse durumu değerlendir.
2. **Sigortalanabilir menfaat.** Zarar sigortasında menfaat şartı TTK m.1453-1454; menfaat yoksa veya son bulmuşsa sözleşme geçersiz/sona ermiş sayılır. Ara sonuç: korunan menfaat var mı?
3. **Teminatın başlangıcı.** TTK m.1421-1422 ve m.1430: kural olarak ilk prim (peşin/ilk taksit) ödenmeden sigortacının sorumluluğu başlamaz; aksi kararlaştırılabilir. Geçici sigortacılık (cover note) ayrıca değerlendirilir.
4. **Genel/özel şartların bağlayıcılığı.** SEDDK onaylı tip genel şartlar sözleşmenin parçasıdır; sigortalı aleyhine emredici hükme aykırı şartlar geçersizdir (TTK m.1452 — nispi emredicilik). Çelişkide özel şart genel şarta üstün; tüketici sigortalarında haksız şart denetimi (6502 m.5).
5. **Geçersizlik halleri.** TTK m.1408 (rizikonun gerçekleşmiş ya da imkânsız olması), kanuna/ahlaka aykırı menfaat. İspat yükü geçersizliği ileri sürende.

## Çıktı modülleri
- Kuruluş ve teminat başlangıcı zaman çizelgesi.
- Sigortalanabilir menfaat değerlendirmesi.
- Genel/özel şart çatışması ve geçerlilik notu.
- Teminat kapsamı/istisna özeti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

