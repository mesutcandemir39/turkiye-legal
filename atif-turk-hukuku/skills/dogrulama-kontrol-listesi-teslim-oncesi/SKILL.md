---
argument-hint: ''
description: Bir layiha, mütalaa veya sözleşme teslim edilmeden hemen önce; tüm mevzuat,
  içtihat ve doktrin atıflarının doğruluğunu, güncelliğini ve işaretlenmemiş uydurma
  kalmadığını topluca denetlemek için kulla
name: dogrulama-kontrol-listesi-teslim-oncesi
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Teslim Öncesi Atıf Doğrulama Kontrol Listesi

## Görev
Bir hukuki metin teslim edilmeden önce, içindeki tüm atıfları sistematik bir kontrol listesinden geçirerek hatalı, güncelliğini yitirmiş veya doğrulanmamış hiçbir dayanağın kalmadığından emin olmak.

## Soğuk başlangıç (intake)
- Belge türü ve muhatabı kim (mahkeme, müvekkil, karşı taraf)?
- Metinde kaç mevzuat, kaç içtihat, kaç doktrin atfı var?
- Hangileri teyit edildi, hangileri hâlâ `[DOĞRULANMADI]`?
- Son değişiklikten sonra yeni eklenen atıf var mı?

## Denetim şeması
1. **Envanter** — Metindeki tüm atıflar listelenir: mevzuat (madde/fıkra/bent), içtihat (künye), doktrin (yazar-sayfa). Her biri için "teyit kaynağı" sütunu açılır.
2. **Mevzuat denetimi** — Her madde mevzuat.gov.tr'den açılır; numara, fıkra, bent ve yürürlük durumu (güncel/değişik/mülga) doğrulanır; zaman bakımından uygulama sorunu yoksa işaretlenir.
3. **İçtihat denetimi** — Her künye resmî bankadan teyit edilir; teyit edilemeyen künye `[DOĞRULANMADI]` ile bırakılır veya çıkarılır — **asla tahmin numarasıyla tamamlanmaz.** İBK/AYM bağlayıcılığı doğru sunulmuş mu kontrol edilir.
4. **Doktrin denetimi** — Yazar-eser-sayfa doğrulanır; doğrulanamayan atıf "kaynak teyit edilecek" notuyla bırakılır.
5. **Tutarlılık ve dürüstlük** — Aleyhe yerleşik içtihat gizlenmemiş; tek karar "yerleşik" diye sunulmamış; doktrin kural gibi gösterilmemiş; kesinlik derecesi dürüstçe yansıtılmış mı?
6. **İşaret taraması** — Metinde kalan tüm `[DOĞRULANMADI]` / `[doldurulacak]` işaretleri raporlanır; bilerek bırakılanlar dışında işaretsiz uydurma kalmadığı teyit edilir.

## Çıktı modülleri
- Atıf envanter tablosu (tür / dayanak / teyit durumu).
- Mevzuat ve içtihat doğrulama sonucu (geçti/düzeltildi/`[DOĞRULANMADI]`).
- Dürüstlük/tutarlılık denetimi notu.
- Kalan işaret listesi ve teslim hazırlık özeti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

