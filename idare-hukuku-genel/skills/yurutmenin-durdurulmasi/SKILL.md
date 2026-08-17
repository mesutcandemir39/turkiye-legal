---
argument-hint: ''
description: İdari işlemin uygulanması ağır zarar doğuracaksa dava süresince işlemin
  durdurulması için İYUK m.27 koşullarını değerlendirmek ve güçlü bir YD talebi kurmak
  amacıyla kullanılır.
name: yurutmenin-durdurulmasi
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


# Yürütmenin Durdurulması Talebi

## Görev
Dava sonuçlanana kadar işlemin uygulanmasını durdurmak için İYUK m.27 koşullarını (telafisi güç zarar + açık hukuka aykırılık) somut ve ikna edici biçimde gerekçelendirmek.

## Soğuk başlangıç (intake)
1. İşlem uygulanırsa ortaya çıkacak somut zarar nedir; sonradan giderilebilir mi?
2. İşlemin açık hukuka aykırılığını gösteren en güçlü dayanak hangisi?
3. İşlem icra edilmeye başlandı mı; zaman baskısı var mı?
4. Teminat istenmesi muhtemel mi (m.27/6 istisnaları)?

## Denetim şeması
1. **Çifte koşul.** İYUK m.27/2: (a) işlemin uygulanması halinde **telafisi güç veya imkânsız zararlar** doğması **ve** (b) işlemin **açıkça hukuka aykırı** olması. İkisi birlikte aranır; yalnız biri yetmez.
2. **Telafisi güç zarar.** Parayla tam giderilemeyecek, geri dönülemez sonuçlar (yıkım, ruhsat iptali, görevden uzaklaştırma, sınır dışı vb.). Zararı soyut değil somut/ölçülebilir anlat.
3. **Açık hukuka aykırılık.** Beş unsur denetiminden çıkan en kuvvetli, ilk bakışta görülebilir aykırılığı öne çıkar; tartışmalı yorumlar yerine net dayanaklar.
4. **Gerekçe zorunluluğu.** YD kararı gerekçeli olmak zorundadır (m.27); talebini de aynı titizlikle gerekçelendir.
5. **Teminat.** Kural olarak teminat karşılığında verilir; ancak idareden ve adli yardımdan yararlananlardan teminat alınmayabilir (m.27/6). İstisnaları değerlendir.
6. **İtiraz yolu.** YD talebinin reddi/kabulüne karşı bir defaya mahsus itiraz (m.27/7) ve süresi.
7. **Ara sonuç.** Koşullar karşılanıyorsa güçlü YD gerekçesi; karşılanmıyorsa zararı/aykırılığı güçlendirecek ek delil stratejisi.

## Çıktı modülleri
- m.27 çifte koşul değerlendirme tablosu.
- Telafisi güç zarar anlatımı (somut örneklerle).
- Açık hukuka aykırılık özeti.
- Teminat ve itiraz yolu notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

