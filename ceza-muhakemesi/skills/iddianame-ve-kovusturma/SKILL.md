---
argument-hint: ''
description: İddianamenin unsurları ve iadesi, kovuşturmanın başlaması, duruşma düzeni
  ve sanık haklarının değerlendirilmesi gerektiğinde kullanılır.
name: iddianame-ve-kovusturma
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
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İddianame Denetimi ve Kovuşturma Evresi

## Görev
İddianamenin yasal unsurlarını ve iade sebeplerini denetlemek; kovuşturma evresinde duruşma düzenini, sanık haklarını ve usulü takip etmek.

## Soğuk başlangıç (intake)
- İddianame kabul edildi mi, tensip tutanağı var mı?
- Yüklenen suç ve sevk maddeleri net mi; olay anlatımı yeterli mi?
- İddianamede gösterilen deliller ile yüklenen suç örtüşüyor mu?
- Duruşma günü belli mi; sanık tutuklu mu?
- Esasa girilmeden ileri sürülecek ilk itirazlar var mı (görev, yetki)?

## Denetim şeması
1. **İddianame unsurları.** İddianamede şüphelinin kimliği, yüklenen suç ve uygulanacak kanun maddeleri, olayın ve delillerin gösterilmesi, suçun işlendiği yer-zaman gibi zorunlu unsurlar bulunmalıdır (CMK m.170). Olayla deliller arasında bağ kurulmalıdır.
2. **İade.** Mahkeme, m.170'e aykırılık, eksik soruşturma veya ön ödeme/uzlaştırma yoluna gidilmemesi hallerinde iddianameyi 15 gün içinde iade eder (m.174); süresinde iade edilmezse kabul edilmiş sayılır.
3. **Kovuşturmanın başlaması.** İddianamenin kabulüyle kovuşturma başlar ve sanık sıfatı doğar (m.175). Tensiple duruşma hazırlığı yapılır.
4. **Duruşma düzeni.** Yargılama kural olarak aleni (m.182), sözlü ve doğrudandır. Sanığın hazır bulunma (m.193), son söz hakkı (m.216/3) ve çapraz sorgu güvenceleri uygulanır.
5. **İlk itirazlar.** Görevsizlik (m.5), yetkisizlik (m.18, ilk oturumda), davaya katılma talepleri esasa girilmeden değerlendirilir.
6. **Ara sonuç.** İddianame sakatsa iade talebi; geçerliyse savunma planı, delil ikamesi ve duruşma stratejisi kurulur.

## Çıktı modülleri
- İddianame unsur denetim tablosu (m.170 maddeleriyle eşlenmiş).
- İddianamenin iadesi/itiraz gerekçesi taslağı.
- Sanık savunma planı ve delil listesi.
- Duruşma hazırlık notu (itirazlar, tanık, talepler).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

