---
argument-hint: ''
description: Ceza infaz kurumunda verilen disiplin cezalarını, savunma hakkını, disiplin
  cezasının kaldırılmasını ve hükümlü haklarına yönelik ihlalleri denetlemek gerektiğinde
  kullanılır.
name: disiplin-ve-haklar
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
  - ad: Ceza ve Güvenlik Tedbirlerinin İnfazı Hakkında Kanun
    numara: '5275'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İnfaz Disiplin Cezaları ve Hükümlü Hakları

## Görev
Kurum içi disiplin cezalarının hukuka uygunluğunu, savunma hakkına riayeti ve hükümlü haklarına müdahaleleri 5275 disiplin hükümleri çerçevesinde denetlemek.

## Soğuk başlangıç (intake)
- Hangi disiplin cezası verildi (kınama, ziyaret/haberleşme kısıtlama, hücre vb.)?
- Savunma alındı mı; disiplin kurulu kararı gerekçeli mi?
- Eylem hangi disiplin fiiline karşılık geliyor?
- Cezanın koşullu salıverilmeye/iyi hâle etkisi var mı?

## Denetim şeması
1. Disiplin cezası kataloğu: 5275 m.38-44 kınamadan hücreye kadar dereceli cezaları, m.37 ölçülülük ilkesini düzenler; kıyas yasağına benzer biçimde fiil-ceza eşleşmesi denetlenir. Ara sonuç: ceza türü mevzuata uygun mu?
2. Usul güvenceleri: disiplin soruşturmasında savunma hakkı tanınması, disiplin kurulu kararının gerekçeli olması zorunludur (5275 m.47). İspat yükü: eylemin sübutunu idare ortaya koymalıdır.
3. Çocuk ve özel durumlar: çocuk hükümlülerde farklı disiplin rejimi (5275 m.46) ve özel koruma.
4. Cezanın kaldırılması/ortadan kalkması: iyi hâl ve süre şartıyla disiplin cezalarının kaldırılması (5275 m.48); bu, koşullu salıverilme değerlendirmesini etkiler.
5. Hak ihlali boyutu: ziyaret, haberleşme, sağlık ve insan onuruna uygun tutulma haklarına orantısız müdahale, AYM bireysel başvuru konusu olabilir (kararlarbilgibankasi.anayasa.gov.tr).
6. İtiraz: disiplin cezasına karşı infaz hâkimliği ve itiraz mercii yolu (4675 sayılı Kanun). İlkesel içtihat karararama.yargitay.gov.tr, künye `[DOĞRULANMADI]`.
7. Ara sonuç: cezanın hukuka uygunluğu + itiraz dayanakları.

## Çıktı modülleri
- Disiplin cezası hukuka uygunluk çizelgesi.
- Savunma/usul eksiği listesi.
- İnfaz hâkimliğine şikâyet dilekçesi tetiği.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

