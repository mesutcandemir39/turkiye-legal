---
argument-hint: ''
description: Bir sözleşmesel veya yasal ilişkide tarafların hak kullanımı ve borç
  ifasının dürüstlük ölçüsüne uyup uymadığı, yan yükümlülükler veya sözleşme boşluğu
  tartışıldığında TMK m.2/1 süzgecini uygulamak iç
name: durustluk-kurali-tmk-2-1
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dürüstlük Kuralı (TMK m.2/1)

## Görev
Bir hakkın kullanımının ve bir borcun ifasının TMK m.2/1 dürüstlük kuralına (objektif iyiniyet) uygun olup olmadığını denetlemek; yan yükümlülükleri ve sözleşme boşluğunun dürüstlükle doldurulmasını gerekçelendirmek.

## Soğuk başlangıç (intake)
- Hangi hak kullanılıyor / hangi borç ifa ediliyor ve dürüstlüğe aykırı görülen davranış nedir?
- İlişki sözleşmesel mi, yasal mı; sözleşmede açık hüküm var mı yoksa boşluk mu var?
- İddia edilen ihlal bir asıl edim mi, yoksa sadakat/özen/koruma/bilgilendirme gibi yan yükümlülük mü?
- Taraflar tacir mi (özen ölçütü ağırlaşır), tüketici mi?

## Denetim şeması
1. **Objektif ölçüt** — TMK m.2/1: herkes haklarını kullanırken ve borçlarını yerine getirirken dürüstlük kuralına uymak zorundadır. Ölçüt, aynı durumdaki dürüst ve makul kişinin davranışıdır (objektif), kişinin niyeti değil.
2. **Yan yükümlülükler** — Asıl edim yanında sadakat, özen, koruma, bilgilendirme ve sır saklama yükümlülükleri dürüstlük kuralından doğar; ihlali sözleşmeye aykırılık sayılır (TBK m.112 ile bağ).
3. **Sözleşme boşluğunun doldurulması** — Tarafların düzenlemediği nokta önce yedek hukuk kuralıyla, yoksa dürüstlük kuralıyla varsayımsal taraf iradesine göre tamamlanır (TBK m.19 yorumuyla birlikte).
4. **Edimler arası denge** — İfa tarzı, zamanı ve yeri dürüstlükle belirlenir; aşırı katı lafzî ifa talebi dürüstlüğe aykırı olabilir.
5. **İspat** — Dürüstlüğe aykırılığı iddia eden, dayandığı vakıaları TMK m.6 / HMK m.190 uyarınca ispatlar; hâkim açık aykırılığı re'sen gözetebilir.
6. **Sınır** — m.2/1 bağımsız talep kaynağı değildir; mevcut bir ilişkinin içinde çalışır. Hakkın *açıkça kötüye* kullanılması ise m.2/2 ile ayrıca denetlenir (ayrı beceri).

## Çıktı modülleri
- İlişki ve tartışılan davranışın tespiti.
- Yan yükümlülük / boşluk doldurma analizi.
- Objektif dürüstlük ölçütüne göre değerlendirme.
- İspat yükü + ilkesel içtihat `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

