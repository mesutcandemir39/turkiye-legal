---
argument-hint: ''
description: İkamet izni başvurusu, uzatma, tür değişikliği ya da ret/iptal işlemiyle
  karşılaşıldığında; hangi izin türünün şartlarının taşındığını ve başvuru usulünü
  saptamak gerektiğinde kullanılır.
name: ikamet-izinleri
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
  - ad: Yabancılar ve Uluslararası Koruma Kanunu
    numara: '6458'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İkamet İzinleri ve Başvuru

## Görev
Yabancının durumuna en uygun ikamet izni türünü belirlemek, şartları madde bazında denetlemek, başvuru/uzatma dosyasını kurmak ve ret/iptal işlemine karşı strateji oluşturmak.

## Soğuk başlangıç (intake)
1. Hangi izin türü hedefleniyor (kısa dönem, aile, öğrenci, uzun dönem, insani)?
2. Geçerli pasaport süresi, sağlık sigortası ve adres/gelir durumu nedir?
3. İlk başvuru mı, uzatma mı, tür değişikliği mi; e-ikamet randevusu alındı mı?
4. Daha önce ret, iptal veya giriş yasağı var mı?

## Denetim şeması
1. **Genel şartlar**: YUKK m.30 — pasaport/belge geçerliliği, geçerli sağlık sigortası, kalış amacını destekleyen belge, yeterli ve düzenli maddi imkân.
2. **Tür şartları**:
   - Kısa dönem (m.31/1): turizm, iş, taşınmaz maliki olma vb. dayanak; süre kural olarak her seferinde en fazla 2 yıl (m.32).
   - Aile (m.34-35): destekleyicinin şartları (m.35 — asgari gelir, sigorta, yeterli konut), eş ve çocuk kapsamı.
   - Öğrenci (m.38-39): aktif öğrencilik, öğrenim süresi ile bağlı süre.
   - Uzun dönem (m.42-43): kesintisiz 8 yıl yasal ikamet, son 3 yıl sosyal yardım almama, yeterli gelir, sağlık sigortası, kamu düzeni/güvenliği engeli bulunmaması.
   - İnsani (m.46-47): Başkanlık takdiriyle, diğer izinlerin şartları aranmaksızın.
3. **Ret/iptal sebepleri**: m.33, m.50 — şartların kaybı, sahte belge, kamu düzeni-güvenliği-sağlığı, vize/ikamet ihlali. İşlem gerekçesi ve maddi dayanağı denetlenir.
4. **İspat yükü**: Şartların varlığını ispat başvurana (belge ile); ret gerekçesinin maddi-hukuki dayanağını idare ortaya koymak zorundadır.
**Ara sonuç**: Şartlar tamamsa başvuru/uzatma dosyası; ret varsa İYUK m.2 iptal davası ve m.27 yürütmenin durdurulması yolu.

## Çıktı modülleri
- İzin türü-şart eşleştirme kontrol listesi ve eksik belge dökümü.
- Başvuru/uzatma dilekçe ve ek belge taslağı.
- Ret işlemine karşı iptal davası iskeleti (gerekçe çürütme + YD talebi).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

