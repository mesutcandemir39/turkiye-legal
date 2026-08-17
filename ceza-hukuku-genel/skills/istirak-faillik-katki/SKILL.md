---
argument-hint: ''
description: Birden fazla kişinin bir suça katıldığı durumlarda müşterek/dolaylı faillik,
  azmettirme ve yardım etme ayrımını ve bağlılık kuralını uygulamak gerektiğinde kullanılır.
name: istirak-faillik-katki
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


# İştirak — Faillik ve Suça Katılma

## Görev
Bir suça birden fazla kişinin katıldığı hâllerde her katılanın konumunu (fail, müşterek fail, dolaylı fail, azmettiren, yardım eden) belirleyip cezai sorumluluğu dağıtmak.

## Soğuk başlangıç (intake)
- Suça kaç kişi, hangi rolde katıldı?
- Fiil üzerinde kim ortak hâkimiyet kurdu; kim sadece destek verdi?
- Bir kişi başkasını suç işlemeye karar verdirdi mi (azmettirme)?
- Katkı, suçun işlenmesinden önce/sırasında mı, manevi mi maddi mi?

## Denetim şeması
1. **Faillik (m.37/1):** Suçun kanuni tanımındaki fiili gerçekleştiren faildir; birlikte işleyenler müşterek faildir (fiil üzerinde ortak hâkimiyet ölçütü).
2. **Dolaylı faillik (m.37/2):** Başkasını araç olarak kullanarak suç işleme; aracın kusur yeteneksizliğinden yararlanmada ceza artırılabilir.
3. **Azmettirme (m.38):** Başkasını belli bir suç işlemeye karar verdirme; fail kadar ceza. Üstsoy-altsoy ilişkisi ve azmettirenin belirlenememesi yönünden özel hükümler vardır.
4. **Yardım etme (m.39):** Suç işlemeye teşvik, kararı kuvvetlendirme, yol gösterme (manevi); araç sağlama, fiilin işlenmesini kolaylaştırma (maddi). Ceza, suçun cezasından indirilerek belirlenir. Ara sonuç: katkı icrai faillik düzeyine ulaştı mı, yardım düzeyinde mi kaldı?
5. **Bağlılık kuralı (m.40):** İştirak için kasten ve hukuka aykırı bir fiilin varlığı yeterlidir; herkes kendi kusuruna göre sorumludur. Özgü suçlarda (failin özel sıfat gerektiren suç) özel sıfatı olmayan kişi ancak yardım eden/azmettiren olabilir.
6. **Gönüllü vazgeçme ve iştirak:** Katılanlardan birinin vazgeçmesi (m.41) kendi sorumluluğunu etkiler.

## Çıktı modülleri
- Katılan bazlı rol-sorumluluk tablosu (madde atıflı).
- Müşterek faillik vs. yardım etme ayrım gerekçesi.
- Her katılan için ceza belirleme notu.
- Eksik delil ve `[DOĞRULANMADI]` içtihat ihtiyacı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

