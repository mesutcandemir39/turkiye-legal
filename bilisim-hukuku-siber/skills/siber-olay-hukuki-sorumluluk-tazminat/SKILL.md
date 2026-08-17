---
argument-hint: ''
description: Veri ihlali, sistem kesintisi veya siber saldırı sonrası kurum-müşteri-iş
  ortağı arasındaki tazminat ve sözleşmesel sorumluluğu; kusur, illiyet ve zarar denetimini
  yapmak gerektiğinde kullanılır.
name: siber-olay-hukuki-sorumluluk-tazminat
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Elektronik Ticaretin Düzenlenmesine Dair Kanun
    numara: '5651'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Siber Olaydan Doğan Hukuki Sorumluluk ve Tazminat

## Görev
Bir siber olay sonrası kimin, kime, hangi hukuki sebeple ve ne kadar sorumlu olduğunu (haksız fiil/sözleşme) çözmek; tazminat talebi veya savunma stratejisi kurmak.

## Soğuk başlangıç (intake)
1. Zarar gören kim, zarar ne? (maddi kayıp, itibar, veri kaybı, manevi zarar?)
2. Taraflar arasında sözleşme var mı? (hizmet, işleme, SLA?)
3. Olayın sebebi ne? (kurumun tedbirsizliği, üçüncü kişi saldırısı, çalışan kusuru?)
4. Talep mi savunma mı, muhatap kim?

## Denetim şeması
1. **Sorumluluk temeli seçimi.** Sözleşme varsa borca aykırılık (TBK m.112 vd.) ve borçlunun yardımcı kişilerden sorumluluğu (TBK m.116) önceliklidir; sözleşme yoksa haksız fiil (TBK m.49). Çoğu olayda yarışan sebep söz konusudur; zarar görenin lehine olan seçilebilir.
2. **Haksız fiil unsurları (TBK m.49 vd.).** Fiil (güvenlik tedbirini almama/ihmal), hukuka aykırılık (KVKK m.12 ihlali, gizlilik ihlali), kusur, zarar ve illiyet bağı aranır. KVKK m.12 yükümlülüğünün ihlali hukuka aykırılığın güçlü göstergesidir. Üçüncü kişinin saldırısı illiyeti kesebilir; ancak öngörülebilir saldırıya karşı tedbirsizlik kusuru ortadan kaldırmaz.
3. **Manevi tazminat ve veri.** Kişilik hakkı ihlali (TMK m.24; TBK m.58) ve özel hayatın ihlali manevi tazminata esas olabilir; veri ihlalinde ilgili kişilerin zararı somutlaştırılır.
4. **İspat yükü ve hesap.** Sözleşmesel sorumlulukta borçlu kusursuzluğunu (TBK m.112) ispatlar; haksız fiilde kural olarak zarar görenin ispatı gerekir, KVKK m.12 ise tedbir ispatını kuruma yükler. Zarar kalemleri (fiili zarar, yoksun kalınan kâr, gideri yapılan müdahale masrafları) belgelenir; tazminattan indirim sebepleri (TBK m.52) gözetilir.
5. **Ara sonuç.** Sorumlu sıfatı, hukuki sebep, ispat dağılımı ve zamanaşımı (TBK m.72 haksız fiilde; m.146/147 sözleşmesel) netleştirilir.

## Çıktı modülleri
- Sorumluluk haritası (taraf-sebep-kusur-illiyet-zarar).
- Tazminat hesap çerçevesi ve indirim notu.
- Talep/ihtar veya savunma dilekçesi iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

