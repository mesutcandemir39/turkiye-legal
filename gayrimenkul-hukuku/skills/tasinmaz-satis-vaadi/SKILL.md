---
argument-hint: ''
description: Bir taşınmazın ileride devredileceğine dair noter sözleşmesi yapıldığında
  veya satıcı devirden kaçındığında; vaadin geçerliliği, şerhi, ifası ve tapu iptali-tescil
  yoluyla zorla tescil için kullanılır
name: tasinmaz-satis-vaadi
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Taşınmaz Satış Vaadi Sözleşmesi

## Görev
Taşınmaz satış vaadini kurmak, geçerliliğini denetlemek ve ifasını sağlamak: vaad borçlusu devirden kaçınırsa vaad alacaklısının tapu iptali ve tescil yoluyla mülkiyeti zorla edinmesini değerlendirmek; şerhin üçüncü kişilere karşı koruyucu etkisini işletmek.

## Soğuk başlangıç (intake)
- Vaad noterde resmî şekilde mi düzenlendi/tasdik mi edildi; tarih ve taraflar net mi?
- Satış vaadi tapuya şerh edildi mi (TMK m.1009); şerh tarihi ne?
- Alıcı bedeli (kısmen/tamamen) ödedi mi, taşınmaz fiilen teslim edildi mi?
- Taşınmaz bu arada üçüncü bir kişiye devredildi mi; o kişi iyiniyetli mi?

## Denetim şeması
1. **Geçerlilik şekli**: Taşınmaz satış vaadi resmî şekle tabidir; noterde düzenleme şeklinde yapılır (TBK m.29; Noterlik K. 1512 m.60/3, m.89). Adi yazılı vaad kural olarak geçersizdir (TBK m.27).
2. **Şerh ve üçüncü kişiye etki**: Satış vaadi tapu kütüğüne şerh edilebilir (TMK m.1009; TST). Şerhle, vaad sonraki maliklere karşı ileri sürülebilir hâle gelir; şerh yoksa üçüncü iyiniyetli kazananın hakkı korunur (m.1023) ve alacaklı tazminata yönelir.
3. **İfa talebi (tapu iptali ve tescil)**: Vaad borçlusu devirden kaçınırsa alacaklı, aynen ifa olarak tapu iptali ve tescil davası açar; mahkeme kararı tescili sağlar (TMK m.705/2 çerçevesinde). Karşılıklı edimlerde alıcının bedeli ifaya hazır olması (ödeme/depo) aranır.
4. **Zamanaşımı**: Satış vaadinden doğan ifa talebi genel zamanaşımına (10 yıl, TBK m.146) tabidir; sürenin başlangıcı sözleşmede kararlaştırılan ifa anına bağlanır. Taşınmazın teslim edilip kullanılması zamanaşımı savunmasını dürüstlük süzgecinden geçirir (TMK m.2) [ilkeler için karararama.yargitay.gov.tr].
5. **Kat karşılığı ile ilişki**: Arsa sahibi-yüklenici ilişkisinde, yükleniciden bağımsız bölüm satın alan üçüncü kişi de satış vaadi/temlik zincirine dayanarak doğrudan arsa sahibine karşı tescil isteyebilir (yüklenicinin edimini ifa etmiş olması kaydıyla) [doğrulanacak — karararama.yargitay.gov.tr].
6. **Ara sonuç**: Geçerli + (varsa) şerhli vaadde ifaya hazır alacaklı tescili icbar eder; aksi hâlde tazminat.

## Çıktı modülleri
- Satış vaadi sözleşmesi taslağı (taraflar, taşınmaz, bedel, ifa tarihi, şerh kaydı) [doldurulacak] yer tutucularıyla.
- Tapu iptali ve tescil dava dilekçesi iskeleti (vaad, ödeme, talep sonucu).
- Şerh/ihtiyati tedbir ve zamanaşımı uyarı notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

