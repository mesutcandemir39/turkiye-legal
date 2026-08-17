---
argument-hint: ''
description: Özgürlüğü kısıtlayan koruma tedbirlerinin yasaya uygunluğunu denetlemek,
  tutuklamaya itiraz, salıverilme ve adli kontrol talepleri hazırlamak gerektiğinde
  kullanılır.
name: yakalama-gozalti-tutuklama
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
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yakalama, Gözaltı ve Tutuklama

## Görev
Özgürlüğü kısıtlayan tedbirlerin sebep, süre ve ölçülülük yönünden hukuka uygunluğunu denetlemek; tutuklamaya itiraz, salıverilme ve adli kontrol taleplerini gerekçelendirmek.

## Soğuk başlangıç (intake)
- Kişi ne zaman ve nasıl yakalandı; gözaltı kararı kim tarafından verildi?
- Tutuklama kararı var mı, hangi suçtan ve hangi tutuklama nedenine dayanıyor?
- Tutuklunun kişisel durumu (sabıka, yerleşik adres, sağlık) nedir?
- Önceki itiraz veya tahliye talebi yapıldı mı, ne zaman?
- Tutuklulukta geçen süre ne kadar?

## Denetim şeması
1. **Yakalama.** Suçüstü halinde herkes yakalayabilir; kolluk gecikmesinde sakınca olan ve savcıya ulaşılamayan hallerde yakalar (CMK m.90). Yakalanana hakları derhal bildirilir (m.90/4).
2. **Gözaltı.** Savcı emriyle, soruşturma için zorunluysa uygulanır; süre yakalama anından itibaren 24 saati, toplu suçlarda her defasında 1 günü geçmemek üzere uzatılabilir (m.91). Yol süresi hariç.
3. **Tutuklama şartları.** Kuvvetli suç şüphesini gösteren somut delil + bir tutuklama nedeni gerekir (m.100): kaçma şüphesi, delil karartma; m.100/3'te sayılan katalog suçlarda neden var sayılabilir. Karar hâkim/mahkemece verilir (m.101).
4. **Ölçülülük ve alternatif.** Tutuklama son çaredir; adli kontrol (m.109) yeterliyse tutuklama orantısızdır (m.100/1 son cümle, Anayasa m.13, m.19).
5. **Süre.** Soruşturmada ve kovuşturmada azami tutukluluk süreleri m.102'de düzenlenir; gerekçeli ve düzenli denetim (m.108, en geç 30 günlük aralıklarla resen inceleme) zorunludur.
6. **İtiraz.** Tutuklama ve uzatma kararlarına karşı m.267-271 uyarınca itiraz edilir; salıverilme her aşamada istenebilir (m.104).
7. **Ara sonuç.** Şart eksikse veya ölçüsüzse itiraz/tahliye talebi; aksi halde adli kontrole çevirme talebi öncelenir.

## Çıktı modülleri
- Tutuklama kararının şart/neden/ölçülülük denetim tablosu.
- Tutuklamaya itiraz veya salıverilme talebi dilekçesi taslağı.
- Adli kontrol önerisi ve dayanak (m.109 tedbir listesi).
- Tutukluluk süresi ve sonraki denetim tarihi takvimi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

