---
argument-hint: ''
description: Bir hukuki metni sadeleştirme işine başlamadan önce sade dilin temel
  ilkelerini, anlama-aktarma-doğrulama katmanlarını ve hukuki doğruluğu koruma sınırlarını
  kurmak gerektiğinde kullanılır.
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Sade Dilin Temel İlkeleri ve Sistematiği

## Görev
Sade hukuk dili işinin yöntemsel temelini kurmak: bir metnin neden, kim için ve hangi düzeyde
sadeleştirileceğini belirlemek; anlama-aktarma-doğrulama katmanlarını uygulayıp hukuki doğruluğu
korumak. Bu beceri, sonraki tüm sadeleştirme işlerinin altlığını verir.

## Soğuk başlangıç (intake)
1. Sadeleştirilecek belge nedir (dilekçe, mahkeme kararı, sözleşme, ihtarname, bilirkişi raporu)?
2. Okuyucu kim (müvekkil, karşı taraf, tanık, hukukçu olmayan yönetici, tüketici)?
3. Amaç ne (bilgilendirme, karar verdirme, onay alma, itiraz hazırlığı)?
4. İstenen düzey: tam çeviri mi, kısa özet mi, terim sözlüğü mü?
5. Bağlayıcı/asıl metin elinizde mi; eksik bilgi var mı?

## Denetim şeması
1. ANLAMA: Kaynak metnin hukuki iskeleti çıkarılır — hangi norm (madde/fıkra ile), hangi süre,
   hangi şart, hangi sonuç, hangi risk. Sadeleştirmeden önce metin hukuken doğru anlaşılmalıdır.
   Vekilin aydınlatma borcu (TBK m.506; Avukatlık K. 1136 s. m.34) bu doğruluğu zorunlu kılar.
2. KİTLE VE DÜZEY: Okuyucuya göre düzey seçilir. Tüketici metinlerinde anlaşılırlık aynı zamanda
   uyum ölçütüdür (TKHK m.4-5; genel işlem koşullarında TBK m.20-23).
3. AKTARMA: Tek fikir-tek cümle, etken çatı, kısa paragraf; jargon ilk geçtiği yerde parantezle
   açıklanır; süreler takvim tarihiyle somutlanır.
4. NÜANS KORUMA (ispat/anlam yükü): Koşullu ifadeler ("…hâlinde", "…koşuluyla") mutlaklaştırılmaz;
   "zamanaşımı" ile "hak düşürücü süre", "fesih/iptal/dönme", "müteselsil sorumluluk" gibi
   terimler açıklanır ama yanlış eşanlamlıyla değiştirilmez.
5. DOĞRULAMA (ara sonuç): Sade metin kaynakla satır satır karşılaştırılır; düşen hak, süre, şart
   veya çekince var mı denetlenir. Anlamı değiştiren basitleştirme geri alınır.
6. İSTİSNA: Hukuki kesinlik gerektiren bağlayıcı belgelerde (icra emri, ihtarname tebliği) sade
   metin yalnızca açıklayıcı eşlik metni olur; asıl metnin yerini almaz.

## Çıktı modülleri
- Sadeleştirme brifi: belge künyesi, okuyucu, düzey.
- Katman notları: anlaşılan hukuki iskelet (madde atıflarıyla).
- Sade metin + korunması gereken terimler listesi.
- Doğrulama kontrol satırı ve "[doldurulacak]" yer tutucuları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

