---
argument-hint: ''
description: Cezai şart, götürü tazminat, gecikme cezası ve dönme cezası maddelerinin
  türünü, geçerliliğini ve fahişliğini değerlendirmek gerektiğinde kullanılır.
name: cezai-sart-ve-tazminat-on-belirleme
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


# Cezai Şart ve Götürü Tazminat Denetimi

## Görev
Cezai şart/götürü tazminat kayıtlarının türünü (seçimlik, ifaya ekli, dönme cezası), geçerliliğini ve fahiş olup olmadığını belirlemek; müvekkil lehine dengeli lafzı kurmak.

## Soğuk başlangıç (intake)
- Ceza hangi ihlale bağlı (gecikme mi, hiç ifa etmeme mi, dönme mi)?
- Müvekkil cezayı ödeyecek taraf mı, talep edecek taraf mı?
- Taraflar tacir mi (TTK m.22 indirim sınırı)?
- Ceza yanında ayrıca tazminat ve aynen ifa talep ediliyor mu?

## Denetim şeması
1. **Tür tespiti**: TBK m.179 — (f.1) seçimlik cezai şart (ya ifa ya ceza), (f.2) ifaya ekli ceza (hem ifa hem ceza), (f.3) dönme cezası/cayma akçesi. Lafız hangisini kurduğu yoruma açıksa m.179'un karinesi uygulanır.
2. **Asıl borca bağlılık**: TBK m.182/f.1 — asıl borç geçersizse ceza da istenemez; ceza asıl borçtan fazla olsa bile kural olarak istenebilir ama (f.3) fahiş ceza hâkimce indirilir.
3. **Fahişlik indirimi**: TBK m.182/f.3 — hâkim aşırı cezayı indirir; bu yetki **emredicidir**, sözleşmeyle bertaraf edilemez. İstisna: tacir, ticari işinde TTK m.22 uyarınca fahişlik def'inden yararlanamaz (ancak ahlaka aykırı/ekonomik yıkım hâli saklı).
4. **Zarar şartı**: Cezai şart için alacaklının zarara uğraması şart değildir (m.180/f.1). Zarar cezayı aşarsa fark TBK m.180/f.2 uyarınca ispatla istenir.
5. **Denge testi**: Tek taraflı ceza, müvekkil aleyhine ağır ceza, ölçülemez tetikleyici işaretlenir; karşılıklılık ve tavan önerilir.
6. **İspat/usul**: İhlali ve cezanın muacceliyetini alacaklı ispatlar; temerrüt cezasında borçlunun temerrüde düşürülmesi (TBK m.117) aranabilir.

## Çıktı modülleri
- Cezai şart tür/geçerlilik/fahişlik değerlendirme notu.
- Dengeli ceza lafzı (karşılıklı, tavanlı, net tetikleyicili) önerisi.
- Tacir-tüketici ayrımına göre indirim riski uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

