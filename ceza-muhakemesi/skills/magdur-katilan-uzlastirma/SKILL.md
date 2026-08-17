---
argument-hint: ''
description: Mağdur/müşteki ve katılanın haklarını, davaya katılmayı, uzlaştırma ve
  seri/basit muhakeme yollarını değerlendirmek gerektiğinde kullanılır.
name: magdur-katilan-uzlastirma
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
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Mağdur, Katılan Hakları ve Uzlaştırma

## Görev
Mağdur/müşteki ve katılanın usuli haklarını kullandırmak; uzlaştırma, seri ve basit muhakeme gibi alternatif/hızlandırılmış yolların uygunluğunu değerlendirmek.

## Soğuk başlangıç (intake)
- Müvekkil mağdur/müşteki mi, davaya katılmak istiyor mu?
- Suç uzlaştırma kapsamında mı (CMK m.253 listesi)?
- Zararın giderilmesi ve tazminat talebi var mı?
- Sanık seri muhakeme/basit yargılamaya uygun mu?
- Katılma talebi için uygun aşama hangisi?

## Denetim şeması
1. **Mağdur hakları.** Mağdur ve şikâyetçi; delil toplanmasını isteme, vekille temsil, soruşturma sonucundan bilgi alma haklarına sahiptir (CMK m.234). Mağdura hakları bildirilir.
2. **Davaya katılma.** Suçtan zarar gören, mağdur veya malen sorumlu, kovuşturma evresinde hüküm verilinceye kadar davaya katılabilir (m.237); katılan kanun yollarına başvurabilir (m.242).
3. **Uzlaştırma.** Soruşturulması/kovuşturulması şikâyete bağlı suçlar ile m.253'te sayılan suçlarda uzlaştırma zorunlu olarak denenir; uzlaşma sağlanırsa KYOK/düşme sonucu doğar (m.253-255). Uzlaştırmacı görevlendirilir.
4. **Seri muhakeme.** Savcı, m.250'deki katalog suçlarda şüphelinin müdafi huzurunda kabulü halinde yarı oranında indirimli yaptırım önerir; mahkeme onaylarsa hüküm kurulur.
5. **Basit yargılama.** Mahkeme, üst sınırı 2 yıl veya altı suçlarda duruşma yapmadan dosya üzerinden basit yargılama uygulayabilir (m.251-252); itiraz halinde duruşmalı yargılamaya dönülür.
6. **Ara sonuç.** Uygun yol (katılma/uzlaştırma/seri/basit) seçilir; zarar giderimi ve tazminat stratejisi buna göre kurulur.

## Çıktı modülleri
- Mağdur/katılan hak ve talep listesi.
- Davaya katılma dilekçesi taslağı (m.237 dayanaklı).
- Uzlaştırma/seri muhakeme uygunluk tablosu (m.253/m.250 kapsamı).
- Zarar giderimi ve tazminat yönlendirme notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

