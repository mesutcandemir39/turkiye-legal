---
argument-hint: ''
description: Gelir unsurlarının tespiti, matrah belirleme, gider-istisna-indirim denetimi
  ve örtülü kazanç/sermaye sorunlarını çözmek; GVK ve KVK matrah uyuşmazlıklarında
  kullanılır.
name: gelir-kurumlar-vergisi
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


# Gelir ve Kurumlar Vergisi Uygulaması

## Görev
Gerçek kişi ya da kurum kazancının vergilendirilmesinde gelir unsurunu, matrahı, indirilebilir giderleri ve istisnaları doğru tespit ederek matrah uyuşmazlığını çözmek veya planlamayı yönlendirmek.

## Soğuk başlangıç (intake)
1. Mükellef gerçek kişi mi (GVK) yoksa kurum mu (KVK)?
2. Gelir hangi unsurdan (ticari, zirai, ücret, serbest meslek, GMSİ, MSİ, diğer kazanç)?
3. Tam mükellef mi, dar mükellef mi; çifte vergilendirme anlaşması var mı?
4. İhtilaf gider reddi, istisna, transfer fiyatlandırması veya örtülü dağıtım mı?
5. İlgili dönem ve beyan durumu nedir?

## Denetim şeması
1. **Gelir unsuru tespiti:** GVK m.2 — yedi gelir unsuru sınırlı sayıdadır; unsura giren kazanç farklı kural ve istisnalara tabidir. Önce hangi unsur olduğunu sabitle.
2. **Ticari kazançta gerçek/basit usul:** GVK m.37 vd.; kurumlarda kazanç KVK m.6 uyarınca GVK ticari kazanç hükümlerine göre tespit edilir (mali kâr = ticari kâr ± kanunen kabul edilmeyen giderler ± istisnalar).
3. **Gider denetimi:** GVK m.40 (indirilebilecek giderler) ile KKEG ayrımı; GVK m.41 ve KVK m.11 (kabul edilmeyen indirimler). Giderin işle illiyeti ve belgelendirilmesi (VUK m.227, m.229) aranır.
4. **İstisna/indirim:** KVK m.5 (iştirak kazançları, taşınmaz/iştirak satış istisnası), KVK m.10 indirimler; GVK istisnaları. İstisna iddiasının ispatı mükelleftedir.
5. **Örtülü sermaye ve örtülü kazanç:** KVK m.12 (örtülü sermaye — borç/özkaynak oranı), KVK m.13 (transfer fiyatlandırması yoluyla örtülü kazanç dağıtımı — emsallere uygunluk). İlişkili kişi ve emsal analizi yap. Ara sonuç: matrah farkı hangi kalemden ve hangi tutarda?
6. **Stopaj ilişkisi:** Bazı ödemelerde GVK m.94 / KVK m.15, m.30 tevkifatı; sorumlu sıfatıyla ödeme yükümlülüğünü kontrol et.

## Çıktı modülleri
- Gelir unsuru ve matrah hesap tablosu (ticari kâr → mali kâr köprüsü).
- Gider/istisna kabul-ret listesi (madde dayanağı ve belge durumu).
- Transfer fiyatlandırması/örtülü sermaye risk notu.
- Beyan düzeltme veya dava argümanı taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

