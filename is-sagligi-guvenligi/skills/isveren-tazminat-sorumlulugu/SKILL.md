---
argument-hint: ''
description: İş kazası veya meslek hastalığı nedeniyle işverenin maddi-manevi tazminat
  sorumluluğunun kurulması, kusur ve illiyetin değerlendirilmesi ile zararın hesaplanması
  için kullanılır.
name: isveren-tazminat-sorumlulugu
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


# İşverenin Tazminat Sorumluluğu (İş Kazası)

## Görev
İş kazası/meslek hastalığı nedeniyle işverenin işçiye veya hak sahiplerine karşı maddi ve manevi tazminat sorumluluğunu kurmak; gözetme borcuna aykırılığı, illiyeti, kusuru ve zararı altlamak.

## Soğuk başlangıç (intake)
- Kaza nitelendirildi mi; kusur/bilirkişi raporu var mı, kusur oranı dağılımı ne?
- Sürekli iş göremezlik oranı (maluliyet) belirlendi mi; SGK gelir bağladı mı?
- Talep maddi mi, manevi mi, destekten yoksun kalma mı; talep eden işçi mi, hak sahipleri mi?
- Müterafik kusur, üçüncü kişi kusuru veya beklenmeyen hal iddiası var mı?

## Denetim şeması
1. **Hukuki temel:** İşverenin işçiyi gözetme borcu sözleşmeseldir (TBK m.417/2); ancak ölüm ve bedensel zararların tazmini haksız fiil hükümlerine tabidir (TBK m.417/3, m.49, m.54-56). Bu nedenle hem sözleşmesel hem haksız fiil esasları birlikte uygulanır.
2. **Sorumluluğun unsurları:** (a) işverenin somut bir İSG yükümlülüğünü ihlali (hangi 6331 maddesi/yönetmelik), (b) zarar (maluliyet/ölüm), (c) illiyet bağı, (d) kusur. İşveren önlemleri eksiksiz aldığını ispatlayamazsa sorumlu olur; ispat yükü işverendedir.
3. **Kusur ve illiyet:** Kusur oranı dosyaya özgü bilirkişi/İSG uzman raporuyla belirlenir; soyut oran verilmez. İşçinin kusuru müterafik kusur (TBK m.52) olarak indirim sebebidir, illiyeti kesen ağır kusur ise sorumluluğu tümüyle kaldırabilir.
4. **Zararın hesabı:** Maddi tazminatta bilinen-bilinmeyen dönem, maluliyet oranı, TRH-2010 vb. yaşam tablosu, %X iskonto, SGK gelirinin rücua konu kısmının düşülmesi (peşin sermaye değeri). Manevi tazminatta TBK m.56 ölçütleri. Destekten yoksun kalma için TBK m.53.
5. **İndirim/savunma:** Müterafik kusur, hatır ilişkisi, üçüncü kişi/mücbir sebep. **Ara sonuç:** Sorumluluk kurulduktan sonra kalem kalem hesap iskeleti çıkar.

## Çıktı modülleri
- Sorumluluk unsurları altlama tablosu.
- Maddi/manevi/destek tazminat hesap iskeleti.
- Savunma ve indirim argümanları listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

