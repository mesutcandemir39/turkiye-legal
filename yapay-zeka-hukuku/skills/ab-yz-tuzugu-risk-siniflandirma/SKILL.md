---
argument-hint: ''
description: Müvekkilin yapay zekâ sistemi AB pazarına ürün veya hizmet sunduğunda
  ya da karşılaştırmalı uyum hedeflendiğinde AB Yapay Zekâ Tüzüğü kapsamında yasak/yüksek
  riskli/sınırlı risk sınıflandırması ve yük
name: ab-yz-tuzugu-risk-siniflandirma
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# AB Yapay Zekâ Tüzüğü ve Risk Sınıflandırması

## Görev
Bir yapay zekâ sisteminin AB Yapay Zekâ Tüzüğü (Regulation (EU) 2024/1689) kapsamında risk sınıfını belirlemek ve buna bağlı yükümlülükleri tespit etmek; Türkiye için bunun bağlayıcı değil karşılaştırmalı/sözleşmesel bir referans olduğunu netleştirmek.

## Soğuk başlangıç (intake)
1. Sistem AB'deki kullanıcılara/pazara sunuluyor mu, çıktısı AB'de kullanılıyor mu?
2. Müvekkilin rolü: sağlayıcı (provider), uygulayıcı (deployer), ithalatçı, dağıtıcı?
3. Sistem ne yapıyor: biyometrik tanıma, kredi/işe alım skorlama, kritik altyapı, genel amaçlı model (GPAI)?
4. Mevcut uyum belgeleri (teknik dokümantasyon, uygunluk değerlendirmesi) var mı?

## Denetim şeması
1. **Uygulanabilirlik**: Tüzük Türkiye'de doğrudan yürürlükte değildir. AB'ye ürün/hizmet sunuluyorsa ülke-dışı etki nedeniyle uygulanabilir; yalnız Türkiye içiyse yön gösterici/sözleşmesel referanstır. Ara sonuç: bağlayıcı mı, referans mı.
2. **Risk sınıfı**: (a) Yasak uygulamalar (ör. sosyal puanlama, manipülatif sistemler); (b) Yüksek riskli sistemler (biyometri, eğitim, istihdam, kredi, kamu hizmeti, kritik altyapı) — uygunluk değerlendirmesi, risk yönetimi, veri yönetişimi, insan gözetimi, kayıt tutma yükümlülükleri; (c) Sınırlı risk — şeffaflık (örn. sohbet botu/derin sahte etiketleme); (d) Asgari risk.
3. **GPAI/temel model**: Genel amaçlı modeller için teknik dokümantasyon, telif uyum politikası ve sistemik risk eşiği yükümlülükleri.
4. **Rol bazlı yükümlülük**: Sağlayıcı ve uygulayıcı için farklı görevler; sözleşmeyle rollerin ve sorumlulukların netleştirilmesi gerekir.
5. **Türkiye'ye yansıma**: Tüzük yükümlülükleri Türk müvekkiline ancak sözleşme veya AB'ye erişim üzerinden gelir; Türkiye'de paralel uyum çoğu zaman KVKK + sektörel mevzuatla sağlanır.

Tüzük metni ve yürürlük takvimi sık güncellenir; her atıfta resmî AB kaynağından versiyon kontrol et, künyeyi [DOĞRULANMADI] işaretle.

## Çıktı modülleri
- Risk sınıflandırma sonucu ve gerekçesi.
- Rol bazlı yükümlülük tablosu.
- Türkiye-AB uyum köprüsü ve sözleşmesel aktarım önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

