---
argument-hint: ''
description: Vekilin özen ve sadakat borcuna aykırılığı, talimat dışı işlem, hesap
  verme talebi veya azil/istifa sonuçları söz konusu olduğunda; vekâlet ilişkisinin
  denetimi için kullanılır.
name: vekalet-sorumluluk-azil
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


# Vekâlet — Özen, Hesap Verme, Azil ve İstifa

## Görev
Vekilin TBK m.502-514 kapsamındaki yükümlülüklerini (özen, sadakat, talimat, hesap verme) ve vekâletin sona erme sonuçlarını denetlemek; vekâletsiz iş görme ile sınırı ayırmak.

## Soğuk başlangıç (intake)
- İşin konusu ve vekâletin kapsamı (genel/özel yetki gerektiren işlem var mı)?
- İhlal iddiası ne (talimat dışı, menfaat çatışması, hesap vermeme)?
- Ücret kararlaştırıldı mı; vekil tacir/serbest meslek mi?
- Azil/istifa gerçekleşti mi, zamanı uygun mu?

## Denetim şeması
1. **Özen ve sadakat (m.506).** Vekil, benzer alandaki basiretli bir vekilin göstereceği özeni gösterir; ücretliyse özen ölçüsü ağırlaşır. Menfaat çatışmasında müvekkil menfaati önceliklidir.
2. **Talimata uyma (m.505).** Vekil talimatla bağlı; talimattan ancak müvekkil yararına ve önceden izin alınamayacak hallerde ayrılabilir, aksi halde sonuçtan sorumlu.
3. **Bizzat ifa ve alt vekâlet (m.506/2, 507).** Kural bizzat ifa; yetkisiz alt vekilin fiilinden vekil sorumlu, yetkili devirde seçim/talimatta özenden sorumlu.
4. **Hesap verme ve iade (m.508).** Vekil her istendiğinde hesap verir ve aldıklarını iade eder; geç teslim edilen paraya faiz. Bu yükümlülük emredici niteliktedir.
5. **Sona erme (m.512-513).** Taraflar her zaman azil/istifa edebilir (m.512); uygun olmayan zamanda sona erdiren diğer tarafın zararını giderir. Ölüm/ehliyet kaybı/iflasla da sona erer (m.513).
6. **İspat ve yargı yolu.** İhlal ve zararı müvekkil; talimata/izne uygunluğu ve hesabın doğruluğunu vekil ispatlar (m.508 hesap verme yükü). Ücret/tazminat uyuşmazlığında görevli mahkeme niteliğe göre Asliye Hukuk/Ticaret. Ara sonuç: sorumluluk ve tazminat kalemleri.

## Çıktı modülleri
- Hesap verme talebi / azil bildirimi taslağı.
- Özen-sadakat ihlali değerlendirme notu.
- Tazminat talebi dava iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

