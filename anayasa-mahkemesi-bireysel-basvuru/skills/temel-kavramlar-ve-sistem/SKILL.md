---
argument-hint: ''
description: Bireysel başvurunun ne olduğu, ikincil (sübsidiyer) niteliği, norm denetiminden
  farkı, kapsam ve genel mimari sorulduğunda; başvurunun hangi yola oturduğunu konumlandırmak
  için kullanılır.
name: temel-kavramlar-ve-sistem
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


# Temel Kavramlar ve Sistematik

## Görev
Olayın bireysel başvuru yoluna uygun olup olmadığını, başvurunun ikincil niteliğini ve diğer denetim yollarından (norm denetimi, AİHM, idari/adli yargı) farkını netleştirmek; başvurucuya doğru yolu göstermek.

## Soğuk başlangıç (intake)
- Şikâyet edilen nedir: bir mahkeme kararı mı, idari işlem mi, kanun hükmü mü, yoksa bir ihmal mi?
- Olağan kanun yolları (istinaf, temyiz, itiraz) tüketildi mi, yoksa hâlâ açık mı?
- Şikâyet, hakkın özüne mi (anayasal) yoksa delil/yorum hatasına mı (kanun yolu) ilişkin?
- Aynı konu AİHM veya başka bir uluslararası mercide derdest mi?

## Denetim şeması
1. Yol tespiti — Anayasa m.148/3 ve 6216 m.45: bireysel başvuru, kamu gücü işlemiyle Anayasa'da ve AİHS'in Türkiye'nin taraf olduğu hükümlerinde ORTAK güvence altına alınan haklara yöneliktir. Kanunun soyut iptali isteniyorsa yol norm denetimidir (m.150 vd.), bireysel başvuru değildir.
2. İkincillik — m.148/3 ve m.45/2: başvuru, ihlali giderebilecek olağan kanun yolları tüketilmeden yapılamaz. AYM bir "süper temyiz" değildir; maddi vakıa ve delil değerlendirmesi kural olarak derece mahkemelerine aittir (kanun yolu şikâyeti yasağı). Ara sonuç: salt yorum/delil itirazı ise başvuru "açıkça dayanaktan yoksun" sayılır (m.48/2).
3. Kapsam süzgeci — yalnızca Anayasa ve AİHS kesişimindeki haklar. Yalnızca Anayasa'da olup AİHS'te karşılığı bulunmayan ya da yalnızca AİHS'te olup Türkiye'nin çekince koyduğu güvenceler kapsam dışı kalabilir.
4. Diğer yollarla ilişki — AYM'ye başvuru iç hukuk yolu sayılır; tüketilmeden AİHM'e gidilemez. AYM kararından sonra AİHS m.34-35 yolu açıktır.
5. Mağdur sıfatı — m.46: ihlalden güncel, kişisel ve doğrudan etkilenme aranır; potansiyel/soyut etki yetmez.

İspat yükü: başvurucu, hangi hakkın hangi kamu gücü işlemiyle ihlal edildiğini ve mağdur sıfatını gösterir.

## Çıktı modülleri
- Yol uygunluk notu (bireysel başvuru mu / norm denetimi mi / kanun yolu mu).
- Kapsam ve ikincillik değerlendirmesi.
- İhlal iddiasının hangi hakka oturduğuna dair ön nitelendirme.
- Sonraki adım önerisi (tüketme, süre, hak analizi becerisine yönlendirme).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

