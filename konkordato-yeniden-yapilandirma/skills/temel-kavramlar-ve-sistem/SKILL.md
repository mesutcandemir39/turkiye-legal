---
argument-hint: ''
description: Konkordato ile yeniden yapılandırmanın temel kavramlarını, türlerini
  ve iflas/icra rejimi içindeki yerini netleştirmek; hangi kurumun (adi konkordato,
  mal varlığının terki, finansal yeniden yapılandır
name: temel-kavramlar-ve-sistem
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
  - ad: İcra ve İflas Kanunu
    numara: '2004'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Konkordato Sistematiği

## Görev
Mali güçlük içindeki borçlunun durumunu doğru hukuki kuruma yerleştirmek: adi konkordato (İİK m.285 vd.), iflastan sonra konkordato (m.309/A), mal varlığının terki suretiyle konkordato (m.309/h vd.) ve mahkeme dışı finansal yeniden yapılandırma arasından doğru aracı seçmek; konkordatonun vade/tenzilat/karma türlerini ayırmak.

## Soğuk başlangıç (intake)
- Borçlu kim: gerçek kişi tacir, sermaye şirketi, kooperatif mi? Ölçeği ve işkolu?
- Mali durum: borca batık mı, yoksa borca batık olmadan ödeme güçlüğü mü var?
- Talep eden kim: borçlu mu, alacaklı mı (İİK m.285)?
- Halihazırda iflas talebi/iflas davası veya icra takipleri var mı?
- Amaç: işletmenin sürdürülmesi mi, alacaklıların iflasa göre daha iyi tatmini mi?

## Denetim şeması
1. **Kurum seçimi.** İflasın ertelenmesi 7101 sayılı Kanunla kaldırıldı; mali güçlükte başat araç konkordatodur (İİK m.285). Mahkeme denetimi istenmiyorsa finansal yeniden yapılandırma (5411 s.K. Geçici m.32 / FYY çerçeve anlaşmaları) değerlendirilir.
2. **Tür tayini.** Tenzilat konkordatosu (alacaktan vazgeçme), vade konkordatosu (ödeme süresi tanıma) veya karma. Proje ekonomisi buna göre kurgulanır.
3. **Borca batıklık ayrımı.** Borca batıklık varsa TTK m.376 ve İİK m.179 ile ilişki kurulur; konkordato talebi iflasa alternatif olarak öne çıkar.
4. **Ehliyet.** Borçlu her hâlde; alacaklı ancak iflas talep edebilecek nitelikteyse talep edebilir (m.285/2). İspat yükü: talep edenin mali güçlük/alacak iddiasını belgelemesi gerekir.
5. **Ara sonuç.** Kurum, tür ve görevli mahkeme (Asliye Ticaret Mahkemesi) tespit edilir; sonraki beceriye (denetim şeması ve mühlet) köprü kurulur.

## Çıktı modülleri
- Kurum ve tür tespiti notu (gerekçeli).
- Konkordato vs. finansal yeniden yapılandırma karşılaştırma tablosu.
- Talep ehliyeti ve görev-yetki özeti.
- Sonraki adım için yol haritası.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

