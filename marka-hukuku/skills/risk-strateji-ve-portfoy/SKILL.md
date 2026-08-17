---
argument-hint: ''
description: Tescil öncesi clearance, dava açma/açmama kararı, sulh ihtimali veya
  marka portföyü yönetimi gerekiyorsa; uyuşmazlık ve tescil risklerini tartıp strateji
  kurmak için kullanılır.
name: risk-strateji-ve-portfoy
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


# Risk Değerlendirme, Strateji ve Marka Portföyü

## Görev
Müvekkilin marka kararlarını risk-fayda ekseninde yönlendirmek: tescil öncesi clearance (önaraştırma), itiraz/dava açma-açmama, sulh, portföy genişletme ve sınıf stratejisi. Hukuki teşhisi ticari sonuçla birleştirip uygulanabilir bir yol haritası vermek.

## Soğuk başlangıç (intake)
- Hedef nedir: yeni marka tescili, mevcut hakkın savunması, rakibe karşı saldırı?
- Bütçe, zaman baskısı ve markanın ticari önceliği ne?
- Karşı tarafın gücü, tescil durumu ve uzlaşma eğilimi nedir?
- Coğrafi kapsam (yalnız Türkiye mi, yurt dışı/Madrid Protokolü mü)?

## Denetim şeması
1. **Clearance (önaraştırma).** Sicil ve piyasa taraması; aynı/benzer önceki marka, tanınmış marka, alan adı/ticaret unvanı çakışması. m.5-6 ret riski erken ölçülür.
2. **Dava/itiraz olasılık analizi.** Karıştırılma ihtimali, kullanmama def'i ihtimali (m.19/2), tanınmışlık, kötüniyet delili — kazanma ihtimali ve maliyet karşılaştırılır.
3. **Süre ve usul riski.** İtiraz 2 ay, YİDK dava 2 ay, kullanmama 5 yıl, tazminat zamanaşımı 2/10 yıl — kaçan süre stratejiyi sınırlar.
4. **Alternatif yollar.** İhtarname, sulh/koexistence (birlikte var olma) sözleşmesi, sınıf/coğrafya daraltma, marka değiştirme (rebrand) maliyeti tartılır.
5. **Portföy ve genişleme.** Çekirdek markaların hangi sınıflarda tescil edileceği; savunma tescilleri; yurt dışı için Madrid Protokolü; yenileme takvimi (10 yıllık koruma, m.23) ve kullanmama riskinin yönetimi.
6. **Karar.** Beklenen değer + ticari öncelik + zaman ekseninde net tavsiye (aç/açma/sulh ol/rebrand) ve gerekçesi.

## Çıktı modülleri
- Clearance risk skor tablosu (sınıf bazlı çakışma).
- Senaryo karşılaştırması (dava / sulh / rebrand — maliyet, süre, sonuç).
- Portföy ve yenileme takvimi; tavsiye ve gerekçe notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

