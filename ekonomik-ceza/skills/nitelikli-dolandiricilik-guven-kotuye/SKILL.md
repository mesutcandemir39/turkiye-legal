---
argument-hint: ''
description: Hileyle menfaat temini (TCK m.157-158) veya devralınan malvarlığının
  amacı dışında kullanılması (TCK m.155) iddiaları; bilişim, bankacılık, ticari faaliyet
  kapsamındaki nitelikli haller ve sözleşmeden
name: nitelikli-dolandiricilik-guven-kotuye
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Kaçakçılıkla Mücadele Kanunu
    numara: '5549'
    tur: kanun
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Nitelikli Dolandırıcılık ve Güveni Kötüye Kullanma

## Görev
TCK m.157-158 dolandırıcılık ve m.155 güveni kötüye kullanma suçlarını unsurlarına göre denetlemek; özellikle ticari/sözleşmesel ihtilafın gerçekten suç oluşturup oluşturmadığını ayırmak.

## Soğuk başlangıç (intake)
- Mağdur nasıl bir işleme/ödemeye yöneltildi; hile fiili somut olarak ne?
- İlişki sözleşmeye mi dayanıyor (alacak/borç ihtilafı mı, hile mi)?
- Nitelikli hal var mı? (banka/kredi kurumu, bilişim sistemi, kamu kurumu, tacir/şirket)
- Güveni kötüye kullanmada: mal kime, hangi amaçla tevdi edildi?

## Denetim şeması
1. **Dolandırıcılığın unsurları (TCK m.157)**: Hileli davranış + mağdurun aldatılması + bu sayede kendi/başkası lehine haksız menfaat + mağdur veya başkasının zararı. Hile, mağdurun denetim imkânını ortadan kaldıracak yoğunlukta olmalı; salt yalan/ödememe yetmez.
2. **Hukuki ihtilaf-suç ayrımı**: Sözleşmenin kurulduğu anda hile yoksa, sonradan ödememe kural olarak hukuki uyuşmazlıktır (alacak davası). Baştan var olan aldatma kastı aranır.
3. **Nitelikli haller (TCK m.158)**: Bilişim sistemlerinin/banka-kredi kurumlarının araç kılınması, ticari faaliyet kapsamında, serbest meslek, kamu kurumlarının zararına vb. Hangi bent uyuyorsa cezayı belirler.
4. **Güveni kötüye kullanma (TCK m.155)**: Zilyetliği devredilen malın, devir amacı dışında veya iade yükümlülüğüne aykırı kullanılması/temellük edilmesi. Hizmet/meslek/sanat/ticaret ilişkisiyle işlenmesi nitelikli haldir (m.155/2). Dolandırıcılıktan farkı: malın hileyle değil, güvene dayalı olarak elde edilmesidir.
5. **Manevi unsur**: Kast (TCK m.21); haksız menfaat/temellük kastı.
6. **Etkin pişmanlık ve içtima**: TCK m.168 malvarlığı suçlarında etkin pişmanlık (kısmi/tam iade ile indirim); zincirleme suç (m.43) ve diğer suçlarla içtima değerlendirilir.
7. **Ara sonuç**: Hile fiilinin yoğunluğu, suç-hukuki ihtilaf sınırı, doğru suç tipi ve nitelikli hal netleşir.

## Çıktı modülleri
- Hile fiili somutlaştırma notu
- Suç/hukuki ihtilaf sınır analizi
- Nitelikli hal bent eşleştirmesi
- m.155 vs m.157 ayrım değerlendirmesi
- Etkin pişmanlık/savunma stratejisi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

