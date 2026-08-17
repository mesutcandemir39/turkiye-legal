---
argument-hint: ''
description: Girişimin çıkış senaryoları (satış, ikincil pay devri, halka arz) planlanırken
  veya işlemin rekabet izni eşiği, vergi ve teşvik (TGB, Ar-Ge, melek yatırımcı, kurumlar)
  boyutu değerlendirilirken kullan
name: cikis-exit-rekabet-vergi
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Çıkış (Exit), Rekabet İzni ve Vergi-Teşvik

## Görev
Çıkış yolunu ve onun düzenleyici/vergisel sonuçlarını planlamak: stratejik satış, ikincil pay devri (secondary) veya halka arz; rekabet izni eşiği ve vergi/teşvik optimizasyonu.

## Soğuk başlangıç (intake)
1. Çıkış tipi: tüm/çoğunluk satışı, ikincil pay satışı, halka arz?
2. Devredilen kontrol/pay oranı ve işlem büyüklüğü ne (rekabet eşiği için)?
3. Satıcı gerçek kişi mi, kurum mu (vergi rejimi farklı)?
4. Şirket TGB/Ar-Ge teşviklerinden yararlanıyor mu; çıkış bunları etkiler mi?
5. SHA'daki drag/tag/önalım çıkışta nasıl işleyecek?

## Denetim şeması
1. Rekabet izni: Devralma kontrol değişikliği yaratıyor ve ciro eşikleri aşılıyorsa Rekabet Kurulu izni gerekir (4054 m.7 ve 2010/4 sayılı Tebliğ eşikleri). İzinsiz kapanış geçersizlik/idari para cezası riski; eşikleri güncel tebliğden teyit et. Erken aşamada genellikle eşik altıdır.
2. SHA çıkış hükümleri: Drag-along ile çoğunluk azınlığı satışa sürükler; tag-along ile azınlık katılır; önalım hakları işletilir. Bunlar taraflar arası borç (TBK); ayni engel için esas sözleşmesel bağlam.
3. Vergi — gerçek kişi: Pay/iştirak hissesi satış kazancında GVK değer artışı kazancı kuralları; anonim şirket hisse senedi (bastırılmış) için iki yıllık elde tutma istisnası gibi koşullar — güncel GVK metninden teyit et.
4. Vergi — kurum: İştirak hissesi satış kazancı istisnası (KVK m.5/1-e: belirli oran ve süre şartıyla) ve emisyon primi istisnası; şartları (elde tutma süresi, fon hesabı) güncel 5520 metninden teyit et.
5. Teşvik etkisi: TGB istisnası (4691) ve Ar-Ge (5746) faaliyet şartına bağlıdır; ortaklık değişimi kural olarak teşviki sonlandırmaz ama faaliyet/bölge şartının sürmesi denetlenmeli. Melek yatırımcı (BKY) indirimi GVK mük. m.82 koşulları.
6. Halka arz: SPK rejimi (6362) — izahname, kamuyu aydınlatma; ayrı uzmanlık alanı, ilgili beceriye yönlendir.
7. İspat/şekil: İşlem belgeleri, kurumsal kararlar, gerekiyorsa Rekabet Kurulu başvurusu; vergi pozisyonu için mali müşavir teyidi.

## Çıktı modülleri
- Çıkış senaryosu ve adım planı (drag/tag/önalım işleyişi).
- Rekabet izni gereklilik testi (eşik kontrol notu).
- Vergi/teşvik etki analizi ve doğrulama listesi (oran/süreler [doldurulacak]).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

