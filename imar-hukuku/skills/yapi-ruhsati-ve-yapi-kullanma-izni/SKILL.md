---
argument-hint: ''
description: Yapı ruhsatı, ruhsat yenileme/temdit veya yapı kullanma izni (iskân)
  süreçleri ve bunların reddine karşı dava gündeme geldiğinde; ruhsata tabi işler,
  ruhsat eki projeler ve fenni mesuliyet ilişkisi so
name: yapi-ruhsati-ve-yapi-kullanma-izni
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
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yapı Ruhsatı ve Yapı Kullanma İzni

## Görev
Ruhsat ve iskân süreçlerini denetlemek; ruhsat verilmesi/reddi ya da iptali işlemlerine karşı hukuki yolu kurmak.

## Soğuk başlangıç (intake)
- Yapı yeni mi, ekleme/tadilat mı, basit onarım mı (ruhsata tabi mi)?
- Ruhsat başvurusu yapıldı mı, reddedildiyse gerekçesi ne?
- Plan, imar durumu ve aplikasyon krokisi uygun mu; eksik belge var mı?
- İskân (yapı kullanma izni) talep edildi mi, ruhsata aykırılık var mı?

## Denetim şeması
1. **Ruhsata tabi işler (3194 m.21)**: Kural olarak bütün yapılar ruhsata tabidir. Basit tamir-onarım ve derz, sıva, boya gibi işler ruhsat gerektirmez (m.21/son). Ruhsata tabi olup olmadığı önce ayrılır.
2. **Ruhsat şartları (m.20-22)**: Plan, yönetmelik ve imar durumuna uygunluk; tapu/yapı sahipliği, mimari-statik-mekanik-elektrik projeleri ve fenni mesuller. İdare başvuruyu **30 gün** içinde sonuçlandırır; eksik varsa bildirir, eksik giderilince 15 günde ruhsat verilir.
3. **Ret işleminin denetimi**: Ret gerekçesi plana/yönetmeliğe somut dayandırılmalı; dayanaksız ret, sebep ve gerekçe yönünden sakattır. İdarenin takdiri kamu yararı ve eşitlikle sınırlıdır.
4. **Süre ve temdit (m.29)**: Ruhsat tarihinden itibaren **2 yıl** içinde inşaata başlanmalı, **5 yıl** içinde bitirilmeli; süre dolarsa ruhsat hükümsüz, yeniden ruhsat (temdit) gerekir. Süre geçmesi kazanılmış hak tartışmasını doğurur.
5. **Yapı kullanma izni (m.30)**: Yapı ruhsat ve eklerine uygun tamamlanınca iskân verilir; aykırılık varsa önce m.32/m.42 süreci işler. İskânsız yapıda abonelik ve hukuki sonuçlar sınırlanır.
6. **İspat ve ara sonuç**: Onaylı projeler, yapı denetim raporları, imar durum belgesi delildir. Hukuka aykırı ret/iptal varsa İYUK m.7 süresinde iptal davası; gerekiyorsa YD. Ruhsatın üçüncü kişi (komşu) tarafından iptali davasında menfaat ve süre ayrıca kurulur.

## Çıktı modülleri
- Ruhsat/iskân başvuru belge kontrol listesi.
- Ret işleminin unsur denetimi notu.
- Süre/temdit ve kazanılmış hak değerlendirmesi.
- Ret veya iptale karşı dava dilekçesi iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

