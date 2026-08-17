---
argument-hint: ''
description: İmza ile kapanış arası dönemin yönetimi, kapanış ön şartlarının (conditions
  precedent) listelenmesi, kapanışta teslim edilecek belgelerin ve eş zamanlı işlemlerin
  kurgulanması için kullanılır.
name: kapanis-ve-sartlar-cp
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  - ad: Rekabetin Korunması Hakkında Kanun
    numara: '4054'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kapanış Şartları (CP) ve Kapanış Yönetimi

## Görev
İmza-kapanış arası dönemi düzenlemek, kapanış ön şartlarını ve kapanış belgelerini eksiksiz kurgulamak; eksik/gecikmeli kapanış sonuçlarını hükme bağlamak.

## Soğuk başlangıç (intake)
- İmza ve kapanış eş zamanlı mı, ayrık mı (signing/closing split)?
- Hangi izinler kapanış şartı (rekabet, sektörel, üçüncü kişi onayı)?
- Kapanış için uzun stop (long-stop date) tarihi belirlendi mi?
- Kapanışta hangi belgeler eş zamanlı teslim edilecek?

## Denetim şeması
1. **CP kataloğu**: Rekabet Kurulu izni, sektörel ön izin (BDDK/EPDK vb.), üçüncü kişi onayları (change-of-control), kurumsal kararlar, beyanların kapanışta doğru olması (bring-down).
2. **Ara dönem taahhütleri**: TBK m.2 dürüstlük kuralı çerçevesinde olağan işletme yürütümü; satıcının değer düşürücü işlem yapmama taahhüdü.
3. **Kapanış belgeleri (deliverables)**: Pay devir ciroları, pay defteri kaydı (TTK m.499), istifa/atama kararları, banka talimatları, disclosure güncellemesi.
4. **Eş zamanlılık**: Kapanış işlemlerinin tek seansta ve birbirine bağlı (interdependent) yapılması; aksi halde geri alma (unwind) mekanizması.
5. **Eksik kapanış**: Long-stop tarihine kadar CP sağlanmazsa fesih hakkı; kusurlu tarafın temerrüt sorumluluğu (TBK m.117 vd.).
6. **İspat/dayanak**: CP'nin sağlandığı belge (izin yazısı, onay kararı) ile kanıtlanır.
7. **Ara sonuç**: Kapanış protokolü (closing memorandum) ile tüm adımlar teyit edilir.

## Çıktı modülleri
- CP kontrol listesi (sorumlu taraf ve durum sütunlu)
- Kapanış belgeleri (deliverables) dizini
- Closing memorandum / kapanış protokolü iskeleti
- Long-stop ve fesih klozu lafzı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

