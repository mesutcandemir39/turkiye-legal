---
argument-hint: ''
description: Otuz günlük başvuru süresinin ne zaman başladığı, tebliğ/öğrenme anı,
  mücbir sebep ve mazeretle eski hale getirme, sürenin kaçırılması halinde yapılabilecekler
  sorulduğunda kullanılır.
name: sure-ve-baslangic-ani
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  - ad: Anayasa Mahkemesinin Kuruluşu ve Yargılama Usulü Hakkında Kanun
    numara: '6216'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler ve Sürenin Başlangıcı

## Görev
Otuz günlük başvuru süresinin doğru başlangıç anını saptamak, hesabı yapmak ve süre aşımı/mazeret durumlarını değerlendirmek.

## Soğuk başlangıç (intake)
- Nihai (kesin) karar nedir ve başvurucuya ne zaman tebliğ edildi?
- Tebligat yapılmadıysa kararı fiilen ne zaman öğrendiniz, bunu neyle ispatlarsınız?
- Süreyi kaçırmaya yol açan bir mücbir sebep / ağır engel var mı?
- Bugün itibarıyla kaç gün geçti?

## Denetim şeması
1. Süre — 6216 m.47/5 ve İçtüzük m.64: bireysel başvurunun, başvuru yollarının tüketildiği tarihten; başvuru yolu öngörülmemişse ihlalin öğrenildiği tarihten itibaren OTUZ GÜN içinde yapılması gerekir.
2. Başlangıç anı — kural olarak nihai kararın başvurucuya TEBLİĞİ esastır. Tebligat yoksa fiilî öğrenme tarihi esas alınır; bu tarihin ispatı başvurucudadır.
3. Hesap — süre gün olarak hesaplanır; başlangıç günü hesaba katılmaz, son gün tatile rastlarsa ilk iş gününe uzar (genel usul ilkesi). Hak düşürücü niteliktedir.
4. Mazeret / eski hale getirme — m.47/5 son cümle ve İçtüzük: mücbir sebep veya ağır hastalık gibi haklı engel nedeniyle süre kaçırılmışsa, engelin kalkmasından itibaren onbeş gün içinde, mazereti belgeleyen delillerle başvuru yapılabilir; AYM mazeretin kabulüne karar verir.
5. Tedbir ihtiyacı — İçtüzük m.73: ciddi ve telafisi imkânsız zarar tehlikesi varsa, süreyle ayrıca tedbir talep edilir.

İspat yükü: öğrenme tarihi ve mazerete ilişkin belgeleri başvurucu sunar.

Ara sonuç: "süresinde / süre aşımı / mazeret yolu açık" tespiti, son başvuru tarihi.

## Çıktı modülleri
- Süre hesabı tablosu (nihai karar, tebliğ/öğrenme, son gün).
- Mazeret/eski hale getirme uygunluk notu.
- Süre aşımı halinde seçenekler ve riskler.
- Tedbir talebi gerekiyorsa hatırlatma.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

