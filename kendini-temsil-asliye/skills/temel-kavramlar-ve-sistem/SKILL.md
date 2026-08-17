---
argument-hint: ''
description: Davasını avukatsız takip etmek isteyen kişi temel kavramları (asil, dava
  ehliyeti, görev, dava şartı arabuluculuk) öğrenmek istediğinde ve uyuşmazlığını
  doğru kategoriye yerleştirmek istediğinde kulla
name: temel-kavramlar-ve-sistem
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Kendini Temsil Sistemi

## Görev
Davasını avukatla değil bizzat takip edecek kişiye sistemin haritasını çıkarmak: kim, hangi mahkemede, hangi ön koşulla, nasıl dava açabilir veya başvuru yapabilir.

## Soğuk başlangıç (intake)
- Uyuşmazlık ne hakkında (alacak, kira, tüketici, zilyetlik, mülkiyet, tazminat)?
- Karşı taraf gerçek kişi mi, şirket mi, kamu kurumu mu?
- Talep ettiğiniz tutar veya konunun değeri yaklaşık nedir?
- Daha önce başvuru, ihtar veya arabuluculuk yapıldı mı?
- Tarafsınız mı yoksa başkası adına mı hareket ediyorsunuz (vekâlet/veli/vasi)?

## Denetim şeması
1. **Dava ehliyeti ve takip yetkisi (HMK m.50-52, 71):** Taraf tam fiil ehliyetine sahipse davasını kendisi açıp takip edebilir; avukat zorunlu değildir. Kısıtlı/küçük ise yasal temsilci (veli-vasi) gerekir. Tüzel kişi adına ancak yetkili organ/temsilci hareket eder.
2. **Görev (dava şartı, HMK m.114/1-c, m.1):** Görev kanunla belirlenir, taraflar değiştiremez, re'sen incelenir. Sulh hukukun görev alanı HMK m.4'te sayılıdır (kira, paydaşlığın giderilmesi, zilyetlik). Aksi belirtilmedikçe genel görevli asliye hukuktur (m.2). Tüketici işlemi varsa tüketici hakem heyeti/tüketici mahkemesi (6502 sayılı Kanun).
3. **Zorunlu ön başvuru:** Dava şartı arabuluculuk; ticari, tüketici, kira, ortaklığın giderilmesi gibi uyuşmazlıklarda dava açmadan önce zorunludur (7036/6325 sayılı düzenlemeler) — atlanırsa dava usulden reddedilir. Tüketici uyuşmazlığında parasal sınır altı işlerde önce hakem heyeti zorunludur.
4. **Yargılama usulü:** Sulh hukuk ve kanunda sayılan işler basit yargılamaya tabidir (HMK m.316). Basit yargılamada dilekçe teatisi kısadır ve cevaba cevap/ikinci cevap yoktur.
5. **Ara sonuç:** Doğru forum + zorunlu ön koşul + ehliyet tamamsa dava/başvuru yoluna geçilir; eksikse önce o giderilir.

## Çıktı modülleri
- Uyuşmazlık sınıflandırma kartı (forum + usul + ön koşul).
- Yapılması gerekenler kontrol listesi (sırasıyla).
- Atlanması durumunda risk uyarıları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

