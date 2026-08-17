---
argument-hint: ''
description: Çocukla ana-baba arasında soybağının kurulması, reddedilmesi (soybağının
  reddi), tanıma ve babalık davası ile evlat edinme süreçlerinde, özellikle sıkı hak
  düşürücü süreler söz konusu olduğunda kullan
name: soybagi-tanima-babalik
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  - ad: Ailenin Korunması ve Kadına Karşı Şiddetin Önlenmesine Dair Kanun
    numara: '6284'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Soybağı, Tanıma ve Babalık Davası

## Görev
Çocuk ile ana-baba arasındaki soybağını kurmak veya kaldırmak; babalık karinesi, soybağının reddi, tanıma, babalık davası ve evlat edinme yollarını ve özellikle hak düşürücü süreleri yönetmek.

## Soğuk başlangıç (intake)
1. Çocuğun doğum tarihi ve ana-babanın o tarihteki medeni hali nedir?
2. Talep soybağı kurmak mı (tanıma/babalık) yoksa kaldırmak mı (soybağının reddi)?
3. Olayı/karineyi sarsan durum (ayrı yaşama, DNA, başka baba) ne zaman öğrenildi?
4. Çocuk ergin mi; vasi/kayyım atanması gerekiyor mu?

## Denetim şeması
1. **Soybağının kurulması.** Ana yönünden doğumla (m.282); baba yönünden ana ile evlilik (babalık karinesi m.285), tanıma (m.295) veya hâkim hükmü/babalık davası (m.301) ile. Evlilik içinde doğan veya evlilikten başlayarak 300 gün içinde doğan çocuğun babası kocadır (m.285/1).
2. **Soybağının reddi (m.286-291).** Kocanın dava açma süresi: doğumu ve baba olmadığını öğrenmeden başlayarak **1 yıl** (m.289/1). Çocuğun dava süresi erginlikten itibaren 1 yıl. Gecikme haklı sebebe dayanıyorsa süre sebebin ortadan kalkmasından işler (m.289/3). Karine çürütülürken DNA esastır.
3. **Tanıma ve babalık davası.** Tanıma resmî senet/vasiyetname/nüfus beyanı ile (m.295); tanımanın iptali (m.297-298). Babalık davası ana ve çocuk tarafından açılır; ananın hakkı doğumdan başlayarak **1 yıl** (m.303). Davada karine: gebe kalma döneminde cinsel ilişki babalığa karine sayılır (m.302).
4. **Evlat edinme.** Küçüğün evlat edinilmesi (m.305 vd.: bir yıl bakım, küçüğün yararı, en az 30 yaş veya 18 yıl evlilik vb.); ergin/kısıtlının evlat edinilmesi (m.313). Hâkim kararıyla kurulur.
5. **Ara sonuç.** Doğru yol (red/tanıma/babalık/evlat edinme) + süre durumu + gerekli deliller (DNA, nüfus, tanık) raporlanır.

## Çıktı modülleri
- Soybağı durum şeması ve uygulanacak dava türü.
- Hak düşürücü süre takvimi ve gecikme mazereti değerlendirmesi.
- Dava dilekçesi için taraf, talep ve delil (DNA tespiti talebi dahil) listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

