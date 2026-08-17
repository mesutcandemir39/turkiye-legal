---
argument-hint: ''
description: Lafzen haklı görünen bir talep ya da savunma somut olayda hakkaniyete
  aykırı düştüğünde; çelişkili davranış, hakkın geç kullanılması veya menfaat dengesizliği
  iddiası gündeme geldiğinde TMK m.2 süzgec
name: durustluk-kurali-ve-hakkin-kotuye-kullanilmasi
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
  - ad: Türk Medeni Kanunu
    madde: '1'
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dürüstlük Kuralı ve Hakkın Kötüye Kullanılması

## Görev
Bir hakkın kullanımının ya da bir yükümlülüğün TMK m.2 dürüstlük kuralıyla bağdaşıp bağdaşmadığını denetlemek ve hakkın açıkça kötüye kullanılmasının hukuk düzenince korunmayacağı sonucunu gerekçelendirmek.

## Soğuk başlangıç (intake)
- Hangi hak/yetki kullanılıyor ve karşı taraf hangi davranışın dürüstlüğe aykırı olduğunu söylüyor?
- Talep sahibi daha önce aksi yönde davranıp güven yaratmış mı (venire contra factum proprium)?
- Hak çok geç mi kullanılıyor; karşı tarafta haklı bir güven oluştu mu?
- Talebin lafzî dayanağı (sözleşme maddesi/kanun hükmü) nedir?

## Denetim şeması
1. **Önce kural, sonra korrektif** — TMK m.2 bağımsız bir talep kaynağı değil, mevcut hak/borcun kullanımını sınırlayan tamamlayıcı süzgeçtir. Önce hakkın varlığı ve kapsamı kuralla tespit edilir.
2. **Dürüstlük ölçütü** — Aynı durumdaki dürüst ve makul kişinin davranışı esas alınır; sözleşmenin boşlukları dürüstlük kuralıyla doldurulur, yan yükümlülükler (sadakat, özen, koruma, bilgilendirme) buradan doğar.
3. **Kötüye kullanma tipleri** — (a) Çelişkili davranış (*venire contra factum proprium*); (b) hakkın çok geç kullanılması ve yaratılan güvene aykırılık; (c) hakkı kullanmakta meşru menfaatin yokluğu, salt zarar verme; (d) menfaatler arası aşırı oransızlık; (e) kendi hukuka aykırılığından yarar sağlama.
4. **İspat** — TMK m.6 uyarınca kötüye kullanmayı iddia eden ispatla yükümlüdür; ancak hâkim açık kötüye kullanmayı re'sen gözetir (kamu düzeni boyutu).
5. **Sonuç** — Açıkça kötüye kullanılan hak korunmaz: talep reddedilir, def'i etkisizleşir veya hak sınırlanır; hakkın tümden düşmesi istisnadır, ölçülülük gözetilir.
6. **İyiniyetle ilişki** — TMK m.2 (dürüstlük, davranış kuralı) ile TMK m.3 (iyiniyet, bir hakkın kazanılmasında bilgisizliğin korunması) karıştırılmaz.

## Çıktı modülleri
- Hakkın tespiti + kötüye kullanma tipi eşleştirmesi.
- Güven/çelişki kronolojisi.
- İspat yükü dağılımı.
- Sonuç önerisi (ret/sınırlama) + ilkesel içtihat `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

