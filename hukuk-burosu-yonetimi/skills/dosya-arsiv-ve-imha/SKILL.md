---
argument-hint: ''
description: İş tamamlandıktan sonra dosyanın kapatılması, ne kadar saklanacağı, arşivlenmesi,
  müvekkile iadesi ve süre sonunda KVKK uyumlu imhası kararlaştırılırken kullanılır.
name: dosya-arsiv-ve-imha
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
  - ad: Avukatlık Kanunu
    numara: '1136'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dosya Saklama, Arşiv ve İmha

## Görev
Sona eren işlerde dosyayı düzenli kapatmak; evrakın iadesi/saklanması ve saklama süresini belirlemek; süre sonunda kişisel verileri KVKK'ya uygun imha etmek; olası sorumluluk ve denetim ihtiyacını dengelemek.

## Soğuk başlangıç (intake)
1. İş nasıl sona erdi (karar kesinleşti, sulh, azil/istifa, danışmanlık bitti)?
2. Müvekkile ait asıl evrak/belge büroda mı; iadesi gerekiyor mu?
3. Dosyada hangi kişisel/özel nitelikli veriler var?
4. İleride sorumluluk, kanun yolu veya icra ihtiyacı doğabilir mi?

## Denetim şeması
1. **Kapanış kontrolü**: Tüm süreler kapanmış, kesinleşme/sulh tutanağı dosyada, vekâlet ücreti tahsil/hesap durumu net mi?
2. **Asıl evrakın iadesi (TBK m.508 hesap verme; 1136 ilişkisi)**: Müvekkile ait asıl belgeler iade edilir; hapis hakkı (1136 m.166) saklı kalır. İade tutanakla yapılır.
3. **Saklama süresi**: Olası sorumluluk zamanaşımı (vekâlet ilişkisinde TBK genel süreleri), mevzuat gerekleri ve kanun yolu ihtimali gözetilerek saklama süresi belirlenir; süre KVKK saklama-imha politikasıyla uyumlandırılır.
4. **Arşiv güvenliği (KVKK m.12)**: Fiziki/dijital arşivde erişim sınırlaması, gizlilik (1136 m.36) ve veri güvenliği sürdürülür.
5. **İmha/anonimleştirme**: Saklama süresi dolan kişisel veriler KVKK saklama-imha rejimine göre silinir/yok edilir/anonim hale getirilir; imha kayıt altına alınır.
6. **Ara sonuç**: İade + saklama süresi + güvenli arşiv + süre sonu imha planı tanımlanınca dosya usulüne uygun kapatılmıştır.

## Çıktı modülleri
- Dosya kapanış kontrol listesi.
- Evrak iade tutanağı taslağı.
- Saklama süresi ve imha planı tablosu (veri kategorisi, süre, imha yöntemi).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

