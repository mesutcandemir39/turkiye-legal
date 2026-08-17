---
argument-hint: ''
description: Vergi inceleme süreci, vergi tekniği raporu, ispat yükünün dağılımı ve
  delillerin değerlendirilmesini yönetmek; inceleme başladığında veya rapora dayalı
  tarhiyatta kullanılır.
name: vergi-incelemesi-ve-ispat
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
  - ad: Gelir Vergisi Kanunu
    numara: '193'
    tur: kanun
  - ad: Kurumlar Vergisi Kanunu
    numara: '5520'
    tur: kanun
  - ad: Katma Değer Vergisi Kanunu
    numara: '3065'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Vergi İncelemesi, İspat ve Delil

## Görev
Vergi inceleme sürecinde mükellef haklarını korumak, vergi tekniği/inceleme raporunu denetlemek, ispat yükünün dağılımını doğru kurmak ve delil stratejisini oluşturmak.

## Soğuk başlangıç (intake)
1. İnceleme hangi vergi türü ve dönem için, tam/sınırlı/özel inceleme mi?
2. İnceleme başlama tutanağı düzenlendi mi, defter-belge istendi mi?
3. Vergi tekniği raporu (VTR) veya inceleme raporu elde var mı?
4. İddia SMİYB, randıman, kayıt dışı hasılat mı; somut tespit nedir?
5. Mükellefin karşıt delilleri (ödeme, kapasite, stok, sözleşme) neler?

## Denetim şeması
1. **İnceleme yetkisi ve usulü:** VUK m.135-141 — incelemeye yetkililer, incelemenin yeri ve zamanı, başlama tutanağı (m.140), inceleme süreleri. Usul ihlali (defter-belge isteme yazısı, tutanak imzalama hakkı) savunmaya dayanak olur.
2. **Defter-belge ibrazı:** VUK m.139, m.256 — ibraz ödevi; ibraz edilmemesi re'sen takdir sebebidir (VUK m.30). Mücbir sebep (m.13) varsa ibraz etmeme mazur görülebilir; bu ayrımı kur.
3. **İspat yükünün dağılımı:** VUK m.3/B — vergiyi doğuran olay ve gerçek mahiyetin tespitinde iktisadi, ticari ve teknik icaplara uygunluk esas; iddia eden ispatla yükümlü. Vergiyi doğuran olayın varlığını idare, lehe istisna/indirim/giderin varlığını mükellef ispatlar.
4. **Delil serbestisi ve sınırı:** VUK m.3/B — yemin hariç her türlü delil; ancak vergiyi doğuran olayla ilgisi açık olmayan tanık beyanı ispatlama vasıtası sayılmaz. Karşıt inceleme, banka kayıtları, sevk irsaliyesi, kapasite raporu gibi somut delilleri öne çıkar.
5. **VTR denetimi:** Raporun somut tespite mi yoksa varsayım/oranlamaya mı dayandığını ayır; randıman/karşılaştırmalı yöntemlerin gerçek faaliyete uygunluğunu sorgula. Gerekçesiz rapor iptal sebebidir. Ara sonuç: tarhiyatın delil temeli ne kadar sağlam?
6. **Mükellef hakları:** İzaha davet (VUK m.370) imkânı kullanıldı mı; raporu okuma, tutanağa şerh düşme, görüş bildirme hakları.

## Çıktı modülleri
- İnceleme usulü kontrol listesi (tutanak, süre, ibraz, yetki).
- İspat yükü dağılım tablosu (iddia → ispat yükümlüsü → mevcut delil).
- VTR çürütme notu (somut tespit / varsayım ayrımı, karşı delil eşleştirmesi).
- İzah/savunma dilekçesi argüman iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

