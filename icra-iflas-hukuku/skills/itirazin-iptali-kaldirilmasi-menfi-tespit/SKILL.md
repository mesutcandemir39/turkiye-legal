---
argument-hint: ''
description: Ödeme emrine itiraz nedeniyle duran takipte hangi davanın açılacağına
  karar vermek; itirazın iptali, itirazın kaldırılması veya menfi tespit-istirdat
  davasını kurgulamak ve icra inkâr/kötüniyet tazmin
name: itirazin-iptali-kaldirilmasi-menfi-tespit
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


# İtirazın İptali, İtirazın Kaldırılması ve Menfi Tespit

## Görev
Duran takibi devam ettirmek için itirazın iptali (m.67) ile itirazın kaldırılması (m.68 vd.) arasında seçim yapmak; borçlu tarafında menfi tespit/istirdat (m.72) ile savunma kurmak; tazminat risk ve fırsatlarını yönetmek.

## Soğuk başlangıç (intake)
- Elde m.68'deki belge (imzası ikrar/noterlikçe onaylı belge, resmî kayıt) var mı?
- İtiraz tebliğ/öğrenme tarihi nedir (iptal 1 yıl, kaldırma 6 ay)?
- Borç gerçekten var mı; ödeme/takas/zamanaşımı def'i var mı?
- Tazminat (icra inkâr/kötüniyet) talebi gündemde mi?

## Denetim şeması
1. **Yol seçimi**: m.68'deki nitelikli belge varsa hızlı yol olan **itirazın kaldırılması** (icra mahkemesi, dar inceleme); belge yoksa **itirazın iptali** (genel mahkeme, tam yargılama, m.67).
2. **İtirazın iptali (m.67)**: 1 yıllık hak düşürücü süre; dava kabul edilirse itiraz iptal edilir, takip devam eder. Borçlu itirazında haksız ve alacak likit ise alacaklı lehine en az %20 **icra inkâr tazminatı**; dava reddedilir ve takip kötüniyetli ise borçlu lehine aynı oranda tazminat.
3. **İtirazın kaldırılması (m.68, m.68/a, m.69)**: 6 aylık süre; icra mahkemesi yalnızca belge üzerinden karar verir, yargılama yapmaz. İmzaya itirazın kaldırılması m.68/a usulüne tabidir.
4. **Menfi tespit/istirdat (m.72)**: Borçlu, borçlu olmadığının tespitini takipten önce/sonra isteyebilir; takipten sonra teminatla icranın durdurulması mümkündür. Ödedikten sonra istirdat 1 yıl içinde açılır. Haksız takipte borçlu lehine %20 tazminat.
5. **İspat yükü**: İtirazın kaldırılmasında alacaklı belgeyle; menfi tespitte kural olarak borçlu borcun bulunmadığını, ancak alacağın varlığını alacaklı ispatlar (ispat yükü ters çevrilmez).
6. **Ara sonuç**: Hız/maliyet/ispat gücüne göre yol ve tazminat stratejisi netleşir.

## Çıktı modülleri
- Yol seçim notu (belge envanteri + süre).
- Dava dilekçesi iskeleti (iptal/kaldırma/menfi tespit).
- Tazminat ve teminat değerlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

