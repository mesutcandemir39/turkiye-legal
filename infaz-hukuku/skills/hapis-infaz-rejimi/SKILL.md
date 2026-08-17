---
argument-hint: ''
description: Hapis cezasının kapalı/açık kurum rejimi, açığa ayrılma şartları, çağrı
  ve infaza başlama usulü ile nakil işlemlerini değerlendirmek gerektiğinde kullanılır.
name: hapis-infaz-rejimi
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


# Hapis Cezası İnfaz Rejimi ve Açık Kuruma Ayrılma

## Görev
Hapis cezasının fiziki infaz rejimini belirlemek: çağrı ve infaza başlama, kapalı/açık kurum ayrımı, açığa ayrılma şartları ve nakil/gözlem süreçleri.

## Soğuk başlangıç (intake)
- Hükümlüye çağrı kâğıdı tebliğ edildi mi; kendiliğinden teslim mi olacak?
- Ceza miktarı ve suç tipi açık kuruma doğrudan ayrılmaya uygun mu?
- Sağlık, yaş, kadın/çocuk hükümlü gibi özel durum var mı?
- Tutuklu olarak hâlihazırda kapalı kurumda mı?

## Denetim şeması
1. İnfaza başlama: kesinleşen ilam Cumhuriyet Başsavcılığınca infaza verilir; hükümlüye çağrı kâğıdı çıkarılır (5275 m.19-20). Belirli hâllerde doğrudan yakalama emri düzenlenir. Ara sonuç: infaza giriş usulü.
2. Kurum türü: kural olarak kapalı kuruma alınma; ancak doğrudan açık kuruma ayrılma şartlarını taşıyanlar (kısa ceza, belirli suç dışı tipler) açık kuruma alınır (5275 m.14 ve Açık Ceza İnfaz Kurumlarına Ayrılma Yönetmeliği).
3. Açığa ayrılma: kapalı kurumdaki hükümlünün, koşullu salıverilmeye kalan süre ve iyi hâl şartıyla açık kuruma ayrılması; idare ve gözlem kurulu kararı (5275 m.89, m.14) belirleyicidir. İspat: iyi hâl ve disiplin sicili kurum kayıtlarıyla.
4. Nakil ve gözlem: gözlem ve sınıflandırma (5275 m.23), güvenlik ve disiplin gerekçeli nakiller; hükümlünün talebi veya idare kararıyla.
5. Özel rejimler: kadın, çocuk ve hasta hükümlüler için ayrı düzenlemeler; hastalık nedeniyle infazın ertelenmesi ayrı bir beceride değerlendirilir.
6. İtiraz: ayırma/nakil işlemine karşı infaz hâkimliği yolu (4675 sayılı Kanun). İlkesel içtihat karararama.yargitay.gov.tr, künye `[DOĞRULANMADI]`.
7. Ara sonuç: kurum türü + açığa ayrılma uygunluğu + usul takvimi.

## Çıktı modülleri
- Rejim ve kurum türü tablosu.
- Açığa ayrılma şart kontrol listesi.
- Nakil/itiraz başvuru tetiği.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

