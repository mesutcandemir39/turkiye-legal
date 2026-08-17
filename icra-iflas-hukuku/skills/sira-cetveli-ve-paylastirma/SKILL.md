---
argument-hint: ''
description: Hacze birden çok alacaklı katıldığında veya iflasta, satış bedelinin
  alacaklılar arasında hangi sırayla dağıtılacağını belirlemek ve sıra cetveline itiraz/şikâyet
  etmek gerektiğinde kullanılır.
name: sira-cetveli-ve-paylastirma
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


# Sıra Cetveli ve Paraların Paylaştırılması

## Görev
Satıştan elde edilen bedeli alacaklılar arasında doğru sırayla paylaştırmak; rehinli, imtiyazlı ve adi alacakların sırasını belirlemek; sıra cetveline karşı sıra (icra mahkemesi) veya esas (genel mahkeme) itirazını yürütmek.

## Soğuk başlangıç (intake)
- Birden çok haciz/alacaklı var mı; iflas masası söz konusu mu?
- Rehinli alacak var mı (öncelik); kamu alacağı (6183) gündemde mi?
- Sıra cetveli tebliğ edildi mi (7 günlük itiraz süresi)?
- İtirazın konusu sıraya mı, alacağın esasına/miktarına mı yönelik?

## Denetim şeması
1. **Garameten paylaşım kuralı (m.140)**: Satış tutarı tüm alacakları karşılamıyorsa icra müdürü sıra cetveli düzenler; aynı derecedeki alacaklılar arasında garameten (oranlı) paylaşım yapılır.
2. **Öncelik sırası**: Rehinli alacaklar rehin konusu bedelden öncelikle ödenir (m.151 vd.); kamu alacaklarının önceliği 6183 s.K. çerçevesinde değerlendirilir; iflasta alacak sıraları İİK m.206-207'ye göre belirlenir (rehinli, imtiyazlı I-IV, adi).
3. **İtiraz türü (m.142)**: Sıraya itiraz icra mahkemesine; alacağın esasına/miktarına itiraz genel mahkemede ayrı davayla ileri sürülür. Süre tebliğden 7 gündür.
4. **İspat yükü**: İtiraz eden, cetveldeki tertibin/alacağın hatalı olduğunu ispatlar; muvazaa/sıra önceliği iddiaları belgeyle desteklenir.
5. **Hacze iştirak etkisi**: m.100/101 iştiraki cetveldeki payları değiştirir; ilk haciz tarihi belirleyicidir.
6. **Ara sonuç**: Düzeltilmiş dağıtım tablosu ve itiraz stratejisi oluşturulur.

## Çıktı modülleri
- Sıra/dağıtım tablosu (alacaklı × sıra × pay).
- Sıra cetveline itiraz dilekçesi (sıra/esas ayrımıyla).
- Öncelik analizi (rehinli/imtiyazlı/kamu/adi).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

