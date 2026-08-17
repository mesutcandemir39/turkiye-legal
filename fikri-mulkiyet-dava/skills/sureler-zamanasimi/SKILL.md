---
argument-hint: ''
description: Fikri-sınai uyuşmazlıkta TÜRKPATENT itiraz süreleri, hükümsüzlük/iptal,
  tazminat zamanaşımı, ihtiyati tedbir sonrası dava süresi ve sessiz kalma yoluyla
  hak kaybını hesaplamak gerektiğinde kullanılır.
name: sureler-zamanasimi
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler ve Zamanaşımı

## Görev
Davaya etki eden tüm süreleri (idari itiraz, dava, tedbir, zamanaşımı, hak düşürücü) doğru hesaplayıp takvime bağlamak; hak kaybını önlemek.

## Soğuk başlangıç (intake)
- Bir TÜRKPATENT/YİDK kararı var mı ve tebliğ tarihi nedir?
- Tecavüz ne zaman öğrenildi, ne zaman gerçekleşti, devam ediyor mu?
- İhtiyati tedbir dava açılmadan mı alındı?
- Marka kaç yıldır biliniyor/kullanılıyor (sessiz kalma riski)?

## Denetim şeması
1. İdari süreçler: Marka yayımına itiraz ve karara itiraz süreleri SMK m.18-20 çerçevesinde (yayımdan itibaren itiraz; YİDK kararına karşı dava süresi tebliğden 2 ay — SMK m.21 ilgili hükmü). Süre kaçırılırsa idari karar kesinleşir.
2. Tazminat zamanaşımı: Tecavüz haksız fiildir; TBK m.72 — zararı ve faili öğrenmeden itibaren 2 yıl, her hâlde 10 yıl. Fiil aynı zamanda suç ise daha uzun ceza zamanaşımı uygulanabilir (TBK m.72/1 son cümle).
3. Süregelen tecavüz: İhlal devam ediyorsa zamanaşımı her gün yeniden işlemeye başlar; geçmişe dönük talepte 2 yıllık kesit korunur.
4. Tedbir sonrası dava: Dava açılmadan alınan ihtiyati tedbirde 2 hafta içinde esas dava açılmazsa tedbir kendiliğinden kalkar (HMK m.397/1). Delil tespitinde benzer disiplin.
5. Sessiz kalma: Marka hükümsüzlüğünde 5 yıl boyunca sonraki markaya sessiz kalma hak kaybı doğurur; kötüniyet istisnadır (SMK m.25/6).
6. Hak düşürücü-zamanaşımı ayrımı: Hükümsüzlük davaları kural olarak süreye tabi değildir (kullanmama/sessiz kalma istisnaları hariç). Ara sonuç: her süre kaynağı (idari, adli, tedbir) ayrı izlenir.

## Çıktı modülleri
- Süre takvimi tablosu (kaynak / başlangıç / bitiş / dayanak madde).
- Zamanaşımı risk notu (süregelen ihlal vurgusuyla).
- Tedbir/delil tespiti dava açma süresi uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

