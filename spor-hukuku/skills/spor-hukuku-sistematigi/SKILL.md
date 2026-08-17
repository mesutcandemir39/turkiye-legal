---
argument-hint: ''
description: Bir spor uyuşmazlığında devlet mevzuatı, federasyon talimatları, sözleşme
  ve milletlerarası lex sportiva katmanlarını ayırmak, uyuşmazlığı doğru nitelemek
  ve uygulanacak normu belirlemek gerektiğinde
name: spor-hukuku-sistematigi
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
  - ad: Çalışma ve Sosyal Güvenlik Bakanlığı Kuruluş ve Görevleri Hakkında Kanun
    numara: '7405'
    tur: kanun
  - ad: Tıbbi Deontoloji Tüzüğü Hakkında Kanun
    numara: '6222'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Spor Hukuku Sistematiği ve Norm Katmanları

## Görev
Spor uyuşmazlığını doğru nitelemek (disiplin, sözleşme, transfer, doping, idari, ceza), hangi norm katmanının ve hangi federasyonun uygulanacağını belirlemek ve devlet hukuku ile özerk spor düzeni (lex sportiva) arasındaki ilişkiyi kurmaktır.

## Soğuk başlangıç (intake)
1. Hangi branş ve hangi federasyon? (TFF mi, bağımsız bir federasyon mu?)
2. Uyuşmazlığın türü ne: disiplin cezası, sözleşmesel alacak, transfer/uygunluk, doping, idari işlem, ceza?
3. Taraflar kim: sporcu, kulüp, menajer, federasyon, üçüncü kişi?
4. Milletlerarası unsur var mı (yabancı kulüp, FIFA/uluslararası federasyon, CAS)?
5. Daha önce bir kurul/merci karar verdi mi; eldeki karar ve tarihi nedir?

## Denetim şeması
1. **Branş ve federasyon tespiti**: Futbolsa 5894 sayılı Kanun ve TFF talimatları; diğer branşlarda 3289 sayılı Kanun çerçevesinde ilgili bağımsız federasyonun ana statüsü ve talimatları uygulanır.
2. **Katman ayrımı**: (a) devlet mevzuatı (7405, 6222, TCK, TBK); (b) federasyon ana statüsü ve talimatları; (c) özel hukuk sözleşmeleri; (d) milletlerarası düzen (FIFA, WADA Kodu, CAS). Aynı olay birden çok katmana değebilir (ör. şike hem TFF disiplinine hem 6222 m.11 ceza normuna girer).
3. **Nitelendirme**: Disiplin → federasyon disiplin kurulu + tahkim. Sözleşmesel → federasyon uyuşmazlık çözüm kurulu/tahkim ya da genel mahkeme (tahkim şartına göre). İdari → kural olarak federasyon tahkimi; istisnaen idari yargı. Ceza → adli yargı.
4. **Özerklik ve Anayasa m.59**: Federasyonların yönetsel ve disipline ilişkin kararlarında zorunlu tahkim ve tahkim kararlarının kesinliği anayasal temele dayanır; bu, devlet yargısına başvuru imkânını sınırlar.
5. **Ara sonuç**: Uygulanacak norm metni, görevli merci ve süre rejimi tek cümlede sabitlenir.

## Çıktı modülleri
- Katman ve nitelendirme tablosu (olay → katman → norm → merci)
- Uygulanacak talimat/madde listesi (yürürlük tarihiyle)
- Görev-yetki ve süre özeti
- Açık sorular ve doğrulanacak içtihat notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

