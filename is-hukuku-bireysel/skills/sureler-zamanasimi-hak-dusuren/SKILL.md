---
argument-hint: ''
description: İş hukukunda zamanaşımı ve hak düşürücü sürelerin (haklı fesih 6 işgünü,
  işe iade 1 ay/2 hafta, alacaklarda 5 yıl) hesabı gerektiğinde; hangi talebin ne
  zaman zamanaşımına uğradığını ve kritik süre ka
name: sureler-zamanasimi-hak-dusuren
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
  - ad: İş Kanunu
    numara: '4857'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler, Zamanaşımı ve Hak Düşürücü Süreler

## Görev
İş uyuşmazlığındaki tüm süreleri (hak düşürücü ve zamanaşımı) doğru kanun atfıyla hesaplamak ve süre riski oluşturan kalemleri işaretlemek.

## Soğuk başlangıç (intake)
1. Fesih ve fiili çalışma sona erme tarihi nedir?
2. Talep edilen kalemler hangileri ve hangi tarihte muaccel oldu?
3. Haklı fesih düşünülüyorsa sebebi öğrenme tarihi nedir?
4. İşe iade gündemde mi, fesih bildirimi ne zaman tebliğ edildi?

## Denetim şeması
1. **Hak düşürücü süreler:**
   - Haklı (derhal) fesih: İş K. m.26 — sebebi öğrenmeden itibaren **6 işgünü** ve her halde fiilin gerçekleşmesinden itibaren **1 yıl**.
   - İşe iade: Arabuluculuğa fesih bildiriminin tebliğinden **1 ay**; arabuluculuk anlaşamama tutanağından **2 hafta** içinde dava (7036 m.11, m.3).
2. **Zamanaşımı (7036 Geç. m.8 ve TBK):**
   - Kıdem tazminatı, ihbar tazminatı, kötüniyet tazminatı, eşit davranma (ayrımcılık) tazminatı ve yıllık izin ücreti: **5 yıl** (7036 ile getirilen özel süre; yürürlük tarihi ayrımı için geçiş hükmü gözetilir).
   - Ücret, fazla çalışma, hafta tatili, UBGT gibi ücret nitelikli alacaklar: **5 yıl** (TBK m.147/1).
3. **Başlangıç:** Kıdem/ihbarda zamanaşımı kural olarak fesih tarihinden; ücret ve fazla çalışma gibi dönemsel alacaklarda her dönem muaccel oldukça işler (her ay ayrı).
4. **Kesilme/durma:** Dava, icra takibi, arabuluculuğa başvuru gibi sebepler zamanaşımını keser/durdurabilir; arabuluculukta sürelerin durması (6325 m.16 atfı) gözetilir.
5. **Ara sonuç:** Süresi geçmiş kalem talep edilemez; kısmi dava/ıslah halinde ek talep edilen kısmın zamanaşımı ıslah/ek talep tarihine göre değerlendirilir.

## Çıktı modülleri
- Süre tablosu (kalem / süre türü / başlangıç / bitiş).
- Riskli/kaybedilmiş kalemler uyarısı.
- Zamanaşımını kesecek/durduracak işlem önerisi.
- Geçiş hükmü ve [DOĞRULANMADI] yürürlük notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

