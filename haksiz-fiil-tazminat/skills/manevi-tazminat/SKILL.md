---
argument-hint: ''
description: Ölüm, bedensel bütünlüğün ihlali veya kişilik hakkı saldırısı nedeniyle
  manevi tazminat istenebileceğinde; talebin şartlarını, miktar ölçütlerini ve hak
  sahiplerini belirlemek için kullanılır.
name: manevi-tazminat
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Manevi Tazminat Talebi

## Görev
Manevi zararın varlığını ve manevi tazminatın şartlarını TBK m.56 (bedensel zarar/ölüm) ve m.58 ile TMK m.24-25 (kişilik hakkı) çerçevesinde denetlemek; miktarın hakkaniyet ölçütlerini ve hak sahiplerini belirlemek. Manevi tazminat zenginleşme aracı değildir; tatmin ve denkleştirme amacı taşır.

## Soğuk başlangıç (intake)
- İhlal edilen değer ne (yaşam, beden/sağlık, onur-saygınlık, özel hayat, ad)?
- Ölüm/ağır bedensel zarar varsa yakınların durumu (eş, çocuk, ana-baba) nedir?
- Saldırının ağırlığı, süresi ve tarafların kusur durumu?
- Maddi tazminatla birlikte mi isteniyor?

## Denetim şeması
1. **Hukuki temeli seç.** Bedensel zarar/ölümde TBK m.56; kişilik hakkı ihlalinde TBK m.58 ile TMK m.24-25 birlikte uygulanır. Sözleşmeye aykırılıkta da koşulları varsa kişilik ihlali için manevi tazminat istenebilir.
2. **Şartlar.** Hukuka aykırı fiil, manevi zarar (acı, elem, üzüntü, kişiliğe saldırı) ve illiyet bağı; kusur kural olarak aranır, ancak objektif sorumluluk hallerinde içtihatla manevi tazminat da kabul edilebilir (`[DOĞRULANMADI]`).
3. **Hak sahipleri.** Bedensel zararda doğrudan zarar gören; ölümde ve ağır bedensel zararda yakınlar (m.56/2) manevi tazminat isteyebilir. Talep kişiye sıkı sıkıya bağlıdır; kural olarak devredilmez, mirasçıya kalması sınırlıdır.
4. **Miktar ölçütleri.** Olayın özelliği, tarafların ekonomik-sosyal durumu, kusurun ağırlığı, saldırının niteliği ve ihlalin sonuçları göz önünde tutulur; somut ve gerekçeli takdir gerekir. Tek kalem, bölünmez taleptir.
5. **Birlikte istemler.** Maddi tazminat, durdurma/önleme (TMK m.25) ve özür/yayın gibi taleplerle birlikte değerlendirilir.
6. **Ara sonuç ve ispat.** Manevi zararın varlığını ve ağırlığını zarar gören ortaya koyar; miktarda hâkimin takdiri esastır. Talep sonucu makul ve gerekçeli tutulur.

## Çıktı modülleri
- Talep şartları ve hak sahibi kontrol listesi.
- Miktar gerekçe notu (ölçütler + somut olay).
- Talep sonucu paragrafı taslağı (m.56/m.58 dayanaklı).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

