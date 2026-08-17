---
argument-hint: ''
description: Taşınmaz üzerinde ipotek kurulması, derecesi, kapsamı, paraya çevrilmesi
  (icra) ve terkini söz konusu olduğunda; alacağın teminat altına alınması, üst sınır/anapara
  ipoteği ayrımı ve rehnin sona ermes
name: ipotek-ve-tasinmaz-rehni
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
  - ad: Tapu Kanunu
    numara: '3402'
    tur: kanun
  - ad: Kat Özel Koşulu Olmak Üzere Yapılan Satış Mukavelelerine Dair Kanun
    numara: '2644'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İpotek ve Taşınmaz Rehni

## Görev
Taşınmaz rehninin kuruluşunu, kapsamını, derece sistemini, paraya çevrilmesini ve terkinini hukuki dayanakla çözümlemek; teminat ile alacak ilişkisini doğru kurmak.

## Soğuk başlangıç (intake)
- Rehin türü: anapara ipoteği mi, üst sınır (azami meblağ) ipoteği mi?
- Teminat altına alınan alacak mevcut mu, doğacak/koşullu mu; tutarı belirli mi?
- Rehin derecesi ve önceki/sonraki takyidatlar (boş derece, sabit/ilerleme sistemi) ne durumda?
- Borç ödendi mi; terkin mi, paraya çevirme (takip) aşaması mı?

## Denetim şeması
1. **Kuruluşu denetle.** İpotek resmi senetle tapu müdürlüğünde kurulur (TMK m.856; TMK m.795 — rehin tescille doğar). Geçerli bir alacağı teminat altına alır; rehin fer'idir, alacağa bağlıdır.
2. **Türü ayır.** Anapara ipoteği: belli, kesin alacak (TMK m.875 kapsamı — asıl alacak, takip giderleri, gecikme faizi). Üst sınır ipoteği: doğmuş/doğacak alacaklar belirli bir azami meblağ ile teminatlandırılır (TMK m.851). Tür, kapsamı ve faizin teminat alanını belirler.
3. **Kapsamı belirle.** Rehin, taşınmazla birlikte bütünleyici parça ve eklentiyi (TMK m.862), kira/ürün gelirlerini koşullu kapsar; kapsam dışı kalanlar ayrıca değerlendirilir.
4. **Derece sistemini uygula.** İpotek tescil edilen derecede yer alır; boşalan dereceden yararlanma (sabit dereceler ilkesi) sözleşme ve sicile göre çözülür. Sonraki rehinli alacaklının durumu sıraya bağlıdır.
5. **Paraya çevirme.** Muaccel alacak için rehnin paraya çevrilmesi yoluyla takip (2004 sayılı İİK m.145 vd.); ipoteğin türüne göre ilamlı/ilamsız ayrımı ve itiraz imkânı. Lex commissoria yasağı: doğrudan mülkiyete geçiş kararlaştırılamaz (TMK m.873/2).
6. **Terkin.** Alacak sona erince malik terkin isteyebilir (TMK m.883); rehin hakkı sona erse de sicilden silinene kadar şeklen durur.
7. **Ara sonuç.** Rehnin geçerliliği, kapsamı ve istenen işlem (tesis/terkin/takip) netleştirilir.

## Çıktı modülleri
- İpotek türü–kapsam–derece analizi.
- Resmi senet / terkin talebi veya rehnin paraya çevrilmesi takip taslağı iskeleti.
- Teminat–alacak uyumu ve faiz kapsamı risk notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

