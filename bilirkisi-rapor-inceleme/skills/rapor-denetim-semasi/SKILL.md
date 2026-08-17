---
argument-hint: ''
description: Eldeki bilirkişi raporunu uçtan uca eleştirel biçimde denetlemek ve hangi
  usulî hamlenin (ek rapor, yeni heyet, esasa itiraz) seçileceğine karar vermek istendiğinde
  kullanılır.
name: rapor-denetim-semasi
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
  - ad: Sağlık Turizmi Kanunu
    numara: '6754'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Rapor Denetim Şeması ve İtiraz Stratejisi

## Görev
Raporu dört eksende (usul, metodoloji, hesap, çelişki) sistematik denetleyip her bulguyu görevlendirme sorusuna ve dosya deliline çıpalamak; ardından bulguların ağırlığına göre doğru usulî yolu (HMK m.281) seçmek.

## Soğuk başlangıç (intake)
- Görevlendirme kararındaki sorular ile raporun yanıtladığı sorular örtüşüyor mu?
- Hangi husus(lar) sizin aleyhinize ve neden hatalı olduğunu düşünüyorsunuz?
- Dosyada raporla çelişen başka delil/rapor var mı?
- Hedefiniz raporu tümden çürütmek mi, yoksa belirli kalemleri düzeltmek mi?

## Denetim şeması
1. **Usul ekseni:** Bilirkişinin yetkisi, yemini, uzmanlık alanı sınırı (6754 s.K. m.3), görevlendirme kapsamına uygunluk (HMK m.273). Kapsam aşımı veya eksik yanıt belirlenir.
2. **Metodoloji ekseni:** Kullanılan yöntem açıkça belirtilmiş mi; kabuller ve varsayımlar dosya verisiyle örtüşüyor mu; veri kaynağı gösterilmiş mi (HMK m.279 gerekçe zorunluluğu)? Gerekçesiz sonuç denetlenebilir değildir.
3. **Hesap ekseni:** Aritmetik doğruluk, birim/tarih tutarlılığı, faiz başlangıcı ve türü, zamanaşımı/ıslah kesişimi. (Detaylı kontrol için hesap denetimi becerisi.)
4. **Çelişki ekseni:** Rapor içi çelişki, dosyadaki diğer delillerle çelişki, sorulara verilmeyen yanıtlar.
5. **Strateji seçimi (HMK m.281):** Tamamlanabilir eksik → **ek rapor**; yöntem hatası veya tarafsızlık kusuru → **yeni bilirkişi/heyet**; hukuki nitelendirme aşımı veya caizsizlik → **doğrudan esasa itiraz** (rapor hâkimi bağlamaz, HMK m.282). **Ara sonuç:** her bulgu için "hangi yol, hangi gerekçe, hangi dayanak" üçlüsü doldurulur.

## Çıktı modülleri
- Eksen-bulgu-dayanak (görevlendirme sorusu + dosya sayfası) matrisi.
- Bulgu başına önerilen usulî yol ve gerekçesi.
- İki hafta içinde sunulacak itiraz dilekçesinin omurgası.
- Talep sonucu önerisi (ek rapor / yeni heyet / rapora itibar edilmemesi).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

