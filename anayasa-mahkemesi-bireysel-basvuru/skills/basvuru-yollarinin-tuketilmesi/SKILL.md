---
argument-hint: ''
description: Bireysel başvurudan önce hangi olağan kanun yolunun etkili ve erişilebilir
  olduğu, istinaf/temyiz/itirazın tüketilip tüketilmediği, olağanüstü yolların gerekip
  gerekmediği sorulduğunda kullanılır.
name: basvuru-yollarinin-tuketilmesi
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
  - ad: Anayasa Mahkemesinin Kuruluşu ve Yargılama Usulü Hakkında Kanun
    numara: '6216'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Başvuru Yollarının Tüketilmesi

## Görev
İhlali giderebilecek etkili ve erişilebilir olağan kanun yollarının doğru tespiti ve usulüne uygun tüketildiğinin doğrulanması; erken veya geç başvuru riskini önlemek.

## Soğuk başlangıç (intake)
- Şikâyet edilen işlem adli yargıdan mı, idari yargıdan mı, yoksa idari bir işlemden mi kaynaklanıyor?
- Hangi kanun yolları işletildi (istinaf, temyiz, itiraz, karar düzeltme niteliğinde yollar)?
- İşletilen yolda esasa ilişkin şikâyetler açıkça dile getirildi mi?
- Hâlâ açık ve etkili bir kanun yolu kaldı mı?

## Denetim şeması
1. Kural — Anayasa m.148/3 ve 6216 m.45/2: ihlal iddiasına ilişkin olarak kanunda öngörülmüş idari ve yargısal başvuru yolları tüketilmeden bireysel başvuru yapılamaz.
2. Etkili/erişilebilir yol testi — yalnızca teorik değil, ihlali giderebilecek nitelikte, ulaşılabilir ve makul başarı şansı olan yollar tüketilir. Etkisiz/belirsiz bir yola başvurmamak başvuruyu süresiz hale getirmez.
3. Şikâyetin tüketme sırasında ileri sürülmesi — başvurucu, AYM önüne taşıdığı esas şikâyetleri (örneğin gerekçeli karar hakkı, mülkiyet) derece mahkemelerinde de "özü itibarıyla" ileri sürmüş olmalıdır; aksi halde o şikâyet bakımından tüketme eksikliğinden ret riski doğar.
4. Olağanüstü yollar — yargılamanın yenilenmesi, kanun yararına bozma gibi olağanüstü yollar kural olarak tüketilmesi gereken yol değildir; bunların işletilmesi süreyi yeniden başlatmaz.
5. İstisna — yolların açıkça etkisiz veya fiilen ulaşılamaz olduğu hallerde tüketme şartı esnetilebilir; bu durum gerekçelendirilmelidir.

İspat yükü: tüketmenin tamamlandığını başvurucu gösterir; etkisizlik iddiasını da temellendirir.

Ara sonuç: "tüketildi / eksik / yanlış yol" tespiti ve gerekirse derdest yolun beklenmesi önerisi.

## Çıktı modülleri
- Tüketilen ve kalan kanun yolları haritası.
- Etkili yol değerlendirmesi.
- Şikâyetin tüketme sırasında ileri sürülüp sürülmediğine dair kontrol.
- Erken/geç başvuru riski uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

