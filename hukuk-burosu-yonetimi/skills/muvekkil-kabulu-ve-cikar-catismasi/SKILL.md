---
argument-hint: ''
description: Yeni bir iş veya müvekkil teklifi geldiğinde dosya açmadan önce çıkar
  çatışması taraması, kabul-ret kararı ve kabul koşullarının belirlenmesi gerektiğinde
  kullanılır.
name: muvekkil-kabulu-ve-cikar-catismasi
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
  - ad: Avukatlık Kanunu
    numara: '1136'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Müvekkil Kabulü ve Çıkar Çatışması Taraması

## Görev
Yeni bir müvekkil/iş teklifi geldiğinde, işin kabul edilip edilemeyeceğini meslek hukuku açısından denetlemek; çıkar çatışmasını taramak; kabul edilebilirse kabul koşullarını (kapsam, ücret, masraf) çerçevelemek.

## Soğuk başlangıç (intake)
1. Karşı taraf(lar) ve gerçek lehtar kim? Tam kimlik/unvan nedir?
2. Büro daha önce bu işte, karşı tarafta veya bağlantılı bir uyuşmazlıkta yer aldı mı?
3. İşin türü, değeri ve aciliyeti (yaklaşan bir süre var mı) nedir?
4. Müvekkil başka bir avukattan bu iş için vekâlet aldı/azletti mi?

## Denetim şeması
1. **Çıkar çatışması (1136 m.38; TBB Meslek Kuralları m.35-37)**: Aynı işte karşı tarafa hukuki yardım, ya da menfaati çatışan başka bir müvekkilin temsili yasaktır. Büro müvekkil/karşı taraf veri tabanı taranır. Çatışma varsa iş REDDEDİLİR; geçmiş müvekkile ait sır söz konusuysa m.36 sır saklama yükümlülüğü devam eder.
2. **Sır ve bilgi engeli**: Çatışma "olası" düzeydeyse, bilgi bariyeri yeterli değildir; Türk hukukunda kural ret yönündedir.
3. **Yetki/uzmanlık ve kapasite**: İşin gerektirdiği süre/uzmanlık karşılanamıyorsa kabul edilmez (özen borcu, TBK m.506).
4. **Süre kontrolü**: Yaklaşan zamanaşımı/hak düşürücü süre/dava süresi varsa, kabul ancak süreye yetişilebiliyorsa anlamlıdır; aksi halde müvekkil derhal uyarılır.
5. **Ücret ve sözleşme (1136 m.163-164)**: Avukatlık ücreti sözleşme ile belirlenir; yazılılık esastır. Asgari Ücret Tarifesi altına inilemez. Karşı taraf vekâlet ücreti avukata aittir (m.164/son).
6. **Ara sonuç**: Çatışma yok + kapasite var + süreye yetişilir ise KABUL; aksi halde gerekçeli RET ve gerekirse yönlendirme.

## Çıktı modülleri
- Çatışma tarama sonucu (taranan isimler, sonuç).
- Kabul/ret kararı ve gerekçesi.
- Kabul halinde: avukatlık sözleşmesi taslağı, vekâletname kalemi listesi, kritik süre uyarısı.
- Reddedilen işte sır saklama hatırlatması.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

