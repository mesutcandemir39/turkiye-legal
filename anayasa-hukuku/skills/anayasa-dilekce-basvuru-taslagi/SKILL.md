---
argument-hint: ''
description: AYM bireysel başvuru formu, norm denetimi başvuru gerekçesi veya anayasaya
  aykırılık itirazı gibi anayasal metinlerin yapılandırılmış taslağını üretmek; başvurunun
  biçim ve içerik şartlarına uygun isk
name: anayasa-dilekce-basvuru-taslagi
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Anayasal Başvuru ve Dilekçe Taslağı

## Görev
Anayasa hukukuna özgü metinlerin — AYM bireysel başvuru formu, iptal davası dilekçesi, görülmekte olan davada Anayasaya aykırılık itirazı — biçim ve içerik şartlarına uygun, gerekçeli ve yer tutuculu bir taslağını üretmek.

## Soğuk başlangıç (intake)
1. Üretilecek metin türü: bireysel başvuru, iptal davası dilekçesi, yoksa aykırılık itirazı mı?
2. İhlal/aykırılık iddiasının dayandığı Anayasa maddeleri ve AİHS karşılıkları neler?
3. Başvurucunun sıfatı, ihlali doğuran nihai işlem ve tarihleri belli mi?
4. Talep edilen sonuç: iptal, ihlal tespiti, yeniden yargılama, yoksa tazminat mı?

## Denetim şeması
1. **Tür ve form belirleme.** Bireysel başvuruda 6216 ve AYM İçtüzüğü'nün öngördüğü resmî form ve zorunlu unsurlar; iptal davasında m.150 ehliyeti ve 60 günlük süre; itirazda m.152 ciddiyet ve uygulanacak norm şartı.
2. **Zorunlu unsurları yerleştir.** Başvurucu/kanuni temsilci kimliği, ihlale yol açan işlem, tüketilen yollar, başvuru tarihleri, ihlal edilen Anayasa ve AİHS maddeleri, açık ve gerekçeli ihlal iddiası, talep. Ara sonuç: zorunlu unsur eksikse başvuru reddi riski.
3. **Gerekçe mimarisi.** Her hak için: koruma alanı → müdahale → m.13/m.15 testi → somut olaya uygulama. Eşitlikte m.10 matrisi. Adil yargılanmada güvence bazlı inceleme.
4. **Süre ve tüketme beyanı.** Bireysel başvuruda otuz günlük süre (6216 m.47/5) ve yolların tüketildiği açıkça belirtilir; iptal davasında 60 gün hesaplanır.
5. **Atıf ve yer tutucu disiplini.** İçtihat künyeleri `[DOĞRULANMADI]`; bilinmeyen tarih/numara/ad alanları `[doldurulacak]` olarak işaretlenir. Sahte esas/karar numarası yazılmaz.

## Çıktı modülleri
- Seçilen tür için başlıklandırılmış dilekçe/form iskeleti.
- Hak bazlı gerekçe blokları ve talep sonucu.
- Eksik bilgi (`[doldurulacak]`) ve doğrulanacak içtihat (`[DOĞRULANMADI]`) listesi ile süre/teslim uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

