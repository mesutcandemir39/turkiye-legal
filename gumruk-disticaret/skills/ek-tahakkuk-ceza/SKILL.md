---
argument-hint: ''
description: Sonradan kontrol veya inceleme sonucu çıkarılan ek tahakkuk ve gümrük
  idari para cezası kararlarının hukuka uygunluğunu denetlemek gerektiğinde; ceza
  tipini, matrahı ve dayanağı madde madde sınamak iç
name: ek-tahakkuk-ceza
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
  - ad: Gümrük Müsait Müşterek Gümrük Bölgeleri Hakkında Kanun
    numara: '4458'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Ek Tahakkuk ve Ceza Kararlarının Denetimi

## Görev
Gümrük idaresinin sonradan kontrol/inceleme sonucu düzenlediği ek tahakkuk ve idari para cezası kararlarını hukuka uygunluk yönünden denetlemek; ceza tipini doğru sınıflandırmak ve indirim/iptal imkânlarını ortaya koymak.

## Soğuk başlangıç (intake)
- Karar hangi tarihte tebliğ edildi; ek tahakkukun ve cezanın tutarı ve dayanağı nedir?
- İhtilaf kıymet, menşe, sınıflandırma yoksa beyana aykırılık ekseninde mi?
- Ceza hangi maddeye dayandırılmış (m.234 vergi farkı, m.235 yasak/kısıtlama, m.241 usulsüzlük)?
- Beyanın düzeltilmesi (m.234/3) veya kendiliğinden bildirim imkânı kullanıldı mı?

## Denetim şeması
1. Karar tipini ayır: Vergi kaybına bağlı ceza için 4458 m.234 (kıymet/menşe/sınıflandırma farkına bağlı, vergi farkının belirli katı). İthalat/ihracatta yasak-kısıtlama ihlalleri için m.235. Şekle/usule aykırılık için m.241 (usulsüzlük cezası). Yanlış maddeye dayanan ceza sakattır.
2. Ek tahakkuk dayanağı: Tahakkuk ettirilmeyen vergiler m.193-197 çerçevesinde sonradan tahakkuk ettirilir. Hesap hatası, çifte tahakkuk veya matrah yanlışlığı denetlenir.
3. İndirim/bertaraf: m.234/3 uyarınca yükümlünün beyanın yanlışlığını idare tespit etmeden önce bildirmesi veya kararın tebliğinden itibaren süresinde ödeme cezada indirim sağlayabilir; m.234/6 (indirimli ödeme) ve uzlaşma (m.244) imkânları değerlendirilir.
4. Geri verme/kaldırma: Kanunen alınmaması gereken vergi alınmışsa m.211 uyarınca geri verme/kaldırma talebi; süre ve usul kontrol edilir.
5. İspat yükü: Cezayı gerektiren maddi olayı (vergi farkı, beyana aykırılık) idare ispatlar; yükümlü beyanının doğruluğunu ve iyi niyetini, hesap hatasını veya ceza şartlarının oluşmadığını ortaya koyar.
6. Ara sonuç: Cezanın tipi, matrahı ve dayanağı doğrulanır; iptal/indirim gerekçeleri ve hangi yolun (itiraz, uzlaşma, dava) öncelikli olduğu belirlenir. İlkesel içtihat için Danıştay 7. ve 9. Daire kararlarına bakılır [DOĞRULANMADI].

## Çıktı modülleri
- Ceza tipi-dayanak-matrah denetim tablosu
- İndirim/uzlaşma/dava karşılaştırmalı strateji notu
- Geri verme-kaldırma başvuru taslağı (uygunsa)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

