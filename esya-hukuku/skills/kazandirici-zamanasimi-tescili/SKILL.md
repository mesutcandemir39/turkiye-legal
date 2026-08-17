---
argument-hint: ''
description: Tapulu taşınmazda kaydın yanlış/eksik olduğu ya da tapusuz taşınmazda
  uzun süreli malik gibi zilyetlik bulunduğu hâllerde; olağan ve olağanüstü kazandırıcı
  zamanaşımı şartları ile tescil davasını kurm
name: kazandirici-zamanasimi-tescili
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kazandırıcı Zamanaşımı ile Mülkiyet Kazanımı

## Görev
Uzun süreli zilyetliğe dayanarak taşınmaz mülkiyetinin kazanılması talebini değerlendirmek: olağan (m.712) ve olağanüstü (m.713) zamanaşımı şartlarını denetlemek ve tescil davasını kurmak.

## Soğuk başlangıç (intake)
- Taşınmaz tapuda kayıtlı mı; kayıtlıysa kimin adına, değilse hiç mi kaydı yok?
- Müvekkil taşınmazı kaç yıldır, ne sıfatla (malik gibi) kullanıyor; aralıksız ve nizasız mı?
- Zilyetlik nasıl başladı; bir tapu/satış belgesine mi dayanıyordu (olağan), yoksa belgesiz mi (olağanüstü)?
- Taşınmaz tarım arazisi, orman, kıyı, mera gibi kazanılması yasak bir nitelikte mi?

## Denetim şeması
1. **Olağan zamanaşımı (TMK m.712)**: Geçerli olmayan bir hukuki sebebe dayanarak tapuya malik olarak yazılan kişi, taşınmaza davasız ve aralıksız 10 yıl iyiniyetle (m.3) malik gibi zilyet olursa mülkiyeti kazanır. Burada zaten adına tescil vardır; dava bu tescili sağlamlaştırır.
2. **Olağanüstü zamanaşımı (TMK m.713)**: Tapuda kayıtlı olmayan veya maliki kim olduğu belirlenemeyen ya da malikinin 20 yıl önce ölmüş/gaip olduğu taşınmazı, davasız ve aralıksız 20 yıl süreyle malik sıfatıyla zilyet bulunan kişi tescil isteyebilir.
3. **Ortak unsurlar**: Zilyetliğin (a) malik sıfatıyla, (b) davasız (nizasız), (c) aralıksız ve (d) süre boyunca sürmesi gerekir. Önceki zilyedin süresi devralanın süresine eklenir (m.996, zilyetlikte halefiyet).
4. **Kazanılamayan mallar**: Orman, kıyı, mera/yaylak/kışlak, devletin hüküm ve tasarrufundaki yerler kazandırıcı zamanaşımına konu olamaz; bu husus re'sen araştırılır.
5. **Usul**: m.713 davası Hazine ve ilgili kamu tüzel kişilerine husumetle açılır; ilan yapılır, keşif ve tanık delili belirleyicidir. Kadastro sırasında ise 3402 sayılı Kanun hükümleri devreye girer.
6. **Ara sonuç**: Şartlar tamsa mahkeme kararıyla tescil; mülkiyet karar kesinleşince (m.705/2 çerçevesinde) kazanılır.

## Çıktı modülleri
- Tescil davası dilekçesi iskeleti (zilyetlik süresi, sıfat, husumet).
- Delil planı (tanık, keşif, kadastro/vergi kaydı, hava fotoğrafı).
- Kazanma yasağı kontrol listesi (orman/kıyı/mera/Hazine).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

