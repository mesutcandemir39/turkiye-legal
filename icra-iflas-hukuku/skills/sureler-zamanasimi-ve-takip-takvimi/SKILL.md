---
argument-hint: ''
description: İcra-iflas dosyasındaki tüm hak düşürücü süreleri, takip ve dava zamanaşımlarını
  ve dosyanın işlemden kalkmaması için kritik tarihleri tek tabloda çıkarmak gerektiğinde
  kullanılır.
name: sureler-zamanasimi-ve-takip-takvimi
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


# Süreler, Zamanaşımı ve Takip Takvimi

## Görev
Dosyadaki bütün süreleri (itiraz, şikâyet, dava açma, haciz/satış isteme, zamanaşımı) tek bir takvimde toplamak; süre kaçırma ve dosyanın işlemden kalkması riskini önlemek.

## Soğuk başlangıç (intake)
- Takip yolu hangisi (ilamsız/ilamlı/kambiyo)?
- Ödeme/icra emri tebliğ tarihi nedir?
- Hangi aşamadayız (itiraz, haciz, satış, dağıtım)?
- Alacağın maddi hukuk zamanaşımı ne (TBK/TTK)?

## Denetim şeması
1. **İtiraz süreleri**: İlamsızda ödeme emrine itiraz 7 gün (m.62); kambiyoda borca/imzaya itiraz 5 gün (m.168/4-5). Süreler tebliğden işler ve kesindir.
2. **Dava süreleri**: İtirazın iptali 1 yıl (m.67); itirazın kaldırılması 6 ay (m.68); istirdat 1 yıl (m.72); tasarrufun iptali 5 yıllık zamanaşımı (m.284); ihalenin feshi 7 gün (m.134).
3. **Takip işlemleri süreleri**: Haciz isteme 1 yıl (m.78); satış isteme süreleri ve elektronik artırma takvimi; aksi halde haciz/dosya düşer ve yenileme gerekir.
4. **Takip zamanaşımı vs. maddi hukuk zamanaşımı**: İlama dayalı alacakta ilamların zamanaşımı 10 yıl (m.39); ilamsız alacakta dayanağın maddi hukuk zamanaşımı (TBK m.146 genel 10 yıl, m.147 istisnalar 5 yıl; kambiyoda TTK özel süreleri; çekte 5941 s.K.) ayrıca denetlenir.
5. **Sürelerin durması/kesilmesi**: Adli tatil, takip işlemleri ve dava açılmasıyla kesilme; her tarih için dayanağı not edilir.
6. **Ara sonuç**: Kritik tarihlerin renk kodlu takvimi ve uyarı eşikleri oluşturulur.

## Çıktı modülleri
- Tek tablo süre/zamanaşımı takvimi (tarih × işlem × dayanak).
- Yenileme/düşme uyarı listesi.
- Maddi hukuk + takip zamanaşımı çapraz kontrolü.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

