---
argument-hint: ''
description: Toplu is hukukundaki usuli sureleri (yetki itirazi, cagri, gorusme, grev
  bildirimi) ve sendikal tazminat ile TIS alacaklarinda zamanasimini hesaplar; herhangi
  bir surenin kacirilmamasi veya zamanasimi
name: surelerin-ve-zamanasimi-yonetimi
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
  - ad: Sendikalar ve Toplu İş Sözleşmesi Kanunu
    numara: '6356'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler, Hak Düşürücü Süreler ve Zamanaşımı

## Görev
Toplu iş hukukundaki kritik usuli süreleri ve zamanaşımını tek yerde toplayıp somut tarihlere bağlamak. Süre kaçırmak yetkiyi, davayı veya alacağı doğrudan düşürür.

## Soğuk başlangıç (intake)
- Hangi tetikleyici işlem oldu (yetki tespiti tebliği, çağrı, uyuşmazlık tutanağı, fesih)?
- İşlemin tebliğ/öğrenme tarihi tam olarak nedir?
- Talep edilen şey: yetki itirazı mı, sendikal tazminat mı, TİS alacağı mı?
- Süre durduran/kesen bir işlem var mı?

## Denetim şeması
1. **Yetki süreçleri:** Yetki tespitine itiraz **6 işgünü** (6356 m.43). Toplu görüşmeye çağrı **15 gün** (m.46), çağrıdan ilk toplantıya **30 gün** (m.46), toplu görüşme süresi **60 gün** (m.47).
2. **Grev/lokavt:** Uyuşmazlık tutanağının/arabuluculuk tutanağının tebliğinden itibaren grev kararı **60 gün** içinde alınmalı; uygulamadan **6 işgünü** önce bildirim (m.60). Süreler kaçırılırsa yetki düşer.
3. **Sendikal tazminat:** Sendikal tazminat talebinde, fesihle bağlantılı ise iş güvencesi başvuru süreleri (4857 m.20 — feshin tebliğinden itibaren bir aylık dava/arabuluculuk süresi) ile birlikte değerlendirilir; bağımsız sendikal tazminat talebinde genel zamanaşımı tartışılır (künye/uygulama için Yargıtay kararı `[DOĞRULANMADI]`).
4. **TİS'ten doğan alacaklar:** TİS'in normatif hükümlerinden doğan ücret/ikramiye türü alacaklarda iş hukuku zamanaşımı rejimi (ücret alacakları 5 yıl — TBK m.147; kıdem/ihbar gibi tazminat alacaklarında 7036 sayılı Kanun ek/geçici düzenlemeleri ile 5 yıl) gözetilir.
5. **Ara sonuç:** Her tetikleyici için son gün hesaplanır; işgünü/takvim günü ayrımına dikkat edilir (yetki itirazı işgünü, görüşme süresi takvim günü).

İspat: tebliğ mazbatası, tutanak tarihi ve PTT/UYAP kayıtları esastır.

## Çıktı modülleri
- Süre takvimi tablosu (tetikleyici – süre türü – son gün).
- Zamanaşımı/hak düşürücü süre risk notu.
- Hatırlatma/kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

