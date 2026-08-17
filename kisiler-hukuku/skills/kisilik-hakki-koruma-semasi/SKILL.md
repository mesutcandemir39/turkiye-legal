---
argument-hint: ''
description: Şeref ve itibara, özel hayata, beden bütünlüğüne, isme ya da resme yönelik
  bir saldırı iddiasında saldırının hukuka aykırılığını ve uygun talep yolunu belirlemek
  için kullanılır.
name: kisilik-hakki-koruma-semasi
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


# Kişilik Hakkı İhlali Denetim Şeması (m.24-25)

## Görev
Bir kişilik değerine (şeref-itibar, özel/gizli alan, beden ve ruh bütünlüğü, ad, resim, ses) yönelik müdahalenin hukuka aykırı saldırı oluşturup oluşturmadığını TMK m.24 süzgecinden geçirmek ve m.25'teki davalardan uygununu seçmek.

## Soğuk başlangıç (intake)
- Hangi kişilik değeri zedelendi: şeref/itibar mı, özel hayat mı, beden bütünlüğü mü, ad/resim mi?
- Müdahale ne zaman, hangi araçla (söz, yazı, yayın, görüntü, fiil) yapıldı; sürüyor mu, tekrar tehlikesi var mı?
- Saldıran kim; bir hukuka uygunluk sebebi (rıza, üstün kamu/özel yarar, yetki kullanımı) ileri sürüyor mu?
- İstenen: önleme, durdurma, tespit, maddi/manevi tazminat, kazancın iadesi?

## Denetim şeması
1. **Saldırının tespiti** — TMK m.24/1: kişilik hakkı hukuka aykırı saldırıya uğrayan, hâkimden koruma isteyebilir. Önce bir kişilik değerine müdahale ortaya konur.
2. **Hukuka aykırılık karinesi** — TMK m.24/2: her saldırı hukuka aykırıdır; saldıranın hukuka uygunluk sebebi ispatı gerekir. Hukuka uygunluk sebepleri: (a) zarar görenin rızası, (b) daha üstün nitelikte özel veya kamusal yarar, (c) kanunun verdiği yetkinin kullanılması.
3. **Menfaat tartımı** — Özellikle ifade/basın özgürlüğü ile çatışmada: gerçeklik, güncellik, kamu yararı ve konu-ifade arasındaki ölçü (öz-biçim dengesi) ölçütleri tartılır. Anayasa m.13 ölçülülük ve AYM bireysel başvuru içtihadı esas alınır.
4. **Talep türleri — TMK m.25/1**: (a) saldırı tehlikesinin önlenmesi (men) davası; (b) sürmekte olan saldırıya son verilmesi (durdurma/ref); (c) sona ermiş saldırının hukuka aykırılığının tespiti davası. Ayrıca düzeltme/cevap, kararın yayınlanması istenebilir.
5. **Tazminat — TMK m.25/3 yollamasıyla**: maddi tazminat (TBK m.49 vd.), manevi tazminat (TBK m.58; bedensel zarar/ölümde m.56), saldırı sonucu elde edilen kazancın vekâletsiz iş görme hükümlerine göre iadesi.
6. **İhtiyati tedbir** — HMK m.389 vd.: yayın/saldırının durdurulması için tedbir; ölçülülük ve ifade özgürlüğü dikkate alınır.

## Çıktı modülleri
- Saldırı + hukuka aykırılık + savunma (uygunluk sebebi) tablosu.
- Menfaat tartımı gerekçesi (özellikle yayın hâllerinde).
- Seçilen dava türü ve talep sonucu taslağı.
- İlkesel AYM/Yargıtay atfı, künye `[DOĞRULANMADI]` (kararlarbilgibankasi.anayasa.gov.tr).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

