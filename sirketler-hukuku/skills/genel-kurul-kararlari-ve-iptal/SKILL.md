---
argument-hint: ''
description: Anonim veya limited şirkette genel kurul çağrısı, gündem, nisaplar, kararların
  butlanı (TTK m.447) ve iptali (m.445-446) ile azlık haklarının kullanımı gündeme
  geldiğinde; karar sakatlığını teşhis ve
name: genel-kurul-kararlari-ve-iptal
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
  version: 0.1.0
user-invocable: true
---


# Genel Kurul Kararları ve İptal/Butlan

## Görev
Genel kurul kararının geçerliliğini denetlemek; sakatsa butlan mı iptal mi olduğunu, kimin, hangi sürede dava açabileceğini saptamak ve azlık haklarını işletmek.

## Soğuk başlangıç (intake)
1. Karar tarihi, gündem maddesi ve alınan kararın özü ne?
2. Çağrı usulü ve nisaplar tutturuldu mu; bakanlık temsilcisi gerekiyorsa hazır mıydı?
3. İtiraz eden pay sahibi toplantıya katıldı mı, muhalefetini tutanağa geçirdi mi?
4. Karar emredici hükme/temel pay sahipliği haklarına mı aykırı (butlan emaresi)?
5. Karar tarihinden bu yana ne kadar süre geçti?

## Denetim şeması
1. Çağrı ve gündem: AŞ m.410-414 (çağrı yetkisi, ilan, gündem); gündemde olmayan konu görüşülemez (m.413), istisnalar (azlık/genel kurulun yetkili olduğu hâller). Çağrısız genel kurul m.416 (tüm payların temsili + itirazsızlık).
2. Nisaplar: Olağan toplantı/karar nisapları m.418; ağırlaştırılmış nisaplar m.421 (esas sözleşme değişikliği türlerine göre).
3. Butlan: m.447 — vazgeçilemez pay sahipliği haklarını sınırlayan, anonim şirketin temel yapısına/sermayenin korunmasına aykırı kararlar batıl; süreye bağlı değil, tespit davası niteliğinde.
4. İptal: m.445 — kanuna, esas sözleşmeye veya dürüstlük kuralına aykırı kararlar; iptal davası açma hakkı m.446 (toplantıda muhalefet şerhi veren/katılması engellenen pay sahibi, çağrı/gündem usulsüzlüğü, yönetim kurulu, kişisel sorumluluk doğacaksa üye). Süre: karar tarihinden itibaren üç ay (m.445).
5. Görev/yetki: Asliye ticaret mahkemesi, şirket merkezi (m.445/2). Teminat ve yürütmenin geri bırakılması m.448-449.
6. Azlık hakları: özel denetçi atanması talebi (m.438-439), finansal tabloların müzakeresinin ertelenmesi (m.420), genel kurulu toplantıya çağırma (m.411-412).
7. İspat: Çağrı/nisap usulsüzlüğünü ve muhalefet şerhini davacı, kararın yerindeliğini şirket ortaya koyar.

## Çıktı modülleri
- Karar sakatlık teşhisi (butlan/iptal ayrımı, madde atıflı).
- İptal davası dilekçesi iskeleti (süre, taraf, talep sonucu, [doldurulacak]).
- Azlık hakkı başvuru/ihtar taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

