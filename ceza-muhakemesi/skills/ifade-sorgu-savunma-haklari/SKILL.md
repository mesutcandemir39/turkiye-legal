---
argument-hint: ''
description: Şüpheli/sanık ifadesi ve sorgusunda susma hakkı, müdafi yardımı, zorunlu
  müdafilik ve hukuka aykırı ifade yasağı konularında denetim ve itiraz hazırlanırken
  kullanılır.
name: ifade-sorgu-savunma-haklari
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


# İfade, Sorgu ve Savunma Hakları

## Görev
İfade ve sorgunun savunma hakları yönünden hukuka uygunluğunu denetlemek; ihlal halinde ifadenin delil değerini tartışmak ve etkili savunma stratejisi kurmak.

## Soğuk başlangıç (intake)
- İfade kim tarafından, hangi sıfatla (şüpheli/tanık) alındı?
- Haklar hatırlatıldı mı (susma, müdafi, yakına haber)?
- Müdafi hazır mıydı; zorunlu müdafilik gereken bir hal var mıydı?
- İfade sırasında baskı, vaat, yorma iddiası var mı?
- Sanık daha önceki ifadesini değiştirmek istiyor mu?

## Denetim şeması
1. **Hak bildirimi.** İfade/sorgudan önce yüklenen suç, susma hakkı, müdafiden yararlanma, somut delil isteme ve yakına haber verme hakları bildirilir (CMK m.147/1). Bildirim yapılmadan alınan beyan sakattır.
2. **Müdafi yardımı.** Şüpheli/sanık her zaman bir müdafiin yardımından yararlanabilir (m.149); ifade/sorguda müdafi hazır bulunabilir.
3. **Zorunlu müdafi.** Müdafi yoksa istem aranmaksızın görevlendirme: 18 yaşından küçük, sağır-dilsiz, kendini savunamayacak durumda olan ya da alt sınırı 5 yıldan fazla hapsi gerektiren suçtan yargılananlar için (m.150). Müdafi olmadan alınan ifade hükme esas alınamaz (m.148/4).
4. **Yasak yöntemler.** Kötü muamele, işkence, yorma, ilaç verme, hile, kanuna aykırı vaat ile elde edilen beyanlar rıza olsa da delil olamaz (m.148).
5. **Tekrar ve değiştirme.** Kollukça alınan ve müdafi olmadan alınmış ifade, hâkim/mahkeme önünde doğrulanmadıkça hükme esas alınamaz (m.148/4 ile bağlantılı uygulama).
6. **Ara sonuç.** Hak ihlali tespit edilirse ifadenin dışlanması ve buna dayanan delillerin tartışılması; aksi halde savunma beyanının içeriğine odaklanma.

## Çıktı modülleri
- İfade tutanağı hak-bildirimi denetim listesi.
- İfadenin/sorgunun hükümden dışlanması talebi gerekçesi.
- Zorunlu müdafi gerektiren hallerin kontrol tablosu.
- Sanık savunması taslağı ve çelişki/değişiklik açıklaması.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

