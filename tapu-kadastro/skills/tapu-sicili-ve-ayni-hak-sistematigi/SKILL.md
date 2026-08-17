---
argument-hint: ''
description: Taşınmaz üzerindeki ayni hakların kuruluş ve devir mantığını, tescilin
  kurucu etkisini, tescilli ve tescilsiz kazanım ayrımını ve sicil ilkelerini çözümlerken;
  bir tapu kaydının ne anlama geldiğini ve
name: tapu-sicili-ve-ayni-hak-sistematigi
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
  - ad: Tapu Kanunu
    numara: '3402'
    tur: kanun
  - ad: Kat Özel Koşulu Olmak Üzere Yapılan Satış Mukavelelerine Dair Kanun
    numara: '2644'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tapu Sicili ve Ayni Hak Sistematiği

## Görev
Taşınmaz üzerindeki ayni hakkın hangi yolla doğduğunu, sicile nasıl yansıdığını ve sicilin sağladığı korumayı sistematik biçimde ortaya koymak; sonraki tüm dava/işlem becerilerine zemin hazırlamak.

## Soğuk başlangıç (intake)
- Taşınmazın güncel tapu kaydını (ada-parsel, malik, edinme sebebi/tarihi, takyidatlar) ve akit tablosu tarihçesini görüyor muyuz?
- İhtilaf hangi hakka ilişkin: mülkiyet mi, sınırlı ayni hak (ipotek/irtifak/intifa) mı, kişisel hakkın şerhi mi?
- Hak nasıl kazanılmış: resmi senetle devir mi, miras/mahkeme kararı/cebri icra (tescilsiz) mi?
- Tapuda görünen malik ile fiili durum (zilyet) örtüşüyor mu?

## Denetim şeması
1. **Kazanım türünü ayır.** Kural: ayni hak ancak tescil ile doğar (TMK m.705/1). İstisna: miras, mahkeme kararı, cebri icra, işgal, kamulaştırma hallerinde hak tescilden önce doğar, tescil açıklayıcıdır (m.705/2) — ancak tasarruf için tescil gerekir.
2. **Resmi şekil şartını denetle.** Taşınmaz mülkiyetini devir borcu doğuran sözleşmeler resmi şekilde, tapu müdürlüğünde yapılır (TMK m.706, TBK m.237, 2644 sayılı Tapu Kanunu m.26). Adi yazılı/harici satış mülkiyet geçirmez; en çok kişisel hak/sebepsiz zenginleşme doğurur.
3. **İllilik (sebebe bağlılık) ilkesini uygula.** Tescil geçerli bir hukuki sebebe (satış, bağış vb.) dayanmazsa yolsuzdur; sebep geçersizse tescil de yolsuz hale gelir.
4. **Aleniyet ve güveni değerlendir.** Sicil aleni kabul edilir (TMK m.1020); kimse sicildeki bir kaydı bilmediğini ileri süremez. İyiniyetli üçüncü kişinin yolsuz tescile güvenerek kazanımı korunur (TMK m.1023) — bu, düzeltme talebinin sınırıdır.
5. **Sınırlı ayni hakları yerleştir.** İpotek (TMK m.881 vd.), intifa/oturma, geçit/kaynak gibi irtifaklar (m.779 vd.) sicildeki sıraya ve içeriğe göre değerlendirilir.
6. **Ara sonuç.** Hakkın türü, kazanım anı, geçerliliği ve üçüncü kişilere karşı durumu tek cümlede sabitlenir.

## Çıktı modülleri
- Taşınmazın hukuki durum özeti (hak türü / malik / edinme sebebi / takyidat tablosu).
- Kazanım türü ve geçerlilik değerlendirmesi (tescilli/tescilsiz, illilik notu).
- Üçüncü kişiye karşı koruma haritası ve sonraki adım önerisi (iptal-tescil, düzeltim, tescil davası).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

