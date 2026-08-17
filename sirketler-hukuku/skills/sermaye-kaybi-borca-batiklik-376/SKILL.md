---
argument-hint: ''
description: Şirketin son bilançosunda sermaye ve kanuni yedeklerin yarısının ya da
  üçte ikisinin karşılıksız kalması veya borca batıklık (teknik iflas) ortaya çıktığında;
  m.376 iyileştirme tedbirlerini, YK yüküml
name: sermaye-kaybi-borca-batiklik-376
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


# Sermaye Kaybı ve Borca Batıklık (TTK m.376)

## Görev
Sermaye kaybı/borca batıklık eşiğini saptamak; yönetim kurulunun çağrı, tedbir önerme ve mahkemeye bildirim yükümlülüklerini işletmek; teknik iflasa karşı iyileştirme yollarını planlamak.

## Soğuk başlangıç (intake)
1. Son yıllık/ara bilançoya göre sermaye + kanuni yedeklerin ne kadarı karşılıksız?
2. Borca batıklık şüphesi var mı (aktifler borçları karşılamıyor mu)?
3. YK genel kurulu çağırdı mı; hangi tedbirler önerildi/uygulandı?
4. Sermaye artırımı/azaltımı, sermaye taahhüdü veya borçların ertelenmesi mümkün mü?
5. Konkordato başvurusu düşünülüyor mu; alacaklı yapısı nasıl?

## Denetim şeması
1. Yarı kaybı (m.376/1): Son bilançoya göre sermaye + kanuni yedeklerin yarısı karşılıksızsa, YK genel kurulu derhal toplantıya çağırır ve iyileştirici tedbirleri sunar (bilgilendirme + öneri).
2. Üçte iki kaybı (m.376/2): Sermaye + kanuni yedeklerin üçte ikisi karşılıksızsa, genel kurul ya kalan üçte birle yetinmeye (sermaye azaltımı) ya da sermayenin tamamlanmasına/artırılmasına karar vermeli; aksi halde şirket kendiliğinden sona erer. Tamamlama akçesi ve azaltım-artırım kombinasyonu.
3. Borca batıklık (m.376/3): Aktiflerin şirket borçlarını karşılamadığı yönünde işaretler varsa YK, hem işletmenin devamlılığı esasına hem muhtemel satış değerine göre ara bilanço düzenler. Batıklık varsa YK durumu mahkemeye bildirir (iflas talebi).
4. İflasın ertelenmesi yerine: Bildirim öncesi/yerine İİK m.285 vd. konkordato yoluna gidilebilir; iyileştirme projesi ve mühlet.
5. Bağlı düzenlemeler: m.376 uygulamasına ilişkin Bakanlık tebliği (zararların mahsubu, yabancı para/kur etkilerinin değerlendirilmesi gibi geçici/idari ölçütler) güncel metinden teyit edilmeli.
6. Sorumluluk bağı: m.376 yükümlülüklerinin ihlali YK üyeleri için m.553 sorumluluğu doğurabilir.
7. İspat: Bilanço/ara bilanço ve değerleme belgeleri esas; batıklık tespiti mahkemece bilirkişi ile.

## Çıktı modülleri
- Eşik tespiti tablosu (yarı/üçte iki/borca batıklık).
- YK çağrı ve tedbir önerisi taslağı; genel kurul karar seçenekleri.
- Mahkemeye bildirim veya konkordato yol haritası.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

