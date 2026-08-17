---
argument-hint: ''
description: Tıbbi müdahaleden doğan tazminat talebinin esasını madde madde denetlemek
  için kullanılır; kusur, illiyet ve zarar unsurlarını sözleşme ve haksız fiil rejimine
  göre adım adım çözer.
name: hekim-sorumlulugu-denetim-semasi
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
  - ad: Banka Muhasebe Sistemi Hakkında Kanun
    numara: '1219'
    tur: kanun
  - ad: Gayrimenkul Ek Vergisi Hakkında Kanun
    numara: '3359'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Hekimin Hukuki Sorumluluğu Denetim Şeması

## Görev
Tıbbi müdahaleden doğan maddi/manevi tazminat talebinin hukuki dayanağını ve başarı şansını sistematik biçimde değerlendirmek.

## Soğuk başlangıç (intake)
1. Hangi tıbbi işlem ve hangi tıbbi sonuç (zarar) söz konusu?
2. İddia edilen kusur teşhiste mi, tedavide mi, takipte mi, onamda mı?
3. Daha önce ATK/bilirkişi/Sağlık Bakanlığı raporu alındı mı?
4. Müdahale öncesi hastanın komorbiditeleri/risk faktörleri var mıydı?

## Denetim şeması
1. **Hukuki sebep seçimi**: Sözleşmesel sorumlulukta kusur karinesi işler; borçlu (hekim) kusursuzluğunu ispatlar (TBK m.112). Haksız fiilde kusuru davacı ispatlar (TBK m.49, m.50). Yarışma halinde davacı lehine olan tercih edilir.
2. **Hukuka aykırılık / özen ihlali**: Tıbbın güncel standardına (endikasyon, doğru teşhis, doğru teknik, takip) aykırılık var mı? Aydınlatma eksikliği başlı başına hukuka aykırılıktır.
3. **Kusur**: Taksir derecesi (basit/ağır). Standart sapması bilirkişi/ATK ile somutlanır.
4. **Zarar**: Maddi zarar (tedavi gideri, iş gücü kaybı, destekten yoksun kalma TBK m.53), manevi zarar (TBK m.56), bedensel bütünlük zararı (TBK m.54).
5. **Uygun illiyet bağı**: Kusur ile zarar arasında uygun nedensellik. Komplikasyon veya hastanın bünyesel durumu illiyeti kesiyor mu? Müterafik kusur indirim sebebidir (TBK m.52).
6. **Ara sonuç**: Unsurlardan biri eksikse sorumluluk doğmaz; tümü varsa tazminat kalemleri hesaplanır.
7. **Hastane işleteninin sorumluluğu**: Özel hastane, ifa yardımcısı olan hekimin fiilinden TBK m.116 uyarınca sorumludur.

## Çıktı modülleri
- Unsur unsur değerlendirme matrisi (var/yok/şüpheli)
- Tazminat kalemleri ve hesap çerçevesi
- Delil ve bilirkişi ihtiyacı listesi
- İlkesel içtihat atfı (Yargıtay 3./15. HD; karararama.yargitay.gov.tr) [DOĞRULANMADI]



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

