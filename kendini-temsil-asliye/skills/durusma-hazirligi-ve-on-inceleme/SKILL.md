---
argument-hint: ''
description: Duruşmaya kendisi katılacak taraf ön inceleme ve tahkikat duruşmasına
  nasıl hazırlanacağını, ne söyleyeceğini, hangi belgeleri götüreceğini ve davranış
  kurallarını öğrenmek istediğinde kullanılır.
name: durusma-hazirligi-ve-on-inceleme
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Duruşma Hazırlığı ve Ön İnceleme

## Görev
Tarafı duruşmaya hazır göndermek: ön incelemenin işlevini anlatmak, sulh ihtimalini değerlendirmek, savunma ve soru notlarını hazırlamak.

## Soğuk başlangıç (intake)
- Duruşma türü nedir (ön inceleme, tahkikat, sözlü yargılama)?
- Duruşma günü ve mahkeme bilgisi nedir?
- Tarafların üzerinde anlaştığı ve çekiştiği hususlar neler?
- Dinletmek istediğiniz tanık var mı, geldi mi?
- Sulh/uzlaşma ihtimaliniz var mı, sınırınız nedir?

## Denetim şeması
1. **Ön inceleme (HMK m.137-142):** Mahkeme önce dava şartları ve ilk itirazları inceler; sonra tarafların **anlaştığı ve anlaşamadığı hususları** tespit eder (m.140) ve tarafları sulhe/arabuluculuğa teşvik eder. Bu duruşma kritiktir; uyuşmazlığın çerçevesi burada çizilir.
2. **İddia/savunmanın genişletilmesi (m.141):** Ön inceleme duruşmasında, karşı taraf muvafakat etmedikçe veya ıslah yoluyla olmadıkça yeni iddia/savunma serbestçe eklenemez. Bu nedenle eksik kalan bir husus varsa bu aşama son fırsattır.
3. **Tahkikat:** Deliller toplanır; tanıklar dinlenir, bilirkişi raporu tartışılır. Taraf, tanığa sorulmasını istediği soruları ve rapora itirazlarını hazırlar.
4. **Usul disiplini:** Duruşmaya zamanında gidilir; mazeretsiz gelinmezse dosya işlemden kalkabilir veya yokluğunda karar verilebilir (HMK m.150). Söz hâkim tarafından verilir; saygı kurallarına uyulur.
5. **Sözlü yargılama:** Tahkikat bitince taraflar son sözlerini sunar; talep özetle yinelenir.
6. **Ara sonuç:** Anlaşılan/anlaşılamayan hususlar listesi + delil durumu + sulh sınırı netse taraf duruşmaya hazırdır.

## Çıktı modülleri
- Duruşma hazırlık notu (anlaşma/çekişme listesi, talep özeti).
- Tanığa soru taslağı ve rapora itiraz başlıkları.
- Duruşma davranış ve evrak kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

