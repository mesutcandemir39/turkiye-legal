---
argument-hint: ''
description: Kamu görevlisinin veya banka mensubunun malı zimmetine geçirmesi (TCK
  m.247, Bankacılık K. m.160), rüşvet (TCK m.252), irtikâp (m.250) ve görevi kötüye
  kullanma (m.257) iddiaları; etkin pişmanlık ve g
name: zimmet-rusvet-gorev-suclari
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


# Zimmet, Rüşvet ve Görevle Bağlantılı Suçlar

## Görev
Kamu görevlisi/banka mensubu sıfatına bağlı zimmet, rüşvet, irtikâp ve görevi kötüye kullanma suçlarını ayrıştırmak, doğru tipe yerleştirmek ve etkin pişmanlık imkânını değerlendirmek.

## Soğuk başlangıç (intake)
- Failin sıfatı: kamu görevlisi mi (TCK m.6), banka mensubu mu, özel hukuk kişisi mi?
- Fiil: kendisine tevdi edilen malı mı mal edindi (zimmet), menfaat mi sağladı/aldı (rüşvet/irtikâp), yoksa görevin gereklerine mi aykırı davrandı (m.257)?
- Menfaat-iş ilişkisi: belirli bir iş için mi, genel mi?
- Etkin pişmanlık aşamasında mı (soruşturma öncesi/sonrası)?

## Denetim şeması
1. **Sıfat tespiti**: Zimmet/rüşvet kamu görevlisine özgüdür (TCK m.6 tanımı). Banka görevlisinin bankaya ait malı mal edinmesi 5411 s. Bankacılık Kanunu m.160 (banka zimmeti) kapsamındadır — bu özel norm TCK m.247'ye göre uygulanır.
2. **Zimmet (TCK m.247)**: Görevi sebebiyle zilyetliği devredilen/koruma-gözetimiyle yükümlü olunan malın mal edinilmesi. Basit/nitelikli (hileli fiillerle gizleme — m.247/2) ayrımı yapılır. Kullanma zimmeti (m.247/3) ayrı düzenlenmiştir.
3. **Rüşvet (TCK m.252)**: Görevin yapılması/yapılmaması için anlaşma çerçevesinde menfaat. Rüşvet, iki taraflı anlaşma suçudur; rüşvet veren ve alan ayrı ayrı cezalandırılır. İrtikâptan (m.250) farkı: irtikâpta görevlinin nüfuzunu kötüye kullanarak mağduru menfaate icbar/ikna etmesi vardır.
4. **Görevi kötüye kullanma (m.257)**: Tali norm; zimmet/rüşvet/irtikâp oluşmuyorsa, görevin gereklerine aykırılıkla kişilerin mağduriyeti/kamu zararı/haksız menfaat aranır.
5. **Etkin pişmanlık**: Zimmette TCK m.248 (soruşturma başlamadan iade ile ciddi indirim), rüşvette m.254 — şartları ve zaman dilimleri suç tipine göre ayrı ayrı kontrol edilir.
6. **Ara sonuç**: Fail sıfatı, doğru suç tipi (özel norm/genel norm), nitelikli hal ve etkin pişmanlık penceresi netleşir.

## Çıktı modülleri
- Fail sıfatı ve özel/genel norm seçimi
- Zimmet/rüşvet/irtikâp/m.257 ayrım tablosu
- Nitelikli hal değerlendirmesi
- Etkin pişmanlık zaman çizelgesi
- Savunma/iade stratejisi notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

