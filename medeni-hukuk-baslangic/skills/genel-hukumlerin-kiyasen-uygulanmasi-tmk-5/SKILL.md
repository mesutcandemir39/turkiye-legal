---
argument-hint: ''
description: Bir özel hukuk ilişkisinde doğrudan hüküm bulunmadığında, TMK ve TBK
  genel hükümlerinin bu ilişkiye kıyasen uygulanıp uygulanamayacağı tartışıldığında
  TMK m.5 köprüsünü kurmak için kullanılır.
name: genel-hukumlerin-kiyasen-uygulanmasi-tmk-5
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Genel Hükümlerin Kıyasen Uygulanması (TMK m.5)

## Görev
TMK ve TBK'nın genel nitelikli hükümlerinin, başka bir özel hukuk ilişkisine (aile, miras, eşya, ticaret, fikrî haklar) "uygun düştüğü ölçüde" kıyasen uygulanıp uygulanamayacağını belirlemek.

## Soğuk başlangıç (intake)
- Eldeki ilişkiyi düzenleyen özel hüküm gerçekten yok mu (önce o aranır)?
- Taşınmak istenen hüküm "genel nitelikli" mi, yoksa kendi alanına özgü istisnai bir hüküm mü?
- Hükmün amacı (ratio) eldeki ilişkiye uygun düşüyor mu, yoksa niteliği engelliyor mu?
- İlişki TBK genel hükümlerine zaten tabi mi (ör. borç ilişkisiyse doğrudan uygulanır, kıyasa gerek yok)?

## Denetim şeması
1. **Köprü hükmü** — TMK m.5: TMK ve TBK'nın genel nitelikli hükümleri, *uygun düştükleri ölçüde* tüm özel hukuk ilişkilerine uygulanır. Bu, doğrudan uygulama değil, kıyasen (analojik) uygulamadır.
2. **Önce boşluk kontrolü** — İlişkiyi düzenleyen özel norm varsa m.5 devreye girmez. Boşluk gerçek mi (kural yok) yoksa bilinçli susma mı (a contrario) ayrılır.
3. **"Genel nitelik" testi** — Taşınacak hüküm, yalnızca borç ilişkilerine özgü teknik bir kural değil, tüm özel hukuka yayılabilecek genel bir ilke içermeli (ör. temsil, ehliyet, irade sakatlığı, ifa, temerrüt ilkeleri). İstisnai/özel amaçlı hükümler kural olarak taşınmaz.
4. **"Uygun düşme" testi** — Hükmün amacı eldeki ilişkinin niteliğiyle bağdaşmalı; aile/miras gibi kişiye sıkı bağlı alanlarda borçlar hukuku mantığı her zaman taşınmaz (ör. irade sakatlığı hükümleri evlenme/vasiyette kendi özel rejimine tabidir).
5. **Sonuç** — Şartlar sağlanırsa genel hükmün sonucu, gerekli uyarlamayla eldeki ilişkiye uygulanır; sağlanmazsa TMK m.1 sırasına (örf-âdet, hâkimin hukuk yaratması) geçilir.

## Çıktı modülleri
- Boşluk tespiti (özel norm var/yok).
- Taşınacak hükmün "genel nitelik" ve "uygun düşme" analizi.
- Kıyasen uygulama sonucu + gerekli uyarlama.
- Uygulanamazsa m.1 yönlendirmesi + ilkesel içtihat `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

