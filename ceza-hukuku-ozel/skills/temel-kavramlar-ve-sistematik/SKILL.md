---
argument-hint: ''
description: Somut bir olayda hangi suç tipinin (veya tiplerinin) gündeme geldiğini
  belirlemek, TCK İkinci Kitap sistematiğine yerleştirmek ve genel hükümlerle bağ
  kurmak gerektiğinde kullanılır.
name: temel-kavramlar-ve-sistematik
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Özel Hükümler Sistematiği ve Suç Tipi Belirleme

## Görev
Bir olay anlatımından hareketle gündeme gelebilecek tüm suç tiplerini TCK 5237 İkinci Kitap sistematiği içinde tespit etmek, bunları korunan hukuki değere göre tasnif etmek ve hangi maddelere odaklanılacağını belirlemek.

## Soğuk başlangıç (intake)
- Olayda kim kime, ne yaptı; somut fiil(ler) nelerdir?
- Bir zarar/netice doğdu mu (ölüm, yaralanma, malvarlığı kaybı, itibar zedelenmesi)?
- Fail kamu görevlisi mi; mağdurla aralarında özel bir ilişki (akrabalık, vesayet, hizmet) var mı?
- Birden fazla fiil/mağdur veya tek fiille birden çok ihlal söz konusu mu?

## Denetim şeması
1. Fiil ayrıştırması: Anlatımı tek tek hareketlere böl. Her hareket için ayrı tipiklik araması yap; tek fiille birden çok suç olabileceğini (fikrî içtima TCK m.44) unutma.
2. Korunan hukuki değere göre tasnif: hayat (m.81 vd.), vücut dokunulmazlığı (m.86 vd.), hürriyet (m.106, m.109), şeref (m.125 vd.), cinsel dokunulmazlık (m.102-105), malvarlığı (m.141 vd., m.155, m.157), kamu güveni (m.204, m.207), kamu idaresi (m.247, m.252, m.257).
3. Tip seçimi ve sınır çizme: Benzer tipleri ayır. Örneğin malın rızayla teslim alınıp sonra mal edinilmesi güveni kötüye kullanma (m.155); hileyle teslim alınması dolandırıcılık (m.157); rıza olmaksızın alınması hırsızlık (m.141); cebir/tehditle alınması yağma (m.148).
4. Genel hükümlerle bağ: Seçilen her tip için kast/taksir (m.21-22), teşebbüs (m.35), iştirak (m.37-41) ve içtima kurallarının uygulanıp uygulanmadığını işaretle; ileri analiz için ilgili uzman beceriye yönlendir.
5. Ara sonuç: Olası suç tiplerinin listesi, her biri için dayanak madde ve "kuvvetli/zayıf ihtimal" notu; eksik bilgi varsa hangi olgunun açıklığa kavuşturulması gerektiği.

## Çıktı modülleri
- Suç tipi haritası (madde atıflı tablo: tip, korunan değer, dayanak madde, ihtimal derecesi).
- Sınır tipler arası ayrım notu (neden bu tip, neden öteki değil).
- Genel hükümler kontrol bayrakları (teşebbüs/iştirak/içtima/şikâyet) ve hangi uzman beceriye gidileceği.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

