---
argument-hint: ''
description: Kullanıcı bir kira uyuşmazlığını ilk kez sunduğunda, sözleşmeyi nitelendirmek
  (konut, çatılı işyeri, ürün kirası), genel ve özel hükümler ayrımını kurmak ve hangi
  rejimin uygulanacağını saptamak için
name: kira-temel-kavramlar-ve-sistem
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


# Temel Kavramlar ve Kira Sözleşmesi Sistematiği

## Görev
Önüne gelen kira ilişkisini doğru hukuki rejime oturtmak: TBK genel hükümleri (m.299-338), konut/çatılı işyeri kiraları (m.339-356) ve ürün kirası (m.357 vd.) arasında ayrım yapmak; emredici-koruyucu kuralların devreye girip girmediğini belirlemek.

## Soğuk başlangıç (intake)
- Kiralanan taşınmaz konut mu, işyeri mi, arsa/depo/tarım arazisi mi; çatılı bir yapı mı?
- Sözleşme yazılı mı, tarihi nedir (1.7.2012 öncesi/sonrası)?
- Belirli süreli mi, belirsiz süreli mi; kaç yıldır devam ediyor?
- Taraflar kim (gerçek/tüzel kişi), kiraya veren malik mi?
- Talep ne: tahliye mi, kira tespiti/alacak mı, ayıp/onarım mı?

## Denetim şeması
1. **Tür tespiti**: TBK m.299 kira sözleşmesinin genel tanımıdır. Konut ve çatılı işyeri kiraları için koruyucu rejim (m.339 vd.) uygulanır. m.339/2: geçici kullanım amaçlı en çok altı aylık kiralar bu özel hükümlerin dışındadır. Ürün/hasılat kirasında (m.357) bağımsız bir rejim işler.
2. **Çatılı işyeri/konut niteliği**: Üstü örtülü, bağımsız kullanıma elverişli yer. Niteleme yanlışsa tüm denetim şeması kayar; bu yüzden tapu, kullanım amacı ve fiili durum birlikte değerlendirilir.
3. **Emredici süzgeç**: m.343 (kiracı aleyhine değişiklik), m.346 (kiracı aleyhine düzenleme — gecikme cezası/muacceliyet yasağı), m.342 (güvence en çok üç aylık kira). Sözleşmedeki aykırı kayıtlar kiracı yönünden geçersizdir.
4. **Geçiş hükmü**: 6101 sayılı Kanun, 6098'in kira hükümlerinin eski sözleşmelere uygulanma esaslarını belirler; özellikle m.344 ve m.346'nın yürürlüğü açısından doğrula.
5. **Ara sonuç**: Uygulanacak rejim + tarafın sıfatı + koruyucu kuralların etkisi tek paragrafta sabitlenir; sonraki tüm becerilerin temeli budur.

## Çıktı modülleri
- Niteleme notu (tür + rejim + emredici kurallar).
- Tespit edilen eksik bilgi listesi.
- İlgili özel beceriye yönlendirme (tahliye, kira tespiti, ayıp vb.).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

