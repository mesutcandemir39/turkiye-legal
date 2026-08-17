---
argument-hint: ''
description: Ekonomik suç dosyasında belge, banka kaydı, dijital veri ve kurum raporlarının
  (VDK, MASAK, SPK, BDDK) delil değeri, delil yasakları ve mali bilirkişi raporunun
  denetimi söz konusu olduğunda kullanılı
name: ispat-delil-bilirkisi
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Kaçakçılıkla Mücadele Kanunu
    numara: '5549'
    tur: kanun
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İspat, Delil ve Bilirkişi Değerlendirmesi

## Görev
Ekonomik suç dosyasının delil mimarisini kurmak; kurum raporları ile bilirkişi raporlarının değerini, hukuka aykırı delil sorununu ve maddi hesabı denetlemek.

## Soğuk başlangıç (intake)
- Hangi deliller var? (fatura/defter, banka hareketleri, e-posta/mesaj, müfettiş raporu)
- Delil nasıl elde edildi? (arama-elkoyma kararı, MASAK bildirimi, açık kaynak)
- Hesaba/zarara ilişkin bilirkişi raporu düzenlendi mi?
- Çelişkili veya eksik delil/rapor var mı?

## Denetim şeması
1. **Delil serbestisi ve yasak (CMK)**: Ceza muhakemesinde her şey delil olabilir (m.217), ancak hukuka aykırı yöntemle elde edilen deliller hükme esas alınamaz (Anayasa m.38/6, CMK m.206/2-a, m.217/2, m.230). Dijital delilde elkoyma usulü ve imaj/hash zinciri (CMK m.134 yöntemi) kontrol edilir.
2. **Kurum raporlarının niteliği**: VDK vergi suçu raporu, MASAK inceleme raporu, SPK denetim raporu ve BDDK raporları delil/uzman görüşü niteliğindedir; bağlayıcı değildir, mahkeme serbestçe değerlendirir. Rapordaki tespit-sonuç bağı ve metodoloji denetlenir.
3. **Bilirkişi raporu**: Mali/muhasebe bilirkişisi, görevlendirme kapsamı, dayanak belgeler, hesap yöntemi ve çelişki bakımından incelenir; eksiklik/çelişki halinde ek rapor veya yeni bilirkişi talep edilir. Hukuki nitelendirme bilirkişiye bırakılamaz (hâkimin işi).
4. **İspat yükü ve şüpheden sanık yararlanır**: Kast ve fiil iddia makamınca ispatlanır; şüphe sanık lehine yorumlanır. Savunma karşıt delil ve karşıt inceleme (sahte fatura zincirinde karşıt mükellef kaydı) ile çalışır.
5. **Belge zinciri**: Fatura-ödeme-mal akışı-stok-banka kaydı bütünlüğü kurularak işlemin gerçekliği veya sahteliği gösterilir.
6. **Ara sonuç**: Delil listesi, hukuka uygunluk durumu, rapor güvenilirliği ve ispat boşlukları netleşir.

## Çıktı modülleri
- Delil envanteri ve elde ediliş hukukîliği tablosu
- Kurum raporu metodoloji eleştirisi
- Bilirkişi raporu denetim/itiraz notu
- Belge-akış zinciri analizi
- Karşıt delil ve ispat stratejisi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

