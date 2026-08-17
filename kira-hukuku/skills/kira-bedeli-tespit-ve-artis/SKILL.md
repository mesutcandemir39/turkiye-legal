---
argument-hint: ''
description: Yenilenen dönemde uygulanacak kira artış oranı, sözleşmedeki artış kaydının
  geçerliliği, beş yılı aşan kiralarda hakkaniyet belirlemesi veya kira tespit davası
  açma şartları ve hesabı söz konusu olduğ
name: kira-bedeli-tespit-ve-artis
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


# Kira Bedelinin Belirlenmesi, Artışı ve Kira Tespit Davası

## Görev
Yenilenen kira döneminde geçerli kira bedelini hesaplamak; sözleşmedeki artış kaydını TBK m.344 sınırına göre denetlemek; kira tespit davasının (TBK m.345) şartlarını, süresini ve etkisini ortaya koymak.

## Soğuk başlangıç (intake)
- Sözleşmedeki artış kaydı ne (sabit oran, TÜFE, döviz)?
- Sözleşme kaç yıldır sürüyor; beş yıl doldu mu?
- Talep eden kim, hangi dönem için ne istiyor?
- Emsal kira ve taşınmazın durumu hakkında veri var mı?

## Denetim şeması
1. **Artış sınırı (TBK m.344/1)**: Tarafların yenilenen dönem için anlaştığı artış oranı, bir önceki kira yılında **on iki aylık ortalama TÜFE** oranını geçemez; aşan kısım geçersiz, sınıra çekilir. Bu kural sözleşmede daha yüksek oran kararlaştırılmış olsa da uygulanır.
2. **Anlaşma yoksa (m.344/2)**: Hâkim, TÜFE on iki aylık ortalamasını aşmamak üzere ve kiralananın durumunu gözeterek hakkaniyete göre belirler.
3. **Beş yıldan uzun/beşinci yıl sonrası (m.344/3)**: Beş yıldan uzun süreli veya beş yıldan sonra yenilenen sözleşmelerde, beşinci yılın sonunda hâkim; TÜFE oranı, kiralananın durumu ve **emsal kira bedelleri** ışığında **hakkaniyet** ile yeni bedeli belirler. Sonraki her beş yılda aynı şekilde.
4. **Yabancı para (m.344/4)**: Sözleşme döviz üzerinden ise beş yıl geçmedikçe değişiklik yapılamaz (kambiyo mevzuatı ve aşırı ifa güçlüğü — TBK m.138 saklı).
5. **Kira tespit davası (TBK m.345)**: Her zaman açılabilir; ancak yeni dönem başından önceki son otuz gün içinde açılır veya kiraya veren bu süre içinde yazılı bildirimde bulunmuşsa dava yeni dönem boyunca açılabilir ve karar yeni dönem başından itibaren etkili olur. Görev sulh hukuk mahkemesi.
6. **İspat ve ara sonuç**: Emsal kira, bilirkişi/keşif; hesabın oran + emsal + hakkaniyet üçlüsüyle gerekçelendirilmesi.

## Çıktı modülleri
- Dönem bazlı kira hesap tablosu.
- Artış kaydı geçerlilik notu.
- Kira tespit davası dilekçesi iskeleti (görev, süre, talep).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

