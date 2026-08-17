---
argument-hint: ''
description: Bir işyerinin 6331 sayılı Kanun kapsamındaki önleme, organizasyon, eğitim
  ve dokümantasyon yükümlülüklerine uyumunu denetlemek ve uyum boşluklarını çıkarmak
  için kullanılır.
name: isveren-yukumlulukleri-uyum
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
  - ad: İş Sağlığı ve Güvenliği Kanunu
    numara: '6331'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İşveren Yükümlülükleri ve Uyum Denetimi

## Görev
İşverenin 6331 m.4 vd. yükümlülüklerine uyumunu sistematik olarak denetlemek; eksikleri, idari ceza riskini ve düzeltici eylemleri raporlamak. Hem proaktif uyum hem de kaza sonrası savunma için temel oluşturur.

## Soğuk başlangıç (intake)
- Tehlike sınıfı ve çalışan sayısı; işyeri tek mi, çok lokasyonlu mu?
- İş güvenliği uzmanı/işyeri hekimi hizmeti var mı (kendi bünyesi mi, OSGB mi)?
- Risk değerlendirmesi, acil durum planı, eğitim ve muayene kayıtları mevcut ve güncel mi?
- Alt işveren/geçici iş ilişkisi var mı?

## Denetim şeması
1. **Genel yükümlülük (m.4):** İşveren mesleki risklerin önlenmesi, eğitim ve bilgilendirme, organizasyon ve gerekli araç-gereci sağlamakla yükümlü; risklerden kaçınma, kaynağında önleme, ikame ve toplu korumaya öncelik ilkeleri (m.5) altlanır.
2. **İSG organizasyonu (m.6-8):** Tehlike sınıfı ve çalışan sayısına göre iş güvenliği uzmanı ve işyeri hekimi görevlendirme zorunluluğu; bunların görev, yetki ve süreleri.
3. **Risk değerlendirmesi (m.10):** Yapılmış mı, güncel mi, kaza/değişiklik sonrası yenilenmiş mi? Yokluğu ağır ihlaldir.
4. **Acil durumlar (m.11-12):** Acil durum planı, yangın/tahliye, ilkyardım, destek elemanı atamaları.
5. **Bilgilendirme/eğitim/gözetim (m.16-17, m.15):** İşe giriş ve periyodik muayeneler, belgelendirilmiş İSG eğitimleri, çalışana risk bilgisi.
6. **Katılım yapıları (m.18, m.20, m.22):** Çalışan görüşü, çalışan temsilcisi, 50+ çalışanlı işyerinde İSG kurulu.
7. **İspat yükü:** Uyumun ve önlemlerin ispatı işverende; her yükümlülük için tarih/imza içeren belge aranır. **Ara sonuç:** Her madde için uyumlu / eksik / belgesiz işaretle.

## Çıktı modülleri
- Madde bazlı uyum kontrol listesi (durum + dayanak belge + eksik).
- İdari para cezası risk tablosu (m.26 atfıyla).
- Önceliklendirilmiş düzeltici eylem planı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

