---
argument-hint: ''
description: Özlük dosyası, işe alım verisi, işyeri kamerası, e-posta/log izleme,
  sağlık raporu gibi çalışan kişisel verisinin işlenmesi tasarlanıyor veya denetlenecekse
  kullanılır.
name: calisan-kvkk-uyumu
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
  - ad: İş Kanunu
    numara: '4857'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Çalışan ve Aday Verilerinde KVKK Uyumu

## Görev
İK süreçlerinde işlenen çalışan/aday kişisel verisini KVKK'ya uygun dayanağa oturtmak; aydınlatma, saklama-imha ve aktarım rejimini kurmak; işyeri izleme (kamera, e-posta, log) uygulamasını hukuka uygun sınırda tasarlamak.

## Soğuk başlangıç (intake)
1. Hangi veri, hangi süreçte işleniyor (işe alım, özlük, performans, izleme)?
2. Özel nitelikli veri var mı (sağlık raporu, engellilik, sendika, adli sicil)?
3. Veri yurt dışına/üçüncü kişiye (bordro, SGK aracısı, grup şirketi) aktarılıyor mu?
4. İşyerinde kamera veya e-posta/internet izleme var mı, çalışan bilgilendirildi mi?

## Denetim şeması
1. **İşleme şartı (KVKK m.5)**: Çalışan verisinde **açık rıza zayıf dayanaktır** (güç asimetrisi); bunun yerine sözleşmenin ifası, hukuki yükümlülük (SGK/iş mevzuatı) veya meşru menfaat dayanağı tercih edilir.
2. **Özel nitelikli veri (m.6)**: Sağlık verisi yalnızca sınırlı şartlarla ve gerekli teknik tedbirlerle işlenir; sağlık raporu işyeri hekimi/yetkili eliyle işlenmeli, dosyada gereksiz tutulmamalı.
3. **Aydınlatma (m.10)**: İşe alımda ve istihdam başında çalışan aydınlatma metni tebliğ edilmeli; izleme yapılıyorsa kapsamı önceden açıkça bildirilmeli (aksi halde izleme delili hukuka aykırı sayılabilir — içtihat, `[DOĞRULANMADI]`).
4. **İzleme ölçülülüğü**: Kamera/e-posta izleme meşru amaç + ölçülülük + önceden bilgilendirme şartına tabi; özel alana (soyunma odası vb.) izleme yasak.
5. **Aktarım (m.8-9)**: Bordro/SGK/grup şirketi aktarımı için uygun şart ve sözleşmesel güvence; yurt dışı aktarımda ek rejim.
6. **Saklama-imha**: Her veri kategorisi için saklama süresi ve imha politikası; iş ilişkisi sonrası zamanaşımı süreleri kadar tutma gerekçesi.
7. **Ara sonuç**: Dayanaksız/aşırı işleme → Kurul yaptırımı ve davada delil değeri kaybı.

## Çıktı modülleri
- Çalışan aydınlatma metni ve izleme bilgilendirmesi taslağı.
- Veri kategori-dayanak-saklama tablosu.
- Aktarım ve imha politikası notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

