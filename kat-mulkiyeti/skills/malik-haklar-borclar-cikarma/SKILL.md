---
argument-hint: ''
description: Kat malikinin bağımsız bölümünü ve ortak yerleri kullanma sınırları,
  komşuluk/sükûnet yükümlülükleri ile borçlarını ağır biçimde ve sürekli ihlal eden
  malikin bağımsız bölümünün devrine (çıkarılmasına
name: malik-haklar-borclar-cikarma
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
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kat Malikinin Hak ve Borçları, Çekilmez Malikin Çıkarılması

## Görev
Kat malikinin haklarının (bağımsız bölümde tasarruf, ortak yerden yararlanma) ve borçlarının (özen, sükûnet, gider) sınırlarını belirlemek; borçlarını ağır ve sürekli ihlal ederek diğer malikler için çekilmez hâle gelen malikin bağımsız bölümünü devre zorlama (çıkarma) davasını (m.25) kurmak.

## Soğuk başlangıç (intake)
- İhlalde bulunan malikin davranışı sürekli mi, tekrarlanıyor mu; yazılı uyarı yapıldı mı?
- Davranış neye ilişkin: ortak giderleri ödememe, ortak yere/komşuya rahatsızlık, ahlaka aykırı kullanım?
- Diğer maliklerin çıkarma istemi için kurul kararı (sayı ve arsa payı çoğunluğu) var mı?
- Daha hafif yaptırımlar (gecikme tazminatı, men davası) denendi mi?

## Denetim şeması
1. **Malikin hakları (KMK m.15-16)**: Malik, kendi bağımsız bölümünde TMK sınırları içinde dilediği gibi tasarruf eder (m.15) ve ortak yerlerden arsa payı oranında yararlanır (m.16). Bu haklar, diğer maliklerin haklarıyla ve yönetim planıyla sınırlıdır.
2. **Borçlar (m.18)**: Kat malikleri, gerek bağımsız bölümlerini gerek ortak yerleri kullanırken doğruluk kurallarına uymak, birbirini rahatsız etmemek, birbirinin haklarını çiğnememek ve yönetim planına uymakla yükümlüdür. Bu yükümlülük kiracı ve diğer kullananları da bağlar (m.18/2).
3. **Çıkarma şartları (m.25)**: Kat maliklerinden biri, borçları ve yükümlülükleri ağır biçimde ve **sürekli** ihlal ederek diğerleri için çekilmez hâle getirirse, **sayı ve arsa payı çoğunluğuyla** alınacak kararla aleyhine dava açılarak bağımsız bölümünün **devri istenir** (mahkeme arsa payına karşılık bedelin ödenmesi suretiyle mülkiyetin devrine hükmeder).
4. **Kanunda sayılan tipik çekilmezlik halleri (m.25/2-3)**: (a) Ortak gider/avans payını haklı sebep olmaksızın ödemediği için **iki takvim yılı içinde üç defa** icra/dava takibine sebep olma; (b) ortak yerlere/sair maliklere bağımsız bölümünü ahlaka aykırı kullandırma vb. Bu hâllerde diğer maliklerin **üçte ikisinin** (sayı çoğunluğu) oyu ile dava açılır.
5. **Önkoşul — ihtar**: Çıkarma davasından önce, ihlalin giderilmesi için süreli ihtar (uyarı) ve kurul kararı gereklidir; hak, dava yoluyla mahkemece kullanılır.
6. **Ara sonuç**: Sürekli ve ağır ihlal + kurul kararı + ihtar varsa devre/çıkarmaya hükmü; aksi hâlde önce men/gider takibi.

## Çıktı modülleri
- Çekilmezlik ihtarı ve kurul kararı taslağı (nisap kontrolü).
- Çıkarma (bağımsız bölümün devri) davası dilekçe iskeleti (m.25).
- Daha hafif yaptırım (men, gider takibi) alternatif yol notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

