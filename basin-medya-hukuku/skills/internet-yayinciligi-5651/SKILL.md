---
argument-hint: ''
description: İnternette yayımlanan içeriğin kişilik hakkını ihlali nedeniyle içeriğin
  çıkarılması veya erişimin engellenmesi, içerik/yer/erişim sağlayıcı sorumluluğu
  ve unutulma hakkı söz konusu olduğunda kullanıl
name: internet-yayinciligi-5651
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


# İnternet Yayıncılığı ve Erişim Engelleme (5651)

## Görev
5651 sayılı Kanun kapsamında içeriğin çıkarılması ve erişimin engellenmesi yollarını işletmek; içerik/yer/erişim sağlayıcı sorumluluğunu ve unutulma hakkını değerlendirmek.

## Soğuk başlangıç (intake)
1. İhlal eden içeriğin tam URL'si ve yayın tarihi nedir?
2. İçerik sağlayıcıya başvuru yapıldı mı, sonuç ne oldu?
3. İhlal kişilik hakkı mı yoksa özel hayatın gizliliği mi?
4. İçerik güncel haber değeri taşıyor mu (unutulma hakkı analizi)?

## Denetim şeması
1. **Sorumluluk türleri**: İçerik sağlayıcı kendi içeriğinden sorumludur; yer sağlayıcı uyar-kaldır rejimine tabidir; erişim sağlayıcı hâkimlik/Kurum kararını uygular.
2. **Kişilik hakkı yolu (m.9)**: İhlale uğrayan kişi içerik/yer sağlayıcıdan içeriğin çıkarılmasını ister; sonuç alamazsa sulh ceza hâkimliğine başvurur. Hâkim, ihlali oluşturan kısma yönelik (URL bazlı) erişimin engellenmesine karar verir; ölçülülük esastır.
3. **Özel hayat (m.9/A)**: Özel hayatın gizliliği ihlalinde, gecikmesinde sakınca bulunan hâllerde BTK Başkanı re'sen erişimi engelleyebilir; karar sulh ceza hâkimliği onayına sunulur.
4. **Unutulma hakkı**: Eski haberin güncel kamu yararı kalmamışsa, arama sonuçlarından çıkarılması/indekslenmemesi talep edilebilir; kamu yararı ile kişisel menfaat tartımı yapılır [ilkesel; AYM ve Yargıtay HGK içtihadı doğrulanacak].
5. **Ara sonuç**: İhlal sabit, ölçülü ve URL'ye özgülenmiş talepse erişim engelleme/içeriğin çıkarılması kabule değer.

## Çıktı modülleri
- İçerik/yer sağlayıcıya uyar-kaldır bildirimi
- Sulh ceza hâkimliğine m.9 başvuru dilekçesi (URL listeli)
- Unutulma hakkı tartım notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

