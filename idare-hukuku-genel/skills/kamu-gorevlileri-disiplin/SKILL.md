---
argument-hint: ''
description: Memur ve diğer kamu görevlilerine ilişkin atama, nakil, disiplin cezası,
  görevden uzaklaştırma gibi işlemleri ve bunların iptalini değerlendirmek için kullanılır;
  personel hukuku uyuşmazlıklarında baş
name: kamu-gorevlileri-disiplin
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
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kamu Görevlileri ve Disiplin İşlemleri

## Görev
Kamu görevlisine yönelik personel işlemlerini (özellikle disiplin cezalarını) usul ve esas yönünden denetlemek ve iptal stratejisini kurmak. Dayanak: Anayasa m.128/m.129, 657 sayılı DMK ve özel personel mevzuatı.

## Soğuk başlangıç (intake)
1. İşlem türü nedir (uyarı/kınama/aylıktan kesme/kademe ilerlemesinin durdurulması/memurluktan çıkarma; atama/nakil/görevden uzaklaştırma)?
2. Soruşturma açıldı mı, savunma hakkı tanındı mı?
3. Ceza zamanaşımı süreleri korunmuş mu?
4. İşlem tebliğ edildi mi; başvuru yolları gösterildi mi?

## Denetim şeması
1. **Yetki.** Cezayı veren makam/kurul yetkili mi; ağır cezalarda disiplin kurulu kararı şart mı (657 sayılı DMK m.126 vd.)?
2. **Şekil/usul.** Disiplin soruşturması açılması, **savunma hakkının tanınması** (savunma alınmadan ceza verilemez), muhakkik raporu, gerekçe. Savunma alınmaması esaslı şekil sakatlığıdır ve tek başına iptal sebebi olabilir.
3. **Sebep.** İsnat edilen fiil sabit mi; fiilin karşılığı olan disiplin hükmü doğru nitelendirilmiş mi? Maddi olayın gerçekliği re'sen araştırılır (İYUK m.20).
4. **Konu/ölçülülük.** Verilen ceza fiille orantılı mı; alt ceza uygulaması (657 sayılı DMK m.125 indirim) değerlendirildi mi? Eşitlik ve ölçülülük (Anayasa m.13) denetimi.
5. **Maksat.** İşlem kamu hizmeti yararı yerine kişisel saikle mi tesis edilmiş (yetki saptırması)?
6. **Zamanaşımı.** Disiplin soruşturmasına başlama ve ceza verme süreleri (657 sayılı DMK m.127); süre geçmişse ceza verilemez.
7. **Yargı yolu ve süre.** İdare mahkemesinde iptal davası; İYUK m.7 (60 gün) ve gerekiyorsa parasal/özlük kayıpları için tam yargı talebi. **Ara sonuç:** usul ve esas aykırılıkları + iptal sebepleri.

## Çıktı modülleri
- Disiplin sürecinin usul kontrol listesi (soruşturma/savunma/kurul/zamanaşımı).
- Ceza-fiil orantılılık ve alt ceza değerlendirmesi.
- İptal sebepleri + özlük kaybı tazmin notu.
- Dava dilekçesi için talep sonucu önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

