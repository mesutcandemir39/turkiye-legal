---
argument-hint: ''
description: Hukuki değerlendirmeden çıkan riskleri olasılık ve etki ekseninde haritalandırıp
  somut, sıralı eylem önerileri üretmek gerektiğinde kullanılır; mütalaayı uygulanabilir
  kılan bölümdür.
name: risk-haritasi-ve-eylem-onerisi
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Risk Haritası ve Eylem Önerisi

## Görev
Hukuki değerlendirmenin ortaya çıkardığı riskleri yapılandırmak (hukuki, mali, itibari, süre riski) ve müvekkilin atması gereken somut adımları öncelik sırasıyla önermek. Mütalaa burada teoriden eyleme döner.

## Soğuk başlangıç (intake)
- Müvekkil davacı/talep eden mi, savunan mı?
- Yaklaşan bir süre, zamanaşımı veya hak düşürücü süre var mı?
- Mali maruziyetin büyüklüğü (asıl alacak + faiz + yargılama gideri + vekâlet ücreti) tahmini ne?
- Müvekkilin risk iştahı ve önceliği ne?

## Denetim şeması
1. Risk envanteri: Her hukuki sorundan doğan risk ayrı yazılır — esasa ilişkin (talep haklı çıkmaması), usule ilişkin (görev/yetki/dava şartı eksikliği), ispata ilişkin (delil yetersizliği), süreye ilişkin (zamanaşımı/hak düşürücü süre).
2. Olasılık × etki ekseni: Her risk düşük/orta/yüksek olasılık ve düşük/orta/yüksek etki ile derecelendirilir; kritik bölge (yüksek-yüksek) öne çıkarılır.
3. Süre kritikliği: Yaklaşan zamanaşımı/hak düşürücü süre veya dava açma süresi (örn. İYUK m.7 iptal davasında genel altmış gün; işe iadede İş K. m.20 bir aylık başvuru) en üst öncelikli uyarı olarak işaretlenir.
4. Mali maruziyet tahmini: Kazanma/kaybetme senaryolarında yargılama gideri ve karşı vekâlet ücreti riski dahil edilir.
5. Eylem önerileri: Somut, sıralı ve sorumlulu — "ihtarname çek / dava şartı arabuluculuğa başvur / delil tespiti iste / şu belgeyi temin et / şu süre içinde başvur". Her öneri bir riski azaltmaya bağlanır.
6. Ara sonuç: Risk matrisi + kritik süre uyarısı + numaralı eylem planı.

## Çıktı modülleri
- Risk matrisi (risk | olasılık | etki | azaltıcı tedbir)
- Kritik süre/zamanaşımı uyarı kutusu
- Mali maruziyet senaryoları (kazanma/kaybetme)
- Öncelik sıralı eylem planı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

