---
argument-hint: ''
description: İnternetten yapılan tüketici satışlarında ön bilgilendirme, 14 günlük
  cayma hakkı, iade ve teslim yükümlülüklerinin denetlenmesi veya tüketici/satıcı
  tarafında bir uyuşmazlığın çözülmesi gerektiğinde
name: mesafeli-sozlesmeler-cayma
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
  - ad: Elektronik Ticaretin Düzenlenmesi Hakkında Kanun
    numara: '6563'
    tur: kanun
  - ad: Tüketicinin Korunması Hakkında Kanun
    numara: '6502'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Mesafeli Sözleşmeler ve Cayma Hakkı

## Görev
6502 m.48 ve Mesafeli Sözleşmeler Yönetmeliği kapsamında tüketiciyle elektronik ortamda kurulan satış/hizmet sözleşmelerinde ön bilgilendirme, cayma hakkı, iade ve teslim yükümlülüklerini denetlemek; uyuşmazlığı çözmek.

## Soğuk başlangıç (intake)
- Alıcı tüketici mi (gerçek kişi, ticari amaç dışı)?
- Sözleşme konusu mal mı hizmet mi; cayma istisnası kapsamına giriyor mu (ısmarlama, hızla bozulan, dijital içerik, hijyenik ürün)?
- Ön bilgilendirme formu sunuldu ve onaylandı mı; cayma süresi başladı mı?
- Cayma bildirimi ne zaman, hangi kanaldan yapıldı?

## Denetim şeması
1. Kapsam (6502 m.48): mesafeli sözleşme, satıcı/sağlayıcı ile tüketicinin eş zamanlı fiziksel varlığı olmaksızın, uzaktan iletişim aracıyla kurulan sözleşmedir.
2. Ön bilgilendirme: tüketiciye sözleşme kurulmadan önce malın temel nitelikleri, toplam fiyat, cayma hakkı, teslim ve şikâyet bilgileri yazılı/kalıcı veri saklayıcısıyla verilir; verilmediği takdirde cayma süresi etkilenir.
3. Cayma hakkı: tüketici 14 gün içinde gerekçesiz ve cezasız cayabilir. Süre malda teslim, hizmette sözleşme tarihinden işler. Ön bilgilendirme yapılmamışsa süre uzar (Yönetmelik uyarınca ek süre). Cayma sonrası satıcı bedeli 14 gün içinde iade eder; tüketici malı süresinde geri gönderir.
4. İstisnalar (Yönetmelik): cayma hakkının kullanılamayacağı haller (kişiye özel üretim, çabuk bozulan, ambalajı açılmış hijyenik/dijital ürünler vb.) somut olayla eşleştirilir.
5. Teslim ve ayıp: teslim süresi (kural olarak 30 gün) ve ayıplı maldan sorumluluk (6502 m.8 vd.) ayrıca değerlendirilir.
İspat yükü: ön bilgilendirmenin yapıldığını satıcı, caymanın süresinde olduğunu tüketici ispatlar.
Yol: Tüketici Hakem Heyeti (parasal sınır altında) veya Tüketici Mahkemesi.

## Çıktı modülleri
- Cayma hakkı denetim tablosu (süre-istisna-iade).
- Tüketici Hakem Heyeti/mahkeme başvuru iskeleti.
- Ön bilgilendirme/iade prosedürü düzeltme notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

