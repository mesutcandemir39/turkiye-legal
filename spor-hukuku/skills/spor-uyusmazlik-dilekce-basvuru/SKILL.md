---
argument-hint: ''
description: Federasyon disiplin kuruluna savunma, uyuşmazlık çözüm kuruluna başvuru,
  tahkim kuruluna itiraz ya da CAS başvurusu için yapılandırılmış taslak üretmek gerektiğinde
  kullanın.
name: spor-uyusmazlik-dilekce-basvuru
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
  - ad: Çalışma ve Sosyal Güvenlik Bakanlığı Kuruluş ve Görevleri Hakkında Kanun
    numara: '7405'
    tur: kanun
  - ad: Tıbbi Deontoloji Tüzüğü Hakkında Kanun
    numara: '6222'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Spor Uyuşmazlıklarında Dilekçe ve Başvuru Taslağı

## Görev
Spor uyuşmazlığında doğru mercie hitap eden, talimat/madde atıflı, vakıa-hukuki sebep-talep mimarisine sahip dilekçe veya başvuru taslağı üretmektir (savunma, itiraz, başvuru, CAS başvurusu).

## Soğuk başlangıç (intake)
1. Hangi mercie hitap edilecek (disiplin kurulu, uyuşmazlık çözüm kurulu, tahkim kurulu, CAS)?
2. Talep ne: ceza/kararın kaldırılması veya hafifletilmesi, alacak, tedbir?
3. Karar/sevk tebliğ tarihi ve başvuru süresi?
4. Dayanak vakıalar ve eldeki deliller neler?
5. Tahkim şartı ve dil (CAS için) durumu nedir?

## Denetim şeması
1. **Merci ve format**: Hedef mercie uygun başlık, taraf ve temsil bilgileri; CAS için dil ve usul kuralları (ilgili federasyonun atıf yaptığı CAS Kodu) kontrol edilir.
2. **Süre kontrolü**: Başvuru süresinin dolup dolmadığı en başta doğrulanır; süre kısa ve genelde hak düşürücüdür.
3. **Vakıa kısmı**: Olaylar kronolojik, tartışmasız ve ihtilaflı ayrımıyla; her vakıaya delil bağlanır (rapor, görüntü, sözleşme).
4. **Hukuki sebepler**: İlgili talimat maddesi, 7405/6222/5894 veya TBK/HMK hükümleri pinpoint atıfla; tipiklik yokluğu, usul ihlali, orantısızlık gibi argümanlar sıralanır.
5. **Talep sonucu**: Açık, infaz edilebilir talep (kararın kaldırılması/değiştirilmesi, tedbir, alacak tutarı); kademeli talep gerekiyorsa asıl-fer'i ayrımı yapılır.
6. **Yer tutucu disiplini**: Bilinmeyen veriler `[doldurulacak]` ile işaretlenir; uydurma tarih/numara yazılmaz. İçtihat `[DOĞRULANMADI]` notuyla verilir.

## Çıktı modülleri
- Tam dilekçe/başvuru taslağı (başlık, vakıa, hukuki sebep, talep)
- Delil listesi ve dizini
- Süre ve merci doğrulama notu
- Doldurulacak alanların kontrol listesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

