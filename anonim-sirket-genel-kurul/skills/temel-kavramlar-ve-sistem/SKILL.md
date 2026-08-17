---
argument-hint: ''
description: Anonim sirket genel kurulunun organ yapisi, gorev-yetki dagilimi, toplanti
  turleri ve karar gecersizligi rejiminin haritasini cikarmak gerektiginde; kullanicinin
  sorununu dogru alt-konuya yonlendirmek
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
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Sistematik

## Görev
Anonim şirket genel kurulu (GK) hukukunun temel kavramlarını ve sistematiğini ortaya koymak; somut soruyu doğru alt-rejime (çağrı, nisap, temsil, iptal/butlan, azlık) yerleştirerek çalışma planı çıkarmak.

## Soğuk başlangıç (intake)
1. Şirket kapalı AŞ mi, halka açık/borsada işlem gören mi (SPK rejimi devreye girer mi)?
2. Sorun toplantı öncesi (çağrı/gündem), toplantı anı (nisap/temsil/oy) yoksa toplantı sonrası (karar geçersizliği) aşamasında mı?
3. Müvekkil pay sahibi mi, yönetim kurulu üyesi mi, azlık mı, şirket tüzel kişiliği mi?
4. Pay oranı ve imtiyaz var mı; oydan yoksunluk doğuran ilişki var mı?

## Denetim şeması
1. **Organ ve yetki:** GK'nin devredilemez görevleri TTK m.408'de sayılır (esas sözleşme değişikliği, organ seçimi/ibrası, finansal tabloların onayı, kâr dağıtımı, fesih vb.). Bir kararın hangi organa ait olduğu, yetki aşımının yaptırımını belirler; GK yetkisindeki bir işin YK'ce yapılması yokluk/butlan sorununa gider.
2. **Toplantı türü:** Olağan GK her faaliyet dönemi sonundan itibaren üç ay içinde (m.409/1); olağanüstü GK gerektikçe yapılır. Süreye uyulmaması başlı başına kararı sakatlamaz ama sorumluluk doğurabilir.
3. **Geçersizlik kademesi (ara sonuç):** Sakatlığı önce **yokluk** (hiç toplantı/çağrı yokluğu, irade yokluğu), sonra **butlan** (m.447 — vazgeçilemez pay sahipliği haklarına aykırılık, AŞ'nin temel yapısına/sermayenin korunmasına aykırılık), en sonra **iptal edilebilirlik** (m.445 — kanuna, esas sözleşmeye, dürüstlük kuralına aykırılık) sırasıyla test et. Butlan/yokluk süresiz ve herkesçe ileri sürülür; iptal üç aylık hak düşürücü süreye ve sınırlı davacı çevresine tabidir.
4. **İspat yükü:** Usulsüzlüğü ileri süren taraf vakıayı (örn. çağrı ilanının yapılmadığı) ispatla yükümlüdür; şirket usule uygunluğu tutanak, hazır bulunanlar listesi ve ilan belgeleriyle karşılar (TMK m.6).

## Çıktı modülleri
- Sorunun aşama haritası (öncesi/anı/sonrası) ve uygulanacak madde listesi.
- Geçersizlik kademesi tablosu (yokluk/butlan/iptal + süre + davacı).
- İlgili alt-beceriye yönlendirme ve eksik bilgi listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

