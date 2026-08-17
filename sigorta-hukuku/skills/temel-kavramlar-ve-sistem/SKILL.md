---
argument-hint: ''
description: Sigorta türünün (zarar/can, zorunlu/ihtiyari) belirlenmesi, taraf ve
  kavramların oturtulması, doğru kanun ve genel şartların seçilmesi gerektiğinde;
  uyuşmazlığı hangi rejimin yöneteceğini saptamak içi
name: temel-kavramlar-ve-sistem
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


# Sigorta Hukuku Temel Kavramları ve Sistematik

## Görev
Önündeki sigorta ilişkisini doğru rejime oturtmak: sigorta türünü, uygulanacak normu (TTK Altıncı Kitap, KTK, 5684) ve devreye girecek genel şartları belirleyip uyuşmazlığın iskeletini kurmak.

## Soğuk başlangıç (intake)
1. Hangi tür sigorta? (kasko, trafik, konut/yangın, ferdi kaza, hayat, sağlık, sorumluluk, nakliyat?)
2. Zorunlu mu ihtiyari mi; teminat zarar mı can sigortası mı?
3. Poliçe, genel şartlar ve özel şartlar elde mi; sigorta bedeli/teminat tutarı nedir?
4. Taraflar kim: sigorta ettiren, sigortalı, lehtar, zarar gören üçüncü kişi?
5. Riziko ne zaman/nasıl gerçekleşti; ihbar yapıldı mı?

## Denetim şeması
1. **Tür tespiti.** TTK m.1453 vd. zarar sigortası mı, m.1487 vd. can sigortası mı? Bu ayrım tazminat ilkesi (m.1459) ve halefiyetin (m.1472) uygulanıp uygulanmayacağını belirler.
2. **Sözleşmenin kurulması.** TTK m.1401-1425: icap/kabul, poliçe verme (m.1424), genel şartların bağlayıcılığı. Ara sonuç: geçerli bir sözleşme ve teminat var mı?
3. **Norm seçimi.** İhtiyari sigortada TTK; zorunlu trafik sigortasında öncelikle KTK m.91 vd. ve Karayolları Motorlu Araçlar Zorunlu Mali Sorumluluk Sigortası Genel Şartları; düzenleyici sorunlarda 5684. İstisna: özel kanun genel kanunu önceler.
4. **Genel şartların okunması.** Teminat kapsamı, istisnalar, muafiyet, riziko adresi/aracı poliçeden ve genel şarttan çıkarılır. İspat yükü: teminat kapsamını talep eden, istisnayı sigortacı (TMK m.6 mantığı).
5. **Yol ve süre kontrolü.** Sigorta Tahkim Komisyonu (5684 m.30) mı genel mahkeme mi; zamanaşımı TTK m.1420 (kural iki yıl) ya da KTK m.109.

## Çıktı modülleri
- Sigorta türü ve uygulanacak norm haritası.
- Taraflar ve sıfatları tablosu (sigorta ettiren/sigortalı/lehtar/üçüncü kişi).
- Teminat-istisna-muafiyet özeti ve ispat yükü dağılımı.
- Olası yol ve zamanaşımı uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

