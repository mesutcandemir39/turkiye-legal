---
argument-hint: ''
description: Taşıma, taşıma işleri komisyonculuğu veya lojistik/depolama hizmet sözleşmesi
  hazırlanması, mevcut sözleşmenin riskli/geçersiz şartlar yönünden incelenmesi ve
  emredici hükümlere uyumun denetlenmesi ge
name: tasima-sozlesmesi-taslak
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


# Taşıma ve Lojistik Sözleşmesi Taslağı

## Görev
Taşıma/forwarding/lojistik sözleşmesi taslağı üretmek veya mevcut sözleşmeyi emredici hükümler, sorumluluk dağılımı ve risk yönünden incelemek.

## Soğuk başlangıç (intake)
1. Sözleşme tipi: tek seferlik taşıma, çerçeve taşıma, forwarding mi, depolama+taşıma karması mı?
2. Taşıma iç mi sınır aşan mı; CMR uygulanacak mı?
3. Taraflar: gönderen/yük sahibi mi, taşıyıcı mı, komisyoncu mu temsil ediliyor?
4. Özel ihtiyaçlar: değer beyanı, sigorta, tehlikeli madde, teslim süresi taahhüdü var mı?

## Denetim şeması
1. **Emredici çerçeve:** Sınır aşan karayolunda CMR m.41 — sorumluluğu CMR aleyhine değiştiren şartlar batıldır. İç taşımada TTK m.854 ve m.886 — sorumluluğu hafifleten anlaşmalar sınırlı; kasıt/pervasızlık için sorumsuzluk geçersiz.
2. **Esaslı maddeler:** Taşıma konusu eşya ve güzergâh, teslim/varma süresi, ücret ve ödeme, yükleme-boşaltma yükümlülüğü (m.852 vd.), belge düzenleme.
3. **Sorumluluk maddeleri:** Sorumluluk sınırı (TTK m.882 / CMR m.23) sözleşmeyle taşıyıcı lehine düşürülemez; değer beyanıyla (m.880) artırılabilir. Gecikme tazminatı tavanına dikkat.
4. **Sigorta:** Taşıyıcı mali sorumluluk sigortası (CMR sigortası) ve emtia/nakliyat sigortası ayrımı; sigorta yaptırma yükümlüsü ve rücu (TTK m.1472 halefiyet).
5. **Forwarder klozları:** Sabit ücret kararlaştırılırsa taşıyıcı gibi sorumluluk doğacağı (m.926) açıkça öngörülmeli; aksi halinde komisyon yapısı netleştirilmeli.
6. **Yan klozlar:** Hapis hakkı (TTK m.891), demuraj/bekleme ücreti, mücbir sebep, uygulanacak hukuk ve yetki/tahkim.
7. **Ara sonuç:** Geçersiz/asimetrik şartların ayıklanması ve dengeli risk dağıtımı.

## Çıktı modülleri
- Madde madde sözleşme taslağı ([doldurulacak] yer tutucularıyla).
- Geçersiz/riskli şart raporu (CMR m.41 / TTK m.854 süzgeci).
- Sorumluluk ve sigorta klozları için alternatif lafızlar.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

