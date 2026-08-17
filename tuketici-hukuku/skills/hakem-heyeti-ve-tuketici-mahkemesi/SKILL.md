---
argument-hint: ''
description: Bir tüketici uyuşmazlığında parasal sınıra göre zorunlu hakem heyeti
  mi yoksa tüketici mahkemesi mi gerektiğini belirlemek, görev-yetki ve başvuru usulünü
  kurmak gerektiğinde kullanılır.
name: hakem-heyeti-ve-tuketici-mahkemesi
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
  - ad: Tüketicinin Korunması Hakkında Kanun
    numara: '6502'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tüketici Hakem Heyeti ve Tüketici Mahkemesi Yolu

## Görev
Uyuşmazlığın değerine göre doğru başvuru merciini (tüketici hakem heyeti ya da tüketici mahkemesi) belirlemek, görev ve yetkiyi saptamak, başvuru/dava usulünü ve karara karşı itiraz yolunu kurmak.

## Soğuk başlangıç (intake)
- Uyuşmazlığın parasal değeri ne (faizsiz asıl alacak)?
- Tarafların yerleşim yeri/işlemin yapıldığı yer neresi (yetki için)?
- Daha önce hakem heyetine başvuruldu mu, karar çıktı mı?
- Talep yalnızca para mı, yoksa tespit/men/eda gibi karma talep mi?

## Denetim şeması
1. **Görev — parasal sınır (TKHK m.68):** Değeri her yıl Tebliğ ile belirlenen alt parasal sınırın altında kalan uyuşmazlıklarda tüketici hakem heyetine başvuru zorunludur ve heyet kararları taraflar için bağlayıcıdır. Sınırın üzerindeki uyuşmazlıklarda doğrudan tüketici mahkemesi görevlidir. Güncel rakam Tebliğ'den doğrulanmalıdır [DOĞRULANMADI].
2. **Hakem heyeti çeşidi ve yetki (m.66, m.68):** İl/ilçe tüketici hakem heyetleri; tüketicinin yerleşim yeri ya da işlemin yapıldığı yer hakem heyeti yetkilidir. Başvuru ücretsizdir, elektronik (e-Devlet/TÜBİS) veya yazılı yapılabilir.
3. **Karar ve itiraz (m.70):** Heyet kararı tebliğden itibaren on beş gün içinde tüketici mahkemesine itirazla kaldırılabilir; itiraz üzerine mahkeme kararı kesindir. İtiraz, kararın icrasını kendiliğinden durdurmaz ancak tedbir istenebilir.
4. **Tüketici mahkemesi (m.73):** Tüketici işlemlerinden doğan davalarda görevli mahkeme tüketici mahkemesidir; bulunmayan yerde asliye hukuk mahkemesi tüketici mahkemesi sıfatıyla bakar. Davalar basit yargılama usulüne tabidir.
5. **Harç ve gider muafiyeti (m.73/2):** Tüketici davalarında tüketici, dava açarken harçtan ve bilirkişi dahil yargılama giderlerinden muaftır; bu maddi avantaj strateji kurarken not edilir.
6. **Dava şartı arabuluculuk:** Ticari nitelikteki tüketici davalarında değil ama bazı tüketici uyuşmazlıklarında dava açmadan önce arabuluculuk dava şartı olabilir; somut talebe göre kontrol edilir (TKHK m.73/A) [DOĞRULANMADI].
7. **Ara sonuç:** Hangi mercii görevli, hangi yer yetkili, hangi usul ve hangi itiraz yolu?

## Çıktı modülleri
- Görev-yetki belirleme notu.
- Hakem heyeti başvuru dilekçesi taslağı.
- Tüketici mahkemesi dava/itiraz dilekçesi iskeleti.
- Harç/gider ve süre bilgilendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

