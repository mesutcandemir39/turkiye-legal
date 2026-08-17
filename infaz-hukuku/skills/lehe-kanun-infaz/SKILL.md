---
argument-hint: ''
description: İnfaz oranlarını değiştiren geçici maddeler, 7242 sayılı Kanun türü değişiklikler,
  af ve lehe kanun uygulamasının infaza etkisini çözümlemek gerektiğinde kullanılır.
name: lehe-kanun-infaz
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


# Lehe Kanun, Af ve Geçici Düzenlemelerin İnfaza Etkisi

## Görev
Suç tarihi ile infaz tarihi arasında değişen infaz hükümlerinden hangisinin uygulanacağını, af ve geçici düzenlemelerin etkisini lehe kanun ilkesi (TCK m.7) ışığında çözmek.

## Soğuk başlangıç (intake)
- Suç tarihi ile hüküm/kesinleşme tarihleri nedir?
- Aralıkta infaz oranını değiştiren bir kanun (örn. 7242 sayılı Kanun) yürürlüğe girdi mi?
- Suç tipi geçici düzenlemelerin kapsamına giriyor/dışında mı?
- Bir af, özel af veya seçimlik yaptırım düzenlemesi söz konusu mu?

## Denetim şeması
1. Niteliği belirle: TCK m.7/2 sonradan yürürlüğe giren lehe kanunun uygulanmasını öngörür; ancak infaz rejimine ilişkin hükümlerin maddi ceza hükmü mü yoksa usule ilişkin mi sayılacağı tartışmalıdır. Koşullu salıverilme ve denetimli serbestlik oranları, yerleşik yaklaşım uyarınca suç tarihine göre lehe olan biçimde uygulanır. Ara sonuç: hangi metin uygulanacak?
2. Geçici maddeler: 7242 sayılı Kanun ve TCK geçici m.6 gibi düzenlemeler, belirli suç tipleri dışında oranları değiştirmiştir; kapsam dışı suçlar (terör, kasten öldürme, cinsel suçlar, uyuşturucu ticareti) için istisna rejimi kontrol edilir.
3. Af: genel af mahkûmiyeti tüm sonuçlarıyla, özel af cezanın infazını etkiler (TCK m.65); af kanununun kapsam ve şartları metinden doğrulanır.
4. Karşılaştırmalı uygulama: suç tarihindeki ve hâlihazırdaki düzenlemelere göre iki ayrı infaz hesabı yapılır, hükümlü lehine olan benimsenir. İspat: yürürlük tarihleri ve geçici madde metinleri mevzuat.gov.tr üzerinden.
5. İtiraz/uyarlama: lehe hükmün uygulanması talebi infaz savcılığına/infaz hâkimliğine; uyarlama gereken hâllerde hükmü veren mahkemeye yöneltilir.
6. İlkesel içtihat: lehe kanun ve infaz oranı için karararama.yargitay.gov.tr Yargıtay CGK ve 1. CD; AYM eşitlik/öngörülebilirlik kararları (kararlarbilgibankasi.anayasa.gov.tr). Künye `[DOĞRULANMADI]`.
7. Ara sonuç: uygulanacak metin + lehe hesap + başvuru mercii.

## Çıktı modülleri
- İki senaryolu lehe karşılaştırma tablosu.
- Kapsam/istisna kontrol listesi.
- Lehe hüküm uygulanması veya uyarlama talebi dilekçesi tetiği.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

