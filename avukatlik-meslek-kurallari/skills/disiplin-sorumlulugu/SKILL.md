---
argument-hint: ''
description: Avukat hakkında disiplin şikâyeti, soruşturma ve kovuşturma, disiplin
  cezaları ve bunlara itiraz/iptal yolları söz konusu olduğunda; disiplin riskini
  değerlendirmek için kullanılır.
name: disiplin-sorumlulugu
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
  version: 0.1.0
user-invocable: true
---


# Avukatın Disiplin Sorumluluğu ve Baro Süreçleri

## Görev
Bir davranışın disiplin suçu oluşturup oluşturmadığını, uygulanacak ceza türünü ve sürecin
aşamaları ile kanun yollarını belirlemek.

## Soğuk başlangıç (intake)
1. İsnat edilen davranış nedir (özensizlik, sır ihlali, güveni kötüye kullanma, ücret/emanet
   para sorunu, meslektaşa karşı tavır)?
2. Süreç hangi aşamada (şikâyet, disiplin soruşturması, disiplin kovuşturması, ceza, itiraz)?
3. Daha önce verilmiş disiplin cezası / tekerrür var mı?
4. Aynı fiil hakkında ceza yargılaması da var mı?

## Denetim şeması
1. **Disiplin suçunun çerçevesi.** Avukatlık onuruna, meslek düzenine, meslek kurallarına
   aykırı eylem ve davranışlar disiplin suçudur (Av. K. m.34, m.134; TBB Meslek Kuralları).
   Tip, çoğu zaman somut maddeyle değil genel davranış normuyla kurulur; bu yüzden eylemin
   meslek onuruyla bağı gerekçelendirilir.
2. **Ceza türleri ve ölçek.** Av. K. m.135: uyarma, kınama, para cezası, işten çıkarma
   (geçici olarak mesleki faaliyetten alıkoyma) ve meslekten çıkarma. Ceza, fiilin ağırlığı,
   tekerrür ve kusur derecesine göre belirlenir (orantılılık). Ara sonuç: eylem hangi
   kademeye karşılık gelir?
3. **Süreç.** Baro yönetim kurulu disiplin soruşturması açar; gerekirse baro disiplin kurulu
   kovuşturma yürütür (Av. K. m.136 vd.). Savunma hakkı ve usul güvenceleri esastır; eksik
   tebligat/savunma alınmaması iptal sebebidir.
4. **Kanun yolu.** Baro disiplin kurulu kararına karşı TBB Disiplin Kurulu'na itiraz edilir;
   TBB kararları idari işlem niteliğinde olup idari yargı (Danıştay) denetimine tabidir.
   Süreleri kaçırma hak kaybı doğurur.
5. **Zamanaşımı.** Disiplin kovuşturmasında Av. K. m.157'deki süreler işler; fiilin
   öğrenilmesinden ve işlenmesinden itibaren süreler ayrı ayrı kontrol edilir.
6. **Ceza yargısı ile ilişki.** Disiplin ve ceza sorumluluğu bağımsızdır; beraat tek başına
   disiplin cezasını kaldırmaz, ancak maddi olgu tespitleri dikkate alınır.

İçtihat gerektiğinde TBB Disiplin Kurulu kararları (barobirlik.org.tr) ve Danıştay kararları
ilkesel düzeyde anılır; künye `[DOĞRULANMADI]` işaretlenir.

## Çıktı modülleri
- Davranış-suç-ceza eşleştirmesi ve olası ceza kademesi.
- Süreç ve süre takvimi (soruşturma → kovuşturma → itiraz → idari dava).
- Savunma dilekçesi/itiraz iskeleti ([doldurulacak] yer tutucularla).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

