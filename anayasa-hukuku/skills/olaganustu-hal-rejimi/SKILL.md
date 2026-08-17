---
argument-hint: ''
description: Olağanüstü hâl döneminde alınan tedbirlerin ve temel hak kısıtlamalarının
  Anayasa m.15 ve OHAL rejimi çerçevesinde denetlenmesini sağlamak; çekirdek haklar,
  ölçülülük ve durumun gerektirdiği ölçü anal
name: olaganustu-hal-rejimi
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Olağanüstü Hâl ve Hak Askıya Alma Rejimi

## Görev
Olağanüstü hâl (m.119) döneminde temel hakların kullanımının durdurulması ve sınırlanmasına ilişkin tedbirleri Anayasa m.15'in özel rejimi ve AİHS m.15 (askıya alma) çerçevesinde denetlemek; çekirdek (dokunulamaz) hakları ve durumun gerektirdiği ölçü ölçütünü gözetmek.

## Soğuk başlangıç (intake)
1. Tedbir hangi OHAL dönemine ve hangi düzenlemeye (CB kararnamesi/karar, idari işlem) dayanıyor?
2. Hangi temel hak sınırlanıyor; bu hak m.15/2'deki dokunulamaz haklardan biri mi?
3. Tedbir, ortaya çıkan tehdit/durumun gerektirdiği ölçüyü aşıyor mu?
4. OHAL sona erdikten sonra da etkisini sürdüren kalıcı bir düzenleme mi söz konusu?

## Denetim şeması
1. **OHAL'in varlığı ve dayanağı.** OHAL ilanı ve süresi Anayasa ve ilgili usule uygun mu? Ara sonuç: usule aykırı ilan, tedbirleri sakatlar.
2. **Çekirdek haklar (m.15/2).** Savaş hukukuna uygun fiiller dışında yaşam hakkı, maddi-manevi varlığın bütünlüğüne dokunulamaması, din-vicdan-düşünce ve kanaat açıklamaya zorlanamama, suç-ceza geçmişe yürümezliği ve masumiyet karinesi gibi haklar **askıya alınamaz**. Bu çekirdeğe dokunan tedbir mutlak olarak aykırıdır.
3. **Durumun gerektirdiği ölçü.** Çekirdek dışı haklarda sınırlama, "durumun gerektirdiği ölçüde" ve milletlerarası hukuktan doğan yükümlülükler ihlal edilmemek kaydıyla mümkündür (m.15/1). Bu, olağan m.13 ölçülülüğünden farklı ama yine de orantı arayan bir testtir.
4. **Süre ve kapsam.** Tedbir OHAL'in amacı, yeri ve süresiyle sınırlı olmalı; OHAL sonrası kalıcılaşan, genel ve sürekli düzenlemeler olağan rejime (m.13) tabi olur.
5. **Yargısal denetim.** OHAL döneminde alınan tedbirler de yargı denetimi ve AYM denetimi dışında kalmaz; bireysel başvuru yolu işleyebilir.
AYM ve AİHM OHAL/askıya alma içtihadına ilke düzeyinde atıf yapın; künyeyi `[DOĞRULANMADI]` işaretleyin.

## Çıktı modülleri
- Çekirdek hak/ölçü testi sonucu ve tedbirin sınıflandırılması.
- OHAL süresiyle sınırlılık ve kalıcılaşma değerlendirmesi.
- Uygulanacak denetim yolu (norm denetimi/bireysel başvuru) önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

