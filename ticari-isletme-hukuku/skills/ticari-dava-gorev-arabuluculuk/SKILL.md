---
argument-hint: ''
description: Bir uyusmazligin ticari dava olup olmadigini, asliye ticaret mahkemesinin
  gorevli olup olmadigini, dava sarti arabuluculugun zorunlu olup olmadigini ve yetkili
  mahkemeyi belirlemek gerektiginde kullan
name: ticari-dava-gorev-arabuluculuk
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Ticari Davada Görev, Yetki ve Dava Şartı Arabuluculuk

## Görev
Uyuşmazlığın ticari dava niteliğini, görevli ve yetkili mahkemeyi ve dava şartı arabuluculuğun zorunlu olup olmadığını belirlemek. Görev kamu düzenindendir; yanlış mahkeme veya arabuluculuk atlanması davayı baştan tıkar.

## Soğuk başlangıç (intake)
1. Uyuşmazlığın kaynağı ne (TTK'da düzenlenen iş mi, her iki tarafın ticari işletmesiyle ilgili mi)?
2. Taraflar tacir mi; her ikisi için de ticari iş mi?
3. Talep konusu para alacağı/tazminat mı (arabuluculuk eşiği)?
4. Sözleşmede yetki/tahkim şartı var mı?

## Denetim şeması
1. **Ticari dava türleri:** TTK m.4 — (i) mutlak ticari davalar (tarafların sıfatına bakılmaksızın TTK'da ve bazı kanunlarda sayılan davalar; örn. TTK, TMK rehin/kıymetli evrak, bankacılık, fikri mülkiyet bazı davaları), (ii) her iki tarafın ticari işletmesiyle ilgili nispi ticari davalar. Bu davalar değer/miktara bakılmaksızın asliye ticaret mahkemesinde görülür (TTK m.5/1).
2. **Görev:** TTK m.5 — asliye ticaret mahkemesi ile asliye hukuk arasındaki ilişki görev ilişkisidir (kamu düzeni; re'sen incelenir). Heyet/tek hâkim ayrımı için TTK m.5/3-4 (belirli değer/konu eşikleri).
3. **Dava şartı arabuluculuk:** TTK m.5/A — konusu bir miktar paranın ödenmesi olan alacak ve tazminat talepleri (itirazın iptali, menfi tespit, istirdat dahil) bakımından dava açılmadan önce arabulucuya başvurulmuş olması dava şartıdır. Anlaşmama tutanağı dava dilekçesine eklenmezse dava usulden reddedilir. İstisnalar (örn. ihtiyati tedbir/haciz) ve diğer zorunlu arabuluculuk alanlarıyla (tüketici, iş) ilişki gözetilir.
4. **Yetki:** Genel yetki davalının yerleşim yeri (HMK m.6); sözleşmeden doğanlarda ifa yeri (HMK m.10); tacirler/kamu tüzel kişileri arasında yazılı yetki sözleşmesi geçerli (HMK m.17). Tahkim şartı varsa mahkemenin görevsizliği itiraz üzerine incelenir.
5. **İspat/usul:** Görev ve dava şartları re'sen; yetki itirazı ilk itiraz olarak süresinde ileri sürülür. Ara sonuç: ticari dava + para talebi → arabuluculuk şartı + asliye ticaret mahkemesi.

## Çıktı modülleri
- Görev-yetki-arabuluculuk karar tablosu (dayanak: TTK m.4, m.5, m.5/A).
- Arabuluculuk başvuru ve son tutanak kontrol listesi.
- Yetki/tahkim itirazı veya yetkili mahkeme tespiti notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

