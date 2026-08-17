---
argument-hint: ''
description: Kullanıcı dava açma, itiraz, cevap, istinaf gibi sürelerin ne zaman dolacağını
  veya alacağının zamanaşımına uğrayıp uğramadığını hesaplamak istediğinde kullanılır.
name: sureler-ve-zamanasimi
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler ve Zamanaşımı Takibi

## Görev
Hak düşürücü süreleri, usul sürelerini ve zamanaşımını tespit edip takvimlemek; süre kaçırmaktan doğan hak kaybını önlemek.

## Soğuk başlangıç (intake)
- Hakkınız/alacağınız hangi tarihte doğdu?
- Bir tebligat aldıysanız tebliğ tarihi nedir?
- Daha önce dava, icra takibi veya ihtar yaptınız mı (kesilme/durma)?
- Uyuşmazlık sözleşmeden mi, haksız fiilden mi doğuyor?
- Bir karar/heyet kararı tebliğ edildiyse itiraz süresini mi soruyorsunuz?

## Denetim şeması
1. **Zamanaşımı türü:** Genel sözleşme alacaklarında on yıl (TBK m.146); kira bedeli, faiz, ücret gibi dönemsel edimlerde beş yıl (TBK m.147). Haksız fiilde fiil ve failin öğrenilmesinden iki yıl, her halde on yıl (TBK m.72).
2. **Kesilme/durma:** Zamanaşımı; dava açma, icra takibi, alacağın ikrarı gibi sebeplerle kesilir (TBK m.154) ve kesilmeden sonra yeniden işler (m.156). Durma halleri m.153.
3. **Usul süreleri:** Cevap dilekçesi iki hafta (HMK m.127); istinaf süresi kural olarak kararın tebliğinden iki hafta (m.345); temyiz süresi iki hafta (m.361). Sürelerin hesabı HMK m.92-94'e göre yapılır; tebliğ günü sayılmaz, son gün tatile gelirse ertesi iş gününe uzar.
4. **Hak düşürücü süreler:** Bazı haklarda (örn. bazı tüketici/ayıp ihbarı, iptal davaları) süre hak düşürücüdür; re'sen dikkate alınır, kesilmez/durmaz.
5. **Zamanaşımı def'i (TBK m.161):** Hâkim re'sen uygulamaz; davalı açıkça ileri sürmelidir. Bu nedenle davalı için kritik bir savunmadır.
6. **Ara sonuç:** Tür + başlangıç + kesilme/durma + son gün hesabı yapılırsa süre güvenli takvimlenir.

## Çıktı modülleri
- Süre takvimi (her işlem için son tarih ve dayanak madde).
- Zamanaşımı durumu değerlendirmesi (dolmuş/dolmamış, kesildi mi).
- Kritik süre uyarıları ve hatırlatma listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

