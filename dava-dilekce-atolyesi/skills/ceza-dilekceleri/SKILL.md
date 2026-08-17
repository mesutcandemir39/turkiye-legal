---
argument-hint: ''
description: Suç duyurusu/şikâyet, katılma talebi, tahliye-itiraz ve esas hakkında
  savunma gibi ceza muhakemesi dilekçelerini CMK çerçevesinde hazırlamak gerektiğinde
  kullanılır.
name: ceza-dilekceleri
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
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Ceza Muhakemesi Dilekçeleri (CMK)

## Görev
Soruşturma ve kovuşturma evrelerinde mağdur/şüpheli/sanık vekilliğine uygun dilekçeleri üretmek: şikâyet/suç duyurusu, katılma, koruma tedbirine itiraz ve savunma dilekçeleri.

## Soğuk başlangıç (intake)
- Hangi evre: soruşturma mı, kovuşturma mı?
- Müvekkil mağdur/müşteki mi, şüpheli/sanık mı, katılan mı?
- Şikâyete bağlı suç mu, şikâyet süresi (TCK m.73 — 6 ay) işliyor mu?
- Tutuklama/adli kontrol gibi bir koruma tedbiri var mı?

## Denetim şeması
1. Şikâyet/suç duyurusu (CMK m.158): Cumhuriyet başsavcılığına yazılır; suça konu vakıalar, deliller ve fail bilgileri. Şikâyete bağlı suçlarda TCK m.73 — fiilin ve failin öğrenilmesinden itibaren 6 ay; süre geçerse şikâyet hakkı düşer.
2. Katılma (CMK m.237-239): Suçtan zarar gören, kovuşturmada katılma talep eder; davaya katılma kararı verilirse haklar genişler.
3. Koruma tedbirine itiraz (CMK m.267-271): Tutuklama, adli kontrol ve diğer hâkim/mahkeme kararlarına itiraz; süre kural olarak yedi gün (m.268). Salıverilme talebi (m.104) her zaman mümkündür.
4. Savunma/esas hakkında beyan: İddianamedeki (m.170) suç vasıflandırmasını tartışın; suç genel teorisi katmanlarına göre (tipiklik, hukuka aykırılık, kusurluluk) savunmayı kurun; lehe deliller ve TCK m.21/22 kast-taksir ayrımı.
5. Delil değerlendirme: Hukuka aykırı delil yasağı (CMK m.206/2, m.217/2; Anayasa m.38/6). Ara sonuç: evre ve sıfata uygun dilekçe, süre içinde hazır.

## Çıktı modülleri
- İlgili ceza dilekçesi taslağı (şikâyet/katılma/itiraz/savunma)
- Süre uyarısı (şikâyet 6 ay, itiraz 7 gün)
- Delil ve tanık listesi
- Talep bloğu (soruşturma işlemi/salıverilme/beraat vb.)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

