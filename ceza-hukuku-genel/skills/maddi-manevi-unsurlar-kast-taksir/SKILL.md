---
argument-hint: ''
description: Fiilin maddi unsurları (fail, netice, nedensellik) ile manevi unsurun
  kast mı taksir mi olduğunu, olası kast ile bilinçli taksir sınırını ayırt etmek
  gerektiğinde kullanılır.
name: maddi-manevi-unsurlar-kast-taksir
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Maddi ve Manevi Unsurlar — Kast ve Taksir

## Görev
Suçun maddi unsurlarını çözümlemek ve failin manevi durumunu (kast/taksir) doğru sınıflandırmak; özellikle olası kast (TCK m.21/2) ile bilinçli taksir (TCK m.22/3) arasındaki ince sınırı netleştirmek.

## Soğuk başlangıç (intake)
- Netice fail tarafından öngörüldü mü; öngördüyse kabullenildi mi yoksa istenmedi mi?
- Fiil ile netice arasındaki nedensellik zinciri kesintisiz mi?
- Suç tipi taksirle işlenebiliyor mu, yoksa yalnızca kasten mi cezalandırılıyor?
- Failin dikkat ve özen yükümlülüğü neydi, hangi kuralı ihlal etti?

## Denetim şeması
1. **Maddi unsur analizi:** Fail-fiil-netice-konu-mağdur tespiti; ihmali suçlarda garantörlük (TCK m.83, m.88 örnekleri) ve hareketle netice arasında nedensellik ile objektif isnadiyet.
2. **Manevi unsurun esası (m.21/1):** Kast, suçun kanuni tanımındaki unsurların bilerek ve istenerek gerçekleştirilmesidir. Doğrudan kast: netice amaçlanmış ya da zorunlu sonuç olarak öngörülmüştür.
3. **Olası kast (m.21/2):** Fail neticeyi öngörmüş ve "olursa olsun" diyerek kabullenmiştir; ceza belirli oranda indirilir. Ara sonuç: kabulleniş var mı?
4. **Taksir (m.22):** Dikkat ve özen yükümlülüğüne aykırılıkla öngörülmeyen netice. Basit taksirde netice öngörülmemiştir.
5. **Bilinçli taksir (m.22/3):** Fail neticeyi öngörmüş fakat istememiş ve gerçekleşmeyeceğine güvenmiştir; ceza artırılır. Sınır ölçütü: olası kastta kabulleniş, bilinçli taksirde gerçekleşmeyeceğine güven.
6. **Netice sebebiyle ağırlaşma (m.23):** Ağır netice yönünden en az taksir aranır; kusursuz sorumluluk yasaktır. Ara sonuç: ağır netice fail açısından öngörülebilir miydi?

## Çıktı modülleri
- Kast/taksir sınıflandırması ve gerekçe (olay-madde eşlemesi).
- Olası kast vs. bilinçli taksir karşılaştırma tablosu.
- Nedensellik/isnadiyet zinciri şeması.
- İspat için gerekli delil ve `[DOĞRULANMADI]` içtihat notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

