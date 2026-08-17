---
argument-hint: ''
description: Aile içi şiddet, taciz, tehdit veya ısrarlı takip hallerinde 6284 sayılı
  Kanun kapsamında koruyucu ve önleyici tedbir başvurusu hazırlamak, tedbir türünü
  ve mercii seçmek gerektiğinde kullanılır.
name: koruma-kararlari-6284
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
  - ad: Ailenin Korunması ve Kadına Karşı Şiddetin Önlenmesine Dair Kanun
    numara: '6284'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# 6284 Koruma Kararları ve Aile İçi Şiddet

## Görev
Şiddet veya şiddet tehlikesi altındaki kişi için 6284 sayılı Kanun çerçevesinde doğru tedbiri (koruyucu/önleyici) ve mercii (hâkim/mülki amir/kolluk) belirleyip başvuruyu hızla hazırlamak.

## Soğuk başlangıç (intake)
1. Şiddetin türü nedir: fiziksel, cinsel, psikolojik, ekonomik, ısrarlı takip?
2. Mağdur ve şiddet uygulayan kim; aralarında evlilik/akrabalık/birliktelik var mı?
3. Acil tehlike var mı (gecikmesinde sakınca bulunan hal)?
4. Mağdurun barınma, uzaklaştırma, iletişimin engellenmesi gibi öncelikli ihtiyacı nedir?

## Denetim şeması
1. **Kapsam.** 6284 sK. şiddete uğrayan veya uğrama tehlikesi bulunan kadın, çocuk, aile bireyleri ve tek taraflı ısrarlı takip mağdurlarını korur (m.1). Şiddet delili veya raporu **şart değildir**; beyan esas alınarak tedbir verilebilir.
2. **Önleyici tedbirler — hâkim (m.5).** Şiddet uygulayana yönelik: konuta/işyerine/okula yaklaşmama, iletişim kurmama, mağduru rahatsız etmeme, silah teslimi, alkol/madde kullanmama, sağlık kuruluşuna başvurma; gerekirse elektronik kelepçe (teknik takip).
3. **Koruyucu tedbirler (m.3, m.4).** Mağdura yönelik: uygun barınma yeri/sığınmaevi, geçici maddi yardım, kreş, kimlik/adres gizliliği, geçici koruma.
4. **Mercii ve hız.** Tedbirlere kural olarak aile mahkemesi hâkimi karar verir; **gecikmesinde sakınca bulunan hallerde** mülki amir koruyucu tedbire, kolluk amiri ise belirli önleyici tedbirlere (uzaklaştırma vb.) karar verir ve 24 saat içinde hâkim onayına sunar (m.8). Karar genellikle ilk başta en çok altı aya kadar verilir, uzatılabilir (m.8/3).
5. **İhlal yaptırımı.** Tedbir kararına aykırılıkta zorlama hapsi: her ihlal için 3-10 gün, tekrarında 15-30 güne kadar (m.13). Başvuru **harçtan muaftır**.
6. **Ara sonuç.** Tedbir listesi + mercii + süre + ihlal yaptırımı uyarısı raporlanır.

## Çıktı modülleri
- Talep edilecek tedbirlerin maddeye dayalı listesi.
- Aciliyet ve mercii (hâkim/mülki amir/kolluk) kararı.
- 6284 başvuru dilekçesi taslağı ve ihlal halinde izlenecek yol notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

