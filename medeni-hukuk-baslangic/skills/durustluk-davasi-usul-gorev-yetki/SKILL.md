---
argument-hint: ''
description: TMK m.2/m.3 gibi başlangıç hükümlerinin bir davada nasıl ileri sürüleceği,
  hangi mahkemenin görevli/yetkili olduğu ve def'i mi itiraz mı olduğu tartışıldığında
  usul yol haritasını çıkarmak için kullan
name: durustluk-davasi-usul-gorev-yetki
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


# Başlangıç Hükümlerine Dayalı Uyuşmazlıklarda Usul, Görev ve Yetki

## Görev
Başlangıç hükümlerinin (özellikle TMK m.2/2 kötüye kullanma, m.3 iyiniyet, m.6 ispat) bir yargılamada doğru usulle ileri sürülmesini, görevli-yetkili mahkemenin belirlenmesini ve hâkimce re'sen gözetilip gözetilmeyeceğini netleştirmek.

## Soğuk başlangıç (intake)
- Başlangıç hükmü bağımsız bir talep olarak mı, yoksa asıl talebe karşı savunma/def'i olarak mı ileri sürülüyor?
- Asıl uyuşmazlık hangi mahkemenin görev alanında (sulh hukuk / asliye hukuk / tüketici / aile / ticaret)?
- Hangi yargılama usulü uygulanıyor (yazılı / basit — HMK m.118 vd., m.316 vd.)?
- İddia hangi aşamada ileri sürülmek isteniyor (dilekçeler, ön inceleme, tahkikat)?

## Denetim şeması
1. **Başlangıç hükmü ≠ bağımsız dava** — TMK m.2, m.3 kural olarak bağımsız dava sebebi değildir; asıl hak/borç ilişkisine bağlı olarak ileri sürülür. Görev ve yetki, asıl uyuşmazlığa göre belirlenir.
2. **Görev** — Genel görev kuralı HMK m.2 (malvarlığı/şahıs varlığı davalarında asliye hukuk); sulh hukukun görevi HMK m.4'te sayılıdır. Özel mahkemeler: aile, tüketici (6502), ticaret (TTK m.4-5), iş. Görev kamu düzenindendir, re'sen gözetilir (HMK m.1, m.114/1-c).
3. **Yetki** — Genel yetki davalının yerleşim yeri (HMK m.6); taşınmazda kesin yetki (HMK m.12); sözleşmeden doğan davalarda m.10. Yetki itirazı ilk itiraz olarak cevap dilekçesinde ileri sürülür (HMK m.116, m.117).
4. **Def'i mi, itiraz mı?** — Hakkın kötüye kullanılması ve iyiniyet bir *itiraz* niteliğindedir ve hâkimce re'sen göz önünde tutulur; bu yüzden taraf açıkça ileri sürmese de açık kötüye kullanmayı hâkim dikkate alabilir (kamu düzeni boyutu). Zamanaşımı gibi *def'iler* ise ileri sürülmedikçe gözetilmez.
5. **Aşama ve teksif** — İddia ve savunmanın genişletilmesi yasağı (HMK m.141) kapsamında başlangıç hükmüne dayalı vakıalar zamanında ileri sürülmelidir; ancak hâkimin re'sen gözettiği itirazlar bu yasağın dışındadır.
6. **İspat usulü** — TMK m.6 / HMK m.190; senetle ispat sınırı (HMK m.200-201) ve resmî belge ispat gücü (TMK m.7 / HMK m.204) usul boyutuyla birlikte uygulanır.

## Çıktı modülleri
- Talep mi / savunma mı ayrımı.
- Görev-yetki tespiti (asıl uyuşmazlığa göre) + dayanak madde.
- Def'i/itiraz nitelendirmesi ve re'sen gözetme notu.
- İleri sürme aşaması + ispat usulü + ilkesel içtihat `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

