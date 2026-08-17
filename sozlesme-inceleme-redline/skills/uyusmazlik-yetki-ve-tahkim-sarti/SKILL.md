---
argument-hint: ''
description: Uygulanacak hukuk, yetkili mahkeme, tahkim şartı ve arabuluculuk klozlarının
  geçerliliğini ve müvekkil için elverişliliğini incelemek gerektiğinde kullanılır.
name: uyusmazlik-yetki-ve-tahkim-sarti
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Uyuşmazlık Çözümü, Yetki ve Tahkim Şartı

## Görev
Sözleşmenin uyuşmazlık mimarisini (uygulanacak hukuk, yetkili mahkeme, tahkim/arabuluculuk) denetlemek; klozların geçerliliğini ve müvekkil açısından elverişliliğini değerlendirmek.

## Soğuk başlangıç (intake)
- Taraflar tacir/kamu tüzel kişisi mi (yetki sözleşmesi geçerliliği için)?
- Yabancılık unsuru var mı (milletlerarası tahkim/uygulanacak hukuk)?
- Metin mahkeme mi, tahkim mi öngörüyor; nerede, hangi kurumda?
- Dava şartı arabuluculuk kapsamında bir uyuşmazlık mı (ticari/işçi-işveren/kira)?

## Denetim şeması
1. **Yetki sözleşmesi**: HMK m.17 — yetki sözleşmesi yalnızca **tacirler veya kamu tüzel kişileri** arasında geçerlidir; tüketici/işçi gibi zayıf tarafla yapılan yetki kaydı geçersizdir. Münhasır/seçimlik yetki ayrımı (m.17/f.2) ve kesin yetki halleri kontrol edilir.
2. **Tahkim şartı**: HMK m.412 vd. — tahkim sözleşmesi yazılı şekle tabidir (m.412/f.3), uyuşmazlık tahkime elverişli olmalıdır (m.408: taşınmaz ayni hakları ve iki tarafın iradesine tabi olmayan işler tahkime elverişsiz). Tüketici uyuşmazlıklarında tahkim şartı zayıf tarafı bağlamada sakıncalıdır. Milletlerarası tahkimde 4686 sayılı Kanun.
3. **Tahkim klozunun yeterliliği**: Kurum (ISTAC/ICC), yer, dil, hakem sayısı, uygulanacak usul ve esas hukuku net mi? "Patolojik" (belirsiz/çelişik) tahkim şartı işaretlenir.
4. **Uygulanacak hukuk**: Yabancılık unsuru varsa MÖHUK serbest seçim; emredici hükümler (kamu düzeni) saklı.
5. **Arabuluculuk**: Ticari (TTK m.5/A), işçi-işveren ve kira uyuşmazlıklarında **dava şartı arabuluculuk** zorunluluğu (6325 ve ilgili kanunlar) hatırlanır; sözleşmesel ihtiyari arabuluculuk basamağı eklenebilir.
6. **Ara sonuç**: Müvekkil için elverişli forum mu; kloz icra edilebilir mi, değiştirilmeli mi?

## Çıktı modülleri
- Uyuşmazlık mimarisi değerlendirme notu (geçerlilik + elverişlilik).
- Önerilen yetki/tahkim/arabuluculuk lafzı (kurum-yer-dil-hukuk net).
- Patolojik kloz uyarısı ve düzeltme önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

