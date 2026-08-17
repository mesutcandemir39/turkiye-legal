---
argument-hint: ''
description: Taşıma senedi, CMR belgesi, irsaliye, teslim makbuzu gibi belgelerin
  düzenlenmesi, içeriği, ispat değeri ve gönderenin beyan sorumluluğunun değerlendirilmesi
  gerektiğinde kullanılır.
name: tasima-senedi-ve-belgeler
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Taşıma Senedi ve Taşıma Belgeleri

## Görev
Taşıma belgelerinin içerik, geçerlilik ve ispat değerini denetlemek; belgelerden doğan karine ve sorumlulukları (özellikle gönderenin beyanlarından doğan sorumluluk) tespit etmek.

## Soğuk başlangıç (intake)
1. Hangi belgeler düzenlendi: taşıma senedi, CMR belgesi, sevk irsaliyesi, teslim makbuzu?
2. Belgede zorunlu kayıtlar (taraflar, eşya cinsi/miktarı, ağırlık, varma yeri) tam mı?
3. Eşyanın durumu/ağırlığı hakkında taşıyıcı şerh (rezerv) koydu mu?
4. Gönderen tehlikeli madde/özel değer beyanında bulundu mu (TTK m.880, m.884)?

## Denetim şeması
1. **Senedin niteliği:** TTK m.856 — taşıma senedi düzenlenmesi tarafların isteğine bağlıdır; geçerlilik şartı değil ispat aracıdır. İçeriği m.856'da sayılır.
2. **İspat değeri/karineler:** TTK m.858 — kurallara uygun düzenlenen senet, sözleşmenin yapıldığına ve içeriğine karine teşkil eder; eşyanın senette yazılı durumda teslim alındığı varsayılır. Taşıyıcının şerhi bu karineyi kırar.
3. **Gönderenin sorumluluğu:** TTK m.864 — senetteki ve verilen bilgilerin doğruluğundan gönderen sorumludur; yanlış/eksik beyandan doğan zararı tazmin eder. CMR m.7.
4. **Tehlikeli eşya:** TTK m.868 — gönderen tehlikeli eşyanın niteliğini ve önlemleri bildirmekle yükümlüdür; bildirmezse doğan zarardan sorumlu olur.
5. **Değer/menfaat beyanı:** TTK m.880-881 — eşyanın değerinin veya teslim menfaatinin senede yazılması, sorumluluk sınırının (m.882) aşılmasını sağlar.
6. **Emre/nama yazılı belgeler:** Taşıma senedi emre yazılı düzenlenebilir; tasarruf hakkı ve devir bu çerçevede değerlendirilir.
7. **Ara sonuç:** Belgelerin doğurduğu karineler, ispat dağılımı ve gönderen-taşıyıcı sorumluluk paylaşımı.

## Çıktı modülleri
- Belge envanteri ve zorunlu kayıt eksiklik tablosu.
- Karine/şerh analizi (lehte-aleyhte ispat etkisi).
- Beyan sorumluluğu ve değer beyanının sınır üzerindeki etkisine ilişkin not.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

