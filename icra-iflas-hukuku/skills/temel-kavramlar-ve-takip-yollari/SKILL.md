---
argument-hint: ''
description: İcra-iflas hukukunun sistematiğini, cüzî/külli icra ayrımını ve hangi
  alacak için hangi takip yolunun seçileceğini belirlemek gerektiğinde; takip yolu
  seçimi, görev-yetki ve genel yön bulma için kulla
name: temel-kavramlar-ve-takip-yollari
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
  - ad: İcra ve İflas Kanunu
    numara: '2004'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Takip Yolları Haritası

## Görev
Eldeki alacağı/edimi nitelendirip doğru takip yolunu (ilamsız, ilamlı, kambiyo, rehnin paraya çevrilmesi, tahliye, iflas) seçmek; icra dairesi-icra mahkemesi-genel mahkeme görev dağılımını ve yetkiyi netleştirmek.

## Soğuk başlangıç (intake)
- Alacağın kaynağı ne: ilam/ilam niteliğinde belge mi, kambiyo senedi (çek/bono/poliçe) mi, sözleşme/fatura/adi belge mi, rehinle teminatlı mı?
- Borçlu gerçek kişi/tacir/şirket mi; iflasa tabi mi?
- Talep para alacağı mı, teminat mı, taşınır/taşınmaz teslimi mi, tahliye mi?
- Borçlunun yerleşim yeri/işyeri ve malvarlığının bulunduğu yer neresi?

## Denetim şeması
1. **Nitelendirme**: İlam veya ilam niteliğinde belge (İİK m.38) varsa ilamlı icra (m.24 vd.) — itiraz takibi durdurmaz, ancak icranın geri bırakılması (m.33, m.36) mümkündür. Çek/bono/poliçe varsa kambiyo senetlerine özgü takip (m.167 vd.) tercih edilebilir.
2. **İlamsız takip**: Para ve teminat alacaklarında genel haciz yolu (m.42 vd.); dayanak belge şart değildir ama itiraz takibi durdurur (m.66). Adi kiranın temerrütle tahliyesi için m.269.
3. **Rehinli alacak**: Kural olarak önce rehnin paraya çevrilmesi yoluna gidilir (m.45, m.145 vd.); ipotek/menkul rehni ayrımı yapılır. İstisnalar (m.45/son, kambiyo) gözetilir.
4. **İflas yolu**: Borçlu İİK m.43 anlamında iflasa tabi ise (tacirler vb.) takipli (m.155 vd.) veya doğrudan (m.177) iflas seçilebilir; basit alacak için orantısızlık değerlendirilir.
5. **Görev/yetki**: Takip işlemleri icra dairesi; takip hukukuna ilişkin uyuşmazlıklar icra mahkemesi (m.4); maddi hukuk uyuşmazlıkları (itirazın iptali, menfi tespit, tasarrufun iptali) genel mahkeme. Yetki HMK kuralları + İİK m.50.
6. **Ara sonuç**: Seçilen yol, beklenen itiraz/şikâyet riski, süre ve maliyet tablosu çıkarılır.

## Çıktı modülleri
- Takip yolu karar matrisi (alacak türü × yol × avantaj/risk).
- Görev-yetki tespiti ve dayanak madde listesi.
- İlk adım kontrol listesi (takip talebi unsurları, harç/gider avansı).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

