---
argument-hint: ''
description: Atık üretimi, taşınması, geri kazanımı ve bertarafı; tehlikeli atık yükümlülükleri,
  atık hiyerarşisi ve genişletilmiş üretici sorumluluğu kaynaklı uyuşmazlık ve uyum
  sorularında; izinsiz depolama/dökü
name: atik-yonetimi
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
  - ad: Çevre Kanunu
    numara: '2872'
    tur: kanun
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Atık Yönetimi ve Tehlikeli Atık

## Görev
Atık üreten, taşıyan, geri kazanan veya bertaraf eden işletmelerin yükümlülüklerini belirlemek; izinsiz atık işlemlerinden doğan idari/cezai/özel hukuk sorumluluğunu değerlendirmek.

## Soğuk başlangıç (intake)
1. Atık türü nedir: evsel, ambalaj, tehlikeli, tıbbi, hafriyat, elektronik?
2. Müvekkil zincirde hangi rolde: üretici, taşıyıcı, ara depolama, geri kazanım/bertaraf tesisi?
3. Atık beyanı, MoTAT/atık taşıma belgeleri ve lisanslar tam mı?
4. İzinsiz depolama/döküm iddiası veya çevresel zarar var mı?

## Denetim şeması
1. **Hiyerarşi ve genel yükümlülük**: Atık Yönetimi Yönetmeliği önleme > yeniden kullanım > geri dönüşüm > geri kazanım > bertaraf sırasını dayatır; 2872 m.8 kirletme ve çevreye zarar verme yasağını kurar. Üretici, atığını mevzuata uygun yönetmekle yükümlüdür.
2. **Tehlikeli atık özel rejimi**: Tehlikeli atıklar için ayrı toplama, etiketleme, lisanslı taşıma (MoTAT) ve bertaraf zorunludur; "beşikten mezara" izlenebilirlik aranır.
3. **Genişletilmiş üretici sorumluluğu**: Ambalaj ve belirli ürünlerde piyasaya sürenin toplama/geri kazanım yükümlülüğü doğar.
4. **Yaptırım ve sorumluluk**: İzinsiz/usulsüz atık işlemi 2872 m.20-23 idari para cezası ve m.15 durdurma sonucu doğurur; kasten çevreye atık verme TCK m.181-182 kapsamına girebilir; çevresel zararda m.28 kusursuz/müteselsil sorumluluk işler.
5. **İspat ve ara sonuç**: Beyan kayıtları, taşıma belgeleri, analiz ve numune zinciri belirleyicidir; belge eksikliği hem yaptırım hem sorumluluk doğurur.

## Çıktı modülleri
- Atık türü ve yükümlülük matrisi
- Belge/lisans uyum kontrol listesi
- İzinsiz işlem yaptırım ve sorumluluk değerlendirmesi
- Düzeltici eylem ve uyum planı taslağı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

