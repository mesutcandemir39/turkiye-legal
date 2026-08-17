---
argument-hint: ''
description: İş güvenliği uzmanı, işyeri hekimi ve OSGB'lerin görev, yetki ve hukuki-cezai
  sorumluluğunu, işverenle sorumluluk paylaşımını değerlendirmek için kullanılır.
name: isg-profesyonelleri-sorumluluk
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


# İSG Profesyonelleri ve OSGB Sorumluluğu

## Görev
İş güvenliği uzmanı, işyeri hekimi, diğer sağlık personeli ve ortak sağlık güvenlik birimlerinin (OSGB) görev-yetki sınırlarını ve hukuki/cezai sorumluluğunu; işverenle aralarındaki sorumluluk paylaşımını değerlendirmek.

## Soğuk başlangıç (intake)
- Hizmet işyerinin kendi profesyoneli mi, OSGB üzerinden mi sağlanıyor; sözleşme süresi ve atanan görevlendirme süresi ne?
- Uzmanın belge sınıfı (A/B/C) işyerinin tehlike sınıfına uygun mu?
- Kaza/ihlal öncesi uzman/hekim hangi yazılı uyarı, öneri ve tespitleri yaptı; onay defteri (İSG kaydı) işlendi mi?
- Müvekkil işveren mi, profesyonel mi, OSGB mi?

## Denetim şeması
1. **Görevlendirme zorunluluğu (6331 m.6-8):** Tehlike sınıfı ve çalışan sayısına göre uzman/hekim çalıştırma yükümlülüğü; belge sınıfı uyumu (çok tehlikelide (A), tehlikelide en az (B) vb.).
2. **Görev sınırı ve uyarı yükümlülüğü:** Uzman/hekim önleyici öneri ve tespitlerini yazılı bildirmekle yükümlüdür; işveren bu önerilere uymazsa, profesyonel durumu yetkili makama/işverene yazılı bildirerek sorumluluğunu sınırlayabilir. Yazılı uyarının varlığı sorumluluk paylaşımının ekseni.
3. **İşverenin asli sorumluluğu:** İSG hizmeti alınması veya profesyonel görevlendirilmesi, işverenin 6331 m.4 sorumluluğunu kaldırmaz; profesyonelin kusuru işverenin sorumluluğunu sona erdirmez (zincirleme/paylaşımlı sorumluluk).
4. **Cezai sorumluluk:** Kazada profesyonelin görevini gereği gibi yapmaması taksirle ölüm/yaralama (TCK m.85-89) bakımından bağımsız değerlendirilir; kusur dağılımı bilirkişiyle belirlenir.
5. **Sözleşmesel rücu:** İşveren ile OSGB/uzman arasında hizmet sözleşmesine dayalı iç rücu ilişkisi. **Ara sonuç:** Yazılı uyarı zinciri ve kusur dağılımına göre paylaşımı sabitle.

## Çıktı modülleri
- Görev-belge sınıfı uyum tablosu.
- Yazılı uyarı/öneri kronolojisi.
- Sorumluluk paylaşımı ve iç rücu değerlendirme notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

