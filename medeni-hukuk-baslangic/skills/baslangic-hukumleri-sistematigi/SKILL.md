---
argument-hint: ''
description: Bir medeni hukuk uyuşmazlığında TMK başlangıç hükümlerinden hangisinin
  (m.1-m.7) devreye gireceği belirsiz olduğunda; süzgeç katmanlarını ayırt edip doğru
  hükmü ve onun işlevini seçmek için kullanılır
name: baslangic-hukumleri-sistematigi
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


# Başlangıç Hükümleri Sistematiği ve Doğru Hükmü Seçme

## Görev
Eldeki uyuşmazlıkta TMK m.1-m.7 arasındaki hangi başlangıç hükmünün, hangi işlevle (yorum, ispat, takdir, düzeltme) devreye gireceğini doğru teşhis etmek; başlangıç hükmünü esas özel normla karıştırmamak.

## Soğuk başlangıç (intake)
- Uyuşmazlığa doğrudan uygulanan özel norm hangisi (kira, mülkiyet, nafaka, sözleşme...)?
- Sorun bir hakkın kullanım tarzında mı (m.2), bir hakkın kazanılmasında bilgisizlikte mi (m.3), hâkimin takdirinde mi (m.4), kimin ispatlayacağında mı (m.6)?
- Olayda resmî sicil/senet (tapu, nüfus, resmî senet) var mı (m.7)?
- Başlangıç hükmü talep kaynağı mı sanılıyor, yoksa mevcut hakka mı eklemleniyor?

## Denetim şeması
1. **Önce özel norm, sonra süzgeç** — Başlangıç hükümleri (TMK m.5 yoluyla tüm özel hukukta) bağımsız talep doğurmaz; mevcut hak/borcu yorumlar, sınırlar veya tamamlar. Önce maddi kural tespit edilir.
2. **İşleve göre ayrım** — m.1: kaynak ve boşluk doldurma (kural yoksa). m.2: dürüstlük + hakkın kötüye kullanılması (kural var ama kullanım tarzı sorunlu). m.3: iyiniyet (bir hakkın doğumu bilgisizliğe bağlıysa). m.4: takdir/hakkaniyet (kanun hâkime alan bırakmışsa). m.6: ispat yükü. m.7: resmî sicil/senet karinesi.
3. **m.2 ile m.3 ayrımı** — m.2 bir *davranış* kuralıdır (hakkı nasıl kullanmalı); m.3 bir *bilgi* durumudur (kazanımda bilgisizliğin korunması). İkisi karıştırılmaz.
4. **m.5'in kapsamı** — Genel nitelikli TMK/TBK hükümleri "uygun düştüğü ölçüde" diğer özel hukuk ilişkilerine kıyasen uygulanır; niteliği elvermeyen hükümler taşınmaz.
5. **Ara sonuç** — Hangi başlangıç hükmü, hangi işlevle, hangi özel normun üzerine konuyor? Tek cümlede formüle edilir.

## Çıktı modülleri
- Özel norm + başlangıç hükmü eşleştirme tablosu (madde + işlev).
- Seçilen hükmün gerekçesi ve reddedilen alternatifler.
- İşlev notu (yorum/ispat/takdir/düzeltme).
- İlkesel içtihat atfı, künye `[DOĞRULANMADI]` (karararama.yargitay.gov.tr).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

