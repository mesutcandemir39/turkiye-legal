---
argument-hint: ''
description: Yöneticinin (veya yönetim kurulunun) seçilmesi, görev ve yetkilerinin
  sınırlanması, hesap vermemesi, azli ya da mahkemece atanması ve yönetici aleyhine
  açılacak hesap/sorumluluk davası gündeme geldiği
name: yonetici-secimi-gorev-sorumluluk
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
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yönetici/Denetçi — Atama, Görevler ve Sorumluluk

## Görev
Anagayrimenkul yöneticisinin (veya yönetim kurulunun) seçimini, görev ve yetkilerini, hesap verme yükümlülüğünü ve sorumluluğunu belirlemek; yöneticinin atanmasına/azline ilişkin uyuşmazlıkları ve hesap/sorumluluk davalarını kurmak.

## Soğuk başlangıç (intake)
- Mevcut yönetici nasıl belirlendi: kurul kararıyla mı, yönetim planıyla mı, yoksa mahkemece mi atandı?
- Uyuşmazlık atama/azil mi, hesap vermeme mi, yetkisini aşma mı, yoksa zarar/sorumluluk mu?
- Kat malikleri yönetici seçemiyor/anlaşamıyor mu (mahkemeden atama gereği)?
- İşletme defteri, makbuz ve hesap belgeleri ibraz edildi mi?

## Denetim şeması
1. **Yöneticinin belirlenmesi (KMK m.34)**: Kat malikleri, kendi aralarından veya dışarıdan bir yöneticiyi ya da yönetim kurulunu **kat maliklerinin sayı ve arsa payı çoğunluğuyla** atar. Sekiz ve daha fazla bağımsız bölümü olan anagayrimenkulde yönetici atanması **zorunludur** (m.34/2).
2. **Mahkemece atama (m.34/son)**: Yönetici atanamaz veya kurul anlaşamazsa, kat maliklerinden birinin istemiyle sulh hukuk mahkemesi yönetici atar; bu yönetici altı ay geçmeden ancak haklı sebeple değiştirilebilir.
3. **Görevler (m.35)**: Kurul kararlarını yerine getirme, anagayrimenkulü amacına uygun yönetme, ortak yerlerin bakım-onarım-temizliği, giderlerin toplanması ve avans tahsili, defter tutma, kat maliklerini temsil, sigorta yaptırma vb. Yönetici, yönetim planı ve kurul kararlarıyla bağlıdır.
4. **Hesap verme ve defter (m.36, m.39)**: Yönetici, **işletme defteri** tutar ve gelir-gider belgelerini saklar; her takvim yılı sonunda kesin hesap verir ve kurulca **ibra** edilir. İbra etmeyen malik hesap davası açabilir.
5. **Sorumluluk (m.38, m.40)**: Yönetici, kat maliklerine karşı **vekil gibi** sorumludur (TBK vekâlet hükümleri); kusuruyla verdiği zararı tazmin eder. Aynı zamanda haklı sebeple her zaman azledilebilir.
6. **Denetim (m.41)**: Kurul, yöneticinin yönetimini ve hesaplarını denetler; bu amaçla denetçi veya denetim kurulu seçebilir.
7. **Ara sonuç**: Atama/azil için kurul kararı veya mahkeme; hesap için ibra/hesap davası; zarar için vekilin sorumluluğu (m.38).

## Çıktı modülleri
- Yönetici atama/azil kurul kararı taslağı (nisap kontrolüyle).
- Mahkemeden yönetici atanması başvuru iskeleti (m.34/son).
- Hesap/ibra ve sorumluluk (m.38) davası dilekçe çatısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

