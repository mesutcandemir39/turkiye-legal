---
argument-hint: ''
description: Taşıma uyuşmazlığında görevli-yetkili mahkemenin belirlenmesi, ticari
  dava ve arabuluculuk dava şartının değerlendirilmesi, CMR yetki kuralları ve uygulanacak
  hukukun tespiti gerektiğinde kullanılır.
name: dava-usul-gorev-yetki
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


# Taşıma Davalarında Usul, Görev ve Yetki

## Görev
Taşıma uyuşmazlığında doğru mahkemeyi (görev-yetki), dava şartlarını ve CMR'ye özgü yetki/uygulanacak hukuk kurallarını belirlemek.

## Soğuk başlangıç (intake)
1. Uyuşmazlık ticari mi (taraflar tacir / TTK kapsamı)?
2. Taşıma iç mi, CMR'ye tabi sınır aşan mı?
3. Tarafların yerleşim yeri, teslim alma ve teslim yerleri nerede?
4. Sözleşmede yetki, tahkim veya uygulanacak hukuk şartı var mı?

## Denetim şeması
1. **Görev:** Taşıma işleri TTK'da düzenlendiğinden uyuşmazlık mutlak ticari davadır (TTK m.4/1); görevli mahkeme Asliye Ticaret Mahkemesidir. Ticaret mahkemesi bulunmayan yerde asliye hukuk ticaret sıfatıyla bakar.
2. **Arabuluculuk dava şartı:** Ticari davalarda konusu para alacağı/tazminat olan uyuşmazlıklarda dava şartı arabuluculuk uygulanır (TTK m.5/A; HUAK m.18/A). Dava açmadan önce başvuru zorunludur.
3. **Yetki (iç taşıma):** HMK genel yetki — davalının yerleşim yeri (HMK m.6); sözleşmeden doğan davada ifa yeri (HMK m.10). Yetki sözleşmesi tacirler arası geçerli (HMK m.17).
4. **Yetki (CMR):** CMR m.31 — davacı, tarafların kararlaştırdığı mahkeme ile davalının mutat meskeni/işletme merkezi, eşyanın teslim alındığı yer veya teslim için belirlenen yer mahkemelerinde dava açabilir; bu mahkemeler münhasırdır.
5. **Uygulanacak hukuk:** Sınır aşan taşımada CMR doğrudan uygulanır; boşlukta MÖHUK'a göre tespit edilen hukuk. Sözleşmesel hukuk seçimi MÖHUK m.24 sınırında geçerli.
6. **İhtiyati tedbir/delil tespiti:** Eşyanın durumunun tespiti için delil tespiti (HMK m.400) ve gerekirse ihtiyati haciz (İİK m.257) değerlendirilir.
7. **Ara sonuç:** Görevli-yetkili mahkeme, dava şartı arabuluculuk gerekliliği ve uygulanacak hukuk netleşir.

## Çıktı modülleri
- Görev-yetki belirleme tablosu (iç taşıma / CMR m.31).
- Dava şartı arabuluculuk ve süre kontrol listesi.
- Uygulanacak hukuk ve yetki şartı geçerlilik notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

