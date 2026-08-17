---
argument-hint: ''
description: Reçeteli ilacın halka tanıtım yasağı, ürün tanıtım temsilcileri, bilimsel
  toplantı ve promosyon kuralları ile TİTCK idari yaptırımlarına ilişkin uyuşmazlıklarda
  kullanılır.
name: ilac-tanitim-promosyon
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
  - ad: Hemşirelik Kanunu
    numara: '6197'
    tur: kanun
  - ad: Mimar ve Mühendisler Hakkında Kanun
    numara: '1262'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İlaç Tanıtımı ve Promosyon Kuralları

## Görev
Bir tanıtım faaliyetinin (UTT ziyareti, bilimsel toplantı, dijital içerik, numune, değer aktarımı) Beşeri Tıbbi Ürünlerin Tanıtım Faaliyetleri Yönetmeliği’ne uygunluğunu denetlemek ve idari yaptırıma karşı savunma kurmak.

## Soğuk başlangıç (intake)
- Tanıtım kime yönelik: sağlık meslek mensubu mu, halk mı (reçeteli üründe halka tanıtım yasaktır)?
- Faaliyet türü: UTT ziyareti, toplantı sponsorluğu, numune dağıtımı, dijital/sosyal medya, değer aktarımı?
- TİTCK denetim tutanağı/yaptırımı var mı; gerekçesi nedir?
- İçerik onaylı KÜB/KT ile uyumlu mu, endikasyon dışı vurgu var mı?

## Denetim şeması
1. **Dayanak.** Beşeri Tıbbi Ürünlerin Tanıtım Faaliyetleri Hakkında Yönetmelik (2015) ve TİTCK kılavuzları; reçeteli ürünün halka tanıtımı 1262 ve Yönetmelikle yasaktır.
2. **Hedef kitle kapısı.** Reçeteli ürün → yalnızca sağlık meslek mensubuna; reçetesiz (OTC) için sınırlı koşullar. Ara sonuç: faaliyet yasak kitleye mi ulaştı?
3. **İçerik denetimi.** Tanıtım onaylı Kısa Ürün Bilgisi (KÜB) ile uyumlu, dengeli, abartısız olmalı; endikasyon dışı kullanım teşviki yasak. Değer aktarımı şeffaflık kurallarına tabi.
4. **Yaptırım ve yol.** İhlalde TİTCK idari yaptırım (uyarı, tanıtım durdurma, idari para cezası) uygular; bu birel idari işlemdir → idari yargı, İYUK m.7 (60 gün). İdari para cezasının özel kanun mu 5326 mı çerçevesinde olduğu kontrol edilir. İspat: ihlali idare tutanakla; aykırılığın yokluğunu/ölçüsüzlüğü davacı gösterir.
5. **Uyum boyutu.** İleriye dönük: SOP, onay akışı, materyal arşivi, değer aktarımı kaydı.

## Çıktı modülleri
- Tanıtım materyali/uygulama uyum kontrol listesi.
- İdari yaptırıma karşı iptal dilekçesi iskeleti [doldurulacak].
- Uyum programı (onay akışı, arşiv, eğitim) önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

