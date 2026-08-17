---
argument-hint: ''
description: Başvuru, itiraz, yıllık ücret, dava ve tazminat zamanaşımı sürelerinin
  hesaplanması ve takip edilmesi gerektiğinde kullanılır; hak kaybını önleyen süre
  disiplini için temel beceridir.
name: sure-zamanasimi-takvimi
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


# Süreler ve Zamanaşımı

## Görev
Patent/faydalı model sürecindeki idari süreleri (başvuru, rüçhan, itiraz, ücret) ve dava/tazminat zamanaşımı sürelerini eksiksiz çıkarmak; hak düşürücü ve telafi edilebilir süreleri ayırmak.

## Soğuk başlangıç (intake)
1. Hangi aşamadasın: başvuru, inceleme, itiraz, tescil sonrası, dava?
2. Başvuru/rüçhan/yayım/tescil tarihleri ne?
3. Yıllık ücretler güncel mi; kaçırılan ödeme var mı?
4. Tecavüz/tazminat talebi varsa fiil ne zaman öğrenildi ve gerçekleşti?

## Denetim şeması
1. **Koruma süreleri.** Patent 20 yıl (SMK m.101), faydalı model 10 yıl; süreler başvuru tarihinden işler ve uzatılamaz. Ara sonuç: koruma hangi tarihte sona eriyor?
2. **Rüçhan süresi (SMK m.93).** Paris/PCT rüçhanı ilk başvurudan 12 ay; bu süre yenilik referans tarihini belirler ve kaçırılması telafisi güç hak kaybı doğurur.
3. **İtiraz süresi (SMK m.99).** Patent verme kararının yayımından itibaren altı ay içinde itiraz; YİDD kararına karşı iptal davası süresi (kararın tebliğinden itibaren) kanunda öngörülen süredir — kaçırılırsa idari karar kesinleşir.
4. **Yıllık ücretler (SMK m.101).** Koruma yıllık ücretin süresinde ödenmesine bağlıdır; ödenmeyen yıl için ek süre/cezalı ödeme imkânını ve hakkın düşmesini kontrol et.
5. **Tecavüz/tazminat zamanaşımı (SMK m.157).** SMK m.157, sınai mülkiyet hakkına tecavüzden doğan tazminat istemlerinde TBK m.72 zamanaşımına atıf yapar: zararı ve faili öğrenmeden itibaren iki yıl ve her halde fiilden itibaren on yıl; fiil aynı zamanda suç oluşturup ceza zamanaşımı daha uzunsa o süre uygulanır. Sürekli/yenilenen tecavüzde zamanaşımının her fiil için yeniden işlemesini değerlendir.

## Çıktı modülleri
- Aşamaya göre süre tablosu (başlangıç-bitiş-sonuç).
- Hak düşürücü / telafi edilebilir süre ayrımı.
- Yıllık ücret ödeme takvimi.
- Zamanaşımı hesabı ve uyarı notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

