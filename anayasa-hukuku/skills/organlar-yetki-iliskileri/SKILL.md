---
argument-hint: ''
description: Yasama, yürütme ve yargı arasındaki yetki ve denetim ilişkilerinin, CB
  kararnamesi-kanun ayrımının ve kuvvetler ayrılığına dair sorunların anayasaya uygunluğunu
  değerlendirmek; organlar arası yetki ça
name: organlar-yetki-iliskileri
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
  version: 0.1.0
user-invocable: true
---


# Devlet Organları ve Yetki İlişkileri

## Görev
2017 değişiklikleri sonrası yürürlükteki Cumhurbaşkanlığı hükümet sistemi çerçevesinde yasama (m.75 vd.), yürütme (m.104 vd.) ve yargı (m.138 vd.) arasındaki yetki dağılımını ve denetim ilişkilerini çözümlemek; özellikle kanun-CB kararnamesi yetki sınırını netleştirmek.

## Soğuk başlangıç (intake)
1. Tartışılan tasarruf hangi organdan çıkıyor (TBMM kanunu, CB kararnamesi, CB kararı, yönetmelik)?
2. Sorun organlar arası yetki çatışması mı, yoksa bir hak ihlaliyle mi bağlantılı?
3. Düzenlenen konu münhasıran kanunla mı düzenlenmesi gereken bir alan?
4. Konuda hem kanun hem CB kararnamesi düzenlemesi var mı (çatışma analizi gerekli mi)?

## Denetim şeması
1. **Organ ve tasarruf türünü belirle.** Yasama: kanun (m.87-89). Yürütme: CB kararnamesi (m.104/17), yönetmelik (m.124). Yargı: bağımsız ve tarafsız mahkemeler (m.138).
2. **CB kararnamesinin yetki sınırları (m.104/17).** Kararname (a) yürütme yetkisine ilişkin konularda çıkarılabilir; (b) temel haklar, kişi hakları ve siyasi hak/ödevler kural olarak düzenlenemez; (c) Anayasada münhasıran kanunla düzenlenmesi öngörülen konularda çıkarılamaz; (d) kanunda açıkça düzenlenen konularda çıkarılamaz. Ara sonuç: bu sınırlardan birinin aşılması kararnameyi sakatlar.
3. **Kanun-kararname çatışması.** Aynı konuda kararname ile kanun farklı hüküm içeriyorsa **kanun** esas alınır (m.104/17). Sonradan çıkan kanun, kararname hükmünü hükümsüz kılar.
4. **Münhasıran kanun alanı.** Suç-ceza (m.38), vergi (m.73), temel hak sınırlaması (m.13) gibi alanlar kanun konusudur; idari düzenleme bunları ikame edemez.
5. **Yargı bağımsızlığı.** Yargıya talimat, mahkeme kararlarına uymama (m.138/son) ve doğal hâkim ilkesi (m.37) denetlenir.
6. **Norm denetimi köprüsü.** Yetki aşımı iddiası AYM norm denetimine taşınır (m.148, m.150-152).
AYM yetki/kararname içtihadına ilke düzeyinde atıf yapın; künyeyi `[DOĞRULANMADI]` işaretleyin (kararlarbilgibankasi.anayasa.gov.tr).

## Çıktı modülleri
- Tasarrufun organ-yetki haritası ve dayanak maddesi tespiti.
- CB kararnamesi yetki sınırları kontrol listesi ve çatışma çözümü.
- Norm denetimine taşınacak yetki/şekil aykırılığı gerekçesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

