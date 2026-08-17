---
argument-hint: ''
description: Bir kişinin yerleşim yerinin tespiti, dava yetkisinin ve tebligat adresinin
  belirlenmesi ya da hısımlık derecesi gibi statü sorunları ortaya çıktığında kullanılır.
name: yerlesim-yeri-ve-yetki
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


# Yerleşim Yeri, Hısımlık ve Yetki Sonuçları

## Görev
Bir kişinin yerleşim yerini TMK m.19-21 uyarınca belirleyip bunun yetki, tebligat ve statü sonuçlarını çıkarmak; gerektiğinde kan/kayın hısımlığı derecesini hesaplayarak ilgili hükümlere etkisini saptamak.

## Soğuk başlangıç (intake)
- Kişinin sürekli kalma niyetiyle oturduğu yer neresi; birden çok adresi mi var?
- Küçük/kısıtlı mı (yasal yerleşim yeri sorunu), bir kurumda mı kalıyor?
- Sorun bir davanın yetkili mahkemesini mi, tebligatı mı, yoksa statüyü mü ilgilendiriyor?
- Hısımlık sorusu varsa: taraflar arasındaki bağ kan hısımlığı mı, kayın hısımlığı mı; hangi hükme etkisi soruluyor?

## Denetim şeması
1. **Yerleşim yeri kavramı** — TMK m.19: yerleşim yeri, sürekli kalma niyetiyle oturulan yerdir; bir kimsenin aynı zamanda birden çok yerleşim yeri olamaz (teklik ilkesi). Önceki yerleşim yeri belli değilse oturulan yer (m.20) yerleşim yeri sayılır.
2. **Yasal yerleşim yeri** — TMK m.21: velayet altındaki çocuğun yerleşim yeri ana-babanın, ana-baba ortak yerleşim yerine sahip değilse çocuğun kendisine bırakıldığı tarafın yerleşim yeridir; vesayet altındakinin yerleşim yeri bağlı olduğu vesayet makamının bulunduğu yerdir.
3. **Yetki sonucu** — Genel yetkili mahkeme davalının yerleşim yeri mahkemesidir (HMK m.6); tebligat öncelikle yerleşim yeri/bilinen adrese yapılır. Kişiler hukuku taleplerinde (ad değişikliği, kısıtlama) çoğu kez talep edenin yerleşim yeri yetkilidir.
4. **Hısımlık** — TMK m.17: kan hısımlığının derecesi, hısımları birbirine bağlayan doğum sayısıyla belirlenir; üstsoy-altsoy düz hat, ortak kökten gelenler yan hat hısımıdır. TMK m.18: eşlerden biriyle diğer eşin kan hısımları, aynı tür ve dereceden kayın hısımıdır; kayın hısımlığı, onu doğuran evliliğin sona ermesiyle ortadan kalkmaz.
5. **Bağlantı kontrolü** — Hısımlık derecesi; evlenme engelleri, mirasta zümre, tanıklıktan/hâkimlikten çekinme, vesayet gibi kurumlara doğrudan etki eder; ilgili özel hükme taşınır.

## Çıktı modülleri
- Yerleşim yeri tespiti + dayanak (gerçek/yasal/kurumsal).
- Yetkili mahkeme ve tebligat adresi sonucu.
- Hısımlık derece şeması (gerekiyorsa) ve etkilediği hüküm.
- Açık veri eksikleri için `[doldurulacak]` notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

