---
argument-hint: ''
description: Ekonomik/mali bir fiilin hangi suç tipine ve hangi mevzuat katmanına
  oturduğunu çözmek, suç genel teorisini (kast, iştirak, içtima, tüzel kişi sorumluluğu)
  ekonomik suçlara uyarlamak ve dosyanın iskel
name: temel-kavramlar-ve-sistem
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Kaçakçılıkla Mücadele Kanunu
    numara: '5549'
    tur: kanun
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Ekonomik Ceza Hukuku Temel Kavramlar ve Sistematik

## Görev
Ekonomik/mali nitelikli bir fiili doğru suç tipine yerleştirmek, TCK Genel Hükümler süzgecinden geçirmek ve dosyanın çok katmanlı (ceza + yan mevzuat + idari) yapısını ortaya koymak.

## Soğuk başlangıç (intake)
- Fiil ne? (para/belge/vergi/menkul kıymet/kamu görevi hangisiyle ilgili)
- Failin sıfatı ne? (kamu görevlisi, banka mensubu, şirket yöneticisi, mükellef, üçüncü kişi)
- Bir kurum raporu var mı? (VDK, MASAK, SPK, BDDK, müfettiş)
- Soruşturma evresi: şüpheli/iddianame/kovuşturma hangisinde?
- Tüzel kişi mi işin içinde, gerçek kişiye mi sorumluluk bağlanıyor?

## Denetim şeması
1. **Tipiklik — suç tipi seçimi**: Fiili önce TCK özel hükümleriyle eşle (dolandırıcılık m.157-158, güveni kötüye kullanma m.155, zimmet m.247, rüşvet m.252, aklama m.282), sonra yan mevzuatla (VUK m.359, SPK m.106-107-110). Birden çok tip uyuyorsa görünüşte içtima ve fikri içtima (TCK m.44) ile gerçek içtimayı ayır.
2. **Manevi unsur**: Ekonomik suçlar kural olarak kasıtla işlenir (TCK m.21). Vergi kaçakçılığında "bilerek" sahte belge kullanımı; aklamada öncül suç bilgisi aranır. Taksir istisnaidir (m.22).
3. **İştirak**: Yönetici, mali müşavir, aracı kurum çalışanı için faillik mi şeriklik mi (azmettirme m.38, yardım etme m.39) ayrımını yap.
4. **Tüzel kişi**: TCK m.20/2 uyarınca tüzel kişiye ceza verilmez; m.60 güvenlik tedbiri (faaliyet izni iptali, müsadere) ve ilgili kanundaki idari para cezası gündeme gelir.
5. **Dava/mütalaa şartı**: Vergi (VUK m.367) ve SPK (m.115) suçlarında ön şartı kontrol et — yoksa kovuşturma usulden sakat.
6. **Ara sonuç**: Suç tipi, fail sıfatı, manevi unsur, iştirak biçimi ve ön şart durumu tek tabloda netleşir.

## Çıktı modülleri
- Suç tipi-fiil eşleştirme tablosu (madde atıflı)
- Fail/şerik sıfat haritası
- Yan mevzuat ve kurum raporu bağlantı listesi
- Ön şart/dava şartı kontrol notu
- Sonraki adım önerisi (savunma/şikâyet/mütalaa)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

