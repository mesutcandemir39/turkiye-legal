---
argument-hint: ''
description: Bir ürünü piyasaya sürmeden önce patent ihlali riskinin taranması, dava
  açma/savunma stratejisinin kurulması ya da patent portföyü kararları gündeme geldiğinde
  kullanılır; ticari kararı hukuki riskle
name: risk-strateji-ve-fto
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk, Strateji ve Kullanım Serbestisi (FTO)

## Görev
Bir ürün/teknolojinin üçüncü kişi patentlerini ihlal etme riskini (freedom to operate) değerlendirmek; hak sahibi veya muhatap konumuna göre saldırı/savunma stratejisi kurmak ve ticari kararı hukuki riskle dengelemek.

## Soğuk başlangıç (intake)
1. Konumun ne: piyasaya girecek ürün sahibi mi, hakkını koruyan patent sahibi mi, ihtarname alan muhatap mı?
2. İlgili teknik alanda hangi geçerli patent/faydalı modeller var; sicil taraması yapıldı mı?
3. Ürünü değiştirme/etrafından dolaşma (design-around) imkânı var mı?
4. Karşı tarafın hakkı hükümsüzlük açısından kırılgan mı?

## Denetim şeması
1. **Hak envanteri.** İlgili alandaki yürürlükteki patent/faydalı modelleri TPMK ve EPO/Espacenet üzerinden tara; süresi dolmuş/ücreti ödenmemiş/hükümsüz kılınmış hakları ele. Ara sonuç: hangi haklar canlı engel?
2. **Kapsam-ürün eşleştirmesi.** Her canlı hakkın bağımsız istemlerini ürünle karşılaştır (SMK m.89; istem yorumu becerisi). Literal/eşdeğer kapsama giren var mı?
3. **Hükümsüzlük kırılganlığı.** Engel oluşturan haklar için prior art ve açıklama yeterliliği (SMK m.138) açısından zayıflık ara; saldırıda hükümsüzlük davası/def'i seçeneğini hazırla.
4. **Tasarım etrafından dolaşma.** Kapsam içine sokan öğeyi çıkararak/değiştirerek (eşdeğer doğurmadan) ürünü kapsam dışına taşıma imkânını teknik ekiple değerlendir.
5. **Yol ve maliyet kararı.** Lisans almak, design-around, hükümsüzlük saldırısı veya riski göze almak arasında; ihtiyati tedbir, tazminat (SMK m.151) ve itibar riskini birlikte tart. Muhatap isen ihtarnameye cevap ve süre yönetimini planla.

## Çıktı modülleri
- Canlı hak envanteri ve engel skoru.
- İstem-ürün risk haritası (yüksek/orta/düşük).
- Hükümsüzlük kırılganlık notu.
- Strateji önerisi (lisans / design-around / saldırı / bekle) ve gerekçe.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

