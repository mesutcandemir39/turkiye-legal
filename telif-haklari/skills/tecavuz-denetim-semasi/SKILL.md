---
argument-hint: ''
description: Bir eylemin eser sahibinin mali veya manevi haklarına tecavüz oluşturup
  oluşturmadığını adım adım denetlemek gerektiğinde; izin, istisna ve hukuka uygunluk
  süzgeçlerinden geçirerek ihlal sonucuna varm
name: tecavuz-denetim-semasi
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
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Hak İhlali (Tecavüz) Denetim Şeması

## Görev
İddia edilen eylemin FSEK anlamında hak ihlali (tecavüz) oluşturup oluşturmadığını sistematik biçimde belirlemek ve hukuka uygunluk savunmalarını test etmek.

## Soğuk başlangıç (intake)
- Tecavüz iddiasına konu eylem ve tarihi nedir?
- Eyleme dayanak bir izin, lisans veya devir sözleşmesi gösteriliyor mu?
- Eylem ticari mi, kişisel/eğitim/haber amaçlı mı?
- Eserin tamamı mı yoksa bir kısmı/uyarlaması mı kullanılmış?

## Denetim şeması
1. Korunan hakkın varlığı: Eser + geçerli hak + hak sahibi belirlenir (m.1/B, m.8, m.20-25). Koruma süresi dolmuşsa ihlal yoktur.
2. El atma eylemi: Eylem hangi mali/manevi hakka karşılık geliyor (çoğaltma m.22, yayma m.23, umuma iletim m.25, işleme m.21, ad belirtmeme m.15, değişiklik m.16)?
3. İzin/yetki süzgeci: Sahibin veya hak sahibinin izni var mı? İzin/lisans dar yorumlanır (m.52); sözleşmede sayılmayan hak devredilmiş sayılmaz. İzin yoksa veya kapsam aşılmışsa ihlal karinesi güçlenir.
4. İstisna ve tahditler (m.30-40): Eylem kamu düzeni/genel menfaat istisnalarına, şahsen kullanma (m.38 — kâr amacı gütmeyen, çoğaltmayı sınırlı kılan), iktibas (m.35 — kaynak gösterme ve ölçü şartı), haber/güncel olay (m.37) veya eğitim-öğretim amaçlı kullanıma giriyor mu? İstisnalar dar yorumlanır; üç aşamalı teste benzer biçimde eserin normal kullanımını engellememe ve sahibin meşru menfaatini zedelememe aranır.
5. Manevi hak özelinde: İzinli kullanımda dahi ad belirtilmemesi (m.15) veya esere zarar veren değişiklik (m.16) bağımsız ihlal oluşturabilir.
6. Ara sonuç: İhlal var/yok; varsa hangi hak(lar), kusur şartı aranmayan talepler (ref/men) ve kusura bağlı talepler (tazminat) ayrılır.

İspat yükü: ihlali davacı, izin/istisnayı davalı ispatlar (HMK m.190).

## Çıktı modülleri
- İhlal denetim raporu (eylem — hak — izin/istisna değerlendirmesi — sonuç).
- Savunma (izin/istisna) zayıflık-güçlülük notu.
- Talep yelpazesine köprü.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

