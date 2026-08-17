---
argument-hint: ''
description: Sosyal güvenlik uyuşmazlığında hangi delilin neyi ispatladığı, SGK kayıtları,
  bordro, tanık ve bilirkişi raporunun değeri ile re'sen araştırma ilkesinin uygulanması
  gerektiğinde kullanılır.
name: ispat-ve-delil
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
  - ad: Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu
    numara: '5510'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İspat ve Delil Yönetimi

## Görev
Uyuşmazlık türüne göre ispat yükünü dağıtmak, mevcut ve getirtilebilecek delilleri değerlendirmek ve delil stratejisini kurmak.

## Soğuk başlangıç (intake)
- İspatlanması gereken vakıa ne (çalışma olgusu, kazanç miktarı, kusur, maluliyet)?
- Elde hangi belgeler var (hizmet dökümü, bordro, işe giriş bildirgesi, sağlık raporu)?
- Tanık var mı; bordro tanığı mı komşu işyeri tanığı mı?
- Bilirkişi/sağlık kurulu raporu gerekiyor mu?

## Denetim şeması
1. İspat yükü — TMK m.6 ve özel kurallar: Kural olarak iddia eden ispatla yükümlü; ancak hizmet tespiti gibi kamu düzenine ilişkin davalarda hâkim re'sen araştırma yapar (HMK genel ilkeleriyle birlikte).
2. Resmi/yazılı delil önceliği: SGK hizmet dökümü, işyeri sicil dosyası, dönem bordroları, işe giriş bildirgesi, müfettiş raporu; bunlar aksi ispatlanana dek güçlü karinedir.
3. Tanık delili: Çalışma olgusunun ispatında bordro tanıkları (aynı dönem aynı işyerinde bildirilmiş kişiler) önceliklidir; salt komşu işyeri tanığıyla sonuç güçlü destekleyici delil gerektirir.
4. Bilirkişi/sağlık kurulu: Kusur oranı, maluliyet derecesi, prim/PEK hesabı bilirkişi ve Kurum sağlık kurulu/ATK raporlarıyla saptanır; rapora itiraz ve ek rapor talebi disiplinli yürütülür.
5. Çelişki yönetimi: Belge ile tanık, raporlar arası çelişkiler işaretlenir; gerekirse yeniden inceleme istenir. Ara sonuç: her vakıa için delil eşleşmesi ve eksik delil listesi.

## Çıktı modülleri
- Vakıa-delil eşleştirme matrisi.
- Getirtilecek belge ve tanık listesi.
- Bilirkişi/sağlık kurulu raporuna itiraz noktaları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

