---
argument-hint: ''
description: İmar planına veya plan değişikliğine itiraz ve iptal davası gündeme geldiğinde;
  askı-ilan süreci, üst ölçeğe ve şehircilik ilkelerine aykırılık, kamu yararı denetimi
  ve dava açma süresinin hesabı soru
name: imar-plani-denetimi-ve-iptali
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
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İmar Planı Denetimi ve Plan İptal Davası

## Görev
Bir imar planı veya plan değişikliğinin hukuka uygunluğunu denetlemek; iptal davasının süre, ehliyet ve esas yönünden kurulmasını sağlamak.

## Soğuk başlangıç (intake)
- Plan hangi ölçekte (1/5000 nazım, 1/1000 uygulama) ve hangi idarece onaylandı?
- Plan/değişiklik askıya çıktı mı, askı tarihleri neler, itiraz ettiniz mi?
- Müvekkilin taşınmazı plan sınırı içinde mi, menfaati nasıl etkileniyor?
- Üst ölçekli plana veya ada/parsel dengesine aykırılık iddiası var mı?

## Denetim şeması
1. **Yetki ve usul (3194 m.8/b)**: Plan, yetkili idare meclisince onaylanıp **bir ay süreyle askıya** çıkarılır. Askı süresinde idareye itiraz edilebilir; idare itirazı 15 günde değerlendirir. Süreç usulü işlemediyse şekil sakatlığı doğar.
2. **Dava açma süresi (İYUK m.7, m.11)**: Askı süresi sonundan itibaren 60 gün; askı içinde yapılan itirazın reddi/zımni reddi yeni 60 günlük süre başlatır. Süre, planın askısının dayandığı ilana göre titizlikle hesaplanır (geç öğrenme/menfaat ihlalinin doğduğu an tartışılır).
3. **Ehliyet ve menfaat (İYUK m.2)**: Davacının planla güncel, kişisel ve meşru menfaat ilişkisi; parsel maliki, komşu parsel maliki, meslek odası/dernek dava ehliyeti ayrı ayrı değerlendirilir.
4. **Esas denetimi**: Üst ölçekli plana uygunluk; **şehircilik ilkeleri, planlama esasları ve kamu yararı** üçlü ölçütü (Danıştay yerleşik denetim ölçütü); donatı alanı dengesi, yoğunluk artışı/kazanılmış hak, kademe atlama yasağı. Plan değişikliğinde "zorunluluk ve kamu yararı" gerekçesi aranır.
5. **İspat ve bilirkişi**: Şehir plancısı bilirkişi, plan paftaları, plan açıklama raporu ve plan notları; keşif. İspat yükü işlemin hukuka uygunluğunu kanıtlama bakımından idarededir, aykırılık iddiasını davacı somutlaştırır.
6. **Ara sonuç + tedbir**: Esaslı sakatlık varsa iptal + **yürütmenin durdurulması (İYUK m.27)**; telafisi güç zarar (inşaat başlaması) vurgulanır. İçtihat atfı yapılacaksa Danıştay 6. Daire künyesi `[DOĞRULANMADI]` ile ve karararama.danistay.gov.tr teyidiyle.

## Çıktı modülleri
- Süre hesap tablosu (askı-itiraz-dava).
- Aykırılık gerekçeleri listesi (yetki/şekil/üst plan/kamu yararı).
- YD talepli iptal dilekçesi iskeleti.
- Bilirkişiye yöneltilecek sorular taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

