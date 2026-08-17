---
argument-hint: ''
description: Rehinle temin edilmiş ve imtiyazlı alacakların mühlet, çoğunluk ve tasdik
  aşamalarındaki özel rejimini çözümlemek gerektiğinde kullanılır.
name: rehinli-imtiyazli-alacaklar
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


# Rehinli ve İmtiyazlı Alacaklıların Konumu

## Görev
Konkordatoda en hassas alacaklı gruplarının özel rejimini çözmek: rehinli alacaklıların takip/satış kısıtı, müzakere ve faiz konumu (İİK m.295, m.308/h) ile imtiyazlı alacakların (m.206) çoğunluk dışılığı ve tam ödeme güvencesi.

## Soğuk başlangıç (intake)
- Rehinli alacaklı kim, rehnin kapsadığı malın değeri alacağı karşılıyor mu?
- İmtiyazlı alacaklar (işçi alacakları, nafaka vb. — m.206) var mı?
- Rehinli alacaklılarla ayrı bir anlaşma öngörülüyor mu?
- Mühlet içinde rehnin paraya çevrilmesi talebi var mı?

## Denetim şeması
1. **Rehinli alacaklar — mühlet etkisi (m.295).** Rehnin paraya çevrilmesi yoluyla takip mühletten etkilenmez şekilde başlatılabilir/sürdürülebilir; ancak muhafaza tedbiri alınamaz ve rehinli malın satışı gerçekleştirilemez. Bu sınır titizlikle uygulanır.
2. **Rehinli alacakla anlaşma (m.308/h).** Tasdik kararında, rehinle temin edilmiş alacaklar için yapılandırma (vade, faiz, taksit) ayrıca düzenlenebilir; rehinli alacaklı projenin adi alacaklara ilişkin kısmına oy veremez ölçüde teminat altındaki bölümüyle çoğunluk dışıdır.
3. **İmtiyazlı alacaklar (m.206).** Birinci sıra imtiyazlı alacaklar (örn. işçilik alacakları, nafaka) çoğunluk hesabına katılmaz (m.302/4) ve tasdik için tam ödenmelerinin güvenceye bağlanması şarttır (m.305/1-b), alacaklı feragat etmedikçe.
4. **Karşılıksız kalan rehin bölümü.** Rehin değeri alacağı karşılamıyorsa açık kalan kısım adi alacak gibi işlem görür ve çoğunluk ile yapılandırmaya tabi olur; rehin değerinin tespiti (bilirkişi) önem taşır. İspat: rehin değeri ve alacak tutarı belgeyle ortaya konur.
5. **Ara sonuç.** Her alacaklı grubunun çoğunluk hesabındaki ve tasdikteki konumu netleştirilir; güvence mekanizması (teminat, depo) belirlenir.

## Çıktı modülleri
- Alacaklı sınıf haritası (rehinli/imtiyazlı/adi) ve oy ağırlıkları.
- Rehin değer tespiti ihtiyaç notu.
- İmtiyazlı alacak güvence planı.
- Rehinli alacaklıyla yapılandırma şartı taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

