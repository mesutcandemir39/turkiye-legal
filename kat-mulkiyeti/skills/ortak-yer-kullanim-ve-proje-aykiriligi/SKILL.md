---
argument-hint: ''
description: Ortak yerlerin (çatı, cephe, bahçe, çekme kat, sığınak, otopark) izinsiz
  işgali/değiştirilmesi, bağımsız bölümün projeye veya tahsis amacına aykırı kullanımı
  (mesken-işyeri dönüşümü dahil) söz konusu
name: ortak-yer-kullanim-ve-proje-aykiriligi
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
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Ortak Yer Kullanımı ve Projeye Aykırılığın Giderilmesi

## Görev
Ortak yerlerde izinsiz değişiklik/işgali ve bağımsız bölümün projeye, yönetim planına veya tahsis amacına aykırı kullanımını tespit edip durdurmak; eski hâle getirme (men ve aykırılığın giderilmesi) talebini kurmak.

## Soğuk başlangıç (intake)
- Aykırılık nerede: ortak yerde mi (cephe, çatı, bahçe, kapıcı dairesi, otopark) yoksa bağımsız bölümde mi?
- Yapılan değişiklik nedir: çatı katı/ilave inşaat, cephe kapatma, ortak yere el atma, mesken→işyeri dönüşümü?
- Değişiklik için kurul kararı/oybirliği alındı mı; projeye uygun mu?
- Aykırılık ne zaman başladı; ruhsat/yapı kayıt belgesi var mı?

## Denetim şeması
1. **Ortak yerde değişiklik yasağı (KMK m.19)**: Kat malikleri, anagayrimenkulün bakım ve mimari durumu ile estetiğini titizlikle korumakla yükümlüdür. Kendi bağımsız bölümünde dahi, anataşınmaza zarar verecek veya mimari durumu/estetiği bozacak onarım/tesis/değişiklik yapamaz (m.19/2). Ortak yerlerde esaslı değişiklik **bütün maliklerin oybirliğini** gerektirir.
2. **İzinsiz yapılan değişiklik**: Oybirliği/izin olmadan yapılan değişiklik için her kat maliki eski hâle getirme (men ve refi) talep edebilir; mahkeme aykırılığın giderilmesine karar verir (m.33 ile m.19 birlikte).
3. **Tahsis amacına aykırı kullanım (m.24)**: Anagayrimenkulün, kütükte mesken, iş veya ticaret yeri olarak gösterilen bağımsız bölümü, başka türde kullanılamaz; özellikle hastane, dispanser, klinik, ECZane, sinema, kahvehane, gazino, dans salonu, fırın, lokanta, pavyon gibi yerler **mesken bağımsız bölümde** ancak yönetim planında izin verilmiş veya **bütün maliklerin oybirliğiyle** karar alınmışsa açılabilir (m.24/2). Bazı işyerleri kütükte mesken görünse de açılamaz.
4. **Faydalı/lüks yenilik ayrımı (m.42)**: Ortak yerlerde herkesin yararına yenilik (örn. asansör, ısı yalıtımı) sayı ve arsa payı çoğunluğuyla; çok masraflı/lüks yenilikler ise yararlanmayan malikin katılımı zorunlu kılınmadan yapılabilir, masrafı isteyenler öder.
5. **İlave inşaat / kat ilavesi (m.44)**: Anagayrimenkule yeni kat/eklenti yapılması, arsa payı yeniden düzenlenmesini gerektirir ve **oybirliği** ile mümkündür.
6. **İspat ve keşif**: Projeye/ruhsata aykırılık genellikle onaylı proje karşılaştırması ve keşif-bilirkişi (mimar/inşaat) ile saptanır.
7. **Ara sonuç**: İzinsiz/oybirliksiz değişiklik veya amaç dışı kullanım varsa men + eski hâle getirme; yenilik ise m.42 nisabı denetimi.

## Çıktı modülleri
- Aykırılığın giderilmesi (men + eski hâle getirme) dava dilekçesi iskeleti.
- Onaylı proje / yapılan değişiklik karşılaştırma notu (keşif-bilirkişi talebi).
- Nisap/oybirliği taraması (m.19, m.24, m.42, m.44).
- İhtiyati tedbir notu (devam eden inşaatın durdurulması).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

