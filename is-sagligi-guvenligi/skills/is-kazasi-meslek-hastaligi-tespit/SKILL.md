---
argument-hint: ''
description: Bir olayın iş kazası veya meslek hastalığı sayılıp sayılmadığını belirlemek,
  bildirim yükümlülüklerini ve sürelerini denetlemek için kullanılır.
name: is-kazasi-meslek-hastaligi-tespit
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
  - ad: İş Sağlığı ve Güvenliği Kanunu
    numara: '6331'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İş Kazası ve Meslek Hastalığı Tespiti ve Bildirim

## Görev
Bir olayı iş kazası (5510 m.13) veya meslek hastalığı (5510 m.14) olarak nitelendirmek, bildirim yükümlülüklerini (6331 m.14, 5510 m.13/2) ve sürelerini denetlemek; eksik/geç bildirimin sonuçlarını çıkarmak.

## Soğuk başlangıç (intake)
- Olay nerede, ne zaman, hangi koşulda gerçekleşti; çalışan o sırada işveren otoritesi altında mıydı?
- Yaralanma/ölüm var mı; sağlık raporu/epikriz mevcut mu?
- SGK'ya ve kolluğa bildirim yapıldı mı, tarihleri ne?
- Meslek hastalığı iddiası varsa maruziyet ve yükümlülük süresi nedir?

## Denetim şeması
1. **İş kazası unsurları (5510 m.13):** Sigortalının (a) işyerinde, (b) işveren tarafından yürütülen iş nedeniyle, (c) işveren tarafından görevle başka yere gönderilmesi sırasında, (d) emziren kadının çocuğuna süt verme zamanlarında, (e) işverence sağlanan taşıtla gidiş-gelişte bedence/ruhça zarara uğraması. Bu hallerden biri varsa iş kazasıdır; illiyet geniş yorumlanır.
2. **Meslek hastalığı (5510 m.14):** İşin niteliğine bağlı maruziyet sonucu hastalık; yükümlülük süresi ve maruziyet süresi listeye göre değerlendirilir, gerekirse Meslek Hastalıkları/SGK Sağlık Kurulu raporu.
3. **Bildirim (6331 m.14, 5510 m.13/2):** İşveren kazayı kazadan sonraki üç iş günü içinde SGK'ya bildirir; ölümlü/ağır kazalarda kolluğa derhal haber verme. İSG kayıt yükümlülüğü ve ramak kala olaylarının kaydı (m.14/2) ayrıca denetlenir.
4. **İspat:** Olayın iş kazası olduğunu kural olarak iddia eden (çalışan/hak sahibi) ortaya koyar; SGK tespiti yoksa iş mahkemesinde tespit davası açılabilir. **Ara sonuç:** Nitelendirme + bildirim durumu netleştir; geç bildirim idari cezaya ve SGK'ya doğan masrafların işverene rücuuna zemin olur.

## Çıktı modülleri
- İş kazası/meslek hastalığı nitelendirme notu (madde altlamalı).
- Bildirim takvimi ve eksiklik raporu.
- Gerekirse tespit davası yol haritası.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

