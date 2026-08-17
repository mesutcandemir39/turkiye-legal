---
argument-hint: ''
description: Borçlunun iflasını istemek (takipli/doğrudan iflas), iflas davasını yürütmek,
  iflasın açılmasının sonuçlarını ve masanın tasfiyesini yönetmek gerektiğinde; tacirin
  iflası, alacak kaydı ve sıra cetveli
name: iflas-yollari-ve-masasi
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


# İflas Yolları ve İflas Masası

## Görev
İflasa tabi borçlu hakkında takipli iflas (m.155 vd.) veya doğrudan doğruya iflas (m.177) yolunu seçmek; iflas davasını ticaret mahkemesinde yürütmek; iflasın açılmasının sonuçlarını ve masanın tasfiyesini (adi/basit) yönetmek.

## Soğuk başlangıç (intake)
- Borçlu İİK m.43 anlamında iflasa tabi mi (tacir/şirket)?
- Takipli iflas için ödeme emrine itiraz/ödeme yapıldı mı; depo süresi işledi mi?
- Doğrudan iflas sebeplerinden biri (m.177) var mı?
- Alacaklı isen alacağını masaya kaydettirme süresi geçti mi?

## Denetim şeması
1. **Takipli iflas (m.155-166)**: İflas yoluyla takip talebi → iflas ödeme emri → itiraz edilmez/ödenmezse alacaklı 1 yıl içinde ticaret mahkemesinde iflas davası açar. Mahkeme depo kararı verir; borç ödenmezse iflasa karar verilir.
2. **Doğrudan iflas (m.177-178)**: Borçlunun yerinin bilinmemesi, taahhütlerden kaçınması, ödemelerin tatili gibi hallerde takip şartı aranmadan iflas istenir; borçlu da kendi iflasını isteyebilir (m.178).
3. **İflasın açılması sonuçları (m.184 vd.)**: Borçlunun malları iflas masasını oluşturur; tasarruf yetkisi kısıtlanır; takipler durur, müflisin alacakları muaccel hale gelir.
4. **Tasfiye usulü**: Masa, adi (m.208 vd.) veya basit tasfiye (m.218) ile tasfiye edilir; iflas idaresi ve alacaklılar toplantısı görev yapar.
5. **Alacak kaydı ve sıra (m.206-207)**: Alacaklılar alacağını kaydettirir; iflas idaresi sıra cetveli düzenler; itiraz icra/ticaret mahkemesi ayrımına göre yürütülür.
6. **Ara sonuç**: İflas kararının ihtimali, tasfiye türü ve alacak tahsil beklentisi belirlenir.

## Çıktı modülleri
- İflas yolu seçim notu ve dava dilekçesi iskeleti.
- Masaya alacak kaydı ve takip durumu tablosu.
- Tasfiye/sıra cetveli akış planı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

