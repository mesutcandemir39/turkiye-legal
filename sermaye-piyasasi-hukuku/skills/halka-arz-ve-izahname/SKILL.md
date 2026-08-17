---
argument-hint: ''
description: Payların veya borçlanma araçlarının halka arzı, izahname/ihraç belgesi
  hazırlığı ve onayı, izahnamenin gerçeği yansıtmamasından doğan sorumluluk konuları
  gündeme geldiğinde kullanılır.
name: halka-arz-ve-izahname
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
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Halka Arz ve İzahname

## Görev
Halka arz sürecini SPK m.4-11 ve ilgili Kurul tebliğleri çerçevesinde yapılandırmak; izahname/ihraç belgesi içeriğini denetlemek; izahname sorumluluğu (m.10) riskini değerlendirmek.

## Soğuk başlangıç (intake)
- İhraç türü: pay mı borçlanma aracı mı; ilk halka arz mı, bedelli/bedelsiz sermaye artırımı mı?
- Halka arz mı, yoksa istisna kapsamında tahsisli satış mı (m.11)?
- İzahname mi, ihraç belgesi mi gerekiyor; aracılık yüklenimi sözleşmesi var mı?
- Hangi taraf danışılıyor: ihraççı, aracı kurum, yatırımcı (zarar gören) mi?

## Denetim şeması
1. **Halka arz/istisna ayrımı:** İşlem SPK m.4 anlamında halka arz mı, yoksa m.11 ve tebliğdeki istisna (nitelikli yatırımcı, asgari tutar) kapsamında mı belirlenir. İstisna varsa izahname yerine ihraç belgesi gündeme gelir.
2. **İzahname hazırlığı ve onayı:** İzahnamenin Kurul onayına sunulması, içeriğinin ihraççı, ihraç ve riskleri tam, doğru, anlaşılır yansıtması aranır (m.4, m.6-8); özet bölümü ve risk faktörleri kontrol edilir.
3. **Sorumluluk denetimi (m.10):** İzahnamede yer alan yanlış, yanıltıcı veya eksik bilgiden ihraççı; ihraççı yoksa/karşılanamıyorsa garanti veren, ihraca aracılık eden lider kuruluş, hazırlayanlar ve onaylayan bağımsız denetçi/değerleme kuruluşu kusurları oranında sorumludur. Ara sonuç: zarar gören yatırımcının kime, hangi sırayla başvuracağı netleşir.
4. **İspat yükü:** Bilginin yanlışlığı ve zararla illiyeti yatırımcıda; gerekli özeni gösterdiğini ispat ise sorumlu tarafta (m.10 mantığı). Zarar, ihraç fiyatı ile gerçek değer/satış değeri farkı üzerinden kurulur.
5. **Süre:** Tazminat talebinde zamanaşımı için SPK m.10 ve TBK genel zamanaşımı birlikte değerlendirilir; tarih ve öğrenme anı dosyaya işlenir.

## Çıktı modülleri
- Halka arz/istisna nitelendirme notu
- İzahname içerik denetim listesi (risk faktörleri, finansallar, onay)
- Sorumluluk zinciri ve muhatap analizi (m.10)
- İhraççı için uyum kontrol listesi veya yatırımcı için talep iskeleti



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

