---
argument-hint: ''
description: Vergi ziyaı, usulsüzlük ve özel usulsüzlük cezaları ile VUK m.359 kaçakçılık
  suçunu değerlendirmek; ceza ihbarnamesi geldiğinde veya ceza riski sorulduğunda
  kullanılır.
name: vergi-cezalari-ve-kacakcilik
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
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  - ad: Gelir Vergisi Kanunu
    numara: '193'
    tur: kanun
  - ad: Kurumlar Vergisi Kanunu
    numara: '5520'
    tur: kanun
  - ad: Katma Değer Vergisi Kanunu
    numara: '3065'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Vergi Cezaları ve Kaçakçılık Suçu

## Görev
Kesilen idari vergi cezasının türünü ve tutarını denetlemek, kaçakçılık suçu (VUK m.359) riskini değerlendirmek ve ceza indirimi/kaldırma yollarını planlamak.

## Soğuk başlangıç (intake)
1. Ceza türü nedir (vergi ziyaı / usulsüzlük / özel usulsüzlük)?
2. Vergi ziyaı cezası bir kat mı, üç kat mı kesilmiş?
3. Sahte/muhteviyatı itibarıyla yanıltıcı belge (SMİYB) iddiası var mı?
4. Aynı fiilden vergi suçu raporu düzenlenip Cumhuriyet savcılığına bildirim yapıldı mı?
5. Pişmanlık, uzlaşma veya cezada indirim talep edildi mi?

## Denetim şeması
1. **Vergi ziyaı:** VUK m.341 — verginin zamanında tahakkuk etmemesi/eksik tahakkuku. Ceza VUK m.344 uyarınca ziyaa uğratılan verginin bir katı; fiil m.359'daki kaçakçılık fiiliyle işlenmişse üç katı. Kat hesabını doğrula.
2. **Usulsüzlük:** VUK m.351-352 — kanuni ödevlerin biçimsel ihlali; derecelere göre maktu. Re'sen takdiri gerektiren usulsüzlüklerde ağırlaştırma kontrolü.
3. **Özel usulsüzlük:** VUK m.353, mük.355 — belge düzenine aykırılık (fatura vermeme/almama), bilgi verme ödevinin ihlali; tutar ve üst sınır denetimi.
4. **Tek fiil-çok ceza:** VUK m.336 — bir fiil hem usulsüzlük hem vergi ziyaına yol açıyorsa ağır olan kesilir; içtima kuralını uygula.
5. **Kaçakçılık suçu:** VUK m.359 — defter/belgede hile, sahte belge düzenleme/kullanma, defter gizleme. Bu hapis cezasını gerektiren suç olup vergi mahkemesinin değil ceza mahkemesinin görev alanındadır; idari ceza ile bağımsızdır (non bis in idem tartışması ayrı değerlendirilir). m.359/son: etkin pişmanlık ve ödeme ile indirim imkânı.
6. **İndirim/kaldırma yolları:** VUK m.376 (cezada indirim — süresinde ödeme ve dava açmama şartı), uzlaşma (Ek m.1, m.11), pişmanlık (m.371 — ziyaı cezası kesilmez), düzeltme (m.116 vd.). Ara sonuç: hangi yol süreyi ve tutarı en çok lehe çevirir?

## Çıktı modülleri
- Ceza türü-tutar doğrulama tablosu (madde / oran / hesap).
- Kaçakçılık riski değerlendirme notu (m.359 unsur analizi, ceza yargısı uyarısı).
- İndirim/uzlaşma/pişmanlık karşılaştırma matrisi (süre, tutar, dava hakkı etkisi).
- Savunma dilekçesi argüman iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

