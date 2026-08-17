---
argument-hint: ''
description: Bölge adliye mahkemesi kararına karşı Yargıtaya temyiz başvurusu, temyiz
  edilebilirlik sınırı, hukuka aykırılık sebepleri ve bozma sonuçları değerlendirilirken
  kullanılır.
name: temyiz-kanun-yolu
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
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temyiz Kanun Yolu

## Görev
BAM ceza dairesi kararına karşı temyiz yolunun açık olup olmadığını, süresini ve hukuka aykırılık sebeplerini belirlemek; Yargıtay incelemesini ve bozma sonucunu yönlendirmek.

## Soğuk başlangıç (intake)
- BAM kararı ne zaman tefhim/tebliğ edildi?
- Karar temyiz edilebilir mi (m.286 sınırları, katalog)?
- Mutlak/nispi hangi hukuka aykırılık sebepleri var?
- Sanık lehine mi aleyhe mi temyiz söz konusu?
- Dosyada hukukun yanlış uygulanması mı, eksik inceleme mi öne çıkıyor?

## Denetim şeması
1. **Süre.** Temyiz, BAM kararının tefhiminden, yokluğunda tebliğinden itibaren 15 gün içinde yapılır (CMK m.291).
2. **Temyiz edilebilirlik.** İstinaf üzerine verilen bazı kararlar kesindir; temyiz yalnızca m.286'da gösterilen ağırlıktaki hükümler için açıktır (ör. belirli hapis cezası eşiğinin üzerindeki mahkûmiyetler). Sınır ve istisnalar m.286'dan ve güncel düzenlemeden doğrulanır.
3. **Sebep.** Temyiz ancak hukuka aykırılık nedenine dayanır (m.288); Yargıtay maddi olayı yeniden değerlendirmez, hukukun uygulanmasını denetler.
4. **Mutlak bozma nedenleri.** m.289'da sayılan haller (mahkemenin kanuna aykırı kuruluşu, hâkimin yasaklılığı, aleniyet ihlali, gerekçesizlik, savunma hakkının kısıtlanması, hükmün hukuka aykırı delile dayanması vb.) hukuka aykırılık sayılır.
5. **Karar.** Yargıtay temyiz istemini reddeder, hükmü bozar veya düzelterek onar (m.302-303). Bozmadan sonra direnme/uyma süreci işler (m.307); direnme kararları Ceza Genel Kurulunda incelenir.
6. **Ara sonuç.** Sebepli ve süresinde temyiz hazırlanır; temyiz kapalıysa yalnız itiraz/yargılamanın yenilenmesi yolları kalır.

## Çıktı modülleri
- Temyiz edilebilirlik ve süre denetim notu.
- Temyiz dilekçesi iskeleti (mutlak/nispi sebepler m.289 eşlemesi).
- Bozma sonrası senaryo analizi (uyma/direnme).
- Yargıtay daire içtihadı arama notu (karararama.yargitay.gov.tr).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

