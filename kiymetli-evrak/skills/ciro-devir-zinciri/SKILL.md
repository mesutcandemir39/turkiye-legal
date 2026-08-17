---
argument-hint: ''
description: Emre yazılı senetlerde ciro türlerini, ciro zincirinin muntazamlığını
  ve yetkili hamil sıfatını incelemek; hak sahipliği, devir geçerliliği ve hamilin
  konumunu belirlerken kullanılır.
name: ciro-devir-zinciri
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  - ad: Çek Kanunu
    numara: '5941'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Ciro ve Devir Zinciri

## Görev
Emre yazılı kambiyo senedinin ciro yoluyla devrini denetlemek, ciro zincirinin muntazamlığını ve hamilin yetkili hamil sıfatını tespit etmek; özel ciro türlerinin (tahsil, rehin, beyaz) sonuçlarını belirlemek.

## Soğuk başlangıç (intake)
- Senedin arkasında kaç ciro var; cirolar tarih sırası ve isim bakımından birbirine bağlanıyor mu?
- Beyaz ciro (imza-only) var mı; son hamil senedi nasıl edinmiş?
- Cirolardan biri tahsil ("bedeli tahsil içindir") veya rehin amaçlı mı?
- Devirler arasında temlik, miras veya başka bir kanuni intikal var mı?

## Denetim şeması
1. Devir biçimi: emre senet ciro + teslimle, hamiline senet teslimle, nama senet alacağın temlikiyle devredilir (TTK m.681, m.654). Emre senede "emre yazılı değildir" kaydı eklenirse nama hükmüne girer ve temlikle devredilir (m.681/2).
2. Ciro türleri: tam ciro (devir), beyaz ciro (m.683 — imza yeter; hamil boşluğu doldurabilir veya teslimle devredebilir), tahsil cirosu (m.688 — hamil sadece temsilci, borçlu lehtara karşı def'ilerini ileri sürebilir), rehin cirosu (m.689 — hamile rehin hakkı).
3. Zincir muntazamlığı: hamil, kesintisiz ciro zinciriyle hakkını ispatlarsa yetkili hamil sayılır; beyaz ciroyu izleyen imza önceki ciroyu yapmış gibi kabul edilir (TTK m.686). Çizilmiş cirolar yok sayılır.
4. İyiniyetli iktisap: senedi kesintisiz ciroyla iyiniyetle edinen hamilden senet geri istenemez (TTK m.687/iktisap); kişisel def'iler iyiniyetli hamile karşı ileri sürülemez (m.687/def'i).
5. Ara sonuç: zincir muntazamsa hamil yetkili hamildir ve takip/ödeme talep edebilir; zincirde kopukluk veya tahsil cirosu varsa hamilin hak ve def'i konumu yeniden tartılır.

## Çıktı modülleri
- Ciro zinciri akış şeması (cirant > ciro türü > hamil).
- Yetkili hamil değerlendirme notu (m.686 dayanaklı).
- Def'i konumu özeti (iyiniyet/tahsil cirosu etkisi).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

