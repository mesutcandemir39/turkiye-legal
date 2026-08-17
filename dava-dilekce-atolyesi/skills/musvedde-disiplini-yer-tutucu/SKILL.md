---
argument-hint: ''
description: Taslak layihada eksik bilgileri uydurmadan yer tutucularla işaretlemek,
  kontrol listesi ve eksik raporu üretmek, avukat denetimine hazır müsvedde teslim
  etmek gerektiğinde kullanılır.
name: musvedde-disiplini-yer-tutucu
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Müsvedde Disiplini ve Yer Tutucu Yönetimi

## Görev
Üretilen her layiha müsveddesini avukat denetimine hazır, eksiksiz işaretlenmiş ve doğrulanabilir biçimde teslim etmek. Eksik bilgi asla uydurulmaz; yer tutucularla işaretlenir ve listelenir. Bu beceri atölyenin kalite kapısıdır.

## Soğuk başlangıç (intake)
- Müsveddede hangi bilgiler eksik (tarih, bedel, taraf, delil)?
- Hangi madde atıfları teyit edilmeli (yürürlük/tutar)?
- Hangi içtihat künyesi doğrulanmamış durumda?
- Son kontrol listesi (süre, harç, görev) tamam mı?

## Denetim şeması
1. Yer tutucu standardı: Eksik bilgileri `[doldurulacak]`, `[tarih]`, `[bedel]`, `[TC/vergi no]`, `[delil eki]` gibi tutarlı işaretlerle gösterin; metne tahmini değer yazmayın.
2. Madde teyidi: Süre, tutar ve harç gibi güncellenen normları (parasal sınırlar, faiz oranı) `[yürürlük teyit edilecek]` ile işaretleyin; yürürlük tarihini kontrol önerisi ekleyin.
3. İçtihat hijyeni: İlkesel atıf yapın; karar künyesini doğrulamadan yazmayın. Doğrulanmamış her künyeyi `[DOĞRULANMADI]` ile işaretleyip karararama.yargitay.gov.tr / karararama.danistay.gov.tr / kararlarbilgibankasi.anayasa.gov.tr kaynağını anın.
4. Son kontrol listesi: Görev-yetki, dava şartı/arabuluculuk, süre, harç, talep sonucu netliği, delil-vakıa bağı, imza/vekâletname. Her kalemi tamam/eksik olarak işaretleyin.
5. Teslim notu: Müsveddenin avukat onayı gerektirdiğini, kritik risklerin (süre, teksif) makinece kapatılamadığını belirtin. Ara sonuç: eksik listesi ve kontrol listesi olmadan müsvedde teslim edilmez.

## Çıktı modülleri
- İşaretlenmiş layiha müsveddesi
- Eksik bilgi/yer tutucu raporu
- Doğrulanacak madde ve içtihat listesi
- Teslim öncesi son kontrol listesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

