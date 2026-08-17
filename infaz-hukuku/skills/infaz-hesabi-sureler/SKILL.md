---
argument-hint: ''
description: Hapis cezasının koşullu salıverilme, denetimli serbestlik, açığa ayrılma
  ve bihakkın tahliye tarihlerini hesaplamak, gözaltı/tutukluluk mahsubunu çıkarmak
  gerektiğinde kullanılır.
name: infaz-hesabi-sureler
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
  - ad: Ceza ve Güvenlik Tedbirlerinin İnfazı Hakkında Kanun
    numara: '5275'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İnfaz Hesabı, Mahsup ve Süreler

## Görev
Verilen hapis cezası için açığa ayrılma, denetimli serbestlik, koşullu salıverilme ve bihakkın (kesin) tahliye tarihlerini, mahsuplar dahil olmak üzere doğru biçimde hesaplamak.

## Soğuk başlangıç (intake)
- Toplam hapis cezası ne kadar; birden fazla ilam varsa içtima yapıldı mı?
- Suç tarihi ve suç tipi nedir (oran bu ikisine bağlı)?
- Gözaltı/tutukluluk süresi var mı (mahsup için)?
- Hükümlünün infaza başlama tarihi nedir; firar/ara verme oldu mu?

## Denetim şeması
1. Mahsup: gözaltı ve tutuklulukta geçen süre cezadan düşülür (TCK m.63). Aynı ilam nedeniyle uygulanan adli kontrol/elektronik kelepçe de değerlendirilir. Ara sonuç: net çekilecek ceza.
2. Koşullu salıverilme oranı: kural 5275 m.107 uyarınca uygulanır; suç tarihine göre TCK geçici m.6 ve 7242 sayılı Kanun değişiklikleri lehe hüküm (TCK m.7) süzgecinden geçirilir. İstisnai suç tipleri (kasten öldürme, cinsel dokunulmazlığa karşı suçlar, terör, uyuşturucu ticareti) için ağırlaştırılmış oranlar ayrıca kontrol edilir.
3. Denetimli serbestlik: 5275 m.105/A uyarınca koşullu salıverilmeye belirli süre kala (genel kural ve geçici düzenlemeler farklı olabilir) açık kurumdan denetimli serbestliğe ayrılma hesaplanır.
4. Açığa ayrılma: 5275 m.14 ve Açık Ceza İnfaz Kurumlarına Ayrılma Yönetmeliği kıstasları.
5. İspat/doğrulama: çıkan sonuç UYAP infaz hesabı ve Cumhuriyet Başsavcılığı infaz bürosu hesabıyla karşılaştırılır; tutarsızlık infaz hâkimliğine şikâyet konusu yapılır (4675 sayılı Kanun).
6. Ara sonuç: dört kritik tarih (açığa ayrılma, denetimli serbestlik, koşullu salıverilme, bihakkın tahliye) tablo halinde.

## Çıktı modülleri
- Tarih hesabı tablosu (oran, mahsup, sonuç tarihleri).
- Lehe kanun karşılaştırması (suç tarihi vs. yürürlük).
- Hesap hatası varsa infaz hâkimliğine itiraz taslağı tetiği.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

