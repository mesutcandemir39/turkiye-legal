---
argument-hint: ''
description: İş sağlığı ve güvenliği dosyasının hangi eksende (idari uyum, iş kazası
  tazminatı, SGK rücuu, ceza) ele alınacağını ve 6331 ile 5510-TBK katmanlarının nasıl
  ayrıştırılacağını belirlemek için kullanılı
name: temel-kavramlar-ve-sistem
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


# Temel Kavramlar ve Sistematik

## Görev
İSG dosyasını üç hukuki katmana ayırmak (idari/önleyici 6331; sosyal güvenlik 5510; tazminat TBK), olayı doğru eksene oturtmak ve sonraki becerilere yön vermek. Çoğu dosya karmadır; her katman ayrı altlanır.

## Soğuk başlangıç (intake)
- İşyerinin tehlike sınıfı (az tehlikeli / tehlikeli / çok tehlikeli) ve toplam çalışan sayısı nedir?
- Talep ne yönde: idari ceza/uyum mu, iş kazası-meslek hastalığı tazminatı mı, SGK rücuu mu, ceza soruşturması mı?
- Somut bir kaza/olay var mı; varsa SGK bildirimi yapıldı mı, kusur/bilirkişi raporu mevcut mu?
- Müvekkil sıfatı: işveren mi, çalışan/hak sahibi mi, İSG profesyoneli mi?

## Denetim şeması
1. **Kapsam (6331 m.2):** İşyeri ve çalışan 6331 kapsamında mı? Kapsam dışı istisnaları ele (ör. Kanun m.2/2'deki sınırlı haller). Kapsam belirlenmeden yükümlülük tartışılmaz.
2. **Tehlike sınıfı süzgeci:** İş güvenliği uzmanı/işyeri hekimi zorunluluğu, kurul kuruluşu (m.22 — 50+ çalışan ve altı aydan fazla süren işler), eğitim periyotları tehlike sınıfına bağlıdır. Sınıfı yanlış belirlemek tüm değerlendirmeyi bozar.
3. **Eksen ayrımı:**
   - İdari uyum/ceza → 6331 m.4-22 yükümlülükleri + m.26 idari para cezası.
   - Tazminat → işverenin gözetme borcu (TBK m.417/2), zarar haksız fiile tabi (m.417/3, m.49 vd.).
   - SGK rücuu → 5510 m.21, işverenin kusuru oranında.
   - Ceza → TCK m.85-89 (taksirle öldürme/yaralama), kusur ve öngörülebilirlik.
4. **Ara sonuç:** Her eksen için ayrı bir not düş; ispat yükü ve görevli merci farklıdır (idari ceza → sulh ceza hâkimliği itirazı; tazminat ve rücu → iş mahkemesi).
5. **İstisna/öncelik:** İşveren vekili, alt işveren-asıl işveren birlikteliği ve geçici iş ilişkisi varsa sorumlu süjeyi netleştir.

## Çıktı modülleri
- Eksen haritası (idari / SGK / tazminat / ceza) tablosu.
- Tehlike sınıfı ve çalışan sayısına göre yükümlülük matrisi.
- Sonraki becerilere yönlendirme notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

