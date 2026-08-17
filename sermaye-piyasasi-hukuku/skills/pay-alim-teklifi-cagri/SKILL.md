---
argument-hint: ''
description: Halka açık ortaklıkta yönetim kontrolünün ele geçirilmesi, zorunlu veya
  gönüllü pay alım teklifi (çağrı), muafiyet halleri ve çağrı yükümlülüğünün doğumu
  değerlendirileceğinde kullanılır.
name: pay-alim-teklifi-cagri
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
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Pay Alım Teklifi (Çağrı) ve Yönetim Devri

## Görev
Halka açık ortaklıkta kontrol değişimi sonucu doğan zorunlu pay alım teklifi (çağrı) yükümlülüğünü SPK m.25-26 ve çağrı tebliği çerçevesinde belirlemek; muafiyet hallerini ve çağrı fiyatını değerlendirmek.

## Soğuk başlangıç (intake)
- Hedef ortaklıkta kontrol/yönetim kim tarafından, hangi oranda ele geçirildi?
- Pay devri doğrudan mı, dolaylı mı; birlikte hareket eden kişiler var mı?
- Çağrı zorunlu mu, gönüllü mü; muafiyet talebi gündemde mi?
- Müvekkil teklifte bulunan, hedef ortaklık yönetimi yoksa azınlık pay sahibi mi?

## Denetim şeması
1. **Kontrol tespiti:** Yönetim kontrolünü sağlayan oran/imtiyazın ele geçirilip geçirilmediği (SPK m.26 ve tebliğdeki eşik) belirlenir; doğrudan/dolaylı edinim ve birlikte hareket eden kişiler değerlendirilir.
2. **Çağrı yükümlülüğünün doğumu:** Kontrolün edinildiği an esas alınarak diğer pay sahiplerine pay alım teklifinde bulunma zorunluluğu doğup doğmadığı saptanır; ara sonuç olarak çağrı zorunlu mu gönüllü mü netleşir.
3. **Muafiyet:** Tebliğde sayılan hallerde (örneğin sermaye artırımına katılım, grup içi yapı değişikliği, finansal güçlük) Kurul'dan muafiyet talep edilebilirliği değerlendirilir.
4. **Çağrı fiyatı:** Asgari çağrı fiyatının belirlenme yöntemi (önceki işlem fiyatları/edinim bedeli) tebliğe göre hesaplanır; eksik fiyatlama azınlık pay sahibi açısından risktir.
5. **Yaptırım/ihlal:** Çağrı yükümlülüğünün ihlali idari yaptırım (m.103) ve oy haklarının kullanımına ilişkin tedbirler doğurur. İspatta edinim tarih ve oranları belge ile kurulur.

## Çıktı modülleri
- Kontrol/çağrı yükümlülüğü analizi
- Muafiyet değerlendirmesi ve başvuru iskeleti
- Çağrı fiyatı hesap notu
- Azınlık pay sahibi için hak/talep çerçevesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

