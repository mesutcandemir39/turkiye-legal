---
argument-hint: ''
description: İş kazası tazminatı, SGK rücuu, idari ceza itirazı ve ceza yargılaması
  gibi farklı yolların görevli-yetkili mercilerini, dava şartlarını ve usul yolunu
  belirlemek için kullanılır.
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
  - ad: İş Sağlığı ve Güvenliği Kanunu
    numara: '6331'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İSG Uyuşmazlıklarında Dava, Görev ve Yetki

## Görev
İSG kaynaklı her uyuşmazlığı doğru yargı koluna ve mercie yönlendirmek; görev, yetki, dava şartı (özellikle arabuluculuk) ve usul yolunu netleştirmek.

## Soğuk başlangıç (intake)
- Talep türü: işçi/hak sahibi tazminatı mı, SGK rücuu mu, idari ceza itirazı mı, ceza soruşturması mı?
- Taraflar kim; alt işveren-asıl işveren birlikte mi davalı?
- Olayın ve tebligatın tarihleri (süre ve zamanaşımı için)?
- Arabuluculuğa başvuruldu mu (işçilik alacağı/işe iade dava şartı)?

## Denetim şeması
1. **İş kazası tazminatı:** Görevli mahkeme iş mahkemesidir (7036 sayılı Kanun); yetki kural olarak davalının yerleşim yeri ile işin/işyerinin bulunduğu yer mahkemesi. İşçinin işverenden tazminat talebinde **dava şartı arabuluculuk** uygulanır; ancak iş kazasından kaynaklanan maddi-manevi tazminat ve rücu davaları arabuluculuk dava şartının istisnasıdır (doğrudan dava açılır) — bu istisnayı her dosyada güncel mevzuatla doğrula.
2. **SGK rücu davası:** Görevli mahkeme iş mahkemesi; davacı SGK, davalı kusurlu işveren/üçüncü kişi.
3. **İdari para cezası:** Adli yargı — sulh ceza hâkimliğine itiraz (5326 m.27), idari yargı değil. Bu ayrım sık karıştırılır; yanlış mercie başvuru süre kaybına yol açar.
4. **Ceza yargılaması:** Taksirle öldürme/yaralama (TCK m.85-89) için asliye ceza/ağır ceza; şikâyet ve uzlaşma rejimi suç tipine göre değişir.
5. **Dava şartı ve süre denetimi:** Husumet (asıl işveren-alt işveren birlikte), ehliyet, harç ve süreler. **Ara sonuç:** Her talep için merci-yol-süre üçlüsünü tablola; mevzuata dayalı doğrula.

## Çıktı modülleri
- Talep türü → görevli/yetkili merci → usul yolu tablosu.
- Dava şartı (arabuluculuk) ve istisna notu.
- Husumet ve taraf teşkili kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

