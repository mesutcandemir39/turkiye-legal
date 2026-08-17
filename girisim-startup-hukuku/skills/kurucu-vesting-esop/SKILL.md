---
argument-hint: ''
description: Kurucu paylarının hak edilmesi (vesting) ve çalışanlara hisse/opsiyon
  verme (ESOP) programları kurgulanırken; pay havuzunun oluşturulması, hak ediş ve
  geri alım mekaniği, AŞ kendi pay iktisabı sınırı
name: kurucu-vesting-esop
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kurucu Vesting ve Çalışan Hisse Opsiyonu (ESOP)

## Görev
Ekip teşvik yapısını kurmak: kurucu paylarının vesting takvimi ve ayrılışta geri alımı; çalışan opsiyon havuzunun (ESOP) oluşturulması, tahsisi, hak edişi ve vergisel sonuçları.

## Soğuk başlangıç (intake)
1. Kurucu vesting takvimi ne (ör. 4 yıl, 1 yıl cliff) ve ayrılışta pay ne olacak?
2. ESOP havuzu yüzde kaç; turdan önce mi sonra mı açılıyor (kimi sulandırıyor)?
3. Çalışana gerçek pay mı, sanal/fantom pay mı, yoksa pay opsiyonu mu veriliyor?
4. Hak ediş tetikleyicileri ve ayrılma (good/bad leaver) sonuçları belirlendi mi?
5. Şirket AŞ mi; opsiyon karşılığı paylar nereden gelecek (havuz/artırım/kendi pay)?

## Denetim şeması
1. Kurucu vesting: Kurucu payları baştan ihraç edilir; vesting "hak edilmemiş payların ayrılışta geri alınması/zorunlu satışı" olarak kurgulanır. Mekanik: SHA + esas sözleşmesel zorunlu satış/önalım (TTK m.491-493) + cezai şart (TBK m.179). Good/bad leaver ayrımı ve fiyat (nominal mi gerçek değer mi) yazılır.
2. ESOP yapı seçimi: (a) Gerçek pay + vesting; (b) pay opsiyonu (gelecekte pay alma hakkı); (c) sanal/fantom pay (nakdî, pay vermeyen). Türk hukukunda en yaygını sözleşmesel opsiyon + havuz; her biri farklı kurumsal ve vergisel sonuç doğurur.
3. Pay kaynağı: Opsiyon kullanılınca pay ya (i) mevcut ortaktan devir, ya (ii) sermaye artırımı (m.456), ya (iii) sınırlı ölçüde AŞ'nin kendi payını iktisabı (m.379-381: sermayenin %10'u sınırı, fon şartı) ile sağlanır.
4. Sulandırma: Havuzun turdan önce açılması mevcut ortakları, sonra açılması yeni yatırımcıyı da sulandırır; term sheet'te netleştir (cap table beceresiyle modelle).
5. Vergi: Çalışana piyasa değerinin altında pay/opsiyon menfaati kural olarak ücret (GVK ücret hükümleri); gelir vergisi/stopaj doğabilir. Teşvikli istisnaları (TGB/Ar-Ge kapsamı, 4691/5746) ayrıca teyit et.
6. İspat/şekil: Opsiyon planı + bireysel tahsis sözleşmesi yazılı; pay devri m.490 şekli; kurumsal kararlar.

## Çıktı modülleri
- ESOP planı ve bireysel opsiyon/tahsis sözleşmesi taslağı.
- Kurucu vesting + good/bad leaver geri alım mekaniği.
- Pay kaynağı ve vergi/sulandırma uyarı notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

