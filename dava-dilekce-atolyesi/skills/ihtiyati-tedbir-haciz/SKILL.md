---
argument-hint: ''
description: Dava öncesi veya sırasında hakkı güvence altına almak için ihtiyati tedbir
  veya ihtiyati haciz talebini şartları ve teminatıyla kurmak gerektiğinde kullanılır.
name: ihtiyati-tedbir-haciz
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
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İhtiyati Tedbir ve İhtiyati Haciz Talepleri

## Görev
Yargılama sonuna kadar hakkın korunması için geçici hukuki koruma talebini kurmak: HMK'ya göre ihtiyati tedbir, İİK'ya göre para alacaklarında ihtiyati haciz. Şartlar ve teminat doğru kurulmazsa talep reddedilir veya tazminat riski doğar.

## Soğuk başlangıç (intake)
- Korunacak hak para alacağı mı, başka bir hak mı?
- Gecikmede zarar/sakınca doğuyor mu (aciliyet)?
- Haklılık yaklaşık olarak ispatlanabiliyor mu?
- Teminat yatırılabilir mi, muafiyet hâli var mı?

## Denetim şeması
1. Yol ayrımı: Para alacağında kural olarak ihtiyati haciz (İİK m.257); diğer hak ve durumlarda (mevcut durumun korunması, taşınmaza şerh, vb.) ihtiyati tedbir (HMK m.389).
2. İhtiyati tedbir şartları (HMK m.389-390): Hakkın elde edilmesinin önemli ölçüde zorlaşması veya gecikmede sakınca/ciddi zarar; talep edenin hakkı yaklaşık ispat (m.390/3). Tedbir kararı ve kapsamı somut yazılmalı.
3. İhtiyati haciz şartları (İİK m.257): Muaccel (veya istisnaen müeccel) para alacağı; rehinle temin edilmemiş olması; alacağın ve sebebinin yaklaşık ispatı.
4. Teminat: İhtiyati tedbirde HMK m.392, ihtiyati hacizde İİK m.259 — haksız tedbir/haciz nedeniyle doğabilecek zararlar için teminat; istisna ve muafiyetleri kontrol edin.
5. Uygulama ve süre: Tedbirin uygulanması (HMK m.393 — bir hafta içinde icra); ihtiyati hacizde dava açma/takip süresi (İİK m.264 — yedi/bir hafta). Ara sonuç: şart-teminat-süre uygunsa talep hazır; haksız çıkma tazminatı riski (HMK m.399; İİK m.259/son) notlanır.

## Çıktı modülleri
- İhtiyati tedbir/haciz talep dilekçesi taslağı
- Şart denetim listesi (aciliyet, yaklaşık ispat)
- Teminat tutarı/muafiyet notu
- Uygulama ve dava/takip süresi takvimi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

