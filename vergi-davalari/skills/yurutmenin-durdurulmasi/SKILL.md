---
argument-hint: ''
description: Vergi davası açılmasının tahsile etkisini ve İYUK m.27 kapsamında yürütmenin
  durdurulması talebinin koşullarını değerlendirerek tahsilat baskısını yönetmek için
  kullanılır.
name: yurutmenin-durdurulmasi
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
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yürütmenin Durdurulması ve Tahsilatın Önlenmesi

## Görev
Dava açmanın tahsil üzerindeki etkisini doğru saptamak ve gerektiğinde İYUK m.27 uyarınca yürütmenin durdurulması (YD) talebini koşullarıyla kurmak; haciz, e-haciz ve banka blokesi gibi tahsilat işlemlerinin baskısını yönetmek.

## Soğuk başlangıç (intake)
1. Dava konusu işlem tarhiyat (ihbarname) mı, ödeme emri mi, ihtirazi kayıtlı beyan mı?
2. Halihazırda haciz, e-haciz veya banka bloke uygulandı mı?
3. İşlemin uygulanması telafisi güç/imkânsız bir zarar doğuruyor mu (nakit akışı, iş sürekliliği)?
4. Teminat gösterilebilir mi (banka teminat mektubu, gayrimenkul)?

## Denetim şeması
1. **Otomatik durma var mı.** İYUK m.27/4 — tarhiyata karşı vergi mahkemesinde dava açılması, tahsil işlemlerini **kendiliğinden durdurur**; ayrı YD talebine gerek yoktur. Bu istisna yalnızca tarhiyat davasına özgüdür.
2. **Otomatik durmanın olmadığı haller.** Ödeme emrine karşı davada ve ihtirazi kayıtla beyana dayalı davada otomatik durma yoktur; tahsili durdurmak için İYUK m.27 uyarınca YD talebi şarttır.
3. **YD'nin iki koşulu.** İYUK m.27/2 — (i) işlemin açıkça hukuka aykırı olması ve (ii) uygulanması halinde telafisi güç veya imkânsız zararların doğması; bu iki şart birlikte aranır. Gerekçe somut maddi-hukuki dayanakla yazılır.
4. **Teminat.** YD kararıyla birlikte teminat istenebilir; AATUHK m.10'daki teminat türleri değerlendirilir. Tecil (AATUHK m.48) paralel seçenek olarak tartılır.
5. **İtiraz yolu.** İlk derece YD kararına karşı BİM'e itiraz süresi ve usulü (İYUK m.27/7) not edilir. Ara sonuç: hangi işlem için otomatik durma, hangisi için aktif YD talebi gerektiği netleştirilir.

## Çıktı modülleri
- İşlem türüne göre durma haritası (otomatik / talep gerekli).
- YD talep gerekçesi (iki koşulu somutlaştıran metin).
- Teminat/tecil alternatifi notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

