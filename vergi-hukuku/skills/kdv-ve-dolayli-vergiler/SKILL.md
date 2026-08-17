---
argument-hint: ''
description: Katma değer vergisinde vergiyi doğuran olay, indirim, iade, tevkifat
  ve sahte belge kaynaklı KDV reddi sorunlarını çözmek; KDV ve dolaylı vergi uyuşmazlıklarında
  kullanılır.
name: kdv-ve-dolayli-vergiler
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
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  - ad: Gelir Vergisi Kanunu
    numara: '193'
    tur: kanun
  - ad: Kurumlar Vergisi Kanunu
    numara: '5520'
    tur: kanun
  - ad: Katma Değer Vergisi Kanunu
    numara: '3065'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# KDV ve Dolaylı Vergiler

## Görev
Katma değer vergisi ve diğer dolaylı vergilerde (ÖTV, damga) verginin doğumu, indirim hakkı, iade süreci ve özellikle SMİYB kaynaklı indirim reddi uyuşmazlıklarını çözmek.

## Soğuk başlangıç (intake)
1. İhtilaf indirim reddi mi, iade reddi mi, tevkifat mı?
2. Sahte/yanıltıcı belge (SMİYB) iddiası var mı; karşıt inceleme yapılmış mı?
3. İade türü nedir (ihracat istisnası, indirimli oran, tevkifat iadesi)?
4. Vergiyi doğuran olayın gerçekleştiği dönem ve teslim/hizmet anı nedir?
5. KDV beyannameleri ve YMM raporu/teminat durumu nedir?

## Denetim şeması
1. **Vergiyi doğuran olay:** KDVK m.10 — teslim, hizmetin yapılması, fatura düzenlenmesi veya kısmi teslim anı. Doğru dönemi tespit et; erken/geç beyan ceza riskidir.
2. **Verginin konusu ve mükellef:** KDVK m.1 (ticari/sınai/zirai/serbest meslek faaliyeti, ithalat), m.8 mükellef, m.9 tevkifat ve sorumlu sıfatı.
3. **İndirim hakkı:** KDVK m.29 — yüklenilen KDV'nin indirimi; m.34 indirimin belgeye ve kayda bağlılığı; m.30 indirilemeyecek KDV (özellikle m.30/d — Gelir/Kurumlar yönünden gider kabul edilmeyen harcamalara ait KDV).
4. **SMİYB kaynaklı ret:** İndirim reddinde idare belgenin sahteliğini somut tespitle (VTR, karşıt inceleme) ortaya koymalı; mükellef gerçek mal/hizmet hareketini (ödeme, sevkiyat, stok) ispatla çürütebilir. VUK m.3/B ekonomik yaklaşım ve VUK m.359 sahte belge ilişkisini ayır.
5. **İstisna ve iade:** KDVK m.11-12 (ihracat istisnası), m.32 (istisna işlemlerde yüklenilen verginin iadesi), indirimli oran iadesi m.29/2. İade için aranan belge ve YMM tasdik şartını kontrol et. Ara sonuç: indirim/iade reddi haklı mı, hangi delille çürütülür?
6. **ÖTV ve damga:** ÖTV'de listeye giren mal ve doğuran olay (ÖTVK 4760); damga vergisinde kâğıt ve nispi/maktu oran (488 sayılı Kanun). İlgili özel vergi için ayrı denetim.

## Çıktı modülleri
- KDV doğum-indirim-iade akış tablosu (dönem bazında).
- SMİYB savunma dosyası (gerçeklik delilleri listesi: ödeme, irsaliye, stok, kapasite).
- İade hak ediş ve eksik belge listesi.
- İhtilaf dilekçesi argüman iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

