---
argument-hint: ''
description: Bir yayına karşı cevap ve düzeltme metni hazırlamak, yayımlatmak veya
  yayımlamama hâlinde sulh ceza hâkimliğine başvurmak gerektiğinde; süre ve usul disiplinini
  kurmak için kullanılır.
name: cevap-duzeltme-tekzip
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
  - ad: Basın Meslek İlkeleri ve Yapı İtibarı Hakkında Kanun
    numara: '5187'
    tur: kanun
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Cevap ve Düzeltme (Tekzip)

## Görev
5187 sayılı Kanun m.14 (basılı) ve 6112 sayılı Kanun m.18 (radyo-TV) uyarınca cevap-düzeltme metnini hazırlamak, yayımlatmak ve reddi/ihmali hâlinde sulh ceza hâkimliğine başvuru sürecini yürütmek.

## Soğuk başlangıç (intake)
1. Yayın tarihi ve mecra nedir (basılı/işitsel-görsel/internet)?
2. Düzeltilecek somut ifadeler ve gerçek durum nedir?
3. Başvurucu kişilik hakkı zedelenen kişi mi?
4. Yayından bu yana ne kadar süre geçti?

## Denetim şeması
1. **Hak ve süre**: Basın Kanunu m.14'e göre kişilik hakkı zedelenen kişi, yayından itibaren iki ay içinde, sorumlu müdüre cevap ve düzeltme metnini gönderir. İçeriğin yayını ücretsizdir, hakaret/suç içermemeli ve üçüncü kişilerin haklarını ihlal etmemelidir.
2. **Yayım usulü**: Metin, ilgili yayında (aynı sayfa/sütun, aynı puntoyla) gecikmeksizin yayımlanır. Süreli yayında günlük ise üç gün içinde, diğerlerinde takip eden ilk sayıda yayım kuralı uygulanır (m.14).
3. **Reddi/ihmali**: Sorumlu müdür yayımlamaz veya kurallara aykırı yayımlarsa, ilgili kişi süresi içinde sulh ceza hâkimliğine başvurarak yayım kararı ister. Karara karşı itiraz yolu açıktır.
4. **İnternet**: 5651 sayılı Kanun kapsamındaki içerik için cevap-düzeltme yanında m.9 erişim engelleme/içeriği çıkarma yolu da değerlendirilir.
5. **Ara sonuç**: Metin hukuka uygun, süresinde ve ölçülü ise yayım zorunludur; aksi hâlde hâkimlik kararıyla yayım sağlanır.

## Çıktı modülleri
- Cevap-düzeltme metni taslağı (ölçülü, suç içermeyen)
- Sorumlu müdüre gönderim üst yazısı
- Sulh ceza hâkimliğine başvuru dilekçesi iskeleti



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

