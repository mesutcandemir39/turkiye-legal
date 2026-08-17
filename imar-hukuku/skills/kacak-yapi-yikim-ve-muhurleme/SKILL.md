---
argument-hint: ''
description: Ruhsatsız veya ruhsata aykırı yapı nedeniyle mühürleme, yapı tatil tutanağı,
  encümen yıkım kararı veya yıkımın infazı söz konusu olduğunda; aykırılığın giderilmesi
  süreci ve yıkıma karşı dava sorulduğ
name: kacak-yapi-yikim-ve-muhurleme
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


# Kaçak Yapı, Mühürleme ve Yıkım Kararı

## Görev
Ruhsatsız/ruhsata aykırı yapı sürecinin idari adımlarını denetlemek ve yıkım kararına karşı savunma/iptal stratejisi kurmak.

## Soğuk başlangıç (intake)
- Yapı tatil tutanağı (mühürleme) tutuldu mu, tarihi ve içeriği ne?
- Aykırılık ruhsatsızlık mı, ruhsata/projeye aykırılık mı, hangi imalatlar?
- Encümen yıkım kararı çıktı mı, tebliğ edildi mi?
- Aykırılığı giderme/ruhsata bağlama imkânı var mı, Yapı Kayıt Belgesi var mı?

## Denetim şeması
1. **Tespit ve durdurma (3194 m.32)**: İdare ruhsatsız/ruhsata aykırı yapıyı tespit edince inşaatı **mühürleyip durdurur** ve yapı tatil tutanağı düzenler. Tutanağın usulüne uygunluğu (tarih, imalat tarifi, tebliğ) ilk denetim noktasıdır; eksik tutanak sonraki işlemleri sakatlar.
2. **Aykırılığın giderilmesi süresi**: Mühürlemeden sonra ilgilisine aykırılığı giderme veya ruhsat alma için süre tanınır. Süre içinde aykırılık giderilir/ruhsata bağlanırsa mühür kaldırılır; aksi halde **yıkım** gündeme gelir.
3. **Encümen yıkım kararı (m.32)**: Süre sonunda belediye/il encümeni yıkıma karar verir. Karar yetki, gerekçe ve aykırılığın somut tespitiyle bağlıdır; ölçülülük (aykırı kısmın ayrılabilirliği — tüm yapı yerine aykırı imalatın yıkımı) denetlenir.
4. **Yapı Kayıt Belgesi etkisi (3194 geçici m.16)**: Geçerli YKB varsa yıkım ve ilgili para cezaları durur; ancak YKB belirli istisnaları (kıyı, başkasının taşınmazı, riskli alan vb.) kapsamaz ve mülkiyet uyuşmazlığını çözmez. YKB'nin kapsamı ve geçerliliği denetlenir.
5. **İspat yükü ve dava**: İdare aykırılığı tutanak ve teknik tespitle ispatlar; davacı ruhsata uygunluğu/giderilebilirliği savunur. Yıkım kararına karşı İYUK m.7'de 60 günde iptal davası ve **yürütmenin durdurulması** (yıkım telafisi imkânsız zarar) istenir.
6. **Ara sonuç**: Usul/yetki/ölçülülük sakatlığı varsa iptal + YD; aksi halde aykırılığın giderilmesi yoluyla idari çözüm önerilir. Danıştay 6./14. Daire ilkesel atıfları `[DOĞRULANMADI]` ile.

## Çıktı modülleri
- İdari süreç kronolojisi (tutanak-süre-encümen-tebliğ).
- Yapı tatil tutanağı ve yıkım kararı usul denetim notu.
- Ölçülülük/ayrılabilirlik değerlendirmesi.
- YD talepli yıkım iptali dilekçe iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

