---
argument-hint: ''
description: Delillerin toplanması, vicdani değerlendirme ilkesi, hukuka aykırı delil
  yasağı ve şüpheden sanık yararlanır ilkesi çerçevesinde ispat analizi yapılırken
  kullanılır.
name: delil-ve-delil-yasaklari
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
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Delil, İspat ve Delil Yasakları

## Görev
Dosyadaki delilleri elde ediliş ve değerlendirme yönünden tasnif etmek; hukuka aykırı delilleri ayıklamak; ispat gücünü ve şüphe dengesini ortaya koymak.

## Soğuk başlangıç (intake)
- Hangi delil türleri var (beyan, belge, bilirkişi, keşif, dijital, gizli tanık)?
- Her delil hangi usulle elde edildi; karar/onay var mı?
- İddianın dayandığı çekirdek delil hangisi?
- Lehe deliller toplandı/değerlendirildi mi?
- Çelişen deliller arasında nasıl bir denge var?

## Denetim şeması
1. **Serbest delil ve ilke.** Ceza muhakemesinde deliller serbestçe ileri sürülür ve hâkim vicdani kanaatiyle değerlendirir (CMK m.217/1). Ancak bu serbesti hukuka aykırı delille sınırlanır.
2. **Hukuka aykırı delil yasağı.** Yüklenen suç ancak hukuka uygun şekilde elde edilmiş delillerle ispat edilebilir (m.217/2); hukuka aykırı deliller reddolunur (m.206/2-a). Anayasa m.38/6 ve adil yargılanma (Anayasa m.36) bu yasağın temelidir.
3. **Delil tartışması.** Mahkeme, ortaya konulan her delili tartışır; reddedilen delil için gerekçe gösterir (m.206, m.217). Beyan delilinde teyit edici yan delil aranır.
4. **Şüpheden sanık yararlanır.** Mahkûmiyet, kuşkuya yer bırakmayan kesin ve inandırıcı delile dayanmalıdır; giderilemeyen şüphe sanık lehine yorumlanır (in dubio pro reo; Anayasa m.38, m.223/2 uygulaması).
5. **Özel delil tipleri.** Bilirkişi raporu denetlenir (HMK atfı ve CMK m.62 vd.); gizli tanık/koruma altına alınan tanık beyanı tek başına hükme esas alınamaz; dijital delilde bütünlük/zincir denetlenir.
6. **Ara sonuç.** Hukuka aykırı deliller dışlandıktan sonra kalan delil yeterli mi; değilse beraat/CYOK; yeterliyse nitelendirme ve ceza tayini aşamasına geçilir.

## Çıktı modülleri
- Delil envanteri ve hukuka uygunluk/dışlama notu.
- İspat dengesi analizi (lehe/aleyhe, çekirdek delil).
- Delil reddi/dışlama talebi gerekçesi.
- Bilirkişi/dijital delile itiraz noktaları listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

