---
argument-hint: ''
description: Bir kişi uzun süredir kayıpsa, ölüm tehlikesi içinde kaybolmuşsa ya da
  kişiliğin/ölümün ispatı sorun olduğunda gaiplik kararı veya nüfusa ölüm kaydı için
  kullanılır.
name: gaiplik-olum-karinesi
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Gaiplik ve Ölüm Karinesi

## Görev
Kayıp bir kişinin hukuki durumunu belirlemek: ölüm tehlikesi içinde kaybolma veya uzun süreli haber alınamama hâllerinde gaiplik kararı (TMK m.32 vd.) almak ya da ölüm karinesi/ölü olarak kaydı (TMK m.31, m.44) için doğru yolu kurmak.

## Soğuk başlangıç (intake)
- Kişi ölüm tehlikesi içinde mi (deprem, sel, kaza, savaş) kayboldu, yoksa uzun süredir haber mi alınamıyor?
- Son haberin/kaybın üzerinden ne kadar zaman geçti?
- Cesedi bulunamamasına rağmen ölümünde kuşku yok mu (ölüm karinesi), yoksa belirsizlik mi var (gaiplik)?
- Talebi kim yapıyor; miras, evlilik, sigorta gibi hangi hak buna bağlı?

## Denetim şeması
1. **Ölüm karinesi** — TMK m.31: bir kimse ölümüne kesin gözle bakılmayı gerektiren durumlar içinde (ör. cesedi bulunamasa da) kaybolursa, gerçekten ölmüş gibi mirası açılır; nüfusa ölü kaydı için mahkeme/idari işlem gerekir (m.44).
2. **Gaiplik sebepleri** — TMK m.32: ölüm tehlikesi içinde kaybolan veya kendisinden uzun süre haber alınamayan ve ölümü hakkında kuvvetli olasılık bulunan kişinin, hakları ölümüne bağlı olanların başvurusuyla gaipliğine karar verilir.
3. **Süreler** — TMK m.33: ölüm tehlikesi içinde kaybolmada en az **bir yıl**, son haberden itibaren en az **beş yıl** geçmesi gerekir. Mahkeme ilanla araştırma yapar; bir yıl içinde haber gelmezse gaiplik kararı verir.
4. **Görev ve yetki** — TMK m.32/2: gaiplik kararı, kişinin son yerleşim yeri ya da Türkiye'deki son yerleşim yeri mahkemesinden istenir; asliye hukuk mahkemesi görevlidir.
5. **Sonuçlar** — Gaiplik kararıyla miras gaipliğe (kaybolma/son haber tarihine) göre açılır; mirasçılar teminat gösterir (TMK m.35). Evlilik kendiliğinden sona ermez; sona erdirme için ayrı talep/karar gerekir (TMK m.131).

## Çıktı modülleri
- Karine mi gaiplik mi ayrımı + dayanak.
- Süre hesabı (kayıp/son haber tarihinden itibaren).
- Başvuru iskeleti (görevli/yetkili mahkeme, ilan talebi, sonuç).
- Bağlı hak notu (miras açılışı, sigorta, evlilik) ve `[doldurulacak]` tarih yerleri.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

