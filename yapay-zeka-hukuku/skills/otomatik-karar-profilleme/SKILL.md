---
argument-hint: ''
description: Bireyi etkileyen kredi skoru, işe alım eleme, sigorta fiyatlama, içerik
  moderasyonu gibi münhasıran otomatik kararlar ve profilleme söz konusu olduğunda
  KVKK m.11/1-g itiraz hakkı, hukuki dayanak ve i
name: otomatik-karar-profilleme
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Otomatik Karar ve Profilleme Denetimi

## Görev
Bir yapay zekâ sisteminin kişi hakkında ürettiği kararın "münhasıran otomatik" olup olmadığını, hukuki dayanağını ve ilgili kişinin KVKK m.11/1-g kapsamındaki itiraz hakkını denetleyerek uyum ve savunma stratejisi çıkarmak.

## Soğuk başlangıç (intake)
1. Karar neyi etkiliyor: kredi, sigorta primi, işe alım, abonelik, içerik kaldırma, fiyatlandırma?
2. Sürece insan müdahalesi var mı; varsa anlamlı/etkin bir gözden geçirme mi yoksa biçimsel onay mı?
3. Hangi veriler işleniyor; özel nitelikli (sağlık, biyometrik, etnik) veri var mı?
4. İlgili kişiye otomatik karar uygulandığı aydınlatma metninde belirtilmiş mi?

## Denetim şeması
1. **Münhasıran otomatik mi**: KVKK m.11/1-g, kişinin "münhasıran otomatik sistemlerle analiz edilmesi suretiyle aleyhine bir sonucun ortaya çıkmasına itiraz" hakkını tanır. Anlamlı insan denetimi varsa "münhasıran otomatik" değildir; biçimsel onay yeterli sayılmaz. Ara sonuç: itiraz hakkı doğar mı.
2. **İşleme şartı**: m.5 — açık rıza ya da sözleşmenin kurulması/ifası, hukuki yükümlülük, meşru menfaat gibi bir şart; özel nitelikli veride m.6 daha dar şartlar. Dayanak yoksa işlemenin kendisi hukuka aykırı.
3. **İlkeler**: m.4 — amaçla bağlılık, ölçülülük, doğruluk. Modelin yanlı/güncel olmayan veriyle aleyhe sonuç üretmesi doğruluk ilkesine aykırılık delili olabilir.
4. **Aydınlatma**: m.10 — otomatik karar/profilleme yapıldığı, mantığı ve sonuçları konusunda bilgilendirme. Eksikse aydınlatma ihlali.
5. **Sonuç ve yol**: İhlalde m.13 ilgili kişi başvurusu, ardından m.14 Kurula şikâyet; aleyhe sonuçta tazminat için TBK/haksız fiil değerlendirilir. AB'ye dokunuyorsa GDPR m.22 (kural olarak yasak) karşılaştırmalı kontrol.

İlke kararı ve rehberler için kvkk.gov.tr; doğrulanmamış Kurul/yargı künyesini [DOĞRULANMADI] işaretle.

## Çıktı modülleri
- Münhasıran otomatik karar testi sonucu (evet/hayır + gerekçe).
- İşleme şartı ve aydınlatma uyum tablosu.
- İtiraz/başvuru dilekçesi veya savunma stratejisi taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

