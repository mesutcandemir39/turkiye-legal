---
argument-hint: ''
description: Bir arsa veya yeni tamamlanan yapı üzerinde kat irtifakı ya da kat mülkiyeti
  tesis edilmesi, kat irtifakından kat mülkiyetine geçiş ya da kuruluş belgelerindeki
  eksiklik/uyuşmazlık gündeme geldiğinde;
name: kurulus-ve-kat-irtifakindan-kat-mulkiyetine-gecis
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
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kat İrtifakı ve Kat Mülkiyetinin Kurulması

## Görev
Bir taşınmaz üzerinde kat irtifakı veya kat mülkiyetinin geçerli biçimde kurulmasını sağlamak; kat irtifakından kat mülkiyetine geçişi yönetmek ve kuruluş belgelerindeki (resmî senet, proje, yönetim planı) eksiklik veya uyuşmazlıkları gidermek.

## Soğuk başlangıç (intake)
- Yapı hangi aşamada: arsa hâlinde mi, inşaat sürüyor mu, tamamlanmış/iskânlı mı?
- Kuruluş tek malikin istemiyle mi yoksa paydaşların ortak istemiyle mi yapılacak?
- Onaylı mimari proje, vaziyet planı ve yapı kullanma izni (iskân) mevcut mu?
- Yönetim planı hazırlandı ve tüm maliklerce imzalandı mı?

## Denetim şeması
1. **Kuruluş yolu (KMK m.10, m.12)**: Kat mülkiyeti/irtifakı, malik veya bütün paydaşların istemiyle, tapuda **resmî senet** düzenlenip tescil edilerek kurulur (m.13). Tek taraflı tesis ancak tek malik için mümkündür; paydaşlar varsa oybirliği gerekir.
2. **Zorunlu belgeler (m.12)**: (a) Genel inşaat projesi ve yetkili merci onayı, (b) bağımsız bölümleri gösteren liste (m.12/a), (c) **yönetim planı** (m.12/b, m.28), (d) tek malik değilse paydaşların istemi. Eksik belge tescili engeller.
3. **Kat irtifakı kuruluşu (m.2/c, m.10/son)**: Yapı henüz tamamlanmamışken arsa payına bağlı kat irtifakı kurulur; tapuda "kat irtifakı" olarak gösterilir. İrtifak sahibi, yapının projeye uygun bitirilmesini isteyebilir (m.26).
4. **Kat mülkiyetine geçiş (m.14)**: Yapı tamamlanıp yapı kullanma izni alınınca, kat irtifakına konu yapıda ilgililerin istemiyle kat mülkiyetine geçilir. Yapı fiilen tamamlanmışsa, kat irtifakı sahiplerinden biri dahi resen geçiş için başvurabilir (m.14/son uygulaması).
5. **Arsa payı belirlemesi (m.3/2)**: Resmî senette her bağımsız bölüme değeriyle orantılı arsa payı verilmelidir; orantısızlık sonradan arsa payı düzeltme davasına konu olur.
6. **Ara sonuç**: Belgeler tam ve proje onaylıysa tescil; eksikse tamamlama listesi; kat irtifakı varsa geçiş başvurusu.

## Çıktı modülleri
- Kuruluş belge kontrol listesi (proje, iskân, liste, yönetim planı).
- Kat mülkiyetine geçiş başvuru dilekçesi iskeleti.
- Eksiklik/uyuşmazlık halinde mahkemeye başvuru veya arsa payı düzeltme yönlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

