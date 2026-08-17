---
argument-hint: ''
description: Kefalet sözleşmesinin geçerli kurulup kurulmadığı, eşin rızası, sorumluluk
  üst sınırı veya kefilin sorumluluktan kurtulması söz konusu olduğunda; kefaletin
  sıkı şekil ve koruma rejimini denetlemek içi
name: kefalet-gecerlilik-ve-sona-erme
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kefalet — Geçerlilik Şekli, Eş Rızası ve Sona Erme

## Görev
Kefaletin TBK m.581-603 kapsamındaki sıkı geçerlilik şartlarını, kefilin sorumluluk sınırını ve sona erme/düşme hallerini denetlemek; çoğu uyuşmazlığın şekil eksikliğinde düğümlendiğini gözeterek geçerlilik testini önce yapmak.

## Soğuk başlangıç (intake)
- Kefalet yazılı mı; el yazısıyla azami miktar ve tarih var mı?
- Kefilin eşi var mı, rızası alınmış mı (istisnalar var mı)?
- Kefalet türü (adi/müteselsil); süreli mi süresiz mi?
- Asıl borcun durumu (muaccel mi, takip yapıldı mı)?

## Denetim şeması
1. **Şekil (m.583).** Kefalet yazılı olmalı; **kefilin el yazısıyla** sorumlu olduğu azami miktar, kefalet tarihi ve müteselsil kefalette bu sıfat belirtilmeli. Eksiklik kesin hükümsüzlük doğurur — ilk kontrol budur.
2. **Eş rızası (m.584).** Evli kişinin kefaletinde, kefalet anında veya en geç sözleşme kurulurken eşin yazılı rızası şart; sonradan değişiklik ağırlaştırıyorsa yeniden rıza. İstisnalar (ticaret siciline kayıtlı tacirin işi, mesleki faaliyet vb.) dar yorumlanır.
3. **Tür ve başvuru.** Adi kefalette önce asıl borçluya başvurma (tartma def'i, m.585); müteselsil kefilde alacaklı doğrudan kefile gidebilir (m.586). Kefil, asıl borçlunun def'ilerini ileri sürebilir (m.591).
4. **Sorumluluk kapsamı (m.589).** Azami miktarla sınırlı; faiz, takip giderleri belirli koşullarla eklenir.
5. **Sona erme/düşme (m.598-600).** Gerçek kişi kefaletinde süre kararlaştırılmasa da 10 yılın sonunda kendiliğinden sona erer (m.598/3). Süreli kefalette sürenin sonunda alacaklı bir ay içinde takip/dava yapmazsa kefil kurtulur (m.600). Alacaklının kefili gözetme yükümü ve teminatları koruma (m.592).
6. **İspat.** Geçerli kefaleti (şekil + eş rızası) alacaklı; düşme/sona erme şartlarını kefil ispatlar. Ara sonuç: geçerlilik + sorumluluk tavanı + güncel durum.

## Çıktı modülleri
- Geçerlilik kontrol listesi (şekil + eş rızası).
- Kefile karşı/ kefil lehine savunma stratejisi notu.
- Sona erme/düşme savunması dilekçe iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

