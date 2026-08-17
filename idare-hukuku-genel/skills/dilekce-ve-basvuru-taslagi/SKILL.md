---
argument-hint: ''
description: İdari yargıda iptal/tam yargı dava dilekçesi ile İYUK m.11/m.13 idari
  başvuru ve dilekçe hakkı başvurularının taslağını üretmek için kullanılır; somut
  bir metin istendiğinde başvurulur.
name: dilekce-ve-basvuru-taslagi
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


# Dava Dilekçesi ve İdari Başvuru Taslağı

## Görev
İYUK formatına uygun dava dilekçesi (iptal/tam yargı) ve idari başvuru (m.11/m.13, dilekçe hakkı) metinlerini, yer tutucu disipliniyle üretmek. Dilekçe, önceki becerilerin çıktısını birleştirir.

## Soğuk başlangıç (intake)
1. Hangi metin gerekiyor (iptal dilekçesi, tam yargı dilekçesi, m.11 başvurusu, m.13 başvurusu)?
2. Taraflar, dava konusu işlem ve tebliğ tarihi belli mi?
3. İptal sebepleri ve/veya tazminat kalemleri hazır mı?
4. Yürütmenin durdurulması talep edilecek mi?

## Denetim şeması
1. **Zorunlu unsurlar.** İYUK m.3: davacı/davalı idare, dava konusu işlem ve tebliğ tarihi, olayların özeti, hukuki sebepler, talep sonucu, deliller. Eksik unsur m.15/1-d uyarınca düzeltme/ret sebebidir.
2. **Yapı.** (a) Davalı idare ve dava konusu, (b) tebliğ/öğrenme tarihi ve süre tutar açıklaması, (c) olaylar (kronolojik, tarafsız), (d) hukuki açıklamalar (beş unsur denetiminden gelen sebepler, madde atıflarıyla), (e) yürütmenin durdurulması talebi ve gerekçesi (m.27), (f) deliller, (g) talep sonucu (net ve sayılı).
3. **Talep sonucu disiplini.** İptal davasında "işlemin iptali"; tam yargıda miktar belirterek "… TL maddi/manevi tazminatın … tarihinden işleyecek faiziyle tahsili". Belirsiz alacakta usulü gözet.
4. **İdari başvuru metni.** m.11: işlemin kaldırılması/değiştirilmesi talebi ve sürenin durduğuna dikkat çekme. m.13: eylem ve zararın somutlaştırılması, tazminat talebi.
5. **Yer tutucu disiplini.** Eksik bilgi için `[doldurulacak: …]` kullan; uydurma tarih/sayı/karar künyesi yazma. İçtihat atfını `[DOĞRULANMADI]` ile işaretle.
6. **Ara sonuç.** Eksiksiz, atıfları doğru, talep sonucu net taslak metin.

## Çıktı modülleri
- İptal/tam yargı dava dilekçesi taslağı (İYUK m.3 unsurlarıyla).
- m.11/m.13 idari başvuru dilekçesi taslağı.
- Yürütmenin durdurulması talep paragrafı.
- Doldurulacak alanlar ve eklenecek belgeler listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

