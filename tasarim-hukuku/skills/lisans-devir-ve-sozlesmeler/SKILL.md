---
argument-hint: ''
description: Tasarım hakkının devri, lisans verilmesi ve rehni gibi işlemlerin SMK
  m.148 çerçevesinde sözleşmeye bağlanması, sicile şerh ve geçerlilik şartlarının
  kurulması; tasarımın ticarileştirilmesi veya bir t
name: lisans-devir-ve-sozlesmeler
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


# Lisans, Devir ve Sözleşmeler

## Görev
Tasarım hakkı üzerindeki hukuki işlemleri güvenli biçimde kurmak: devir, inhisari/inhisari olmayan lisans, rehin, haciz ve teminat; geçerlilik şartlarını, sicile şerhi ve tarafların risk dağılımını yönetmek.

## Soğuk başlangıç (intake)
1. İşlem türü nedir (tam devir, lisans, rehin, teminat)?
2. Lisans inhisari mi, inhisari olmayan mı; coğrafi/süre/ürün kapsamı nedir?
3. Tasarım tescilli mi (tescilsizde işlem yapısı farklılaşır)?
4. Sicile şerh ve üçüncü kişilere karşı ileri sürülebilirlik isteniyor mu?

## Denetim şeması
1. İşlemlerin türü (SMK m.148/1): Tasarım hakkı devredilebilir, miras yoluyla geçer, lisans konusu olabilir, rehnedilebilir ve teminat olarak gösterilebilir; hacze de konu olur.
2. Şekil ve geçerlilik (SMK m.148/4): Hukuki işlemler yazılı şekle ve taraf imzalarına tabidir; devir için yazılı şekil geçerlilik şartıdır. Sözleşmeyi yazılı kurun, tarafların temsil yetkisini doğrulayın.
3. Sicile kayıt ve etki (SMK m.148/5): İşlemler talep üzerine sicile şerh edilir; sicile kaydedilmeyen işlemler iyiniyetli üçüncü kişilere karşı ileri sürülemez. Karşı tarafı sicilden teyit edin.
4. Lisans türleri (SMK m.158, m.148): İnhisari lisansta lisans veren başkasına lisans veremez ve aksi kararlaştırılmadıkça kendisi de kullanamaz; inhisari lisans sahibi kural olarak kendi adına dava açabilir, inhisari olmayan lisans sahibi sözleşmede aksi yoksa açamaz (önce hak sahibini bilgilendirme/ihtar).
5. Kritik maddeler: Kapsam (ürün/coğrafya/süre), bedel/royalti, kalite ve denetim, alt lisans, tecavüze karşı dava yetkisi, hükümsüzlük/garaanti, fesih ve devir sonrası kullanım. Tescilsiz tasarımda koruma süresinin (3 yıl) sınırını sözleşmeye yansıtın.
6. Ara sonuç: İşlem türü, geçerlilik şartı, sicil durumu ve dava yetkisi net yazılır.

## Çıktı modülleri
- Sözleşme iskeleti (taraflar, hak tanımı, kapsam, bedel, fesih) ve [doldurulacak] alanları.
- Lisans türüne göre dava açma yetkisi tablosu.
- Sicile şerh kontrol listesi ve üçüncü kişi etkisi notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

