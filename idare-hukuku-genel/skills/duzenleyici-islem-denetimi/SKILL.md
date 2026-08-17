---
argument-hint: ''
description: Yönetmelik, tebliğ, genelge gibi düzenleyici idari işlemlerin üst normlara
  (kanun, Anayasa) aykırılığını denetlemek ve iptalini değerlendirmek için kullanılır;
  bireysel işlemin dayanağı düzenleme tart
name: duzenleyici-islem-denetimi
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Düzenleyici İşlemler ve Norm Denetimi

## Görev
Düzenleyici idari işlemleri (yönetmelik, tebliğ, genelge) normlar hiyerarşisi içinde denetlemek; kanuna/Anayasaya aykırılığı tespit edip iptal yolunu ve uygulama işlemiyle birlikte dava imkânını kurmak.

## Soğuk başlangıç (intake)
1. Tartışılan düzenleme türü nedir (yönetmelik/tebliğ/genelge) ve dayanağı hangi kanun?
2. Düzenleme bir bireysel işleme dayanak mı oluşturuyor (uygulama işlemi var mı)?
3. Düzenleme süresinde mi, yoksa yayımı üzerinden 60 gün geçti mi?
4. Düzenleme usulüne uygun çıkarılmış mı (Danıştay incelemesi, yayım)?

## Denetim şeması
1. **Normlar hiyerarşisi.** Anayasa > kanun > CBK > yönetmelik > diğer düzenlemeler. Düzenleyici işlem, dayandığı kanunun çizdiği çerçeveyi aşamaz; kanunda olmayan yükümlülük getiremez (kanunilik, Anayasa m.123/m.124).
2. **Yetki ve usul.** Düzenlemeyi yapan makam yetkili mi; belirli yönetmelikler için Danıştay'ın incelemesi ve Resmî Gazete'de yayım şartı yerine gelmiş mi?
3. **Üst norma uygunluk.** İçerik kanuna/Anayasaya aykırı mı; eşitlik ve ölçülülük (Anayasa m.13) ölçütlerini karşılıyor mu? İdarenin düzenleme yetkisinin sınırı kamu yararı ve kanunîliktir.
4. **Dava yolu ve süre.** Düzenleyici işleme karşı doğrudan iptal (İYUK m.7) **veya** uygulama işlemiyle birlikte düzenlemeye karşı dava (m.7/4). İlk derecede Danıştay'da görülecek düzenlemeleri ayır (2575 sayılı K.).
5. **İhmal yoluyla uygulamama.** Hâkim, kanuna aykırı düzenlemeyi olaya uygulamayabilir; bunu uygulama işlemi davasında ileri sür.
6. **İspat.** Aykırılık hukuki bir değerlendirme olduğundan üst norm-alt norm karşılaştırmasını metinle göster.
7. **Ara sonuç.** Düzenlemenin hangi üst norma, hangi yönden aykırı olduğu + uygun dava stratejisi (doğrudan/uygulama ile birlikte).

## Çıktı modülleri
- Normlar hiyerarşisi karşılaştırma tablosu (üst norm vs. düzenleme).
- Aykırılık gerekçeleri listesi.
- Dava yolu seçimi (doğrudan / uygulama işlemiyle birlikte).
- Danıştay görevi/yer yetkisi notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

