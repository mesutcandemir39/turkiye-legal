---
argument-hint: ''
description: 6331 sayılı Kanun kapsamında uygulanan idari para cezalarının hukukiliğini
  denetlemek ve sulh ceza hâkimliğine itiraz yolunu kurmak için kullanılır.
name: idari-para-cezalari
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
  - ad: İş Sağlığı ve Güvenliği Kanunu
    numara: '6331'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İdari Para Cezaları ve İtiraz

## Görev
İş müfettişi denetimi sonucu uygulanan idari para cezalarının dayanağını, usulünü ve miktarını denetlemek; 5326 sayılı Kabahatler Kanunu çerçevesinde itiraz yolunu kurmak.

## Soğuk başlangıç (intake)
- Ceza hangi yükümlülük ihlaline dayanıyor (6331 m.26 hangi bent); ceza tutanağı ve denetim raporu elde mi?
- Tebliğ tarihi ne; itiraz süresi kaçtı mı (tebliğden itibaren on beş gün)?
- İşyerinin tehlike sınıfı ve çalışan sayısı (bazı cezalar bunlara göre/her çalışan başına katlanır)?
- Aynı fiil için tekerrür veya birden çok ceza var mı?

## Denetim şeması
1. **Dayanak (6331 m.26):** Her ceza, ihlal edilen yükümlülük maddesine (m.4, 6, 8, 10, 11, 14, 15, 16, 17, 18, 22 vb.) bağlanır; m.26 bentleri hangi maddeye hangi tutarı öngördüğünü gösterir. Cezanın doğru maddeye dayandığını ve eylemin gerçekten o yükümlülüğü ihlal ettiğini denetle.
2. **Çalışan başına/aylık tekrar:** Bazı cezalar her çalışan için ayrı ve aykırılığın devam ettiği her ay için tekrar uygulanır; bu çarpanların doğru hesaplandığını kontrol et.
3. **Usul denetimi:** Yetkili merci, tutanağın usulü, savunma hakkı, tebligatın usulüne uygunluğu (7201). Usul sakatlığı iptal sebebidir.
4. **İtiraz yolu (5326 m.27-28):** İdari para cezasına karşı tebliğden itibaren on beş gün içinde sulh ceza hâkimliğine başvurulur; sulh ceza kararına karşı itiraz mercii bir sonraki numaralı sulh ceza hâkimliğidir. Süreyi kaçırmamak esastır.
5. **İspat ve karine:** İdarenin tespitleri aksi ispatlanana kadar esas alınır; işveren uyumunu belgeyle çürütür. **Ara sonuç:** İptal/indirim argümanlarını madde ve usul ekseninde sırala.

## Çıktı modülleri
- Ceza-madde-tutar eşleştirme tablosu.
- Usul ve esas itiraz gerekçeleri listesi.
- Sulh ceza hâkimliği başvuru dilekçesi taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

