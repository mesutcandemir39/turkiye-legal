---
argument-hint: ''
description: Anonim veya limited şirket kuruluşu, esas/şirket sözleşmesinin zorunlu
  içeriği, sermaye taahhüdü ve ayni sermaye, tescil ve MERSİS adımları gündeme geldiğinde;
  kuruluş sürecinin eksiksiz ve geçerli ku
name: anonim-limited-kurulus
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
  version: 0.1.0
user-invocable: true
---


# AŞ ve Ltd. Kuruluş ve Esas Sözleşme

## Görev
Sermaye şirketini geçerli biçimde kurmak: tip seçimi, esas/şirket sözleşmesi içeriği, sermaye taahhüdü ve ödeme, tescil-ilan; kuruluş sakatlıklarını önlemek.

## Soğuk başlangıç (intake)
1. AŞ mı Ltd. mi; ortak sayısı, tek kişilik mi?
2. Sermaye miktarı ve yapısı: nakdi/ayni; ayni varsa konusu?
3. Faaliyet konusu ve ticaret unvanı belirlendi mi?
4. Yönetim yapısı tercihi (AŞ'de tek üyeli YK mümkün; Ltd.'de müdür) ne?
5. Özel hak/imtiyaz, pay devri sınırı, oy hakkı düzenlemesi isteniyor mu?

## Denetim şeması
1. Asgari sermaye: AŞ m.332 (esas sermaye asgari tutarı; kayıtlı sermaye sistemi m.332/2); Ltd. m.580. Olay tarihindeki güncel tutarı teyit et.
2. Ortak/kurucu: AŞ tek kişiyle kurulabilir (m.338); Ltd. tek ortakla (m.574); azami ortak sayısı Ltd.'de 50 (m.574).
3. Esas sözleşme zorunlu içeriği: AŞ m.339 (unvan, merkez, konu, sermaye ve paylar, yönetim, ilan şekli); Ltd. m.576. Noter onayı veya sicil müdürü huzurunda imza (m.575).
4. Sermayenin ödenmesi: AŞ nakdî sermayenin tescilden önce ödenmesi ve kalanın 24 ayda ödenmesi (m.344, m.459/1 atfı); ayni sermaye değerlemesi mahkemece atanan bilirkişi (m.343); ayni sermaye üzerinde sınırlı ayni hak/haciz olmaması (m.342).
5. Ayni sermaye ve devralma: m.342-343; kuruluşta devralınacak işletme/ayınlar m.349 (kurucular beyanı).
6. Tescil ve tüzel kişilik: m.354-355 (AŞ), m.585-588 (Ltd.); MERSİS üzerinden başvuru; tescille tüzel kişilik doğar. İzne tabi şirketlerde Bakanlık izni (m.333).
7. İspat/şekil: Şekle aykırı esas sözleşme hükmü geçersiz; emredici hükme aykırılık m.340/579.

## Çıktı modülleri
- Kuruluş checklist'i (sermaye, sözleşme, tescil, MERSİS).
- Esas/şirket sözleşmesi taslağı (zorunlu maddeler, [doldurulacak] yer tutucularla).
- Ayni sermaye/değerleme ve özel hak notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

