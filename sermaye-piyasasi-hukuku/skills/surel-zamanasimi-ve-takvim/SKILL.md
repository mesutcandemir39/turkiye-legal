---
argument-hint: ''
description: Sermaye piyasası uyuşmazlıklarında dava açma süreleri, idari yaptırım
  ve suçlarda zamanaşımı, izahname/kamuyu aydınlatma sorumluluğunda zamanaşımı ve
  hak düşürücü sürelerin hesaplanması gerektiğinde k
name: surel-zamanasimi-ve-takvim
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
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler, Zamanaşımı ve Takvim

## Görev
Dosyadaki tüm süreleri (dava açma, zamanaşımı, hak düşürücü) ilgili norma göre hesaplamak; başlangıç anı, durma/kesilme ve son günü belgelemek.

## Soğuk başlangıç (intake)
- Talep türü nedir: idari yaptırıma iptal, tazminat, cezai sorumluluk mu?
- Tetikleyici olay ve öğrenme/tebliğ tarihi nedir?
- Süreyi durduran/kesen işlem (başvuru, dava, Kurul kararı) var mı?
- Birden çok eksen (idari + adli) varsa her biri için ayrı takvim gerekiyor mu?

## Denetim şeması
1. **Eksen ayrımı:** İdari yaptırıma iptal süresi İYUK'a; izahname/kamuyu aydınlatma tazminatı SPK m.10/m.32 ve TBK'ya; piyasa suçlarında dava zamanaşımı TCK'ya tabidir. Her eksen ayrı hesaplanır.
2. **İptal davası süresi:** İYUK m.7 uyarınca kararın tebliğinden itibaren işleyen dava açma süresi; üst makama/Kurul'a başvuru (İYUK m.11) süreyi durdurabilir. Hak düşürücüdür, re'sen dikkate alınır.
3. **Tazminat zamanaşımı:** İzahname/kamuyu aydınlatma sorumluluğunda SPK özel hükmü ile TBK m.72 (haksız fiilde öğrenmeden 2, her hâlde 10 yıl) birlikte değerlendirilir; sözleşmesel sorumlulukta TBK m.146 (10 yıl) esas alınır.
4. **Ceza zamanaşımı:** Piyasa suçlarında (SPK m.106-107) dava zamanaşımı, suçun cezası üzerinden TCK m.66'ya göre belirlenir; Kurul mütalaası şartı (m.115) süreçle birlikte not edilir.
5. **Takvim kurma:** Başlangıç anı, durma/kesilme sebepleri ve son gün tarih olarak yazılır; ara sonuç olarak en yakın kritik tarih öne çıkarılır. Tatil/adli tatil etkisi kontrol edilir.

## Çıktı modülleri
- Eksen bazlı süre tablosu (başlangıç-durma-son gün)
- Kritik tarih uyarı listesi
- Zamanaşımı/hak düşürücü ayrımı notu
- Sonraki adım ve hatırlatma planı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

