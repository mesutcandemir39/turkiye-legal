---
argument-hint: ''
description: Açık kurumdan denetimli serbestliğe ayrılma, denetim yükümlülükleri,
  elektronik izleme ve yükümlülük ihlali sonuçlarını değerlendirmek gerektiğinde kullanılır.
name: denetimli-serbestlik
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
  - ad: Ceza ve Güvenlik Tedbirlerinin İnfazı Hakkında Kanun
    numara: '5275'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Denetimli Serbestlik Tedbirleri ve Yükümlülükler

## Görev
Hükümlünün denetimli serbestlik tedbiriyle cezasını toplum içinde infaz etme imkânını, yükümlülüklerini ve ihlal hâlinde dönüş rejimini 5275 m.105/A ekseninde değerlendirmek.

## Soğuk başlangıç (intake)
- Hükümlü açık kuruma ayrıldı mı; koşullu salıverilmeye ne kadar süre kaldı?
- Daha önce açık kurumdan firar/disiplin sorunu var mı?
- Hangi yükümlülükler öngörülecek (imza, program, elektronik kelepçe)?
- İş/sağlık/eğitim durumu yükümlülük tasarımını etkiliyor mu?

## Denetim şeması
1. Ayrılma şartı: 5275 m.105/A uyarınca açık ceza infaz kurumunda bulunan veya bu kuruma ayrılma şartlarını taşıyan, koşullu salıverilmesine kanunda belirtilen süre kalan iyi hâlli hükümlü denetimli serbestlikten yararlanabilir. Geçici düzenlemelerin süre farkları kontrol edilir. Ara sonuç: uygunluk.
2. Yükümlülükler: denetimli serbestlik müdürlüğünce belirlenen rapor verme, belirli yerlere gitmeme, programlara katılma; uygun hâllerde elektronik izleme (Elektronik Kelepçe). Yükümlülükler 5275 ve Denetimli Serbestlik Hizmetleri Yönetmeliği çerçevesindedir.
3. İhlal sonucu: yükümlülüklere aykırılık veya kasıtlı yeni suç hâlinde tedbir kaldırılır, hükümlü kapalı kuruma iade edilir ve bakiye ceza kurumda çekilir (5275 m.105/A). İspat: ihlal tutanağı denetimli serbestlik müdürlüğünce düzenlenir.
4. Özel gruplar: hamile, ağır hastalık, yaşlılık ve maktu sürelerde özel kolaylıklar; bunlar ayrıca incelenir.
5. İtiraz: müdürlük işlemine/iade kararına karşı infaz hâkimliği yolu (4675 sayılı Kanun). İlkesel içtihat karararama.yargitay.gov.tr üzerinden, künye `[DOĞRULANMADI]`.
6. Ara sonuç: yararlanma uygunluğu + yükümlülük seti + ihlal riski.

## Çıktı modülleri
- Uygunluk ve süre tablosu.
- Yükümlülük listesi ve ihlal sonuç notu.
- İade kararına itiraz tetiği.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

