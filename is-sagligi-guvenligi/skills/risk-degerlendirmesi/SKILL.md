---
argument-hint: ''
description: İşyerinde risk değerlendirmesinin yapılıp yapılmadığını, kapsam ve güncelliğini
  değerlendirmek ve 6331 m.5 önleme hiyerarşisine uygun tedbir tasarlamak için kullanılır.
name: risk-degerlendirmesi
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


# Risk Değerlendirmesi ve Önleme Hiyerarşisi

## Görev
6331 m.10 ve Risk Değerlendirmesi Yönetmeliği çerçevesinde risk değerlendirmesinin varlığı, kapsamı, yöntemi ve güncelliğini denetlemek; m.5 önleme hiyerarşisine göre tedbir önerilerini sıralamak. Hem uyum hem de kaza dosyasında kusur tartışmasının çekirdeğidir.

## Soğuk başlangıç (intake)
- Risk değerlendirmesi yapılmış mı; tarihi ve kullanılan yöntem (ör. matris/L tipi) nedir?
- Tehlike sınıfı nedir (değerlendirmenin yenileme periyodunu belirler)?
- İşyerinde değişiklik (yeni makine, süreç, kaza, ramak kala) sonrası güncelleme yapıldı mı?
- Değerlendirmeye çalışan temsilcisi ve İSG profesyonelleri katıldı mı?

## Denetim şeması
1. **Varlık ve zaman (m.10):** Risk değerlendirmesi yapılmamışsa bu başlı başına yükümlülük ihlalidir; kaza sonrası kusur değerlendirmesinde belirleyici olur.
2. **Kapsam:** Tüm tehlikeler (mekanik, kimyasal, ergonomik, psikososyal, biyolojik) ve etkilenebilecek çalışanlar (genç, gebe, engelli, alt işveren çalışanı) kapsanmış mı?
3. **Yöntem ve güncellik:** Tehlike sınıfına göre yenileme süresi (genelde çok tehlikeli 2, tehlikeli 4, az tehlikeli 6 yıl) ile değişiklik/kaza halinde derhal güncelleme yükümlülüğü.
4. **Önleme hiyerarşisi (m.5):** Önerilen tedbirler sırasıyla: riski ortadan kaldırma → kaynağında önleme → ikame → mühendislik/toplu koruma → idari önlem → kişisel koruyucu donanım. KKD daima son sırada; sadece KKD verilmiş olması yetersizdir.
5. **İspat ve illiyet:** Gerçekleşen kazadaki tehlikenin değerlendirmede öngörülüp öngörülmediği, öngörüldüyse tedbirin uygulanıp uygulanmadığı kusur oranını doğrudan etkiler. **Ara sonuç:** Öngörülmüş + tedbir alınmamış = ağır kusur karinesi.

## Çıktı modülleri
- Risk değerlendirmesi yeterlilik kontrol listesi.
- Tehlike-tedbir-hiyerarşi eşleştirme tablosu.
- Kaza dosyası için "öngörülebilirlik" değerlendirme notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

