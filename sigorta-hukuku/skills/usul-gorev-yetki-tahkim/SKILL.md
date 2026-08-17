---
argument-hint: ''
description: Sigorta uyuşmazlığının nereye götürüleceği (Sigorta Tahkim Komisyonu
  mu mahkeme mi), görevli-yetkili mahkeme, başvuru şartı ve kanun yolları belirlenirken
  kullanılır; doğru forum ve usul seçimi için b
name: usul-gorev-yetki-tahkim
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
  - ad: Bankalar Kanunu
    numara: '5684'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Usul, Görev-Yetki ve Sigorta Tahkim Komisyonu

## Görev
Uyuşmazlığı en doğru forumda başlatmak: Sigorta Tahkim Komisyonu mu, ticaret/tüketici mahkemesi mi; görevli-yetkili yer neresi; başvuru şartı, parasal sınır ve kanun yolu nedir.

## Soğuk başlangıç (intake)
1. Sigortacı, Sigorta Tahkim Komisyonu sistemine üye mi (zorunlu sigortalarda üyelik zorunludur)?
2. Talep tutarı ve uyuşmazlığın niteliği (zarar/can/sorumluluk) ne?
3. Sigortalı tüketici mi, tacir mi?
4. Sigortacıya/Güvence Hesabına önce başvuru yapıldı mı?

## Denetim şeması
1. **Tahkim mi mahkeme mi.** 5684 sayılı Kanun m.30: Sigorta Tahkim Komisyonu, üye sigortacılarla zarar görenler arasındaki uyuşmazlıklara bakar. Başvuru şartı: önce sigortacıya yazılı başvuru ve uyuşmazlığın doğması (kısmen/tamamen red ya da 15 gün sessizlik). Ara sonuç: tahkim yolu açık mı?
2. **Parasal sınır ve kanun yolu.** m.30/12: tutara göre hakem kararı kesin olabilir, belirli tutar üstü kararlara Komisyon nezdinde itiraz ve daha üst tutarda temyiz yolu açıktır (güncel parasal sınırları teyit et). Tahkime başvuran bu yola bağlı kalır.
3. **Görevli mahkeme.** Mahkeme yolu seçilirse: ticari nitelikteki sigorta uyuşmazlığında Asliye Ticaret Mahkemesi (TTK m.4-5); sigortalı tüketici ise Tüketici Mahkemesi (6502 m.73). Görev kamu düzenindendir, re'sen incelenir.
4. **Yetki.** HMK genel yetki (davalı yerleşim yeri, HMK m.6) yanında sözleşmenin ifa yeri, sigorta ettirenin/zarar görenin yerleşim yeri gibi özel yetki kuralları; zorunlu sigortalarda zarar görene elverişli yetki.
5. **Süre.** Zamanaşımı TTK m.1420 ya da KTK m.109; tahkim başvurusu zamanaşımını keser. İspat: usul şartlarının yerine geldiğini başvuran gösterir.

## Çıktı modülleri
- Forum seçimi kararı (tahkim/ticaret/tüketici) ve gerekçe.
- Başvuru şartı ve ön başvuru kontrol listesi.
- Görevli-yetkili yer tespiti.
- Kanun yolu ve parasal sınır notu, süre uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

