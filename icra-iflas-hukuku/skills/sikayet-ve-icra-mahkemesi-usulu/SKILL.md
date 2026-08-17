---
argument-hint: ''
description: İcra dairesinin işlemlerine karşı kanuna aykırılık veya hadiseye uygunsuzluk
  nedeniyle icra mahkemesine şikâyet etmek; süreli-süresiz şikâyet ayrımını ve icra
  memuru muamelelerini denetlemek gerektiği
name: sikayet-ve-icra-mahkemesi-usulu
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
  - ad: İcra ve İflas Kanunu
    numara: '2004'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Şikâyet ve İcra Mahkemesi Usulü

## Görev
İcra/iflas dairesinin işlemlerine karşı şikâyet yolunu (m.16-18) doğru kullanmak; itiraz ile şikâyeti ayırmak; süreli ve süresiz şikâyet hallerini ve icra mahkemesinin inceleme usulünü yönetmek.

## Soğuk başlangıç (intake)
- Şikâyet konusu işlem ne; kanuna mı aykırı, hadiseye mi uygunsuz?
- İşlem öğrenildi/tebliğ edildi mi (7 günlük süre)?
- İddia kamu düzeniyle mi ilgili (süresiz şikâyet)?
- İşlem itiraz konusu mu, yoksa şikâyet konusu mu?

## Denetim şeması
1. **İtiraz/şikâyet ayrımı**: Borca/imzaya itiraz alacağın esasına yöneliktir ve icra dairesine/icra mahkemesine yapılır; şikâyet ise dairenin **işleminin** kanuna/usule aykırılığına yöneliktir (m.16).
2. **Süreli şikâyet (m.16/I)**: İşlemin öğrenilmesinden itibaren 7 gün içinde icra mahkemesine yapılır.
3. **Süresiz şikâyet (m.16/II)**: Bir hakkın yerine getirilmemesi/sebepsiz sürüncemede bırakılması ve kamu düzenine aykırı işlemler (ör. kambiyo vasfı eksikliği, haczedilmezlik gibi kamu düzeni ilgili haller) süreye bağlı olmaksızın şikâyet edilebilir.
4. **İnceleme usulü (m.18)**: İcra mahkemesi kural olarak basit yargılama usulüyle, çoğu kez evrak üzerinden ve duruşmasız inceler; aksi belirtilmedikçe taraflar çağrılmaz.
5. **Sonuç**: Şikâyet kabul edilirse işlem iptal/düzeltme/yapılması yönünde karar verilir (m.17); karar kanun yoluna (istinaf) tabi olabilir.
6. **Ara sonuç**: Doğru yol (itiraz mı şikâyet mi), süre durumu ve beklenen karar belirlenir.

## Çıktı modülleri
- İtiraz/şikâyet ayrım notu.
- Şikâyet dilekçesi taslağı (süreli/süresiz dayanağıyla).
- İnceleme usulü ve kanun yolu öngörüsü.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

