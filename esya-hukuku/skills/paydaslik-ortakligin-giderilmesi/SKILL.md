---
argument-hint: ''
description: Birden çok kişinin malik olduğu taşınmaz/taşınırda kullanım, yönetim
  ve pay tasarrufu sorunları ya da ortaklığın sona erdirilmesi (izale-i şuyu) gündeme
  geldiğinde; aynen taksim ve satış suretiyle gid
name: paydaslik-ortakligin-giderilmesi
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


# Paylı/Elbirliği Mülkiyet ve Ortaklığın Giderilmesi

## Görev
Birlikte mülkiyet ilişkilerini yönetmek: paylı ve elbirliği mülkiyet arasındaki farkı, yönetim ve tasarruf yetkilerini belirlemek ve ortaklığın giderilmesi (izale-i şuyu) davasını aynen taksim veya satış yoluyla kurmak.

## Soğuk başlangıç (intake)
- Mülkiyet paylı mı (belirli paylar) yoksa elbirliği mi (tereke, mal ortaklığı)?
- Talep yönetim/kullanım uyuşmazlığı mı, yoksa ortaklığın tamamen sona erdirilmesi mi?
- Taşınmaz aynen bölünebilir nitelikte mi (imar, yüzölçümü); paydaşlar satışa mı yanaşıyor?
- Üzerinde ipotek, haciz, kira veya muhdesat (bina/ağaç) var mı?

## Denetim şeması
1. **Tür ayrımı**: Paylı mülkiyette her paydaşın belirli (soyut) payı vardır; payını serbestçe devredebilir, rehnedebilir (m.688/3). Elbirliği mülkiyetinde pay belirli değildir; tasarruf bütün üzerinde ve oybirliğiyle yapılır (m.701-702).
2. **Yönetim ve kullanım**: Paylı mülkiyette olağan yönetim pay/paydaş çoğunluğuyla; önemli işlemler çoğunlukla; olağanüstü işlemler oybirliğiyle alınır (m.690-692). Koruma amaçlı işlemleri her paydaş tek başına yapabilir (m.693).
3. **Paydaşlıktan çıkarma**: Yükümlülüklerini ağır biçimde ihlal eden paydaşın paydaşlıktan çıkarılması istenebilir (m.696).
4. **Ortaklığın giderilmesi (m.698-699)**: Her paydaş, aksine sözleşme veya hukuki engel yoksa her zaman paylaşma isteyebilir. Mahkemeden taksim önce **aynen bölme** (m.699/2) ile araştırılır; mümkün değilse **satış suretiyle paylaştırma** (açık artırma) yapılır (m.699/3).
5. **Elbirliğinde önkoşul**: Elbirliği mülkiyetinin önce paylı mülkiyete çevrilmesi veya doğrudan satış istenebilir; terekede tüm mirasçılar davaya dahil edilir (zorunlu dava arkadaşlığı).
6. **Muhdesat ve takyidat**: Üzerindeki bina/ağaç ve ipotek/haciz satış bedelinin paylaşımında ve sıra cetvelinde dikkate alınır.
7. **Ara sonuç**: Aynen taksim mümkünse paylar; değilse satış ve bedelin paylara göre dağıtımı.

## Çıktı modülleri
- Ortaklığın giderilmesi dava dilekçesi iskeleti (paydaş listesi, pay oranları, talep).
- Aynen taksim/satış değerlendirme notu (bölünebilirlik, muhdesat).
- Husumet/zorunlu dava arkadaşlığı kontrol listesi (özellikle tereke).
- Görev: sulh hukuk mahkemesi (HMK m.4); yetki: taşınmazın yeri.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

