---
argument-hint: ''
description: Taşınmaza haksız müdahale, tecavüz, işgal veya izinsiz kullanım halinde
  müdahalenin men'i ve haksız işgal tazminatı (ecrimisil) talep edileceğinde; paylı/elbirliği
  mülkiyette ortaklar arası el atma ve
name: el-atmanin-onlenmesi-ve-ecrimisil
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
  - ad: Tapu Kanunu
    numara: '3402'
    tur: kanun
  - ad: Kat Özel Koşulu Olmak Üzere Yapılan Satış Mukavelelerine Dair Kanun
    numara: '2644'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# El Atmanın Önlenmesi ve Ecrimisil

## Görev
Taşınmaza haksız el atmanın önlenmesi ve haksız işgalden doğan ecrimisil talebini unsur, taraf, süre ve hesap yönünden kurmak.

## Soğuk başlangıç (intake)
- Müdahale türü: fiziki işgal, izinsiz inşaat, geçiş, ortak alanın tek başına kullanımı mı?
- Mülkiyet türü: tek malik mi, paylı (müşterek) mı, elbirliği (iştirak) mi?
- İşgalci kötüniyetli mi; daha önce ihtar/men talebi yapıldı mı?
- Talep men ile birlikte ecrimisil mi; geçmiş kullanım dönemi nedir?

## Denetim şeması
1. **Mülkiyet hakkına dayan.** Malik, haksız el atmaya karşı el atmanın önlenmesini (müdahalenin men'i) ve eski hale getirmeyi isteyebilir (TMK m.683/2). Zilyet de zilyetliğin korunması yollarına başvurabilir (TMK m.982-984).
2. **Müdahalenin haksızlığını kur.** Davalının taşınmazı kullanma hakkı (kira, intifa, irtifak, muvafakat) yoksa müdahale haksızdır. Hukuka uygunluk savunması (rıza, ayni/kişisel hak) öncelikle tüketilir.
3. **Paydaşlar arası el atmayı ayır.** Paylı mülkiyette bir paydaş diğerlerinin payına el atarsa, diğer paydaş kendi payı oranında men ve ecrimisil isteyebilir; intifadan men koşulu kural olarak aranmaz (yerleşik uygulama, künye `[DOĞRULANMADI]`, karararama.yargitay.gov.tr).
4. **Ecrimisil temelini kur.** Ecrimisil, kötüniyetli zilyedin (haksız işgalcinin) malike ödeyeceği haksız işgal tazminatıdır; kötüniyetli zilyedin sorumluluğu TMK m.995'e dayanır (geri verme + tazminat). Hesap, emsal kira/getiri üzerinden bilirkişiyle yapılır.
5. **Süre.** Ecrimisil için geriye dönük 5 yıllık dönem istenir (haksız fiil/zilyetlik tazminatı zamanaşımı uygulaması, künye `[DOĞRULANMADI]`); men davası mülkiyete dayandığı için ayni nitelikte ve kural olarak zamanaşımına tabi değildir.
6. **Görev/yetki.** Görevli asliye hukuk; yetki taşınmaz yeri (HMK m.12). Husumet fiilen işgal eden(ler)e.
7. **Ara sonuç.** Men edilebilir mi, ecrimisil dönemi ve hesabı, kötüniyet ispatı.

## Çıktı modülleri
- Müdahale–hak–talep matrisi (men + ecrimisil).
- Dava dilekçesi iskeleti (keşif, fen ve hesap bilirkişisi talebi, [doldurulacak] dönem).
- Ecrimisil dönemi/zamanaşımı ve emsal kira ispat notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

