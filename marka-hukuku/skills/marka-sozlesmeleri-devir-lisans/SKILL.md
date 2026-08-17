---
argument-hint: ''
description: Markanın devri, lisanslanması, rehni veya teminat gösterilmesi söz konusuysa;
  m.148 vd. tasarruf işlemlerinin şekil, sicil ve içerik şartlarını denetlemek ve
  sözleşme taslağı kurmak için kullanılır.
name: marka-sozlesmeleri-devir-lisans
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Marka Sözleşmeleri — Devir, Lisans ve Rehin

## Görev
Marka üzerindeki hukuki işlemleri (devir, lisans, rehin, teminat, miras) SMK m.148 vd. çerçevesinde kurmak; şekil şartı, sicile şerh ve üçüncü kişilere etki kurallarını denetlemek. Geçerlilik ve ihticaca (üçüncü kişilere karşı ileri sürülebilirlik) şartları ayrıdır.

## Soğuk başlangıç (intake)
- İşlem türü ne: tam/kısmî devir, inhisari/inhisari olmayan lisans, rehin, teminat?
- Marka tescilli mi, başvuru aşamasında mı?
- Lisansta alt lisans, münhasırlık, coğrafya, süre, kalite kontrolü nasıl?
- İşlem sicile şerh ediliyor mu?

## Denetim şeması
1. **Devir (m.148/1, m.148/4).** Marka bağımsız olarak veya işletmeyle devredilebilir; devir yazılı şekilde ve taraflarca imzalı olmalıdır (geçerlilik şartı). Aksi kararlaştırılmadıkça işletmenin devri markayı da kapsar.
2. **Sicile şerh ve etki (m.148/5).** Devir/lisans/rehin sicile kaydedilmezse iyiniyetli üçüncü kişilere karşı ileri sürülemez; kayıt kurucu değil, ihticaca yarar etki sağlar.
3. **Lisans (m.24).** İnhisari (münhasır) veya inhisari olmayan lisans; aksi sözleşmede yoksa inhisari olmayan sayılır. İnhisari lisans sahibi kural olarak dava açabilir; inhisari olmayan lisans sahibi marka sahibine bildirip talep etmedikçe açamaz (sözleşmede aksi düzenlenebilir).
4. **İçerik dengeleri.** Kapsam (mal/hizmet, coğrafya, süre), alt lisans yetkisi, kalite/kullanım denetimi, ücret/royalti, tecavüze karşı dava yetkisi, fesih ve devir sonrası kullanım açıkça düzenlenmelidir.
5. **Rehin/teminat (m.148/3).** Marka rehnedilebilir, haczedilebilir; rehin sicile tescil edilir.
6. **Garanti.** Devredende markanın geçerliliği/sınırlamasız oluşu yönünden TBK genel hükümleri (ayıp/zapt) ve sözleşmesel beyan-tekeffüller değerlendirilir.

## Çıktı modülleri
- İşlem türü-şekil-sicil şartı tablosu.
- Lisans/devir sözleşmesi madde iskeleti ([doldurulacak] yer tutucularla).
- Sicile şerh ve üçüncü kişiye etki kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

