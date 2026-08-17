---
argument-hint: ''
description: Üretim, dağıtım, tedarik gibi lisanslı faaliyetlerde önlisans/lisans
  başvurusu, yükümlülükler, tadil, süre uzatımı veya iptal riski değerlendirildiğinde
  ve EPDK lisans rejimi uyumu kontrol edileceğind
name: lisanslama-onlisans-denetim
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
  - ad: Elektrik Piyasası Kanunu
    numara: '6446'
    tur: kanun
  - ad: Mühendislik ve Mimarlık Meslek Kanunu
    numara: '4646'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Lisanslama ve Önlisans Denetim Şeması

## Görev
Bir enerji faaliyetinin doğru lisans rejimine tabi olup olmadığını, önlisans/lisans yükümlülüklerinin yerine getirilip getirilmediğini ve iptal/sona erme riskini denetleyerek uyum yol haritası çıkarmak.

## Soğuk başlangıç (intake)
1. Faaliyet türü ve kapasite (MWe/MWm) nedir?
2. Önlisans mı lisans mı; veriliş ve geçerlilik tarihleri?
3. Bağlantı görüşü/çağrı mektubu, ÇED, mülkiyet/irtifak durumu tamam mı?
4. Süre uzatımı veya tadil talebi var mı; gerekçesi?

## Denetim şeması
1. **Lisans gerekliliği**: 6446 m.5 — lisansa tabi faaliyetler. İstisna: m.14 ve Lisanssız Elektrik Üretimi Yönetmeliği kapsamı (çatı GES, kendi tüketimi karşılama). Ara sonuç: lisanslı/lisanssız.
2. **Önlisans aşaması**: 6446 m.7 ve Lisans Yönetmeliği — önlisans süresi içinde mülkiyet/kullanım hakkı, ÇED kararı, bağlantı anlaşmasına çağrı, ödenmiş sermaye gibi yükümlülüklerin tamamlanması. İspat yükü başvuru sahibinde; belge eksikliği reddi/iptali doğurur.
3. **Lisansa geçiş ve yükümlülükler**: İnşa ve işletmeye geçiş süreleri, tamamlanma oranı bildirimi, teminat. Yükümlülük ihlali 6446 m.16 yaptırımlarını tetikler.
4. **Tadil/süre uzatımı**: Kurul kararı ve yönetmelikteki mücbir sebep/uzatma halleri; gecikme gerekçesinin müvekkile yüklenemeyen sebeplere dayandığı ispatlanmalı.
5. **Sona erme/iptal**: Yükümlülük ihlali, teminat iradı, başvuru üzerine sona erme. İptal işlemi idari işlem olduğundan İYUK m.7 süresi içinde dava ve m.27 yürütmenin durdurulması istemi değerlendirilir.

İçtihat için lisans iptali/önlisans uyuşmazlıklarında karararama.danistay.gov.tr (13. Daire ağırlıklı) taranır; künye doğrulanmadan [DOĞRULANMADI] işaretlenir.

## Çıktı modülleri
- Lisans uyum kontrol listesi (yükümlülük/durum/eksik).
- Süre ve teminat riski tablosu.
- Tadil/uzatma başvurusu veya iptale karşı dava stratejisi taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

