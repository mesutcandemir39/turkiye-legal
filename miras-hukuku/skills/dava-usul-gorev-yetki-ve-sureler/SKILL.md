---
argument-hint: ''
description: Miras davasını doğru mahkemede ve süresinde açmak; çekişmeli-çekişmesiz
  iş ayrımı, görevli mahkeme, yetki, harç ve hak düşürücü süre/zamanaşımı haritası
  çıkarmak gerektiğinde kullanılır.
name: dava-usul-gorev-yetki-ve-sureler
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


# Dava Usulü, Görev-Yetki ve Süreler

## Görev
Her miras talebini doğru yargı yoluna oturtmak: çekişmeli/çekişmesiz ayrımı, görevli ve yetkili mahkeme, harç-gider ve süre disiplinini HMK ve TMK normlarıyla kurmak.

## Soğuk başlangıç (intake)
- Talep ne? (mirasçılık belgesi, ret, tenkis, muvazaa, istihkak, paylaşma)
- Mirasbırakanın son yerleşim yeri neresi? Taşınmaz nerede?
- Ölüm ve öğrenme tarihleri? Süreler işliyor mu?
- Taraflar kim, mirasçı sayısı? (zorunlu dava arkadaşlığı)
- Önceden açılmış derdest dava/karar var mı?

## Denetim şeması
1. **Çekişmesiz işler — sulh hukuk (HMK m.382, m.4):** Mirasçılık belgesi (m.598), mirasın reddinin tescili (m.609), defter tutma, terekenin tespiti/yönetimi, vasiyetnamenin açılması (m.595-597), ortaklığın giderilmesi.
2. **Çekişmeli davalar — asliye hukuk (HMK m.2):** Tenkis, muris muvazaası (tapu iptali-tescil), miras sebebiyle istihkak, denkleştirme, vasiyetnamenin/miras sözleşmesinin iptali, mirasçılık belgesinin iptali.
3. **Yetki:** Mirasbırakanın son yerleşim yeri mahkemesi (TMK m.576; HMK m.11). Taşınmaza ilişkin tapu iptali-tescilde taşınmazın bulunduğu yer kesin yetkisi (HMK m.12) gündeme gelir.
4. **Taraf — zorunlu dava arkadaşlığı:** Elbirliği mülkiyetini ilgilendiren davalarda (paylaşma, muvazaa) tüm mirasçıların davada yer alması gerekir; aksi halde dava şartı eksikliği.
5. **Süre haritası:** Mirasın reddi 3 ay (m.606); tenkis 1 yıl / 10 yıl (m.571); vasiyet iptali 1 / 10 / 20 yıl (m.559); miras sebebiyle istihkak 10 / 20 yıl (m.639). Muris muvazaası ve ortaklığın giderilmesi süreye tabi değildir.
6. **Ara sonuç:** dava türü + mahkeme + yetki + süre durumu + harç (nispi/maktu). Dilekçe HMK m.119 unsurlarıyla kurulur.

## Çıktı modülleri
- Görev-yetki-süre karar tablosu
- Süre takvimi (hak düşürücü/zamanaşımı, kalan gün)
- Taraf ve zorunlu dava arkadaşlığı listesi
- Dilekçe başlığı ve harç türü notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

