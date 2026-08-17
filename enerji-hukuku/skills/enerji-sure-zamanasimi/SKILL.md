---
argument-hint: ''
description: Lisans yükümlülük süreleri, EPDK dava açma süresi, YEKDEM kayıt son tarihleri,
  sözleşmesel ve idari para cezası zamanaşımı gibi tüm süre hesapları yapılırken kullanılır.
name: enerji-sure-zamanasimi
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
  - ad: Elektrik Piyasası Kanunu
    numara: '6446'
    tur: kanun
  - ad: Mühendislik ve Mimarlık Meslek Kanunu
    numara: '4646'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Enerji Hukukunda Süreler ve Zamanaşımı

## Görev
Bir enerji dosyasındaki tüm süreleri tek tabloda toplamak; hak düşürücü süre, dava süresi ve zamanaşımını ayırarak süre kaçırma riskini ortadan kaldırmak.

## Soğuk başlangıç (intake)
1. Hangi işlem/olay için süre soruluyor (lisans yükümlülüğü, EPDK işlemi, alacak, ceza)?
2. Başlangıç tarihi nedir (tebliğ, öğrenme, ifa, işletmeye giriş)?
3. Süreyi durduran/keser bir başvuru/işlem yapıldı mı?
4. Olay tarihindeki yürürlük hali hangisi?

## Denetim şeması
1. **İdari dava süresi**: EPDK işlemlerine karşı İYUK m.7 — kural 60 gün; özel kanunda farklı süre varsa o uygulanır. İdari başvuru (İYUK m.11) süreyi durdurur; başvurunun reddi/zımni ret ile yeniden işler.
2. **Lisans/önlisans yükümlülük süreleri**: 6446 m.7 önlisans süresi ve Lisans Yönetmeliğindeki tamamlanma/inşa süreleri hak düşürücü niteliktedir; mücbir sebep uzatımı belgeyle aranır.
3. **YEKDEM ve uzlaştırma**: YEKDEM kayıt ve dönemsel beyan son tarihleri kaçırılırsa o dönem destek dışı kalınır; bu süreler hak kaybı doğurur, durmaz.
4. **İdari para cezası zamanaşımı**: Kabahatler bakımından 5326 s.K. soruşturma/yerine getirme zamanaşımı; 6446/4646 özel hükmü varsa öncelikli.
5. **Sözleşmesel zamanaşımı**: TBK m.146 genel 10 yıl, m.147 bazı alacaklarda 5 yıl; haksız fiilde TBK m.72; tüketici işlemlerinde 6502 özel süreleri. Faiz ve uzlaştırma alacaklarında tür ayrımı yapılır.

Tüm süreler başlangıç tarihi + dayanak madde + hak düşürücü/zamanaşımı ayrımı ile yazılır; tereddütte en kısa süreye göre hareket edilir.

## Çıktı modülleri
- Konsolide süre takvimi tablosu (olay/dayanak/son gün).
- Durma-kesilme notları.
- Kritik süre uyarı listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

