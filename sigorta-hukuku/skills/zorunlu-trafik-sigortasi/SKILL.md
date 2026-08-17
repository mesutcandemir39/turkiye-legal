---
argument-hint: ''
description: Trafik kazası nedeniyle zarar görenin sigortacıya doğrudan başvurması,
  teminat sınırları, kusur dağılımı ve zarar kalemleri tartışıldığında kullanılır;
  zorunlu mali sorumluluk sigortası kaynaklı uyuşm
name: zorunlu-trafik-sigortasi
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  - ad: Bankalar Kanunu
    numara: '5684'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Zorunlu Trafik Sigortası ve Üçüncü Kişinin Doğrudan Hakkı

## Görev
Trafik kazasında zarar görenin Zorunlu Mali Sorumluluk (trafik) sigortacısına doğrudan başvuru hakkını, teminat sınırlarını, kusur dağılımına göre sorumluluğu ve karşılanacak zarar kalemlerini belirlemek.

## Soğuk başlangıç (intake)
1. Kaza tarihi, taraflar ve araçların trafik sigortası poliçeleri ne?
2. Zarar bedeni mi (yaralanma/ölüm/destekten yoksunluk) maddi mi (araç hasarı)?
3. Kaza tespit tutanağı ve kusur durumu nedir?
4. Sigortacıya yazılı başvuru yapıldı mı; teminat limiti aşılıyor mu?

## Denetim şeması
1. **Doğrudan dava hakkı.** KTK m.97 ve m.91: zarar gören üçüncü kişi, doğrudan sigortacıya başvurabilir ve dava açabilir. Dava şartı: önce sigortacıya yazılı başvuru ve 15 günlük cevap süresi (KTK m.97).
2. **Teminat ve sorumluluk.** Sigortacı, işletenin sorumlu olduğu zararı poliçe teminat limitiyle sınırlı karşılar (KTK m.85, m.91; her yıl belirlenen teminat tutarları). Limit üstü kalan, işleten/sürücüye kalır.
3. **Zarar kalemleri.** Bedeni zararlarda tedavi giderleri, geçici/sürekli iş göremezlik, destekten yoksun kalma tazminatı (TBK m.53-55); maddi zararlarda araç onarım/değer kaybı. Ara sonuç: hangi kalemler teminatta?
4. **Kusur ve indirim.** Zarar görenin müterafik kusuru oranında indirim (TBK m.52). Genel şart istisnaları (örn. mücbir sebep, üçüncü kişinin ağır kusuru) sigortacı lehine sınır oluşturabilir.
5. **Zamanaşımı.** KTK m.109: kural iki yıl ve her halde sekiz yıl; fiil aynı zamanda suç oluşturup TCK'da daha uzun zamanaşımı öngörülmüşse o süre (uzamış ceza zamanaşımı) uygulanır. İspat: zararı ve kusuru zarar gören, teminat dışılığı sigortacı.

## Çıktı modülleri
- Doğrudan başvuru ve dava şartı kontrolü (KTK m.97).
- Teminat limiti ve karşılanan/karşılanmayan zarar ayrımı.
- Kusur dağılımı ve indirim hesabı.
- Zamanaşımı (m.109) değerlendirmesi ve süre uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

