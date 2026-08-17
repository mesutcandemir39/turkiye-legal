---
argument-hint: ''
description: Bir uyuşmazlıkta idari yargı mı adli yargı mı görevli, hangi mahkeme
  (idare/vergi/Danıştay) ve yer yönünden hangi yer mahkemesi yetkili sorularını çözmek
  için kullanılır; dava açılmadan önce yol harit
name: gorev-yetki-yargi-yolu
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Görev, Yetki ve Yargı Yolu Belirleme

## Görev
Uyuşmazlığın idari mi adli yargıda görüleceğini, idari yargı içinde görevli mahkemeyi (idare/vergi mahkemesi/Danıştay) ve yer yönünden yetkili mahkemeyi belirlemek; yanlış yola gitme riskini sıfırlamak.

## Soğuk başlangıç (intake)
1. Uyuşmazlığın kaynağı idari işlem/eylem/idari sözleşme mi, yoksa özel hukuk ilişkisi mi?
2. Konu vergi/gümrük mü, genel idari mi, kamulaştırma bedeli mi?
3. İşlemi yapan idare nerede; taşınmaz/uygulama yeri neresi?
4. İşlem ilk derecede Danıştay'da mı görülecek nitelikte (belirli düzenleyici işlemler)?

## Denetim şeması
1. **İdari/adli ayrımı.** İdari işlem/eylem/idari sözleşme → idari yargı. İdarenin özel hukuk ilişkileri, kamulaştırma **bedeli**, fiili el atma tazminatı → adli yargı. Tereddütte uyuşmazlık mahkemesi içtihadına başvur (`[DOĞRULANMADI]`).
2. **İdari yargı içi görev.** Vergi/gümrük/benzeri mali yükümlülük uyuşmazlıkları → **vergi mahkemesi**; genel idari uyuşmazlıklar → **idare mahkemesi**; 2575 sayılı Kanun'da sayılan belirli düzenleyici işlemler → ilk derecede **Danıştay**.
3. **Tek hâkim/kurul.** 2576 sayılı Kanun uyarınca belirli parasal sınır altındaki davalar tek hâkimle; üstü kurul halinde. Güncel parasal sınırı teyit et (`[DOĞRULANMADI]`).
4. **Yer yetkisi.** Kural: işlemi/eylemi yapan idarenin bulunduğu yer mahkemesi (İYUK m.32). Taşınmaza, kamu görevlilerine, tam yargıya ilişkin özel yetki kuralları (m.33-36) ayrıdır.
5. **İdari merci tecavüzü.** Önce idari başvuru gerekiyorsa (m.11/m.13) doğrudan dava açılırsa dilekçe ilgili mercie tevdi edilir (m.15/1-e); bunu baştan öngör.
6. **Ara sonuç.** Yargı yolu + görevli mahkeme + yetkili yer + tek hâkim/kurul tespiti; varsa zorunlu ön başvuru uyarısı.

## Çıktı modülleri
- Yargı yolu karar ağacı (idari/adli).
- Görevli mahkeme (idare/vergi/Danıştay) ve yer yetkisi tespiti.
- Zorunlu ön başvuru/idari merci uyarısı.
- Yanlış yola gitme riskine karşı kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

