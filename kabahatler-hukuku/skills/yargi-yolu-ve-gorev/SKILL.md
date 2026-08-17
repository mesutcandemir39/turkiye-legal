---
argument-hint: ''
description: Bir idari yaptırım kararına karşı adli yargı (sulh ceza hâkimliği) ile
  idari yargı arasındaki görev ayrımını çözmek, görevsizlik/yetkisizlik ve olumlu-olumsuz
  görev uyuşmazlığı risklerini yönetmek ger
name: yargi-yolu-ve-gorev
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
  - ad: Kabahatler Kanunu
    numara: '5326'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yargı Yolu ve Görev-Yetki Ayrımı

## Görev
İdari yaptırıma karşı doğru yargı yolunu (sulh ceza hâkimliği mi, idari yargı mı) belirlemek ve görev uyuşmazlığı/süre kaybı riskini önlemek.

## Soğuk başlangıç (intake)
- Yaptırım yalnızca idari para cezası mı, yoksa ruhsat iptali/faaliyet durdurma gibi bir idari işlemle birlikte mi?
- Özel kanun, başvuru yolunu ayrıca düzenlemiş mi?
- Karar tek bir işlemden mi, yoksa zincirleme idari işlemlerden mi doğuyor?
- Daha önce verilmiş görevsizlik/yetkisizlik kararı var mı?

## Denetim şeması
1. **Genel kural (5326 m.27/1):** İdari yaptırım kararlarına karşı sulh ceza hâkimliği görevlidir. Bu, idari para cezalarında ana yoldur.
2. **İstisna — idari yargı (5326 m.27/8):** İdari yaptırım, idari yargının görev alanına giren bir işlemin parçası ise (örn. ruhsat iptali, faaliyet durdurma ile birlikte verilen ceza), uyuşmazlığın bütünü idari yargıda (2577 İYUK) görülür. Bu halde dava açma süresi ve usul İYUK'a tabidir.
3. **Bölünme riski:** Aynı kararın idari para cezası kısmı sulh ceza, idari işlem kısmı idari yargı olabilir; içtihat bütünlük lehine yorumlar — ilkesel atıf yapılır, künye `[DOĞRULANMADI]`.
4. **Görev uyuşmazlığı:** Olumlu/olumsuz görev uyuşmazlığında Uyuşmazlık Mahkemesi devreye girer; bu nedenle baştan doğru mercii seçmek süre kaybını önler.
5. **Süre koruması:** Mercide tereddüt varsa, süreyi korumak için doğru kabul edilen yola başvururken alternatif yolun süresini de takip et.
6. **Ara sonuç:** Yargı yolunu, dayanak işlemin niteliğine göre tek cümlede sabitle ve gerekçesini yaz.

## Çıktı modülleri
- Yargı yolu karar ağacı (m.27/1 vs m.27/8).
- Görevsizlik/yetkisizlik riski notu.
- Süre koruma planı (paralel takip gerekiyorsa).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

