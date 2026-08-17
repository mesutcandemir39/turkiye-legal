---
argument-hint: ''
description: Borç ilişkisinin kaynağını ve yapısını çözmek; sözleşme mi haksız fiil
  mi sebepsiz zenginleşme mi olduğunu ve hangi genel hükmün uygulanacağını saptamak
  gerektiğinde kullanılır.
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Borç İlişkisinin Sistematiği

## Görev
Önündeki olayda borç ilişkisinin kaynağını, taraflarını, edimin türünü ve uygulanacak genel hüküm bloğunu doğru saptamak; sonraki tüm analizin altyapısını kurmak.

## Soğuk başlangıç (intake)
- Talep neye dayanıyor: bir sözleşme mi, bir zarar mı, yoksa haksız bir malvarlığı kayması mı?
- Taraflar kim, aralarında önceden hukuki bir ilişki var mı?
- Edim ne: verme, yapma, yapmama? Para borcu mu, parça borcu mu, cins borcu mu?
- Olay ne zaman gerçekleşti (zamanaşımı ve uygulanacak kanun için)?

## Denetim şeması
1. Kaynak tespiti: TBK m.1 vd. (sözleşme), m.49 vd. (haksız fiil), m.77 vd. (sebepsiz zenginleşme). Birden çok kaynak yarışabilir; talep yarışması hâlinde lehe olan değerlendirilir.
2. Sözleşmesel ise: Borç sözleşmeden mi yoksa kanundan mı doğuyor? İsimli sözleşme varsa özel hükümlere (TBK İkinci Kısım) köprü kur; isimsiz/karma ise genel hükümler ve kıyas.
3. Edimin niteliği: Para borcu mu? (faiz, m.88, 120 ve 3095 s.K. gündeme gelir). Parça borcunda imkânsızlık riski (m.136), cins borcunda kural olarak imkânsızlık savunulamaz.
4. Borç-sorumluluk ayrımı: Borç (Schuld) var ama dava/icra edilemiyor mu (eksik borç, örn. zamanaşımına uğramış borç, kumar borcu)? TBK m.604-605.
5. İspat yükü: Hakkını dayandıran iddiasını ispatla yükümlüdür (TMK m.6). Borcun doğduğunu alacaklı, sona erdiğini/ifa edildiğini borçlu ispatlar.
6. Ara sonuç: Uygulanacak norm bloğu ve takip edilecek alt-beceri (geçerlilik, ifa, temerrüt) belirlenir.

## Çıktı modülleri
- Borç ilişkisi künyesi (kaynak, taraf, edim, muacceliyet).
- Uygulanacak madde haritası ve yönlendirilecek alt-beceri.
- İlk bakışta zamanaşımı/hak düşürücü süre uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

