---
argument-hint: ''
description: Ürün ve coğrafi pazarın sınırlarını, pazar paylarını ve yoğunlaşmayı
  belirlemek, hâkimlik veya yoğunlaşma analizinin iktisadi altyapısını kurmak istendiğinde
  kullanılır; her rekabet analizinin ön koşu
name: ilgili-pazar-tanimi
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
  - ad: Rekabetin Korunması Hakkında Kanun
    numara: '4054'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İlgili Pazar Tanımı ve Pazar Gücü Analizi

## Görev
İlgili Pazarın Tanımlanmasına İlişkin Kılavuz uyarınca ürün ve coğrafi pazarı tanımlamak, pazar paylarını ve yoğunlaşmayı (HHI) hesaplayarak m.4/m.6/m.7 analizinin iktisadi temelini oluşturmak.

## Soğuk başlangıç (intake)
- İncelenen mal/hizmet ve onun makul ikameleri neler?
- Müşteriler hangi coğrafi alanda tedarik seçeneklerine sahip; nakliye/düzenleme engeli var mı?
- Taraf ve rakip satış/üretim rakamları (ciro/hacim) mevcut mu?
- Analiz hangi amaca hizmet ediyor (hâkimlik, yoğunlaşma, muafiyet)?

## Denetim şeması
1. **Ürün pazarı** — talep ikamesi esas alınır: SSNIP mantığıyla, fiyatta küçük ama kalıcı artış karşısında müşterilerin başka ürüne geçip geçmeyeceği sorgulanır. Arz ikamesi (üreticinin hızla o ürünü sunabilmesi) destekleyici ölçüttür. Ürün özellikleri, kullanım amacı, fiyat seviyesi dikkate alınır.
2. **Coğrafi pazar** — rekabet koşullarının yeterince türdeş olduğu alan; nakliye maliyetleri, mevzuat/lisans engelleri, tüketici tercihleri, ithalat olanakları değerlendirilir.
3. **Pazar payı hesabı** — ciro veya hacim üzerinden; tanımın darlığı/genişliği payı doğrudan etkiler. Bu nedenle taraflar pazar tanımını stratejik kullanır.
4. **Yoğunlaşma (HHI)** — teşebbüslerin pay karelerinin toplamı; yoğunlaşma düzeyi ve işlem sonrası artış (delta) ön eleme sağlar. Yüksek HHI ve büyük delta endişe işaretidir.
5. **Giriş engelleri ve dengeleyici güç** — yasal engeller, batık maliyet, ağ etkileri, ölçek; alıcı gücü ve potansiyel rekabet sonucu yumuşatır.
6. **Ara sonuç** — birden çok makul pazar tanımı varsa hepsi üzerinden analiz yapılır (en muhafazakâr senaryo dâhil); ispat ve veri kaynağı her pay için belirtilir.

## Çıktı modülleri
- Ürün ve coğrafi pazar tanımı gerekçesi.
- Pazar payı tablosu ve HHI hesabı (kaynaklı).
- Giriş engeli ve dengeleyici güç değerlendirmesi.
- Pazar tanımına dair zayıf noktalar ve karşı argüman riskleri.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

