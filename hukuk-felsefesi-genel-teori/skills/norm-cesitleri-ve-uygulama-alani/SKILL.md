---
argument-hint: ''
description: Bir kuralın emredici mi yedek mi olduğu, kural-istisna ilişkisi, normun
  zaman (geçmişe etki) ve yer bakımından uygulanması veya çatışan iki normun hangisinin
  önce geleceği belirlenmek istendiğinde kul
name: norm-cesitleri-ve-uygulama-alani
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


# Norm Çeşitleri ve Normun Uygulama Alanı

## Görev
Normları niteliklerine göre sınıflamak (emredici/yedek, genel/özel, kural/istisna) ve normun
zaman, yer ve kişi bakımından uygulama alanını ile norm çatışmalarının çözüm ilkelerini
belirlemek. Bu, "hangi kural, bu olaya, ne zamandan itibaren uygulanır" sorusunun cevabıdır.

## Soğuk başlangıç (intake)
- Kural emredici mi (aksi kararlaştırılamaz) yoksa yedek/tamamlayıcı mı (aksi serbestçe
  kararlaştırılabilir)?
- Olay, yeni bir kanunun yürürlüğünden önce mi gerçekleşti (zaman bakımından uygulama)?
- İki norm çatışıyor mu? Biri özel/sonraki/üst mü?
- Yabancılık unsuru var mı (yer bakımından/MÖHUK devrede mi)?

## Denetim şeması
1. **Niteliği belirle.** Emredici hüküm (kamu düzeni/zayıf koruması; aksi sözleşme TBK m.27
   uyarınca hükümsüz) ile yedek hüküm (tarafların aksini kararlaştırabildiği) ayrımını yap.
   Sözleşme serbestisi (TBK m.26) sınırı buradadır.
2. **Kural-istisna mantığını kur.** İstisna hükmü dar yorumlanır; istisnayı ileri süren
   ispatla yükümlüdür. Genel-özel ilişkisinde özel norm önceliklidir (lex specialis).
3. **Zaman bakımından uygula.** Kanunların geriye yürümezliği esastır; kazanılmış haklar ve
   hukuki güvenlik korunur. Usul kurallarında derhal uygulama, maddi kurallarda yürürlük anı
   esastır. Yürürlük ve uygulama için ilgili yürürlük kanunu/geçiş hükümlerine bak (ör. TMK
   ve TBK'nın yürürlük ve uygulama şekli hakkındaki kanunları).
4. **Çatışmayı çöz.** Lex superior (üst norm; Anayasa m.11), lex specialis (özel norm) ve
   lex posterior (sonraki norm) ilkelerini sırayla uygula; üstünlük ilkesi diğerlerini bastırır.
   Ara sonuç: uygulanacak tek norm.
5. **Yer/kişi bakımından.** Yabancılık unsuru varsa uygulanacak hukuk MÖHUK (5718) bağlama
   kurallarıyla belirlenir; ceza için TCK m.8 vd. mülkilik/şahsilik ilkeleri devreye girer.
   İlkesel atıf yeterli, somut karar künyesi gerekiyorsa [DOĞRULANMADI].

## Çıktı modülleri
- Norm nitelik etiketi (emredici/yedek; genel/özel).
- Zaman bakımından uygulama notu (geçiş hükmü atfıyla).
- Çatışma çözüm zinciri (üst/özel/sonraki).
- Yer-kişi bakımından uygulanacak hukuk tespiti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

