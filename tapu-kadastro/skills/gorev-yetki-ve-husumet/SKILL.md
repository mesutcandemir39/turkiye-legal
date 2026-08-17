---
argument-hint: ''
description: Tapu-kadastro uyuşmazlığında hangi mahkemenin görevli, hangi yerin yetkili
  olduğu ve davanın kime karşı açılacağı belirlenirken; adli/idari yargı ayrımı, kadastro
  mahkemesi-genel mahkeme geçişi ve Haz
name: gorev-yetki-ve-husumet
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
  - ad: Tapu Kanunu
    numara: '3402'
    tur: kanun
  - ad: Kat Özel Koşulu Olmak Üzere Yapılan Satış Mukavelelerine Dair Kanun
    numara: '2644'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Görev, Yetki ve Husumet Haritası

## Görev
Tapu-kadastro davasında doğru mahkeme (görev), doğru yer (yetki) ve doğru davalıyı (husumet) tek bir denetimle belirleyip usulden kayıpları önlemek.

## Soğuk başlangıç (intake)
- Talep türü: tapu iptali-tescil, kadastro itirazı, tescil (m.713), düzeltim, men/ecrimisil, ortaklığın giderilmesi, tazminat (m.1007)?
- Taşınmaz hangi adliye çevresinde; kadastro çalışması/tutanağı kesinleşmiş mi?
- Karşı taraf gerçek kişi mi, Hazine mi, belediye/idare mi, mirasçılar mı?
- Uyuşmazlık özel hukuk işlemine mi, idari işleme (kamulaştırma/imar) mı dayanıyor?

## Denetim şeması
1. **Adli/idari yargı ayrımını yap.** Mülkiyet/ayni hak ve sicil uyuşmazlıkları adli yargıda (asliye/sulh hukuk). İdari işlemden (kamulaştırma kararı, imar planı, idari tasarruf) doğan iptal talepleri idari yargıda (2577 sayılı İYUK). Kamulaştırmasız el atmada el atmanın türüne göre adli/idari ayrım gözetilir.
2. **Görevli mahkemeyi seç.** Tapu iptali-tescil, men, düzeltim, tazminat → asliye hukuk (HMK m.2). Ortaklığın giderilmesi → sulh hukuk (HMK m.4). Kesinleşmemiş kadastro işine ilişkin uyuşmazlık → kadastro mahkemesi (3402 m.25-26), kesinleştikten sonra genel mahkeme.
3. **Yetkiyi belirle.** Taşınmazın aynına ilişkin davalarda taşınmazın bulunduğu yer mahkemesi kesin yetkilidir (HMK m.12); birden çok taşınmazda da bunlardan birinin yeri (HMK m.12/2).
4. **Husumeti kur.** Tapu iptalinde kayıt maliki ve ara malikler; tescil/zilyetlik davasında Hazine ve/veya ilgili idare; TMK m.1007 tazminatında Hazine; ortaklığın giderilmesinde tüm paydaşlar (zorunlu dava arkadaşlığı). Husumet eksikliği davanın reddine yol açar.
5. **Dava şartlarını gözden geçir.** Görev ve kesin yetki re'sen incelenir (HMK m.114-115); kadastroda 10 yıllık hak düşürücü süre (3402 m.12/3) re'sen dikkate alınır.
6. **Ara sonuç.** Mahkeme + yer + davalı çevresi tek tabloya bağlanır; yanlışsa gönderme/ret riski not edilir.

## Çıktı modülleri
- Talep türüne göre görev–yetki–husumet tablosu.
- Adli/idari yargı yolu ayrım notu (kamulaştırma/imar bağlantısı).
- Dava şartı ve süre kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

