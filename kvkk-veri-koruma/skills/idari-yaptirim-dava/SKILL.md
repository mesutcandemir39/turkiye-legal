---
argument-hint: ''
description: Kurul'un idari para cezası veya işleme durdurma kararı verdiği durumlarda;
  yaptırımın hukuka uygunluğu, savunma stratejisi ve karara karşı dava yolu (7499
  sonrası idare mahkemesi) değerlendirilirken k
name: idari-yaptirim-dava
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İdari Yaptırım ve Kurul Kararına Karşı Dava

## Görev
KVKK m.18 idari para cezalarını ve Kurul'un idari işlemlerini değerlendirmek; savunma hazırlamak ve 7499 sayılı Kanunla değişen dava yolunu doğru kurgulamak.

## Soğuk başlangıç (intake)
1. Kurul kararı hangi yükümlülük ihlaline dayanıyor (aydınlatma, güvenlik, bildirim, sicil, Kurul kararına uymama)?
2. Karar müvekkile ne zaman tebliğ edildi (dava açma süresi tebliğden başlar)?
3. Verilen ceza miktarı ve gerekçesi nedir; orantılı mı?
4. Kurul soruşturmasında savunma usulüne uygun alındı mı?

## Denetim şeması
1. **Yaptırım kategorileri — m.18/1**: (a) aydınlatma yükümlülüğüne aykırılık, (b) veri güvenliği yükümlülüklerine aykırılık (m.12), (c) Kurul kararlarını yerine getirmeme, (ç) VERBİS kayıt/bildirim yükümlülüğüne aykırılık için ayrı ayrı idari para cezası öngörülmüştür. Cezalar her yıl yeniden değerleme oranıyla güncellenir [güncel tutarlar doğrulanacak — kvkk.gov.tr].
2. **Orantılılık ve gerekçe**: İdari yaptırım, Kabahatler Kanunu m.17 ve idare hukuku ilkeleri uyarınca orantılı ve gerekçeli olmalıdır; eylemin ağırlığı, kusur, tekerrür ve elde edilen yarar dikkate alınır.
3. **Dava yolu (7499 sonrası)**: 7499 sayılı Kanunla m.18'e eklenen hükümle, idari para cezalarına karşı dava yolu sulh ceza hâkimliğinden idare mahkemesine taşınmıştır. İdari yaptırım kararının iptali için 2577 sayılı İYUK uyarınca idare mahkemesinde iptal davası açılır; geçiş hükümleri ve tebliğ tarihine göre yetkili merci dikkatle belirlenmelidir.
4. **Süre**: İYUK m.7 uyarınca tebliğden itibaren 60 günlük dava açma süresi; gerekiyorsa yürütmenin durdurulması talep edilir (İYUK m.27).
5. **Ara sonuç**: Savunmada usule (savunma hakkı, gerekçe, orantılılık) ve esasa (işleme şartının varlığı, m.4 uyumu) birlikte girilir.

İspat yükü: İşlemenin hukuka uygunluğunu veri sorumlusu; yaptırımın maddi/hukuki dayanağını idare gerekçeli kararla ortaya koyar.

## Çıktı modülleri
- Kurul kararı analiz ve savunma stratejisi notu.
- İdare mahkemesinde iptal dilekçesi iskeleti (İYUK uyumlu).
- Yürütmeyi durdurma talebi gerekçe taslağı ve süre hesabı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

