---
argument-hint: ''
description: Avukatın tahsil ettiği müvekkil parasını saklama ve ödeme, emanet hesabı,
  gecikme faizi ve güveni kötüye kullanma riski ile makbuz-serbest meslek makbuzu
  düzeni söz konusu olduğunda kullanılır.
name: emanet-para-mali-yukumluluk
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


# Müvekkil Parası, Emanet ve Mali Yükümlülükler

## Görev
Avukatın iş sahibi adına aldığı paraları yönetme, ayırma ve zamanında ödeme yükümlülüklerini
uygulamak; güveni kötüye kullanma ve disiplin riskini önlemek.

## Soğuk başlangıç (intake)
1. Avukat müvekkil adına ne tür bir para tahsil etti (icra tahsilatı, dava sonucu, emanet)?
2. Para müvekkile ne zaman, nasıl ödenecek/ödendi?
3. Avukatın bu paradan ücret/masraf mahsubu var mı; yazılı dayanağı var mı?
4. Serbest meslek makbuzu/fatura düzeni nasıl işliyor?

## Denetim şeması
1. **Ayırma ve teslim yükümü.** Avukat, iş sahibi adına aldığı paraları ve değerleri kendi
   malvarlığından ayrı tutmak ve geciktirmeden iş sahibine ödemekle yükümlüdür (Av. K. m.34;
   TBB Meslek Kuralları m.43; TBK m.508 hesap verme). Ara sonuç: para zamanında ve eksiksiz
   teslim/ayrı tutuluyor mu?
2. **Mahsup sınırı.** Avukat, kendi ücret ve masraf alacağını ancak yazılı dayanak ve
   müvekkilin bilgisi/muvafakati çerçevesinde mahsup edebilir; tek taraflı, belgesiz alıkoyma
   ihtilaf doğurur. Hapis hakkı (Av. K. m.166) sınırlı ve şartlıdır.
3. **Gecikmenin sonucu.** Geciktirilen ödeme için temerrüt faizi (TBK m.120) ve müvekkilin
   uğradığı zarar talep edilebilir.
4. **Cezai/disiplin riski.** Müvekkil parasını mal edinme güveni kötüye kullanmadır (TCK
   m.155, meslek/sanat icabı tevdi nedeniyle nitelikli hal); aynı fiil ağır disiplin suçu
   oluşturur ve meslekten çıkarmaya kadar gidebilir (Av. K. m.34, m.135). İspat: tahsilat ve
   ödeme kayıtları belirleyicidir; düzenli kasa/emanet defteri tutulması savunma değeri taşır.
5. **Belge düzeni.** Ücret için serbest meslek makbuzu düzenlenir; tahsilat-ödeme makbuzları
   dosyalanır. Eksik belge hem mali hem disiplin riskini büyütür.

## Çıktı modülleri
- Emanet/ödeme akışının uygunluk denetimi ve risk işaretleri.
- Mahsup/ödeme mutabakat tutanağı taslağı.
- Emanet kayıt ve makbuz düzeni kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

