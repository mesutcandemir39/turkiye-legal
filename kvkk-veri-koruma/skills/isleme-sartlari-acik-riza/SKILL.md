---
argument-hint: ''
description: Bir veri işleme faaliyetinin hangi hukuki sebebe dayandığını belirlemek,
  açık rıza yerine m.5/m.6 istisnalarının uygulanıp uygulanmayacağını değerlendirmek
  gerektiğinde kullanılır.
name: isleme-sartlari-acik-riza
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İşleme Şartları ve Açık Rıza Denetimi

## Görev
Somut bir işleme faaliyetinin KVKK m.5 (genel veri) veya m.6 (özel nitelikli veri) çerçevesinde hangi hukuki sebebe oturduğunu saptamak; açık rıza refleksinin tuzaklarından kaçınıp daha sağlam istisnaları tercih etmek.

## Soğuk başlangıç (intake)
1. İşlemenin somut amacı nedir, hangi faaliyetin parçasıdır?
2. Veri genel mi, özel nitelikli mi?
3. Bir kanun, sözleşme ya da hukuki yükümlülük bu işlemeyi zaten gerektiriyor mu?
4. Şu an dayanılan sebep açık rıza mı; rıza geri alınırsa faaliyet durur mu?

## Denetim şeması
1. **Genel veri — m.5**: Önce açık rıza dışı şartları sırayla dene: (a) kanunlarda açıkça öngörülme, (b) ilgili kişinin fiili imkânsızlık nedeniyle rıza veremediği hal, (c) sözleşmenin kurulması/ifası için zorunluluk, (ç) veri sorumlusunun hukuki yükümlülüğünü yerine getirmesi, (d) ilgili kişinin kendisi tarafından alenileştirme, (e) bir hakkın tesisi/kullanılması/korunması için zorunluluk, (f) meşru menfaat (ilgili kişinin temel hak ve özgürlüklerine zarar vermemek kaydıyla, denge testiyle).
2. **Meşru menfaat dengesi**: m.5/2-f en esnek ama en tartışmalı sebeptir; menfaatin meşruluğu, işlemenin gerekliliği ve ilgili kişi üzerindeki etkisi tartılarak yazılı denge testi (LIA) belgelenmelidir.
3. **Özel nitelikli veri — m.6** (7499 ile 01.06.2024'ten itibaren): açık rıza ya da m.6/3'te sayılan haller (kanunda öngörülme, fiili imkânsızlık, alenileştirme, hakkın tesisi, sağlık/cinsel hayat verisinin sır saklama yükümlüsünce kamu sağlığı vb. amaçla işlenmesi, istihdam ve sosyal güvenlik yükümlülükleri, vakıf-dernek-sendika faaliyetleri). Eski "sağlık dışı/sağlık" ayrımına dayalı ezberi kullanma; güncel metni esas al.
4. **Ara sonuç**: Açık rıza yalnızca başka şart bulunmadığında seçilir; rızaya dayanan işlemede rızanın her an geri alınabileceği (m.11) unutulmamalıdır.

İspat yükü: Geçerli işleme şartının varlığı veri sorumlusundadır; açık rızanın özgür/bilgilendirilmiş/belirli olduğunu da o ispatlar.

## Çıktı modülleri
- İşleme faaliyeti — hukuki sebep eşleştirme tablosu.
- Meşru menfaat denge testi (LIA) taslağı.
- Açık rıza yerine geçecek alternatif sebep önerisi notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

