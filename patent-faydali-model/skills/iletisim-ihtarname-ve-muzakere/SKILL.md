---
argument-hint: ''
description: Patent uyuşmazlığında ihtarname gönderilirken/yanıtlanırken, lisans veya
  sulh müzakeresi yürütülürken ve müvekkile risk anlatılırken kullanılır; dava öncesi
  iletişim ve uzlaşma yönetimi için temel bec
name: iletisim-ihtarname-ve-muzakere
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


# İhtarname, Müzakere ve Taraf İletişimi

## Görev
Patent/faydalı model uyuşmazlığında ihtarname üretmek/yanıtlamak, lisans veya sulh müzakeresini kurgulamak ve müvekkili risk ile seçenekler konusunda doğru bilgilendirmek.

## Soğuk başlangıç (intake)
1. İletişimin amacı ne: tecavüzü durdurma talebi, lisans teklifi, sulh, ihtarnameye cevap?
2. Hakkın geçerliliği ve kapsamı ne kadar sağlam; karşı taraf hükümsüzlük ileri sürebilir mi?
3. Karşı tarafın ticari konumu, iyiniyeti ve müzakereye yatkınlığı ne?
4. Süre/zamanaşımı baskısı ve delil tespiti ihtiyacı var mı?

## Denetim şeması
1. **İhtarnamenin amacı ve içeriği.** Tecavüz iddiasını dayandığı patenti, istem(leri) ve fiili somut belirten, durdurma/giderme ve tazminat talebini içeren; makul süre tanıyan ihtarname kur. Aşırı/dayanaksız tehdit, karşı tarafın menfi tespit davası açma veya haksız rekabet iddiası riskini doğurabilir — bu yüzden iddiayı kapsam analizine yasla.
2. **İspat ve delil hazırlığı.** İhtardan önce/sonra delil tespiti (HMK m.400 vd.) ve numune temini ile fiili durumu sabitle; ihtarname ileride kötüniyet/tazminat başlangıcı bakımından önem taşır.
3. **İhtarnameye cevap.** Muhatap isen: hakkın geçerliliği, kapsam dışılık, önceki kullanım (SMK m.87), tüketilme (SMK m.152) gibi savunmaları değerlendir; süreyi yönet, gerekirse menfi tespit davasını planla.
4. **Müzakere çerçevesi.** Lisans (kapsam, bedel, alan), sulh (geçmiş kullanım + ileriye dönük lisans), stok eritme, design-around taahhüdü seçeneklerini masaya koy; BATNA olarak dava ve ihtiyati tedbir senaryosunu hesapla.
5. **Müvekkil bilgilendirmesi.** Hakkın gücü, hükümsüzlük riski, maliyet ve süre konusunda gerçekçi tablo sun; karar müvekkilindir, hukuki seçenekleri ve olası sonuçlarını yalın anlat.

## Çıktı modülleri
- İhtarname taslağı iskeleti (dayanak istem + fiil + talep + süre) [doldurulacak yer tutucularıyla].
- İhtarnameye cevap savunma envanteri.
- Müzakere seçenek matrisi (lisans/sulh/design-around) ve BATNA.
- Müvekkil bilgilendirme notu (risk-maliyet-seçenek).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

