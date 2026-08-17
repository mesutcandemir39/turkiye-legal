---
argument-hint: ''
description: Faturaya veya teyit mektubuna itiraz suresinin kacirilmasinin sonuclari,
  ticari defterlerin sahibi lehine/aleyhine delil olusturmasi ve defter ibrazi gerektiginde
  kullanilir.
name: fatura-teyit-ve-ticari-defterler
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


# Fatura, Teyit Mektubu ve Ticari Defterler

## Görev
Fatura ve teyit mektubunun ispat gücünü ve itiraz sürelerinin sonuçlarını belirlemek; ticari defterlerin hangi hallerde sahibi lehine ya da aleyhine delil olduğunu değerlendirmek. Bu araçlar ticari uyuşmazlıkta ispatın belkemiğidir.

## Soğuk başlangıç (intake)
1. Fatura/teyit mektubu kim tarafından, ne zaman gönderildi ve tebliğ edildi?
2. Alıcı tacir mi; 8 gün içinde itiraz etmiş mi?
3. Uyuşmazlık faturanın bedeli mi, içeriği (ödeme, vade, miktar) mi?
4. Taraflar usulüne uygun, tasdikli ticari defter tutuyor mu?

## Denetim şeması
1. **Fatura ve ispat:** TTK m.21/1 — ticari işletmesi gereği bir mal/hizmet veren tacir, isteme bağlı fatura verir. TTK m.21/2 — faturayı alan kişi, aldığı tarihten itibaren 8 gün içinde içeriği hakkında itiraz etmezse, içeriğini kabul etmiş sayılır. Bu karine yalnızca faturanın "içeriğine" ilişkindir; sözleşmenin kurulduğunu tek başına ispatlamaz, ancak içerik (miktar, fiyat, vade) yönünden güçlü karine doğurur.
2. **Teyit mektubu:** TTK m.21/3 — sözlü veya yazışmayla yapılan sözleşmenin teyidi için gönderilen mektuba 8 gün içinde itiraz edilmezse mektubun sözleşmeye uygun sayılacağı kabul edilir.
3. **Ticari defterler:** TTK m.64-88 tutma ve saklama (10 yıl) yükümü; usulüne uygun tutulan ve açılış/kapanış onayları yapılmış defterler. İspat değeri HMK m.222'ye göre belirlenir: tacirin ticari defterleri kendi lehine delil olabileceği gibi (karşı tarafın defterleriyle uyumlu, çelişmiyor ve karşı taraf aksini muteber defterle çürütemiyorsa), aleyhine de delildir; defterler sahibinin aleyhine her zaman delil olur.
4. **Defter ibrazı:** Mahkeme re'sen veya talep üzerine defterlerin ibrazını ister (HMK m.222/1); ibrazdan kaçınma aleyhe değerlendirilebilir.
5. **Ara sonuç:** Süresinde itiraz edilmeyen fatura içeriği kabul sayılır; usulüne uygun defter, HMK m.222 şartlarıyla sahibi lehine delil olur.

## Çıktı modülleri
- Süre/itiraz değerlendirme notu (fatura/teyit, 8 gün hesabı).
- Defterlerin delil değeri analizi (HMK m.222 koşulları).
- İtiraz dilekçesi veya defter ibrazı talebi taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

