---
argument-hint: ''
description: Kanunların zaman bakımından uygulanması (lehe kanun) ile yer bakımından
  uygulanması (Türkiye'de/yurt dışında işlenen suçlar) sorunlarını çözmek gerektiğinde
  kullanılır.
name: zaman-yer-bakimindan-uygulama
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
  version: 0.1.0
user-invocable: true
---


# Zaman ve Yer Bakımından Uygulama

## Görev
Hangi ceza normunun zaman (lehe kanun) ve yer (mülkilik/şahsilik) bakımından uygulanacağını belirlemek; özellikle suç tarihi ile karar tarihi arasında değişen mevzuatta lehe hükmü saptamak.

## Soğuk başlangıç (intake)
- Suç tarihi ile karar/inceleme tarihi arasında ilgili norm değişti mi?
- Suç Türkiye'de mi, yurt dışında mı işlendi; fail ve mağdurun vatandaşlığı?
- İnfaz rejimini etkileyen bir değişiklik var mı?
- Suç birden çok ülkede mi gerçekleşti (hareket/netice farklı yerlerde mi)?

## Denetim şeması
1. **Kanunilik (m.2):** İşlendiği zaman kanunda suç sayılmayan fiil cezalandırılamaz; aleyhe kıyas ve geriye yürüme yasaktır.
2. **Lehe kanun (m.7/1-2):** Suçun işlendiği ve sonraki zaman dilimlerindeki normlar arasında failin lehine olan uygulanır; kesinleşmiş hükümlerde dahi infazı ve sonuçlarını etkileyen lehe değişiklik gözetilir. Ara sonuç: hangi metin failin lehine?
3. **Karşılaştırma yöntemi:** Lehe tespit soyut değil, somut olaya uygulanan sonuç üzerinden yapılır; karma uygulama yapılmaz, bir bütün olarak lehe olan metin seçilir.
4. **Mülkilik (m.8):** Türkiye'de işlenen suçlarda Türk kanunu uygulanır; hareket veya netice Türkiye'de gerçekleşmişse suç Türkiye'de işlenmiş sayılır.
5. **Yurt dışında işlenen suçlar (m.9-13):** Vatandaş (m.11) ve yabancı (m.12) tarafından işlenen suçlar, koruma ve evrensellik ilkeleri (m.13); yabancı ülkede mahkûmiyetin etkisi ve non bis in idem (m.9).
6. **Cezadan mahsup (m.16):** Yurt dışında gözaltı/tutukluluk/hükümlülük sürelerinin mahsubu.

## Çıktı modülleri
- Lehe kanun karşılaştırma tablosu (eski/yeni metin, somut sonuç).
- Yer bakımından uygulama yetki analizi.
- Mahsup ve non bis in idem notu.
- Eksik bilgi ve `[DOĞRULANMADI]` içtihat ihtiyacı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

