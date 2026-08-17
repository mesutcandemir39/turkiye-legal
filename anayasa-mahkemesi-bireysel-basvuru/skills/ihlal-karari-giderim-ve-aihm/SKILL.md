---
argument-hint: ''
description: İhlal kararının sonuçları, yeniden yargılama, tazminat, kararın icrası
  ile bireysel başvuru sonrası AİHM yolu ve süresi değerlendirilirken kullanılır.
name: ihlal-karari-giderim-ve-aihm
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


# İhlal Kararı, Giderim ve AİHM İlişkisi

## Görev
6216 m.50 çerçevesinde ihlal kararının doğurduğu sonuçları (yeniden yargılama, tazminat, icra) yönetmek ve gerekiyorsa AİHS m.34-35 yolunu planlamak.

## Soğuk başlangıç (intake)
- AYM ihlal mi, kabul edilemezlik/ret mi, ihlal yok kararı mı verdi?
- Karar yeniden yargılamaya mı gönderdi, yoksa tazminata mı hükmetti?
- İhlali ve sonuçlarını giderecek başka işlem gerekiyor mu?
- AİHM'e gitmek gerekirse süre işliyor mu?

## Denetim şeması
1. Karar türleri — m.49-50: kabul edilemezlik, ihlal yok veya ihlal kararı. İhlal kararında AYM, ihlalin ve sonuçlarının ortadan kaldırılması için yapılması gerekenlere hükmeder.
2. Yeniden yargılama — m.50/2: ihlal bir mahkeme kararından kaynaklanmışsa ve yeniden yargılamada hukuki yarar varsa, dosya ilgili mahkemeye gönderilir; mahkeme ihlali ve sonuçlarını gidermekle yükümlüdür. Yeniden yargılamada ihlal kararı bağlayıcıdır.
3. Tazminat — m.50/2: yeniden yargılamada yarar yoksa veya bu yol mümkün değilse AYM lehe maddi/manevi tazminata hükmedebilir ya da genel mahkemede dava açma yolunu gösterir.
4. İcra ve bağlayıcılık — AYM kararları yasama, yürütme, yargı organlarını ve herkesi bağlar (Anayasa m.153/6 ilkesi bireysel başvuru kararları yönünden de geçerlidir). Kararın gereği gecikmeksizin yerine getirilmelidir.
5. AİHM'e geçiş — AYM bireysel başvurusu etkili iç hukuk yolu sayılır ve tüketilmiş olur. AYM kararının sonucu yetersizse, AİHS m.35 uyarınca nihai iç karardan itibaren süre (güncel dört aylık süre) içinde AİHM'e başvurulabilir; süre ve koşullar resmî kaynaktan teyit edilir.

İspat yükü: giderimde hukuki yararı ve tazminat kalemlerini başvurucu temellendirir.

Ara sonuç: uygulanacak giderim yolu ve gerekiyorsa AİHM takvimi.

## Çıktı modülleri
- Karar türüne göre sonuç haritası.
- Yeniden yargılama / tazminat seçim notu.
- İcra takibi ve gecikme halinde yapılabilecekler.
- AİHM başvuru süresi ve koşul kontrolü [DOĞRULANMADI].



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

