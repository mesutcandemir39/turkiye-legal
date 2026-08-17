---
argument-hint: ''
description: Geçerli bir normun içeriksel adaletsizliği, hukuk-ahlak ilişkisi veya
  aşırı haksız kanunun bağlayıcılığı tartışıldığında; klasik doğal hukuk ile Radbruch
  formülünü Türk hukuk devleti (Anayasa m.2) ve
name: dogal-hukuk-ve-adalet
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Doğal Hukuk, Adalet ve Radbruch Formülü

## Görev
Pozitif olarak geçerli bir normun içeriksel adaleti/meşruiyeti sorununu işlemek; doğal hukuk
geleneğini ve Radbruch formülünü (katlanılmaz adaletsizlik eşiği) Türk hukuk devleti ilkesi
(Anayasa m.2) ve değer ölçütleriyle (TMK m.2-3) bağlantılandırmak.

## Soğuk başlangıç (intake)
- Tartışılan norm geçerli mi, yoksa geçerliliği mi sorgulanıyor (önce pozitivizm becerisine bak)?
- "Adaletsizlik" iddiası hangi değere dayanıyor (insan onuru, eşitlik, orantılılık)?
- Somut bir uyuşmazlıkta mı, yoksa soyut/akademik düzeyde mi soruluyor?
- Temel hak boyutu var mı (Anayasa m.12 vd., AİHS) — adalet iddiası pozitif hakka çevrilebilir mi?

## Denetim şeması
1. **Adalet türünü ayır.** Aristotelesçi dağıtıcı/denkleştirici adalet ile prosedürel adalet
   ayrımını yap; iddianın hangi adalet türüne dayandığını netleştir. "Adaletsiz" yargısı
   ölçütsüz kalmamalı.
2. **Pozitif değer çıpalarını ara.** İçeriksel adalet çoğu zaman pozitif hukukta zaten
   karşılığını bulur: insan onuru ve hukuk devleti (Anayasa m.2), eşitlik (Anayasa m.10),
   ölçülülük (Anayasa m.13), dürüstlük ve hakkın kötüye kullanılması yasağı (TMK m.2). Önce
   bu pozitif kanalları tüket.
3. **Radbruch eşiğini uygula.** Salt adaletsizlik normu geçersiz kılmaz; ancak adaletsizlik
   "katlanılmaz" boyuta ulaşır ve eşitlik bilinçli olarak inkâr edilirse, kanunun "doğru
   olmayan hukuk" olarak geri çekildiği savunulabilir. Bu istisnai eşiği vurgula; günlük
   uyuşmazlığa taşımaktan kaçın.
4. **Yöntemsel çıkış.** Türk hukukunda mahkeme kanunu kendiliğinden "adaletsiz" diye
   uygulamadan bırakamaz; yolu (a) Anayasaya aykırılık iddiasıyla AYM'ye taşıma (somut norm
   denetimi, Anayasa m.152), (b) anayasaya uygun/temel hakka uygun yorum, (c) TMK m.2 ile
   sonucu düzeltmedir. Ara sonuç: adalet itirazı → pozitif kanal.
5. **Dayanak.** Radbruch, Aquinas, Finnis ve Türk hukuk felsefesi külliyatına atıf;
   sayfa [DOĞRULANMADI]. İçtihat zikredilecekse künye teyidi şarttır, aksi halde [DOĞRULANMADI].

## Çıktı modülleri
- Adalet türü ve ölçüt notu.
- Pozitif değer çıpaları haritası (madde atıflarıyla).
- Radbruch eşiği değerlendirmesi (eşiğin altında/üstünde).
- Yöntemsel çıkış önerisi (AYM / uygun yorum / TMK m.2).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

