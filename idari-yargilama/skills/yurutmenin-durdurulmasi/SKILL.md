---
argument-hint: ''
description: İdari işlemin uygulanması telafisi güç zarar doğuracaksa ve işlem açıkça
  hukuka aykırıysa geçici koruma talebinin hazırlanmasında kullanılır; YD şartlarının
  değerlendirilmesi, teminat ve itiraz yollar
name: yurutmenin-durdurulmasi
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
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yürütmenin Durdurulması (YD)

## Görev
İYUK m.27 koşullarını somut olaya uygulayarak güçlü gerekçeli bir yürütmenin durdurulması talebi kurmak; itiraz yolu ve usule ilişkin özellikleri yönetmek.

## Soğuk başlangıç (intake)
- İşlemin uygulanması hangi somut ve telafisi güç zararı doğurur?
- İşlemin açık hukuka aykırılığı hangi unsurda ve hangi delille gösterilebilir?
- İşlem henüz uygulanmaya başladı mı; aciliyet derecesi nedir?
- Talep dava dilekçesiyle birlikte mi, ayrı dilekçeyle mi ileri sürülecek?

## Denetim şeması
1. **İki şartın birlikteliği** (İYUK m.27/2): YD kararı için (i) işlemin uygulanması hâlinde **telafisi güç veya imkânsız zarar** doğması ve (ii) işlemin **açıkça hukuka aykırı** olması şartlarının **birlikte** gerçekleşmesi ve kararda **gerekçe** gösterilmesi zorunludur.
2. **Gerekçe zorunluluğu**: YD isteminin reddi veya kabulü gerekçeli olmalıdır; standart kalıp gerekçe yeterli değildir. Talepte iki şart ayrı ayrı somutlaştırılır.
3. **Teminat** (İYUK m.27/6): Kural olarak YD kararı teminat karşılığında verilir; ancak durumun gereklerine göre teminat aranmayabilir. İdareden ve adli yardımdan yararlananlardan teminat alınmaz.
4. **Vergi davalarında özel rejim**: Vergi mahkemelerinde dava açılması tarh edilen vergi/cezanın tahsilini kural olarak durdurur (İYUK m.27/4); bu nedenle ayrı YD talebine her zaman gerek olmayabilir. İhtirazi kayıt ve ödeme emri hâlleri ayrıdır.
5. **İtiraz** (İYUK m.27/7): YD istemleri hakkındaki kararlara karşı, kararın tebliğini izleyen günden itibaren **7 gün** içinde bir defaya mahsus itiraz edilebilir. İtirazı, idare/vergi mahkemesi kararlarında bölge idare mahkemesi inceler.
6. **Ara sonuç**: YD kararı işlemin tesisinden önceki hukuki durumu askıya alır; idare kararın gereğini gecikmeksizin uygulamak zorundadır (Anayasa m.138/4; İYUK m.28).

## Çıktı modülleri
- m.27 iki şart için somut gerekçe metni
- Teminat ve aciliyet değerlendirmesi
- YD talep paragrafı (dilekçeye eklenebilir)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

