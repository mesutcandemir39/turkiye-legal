---
argument-hint: ''
description: Bir normun anlamı tartışmalıyken ya da hiç norm yokken (kanun boşluğu);
  lafzî-sistematik-tarihsel-amaçsal yorum, kıyas, a contrario ve TMK m.1 çerçevesinde
  hâkimin hukuk yaratması yöntemini uygulamak
name: yorum-yontemleri-ve-bosluk
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


# Yorum Yöntemleri ve Boşluk Doldurma

## Görev
Normun anlamını yöntemli biçimde belirlemek (yorum) veya norm yokluğunda boşluğu TMK m.1
disipliniyle doldurmak; yorum argümanlarını hiyerarşik ve gerekçeli biçimde sıralamak.

## Soğuk başlangıç (intake)
- Norm var mı? Varsa anlamı mı tartışmalı (yorum), yoksa hiç mi yok (boşluk)?
- Boşluk gerçek (kural hiç yok) mü, örtülü/açık mı, yoksa "kasıtlı sessizlik" (a contrario) mi?
- Tartışmada karşı tarafın dayandığı yorum argümanı ne?
- Emredici/yasaklayıcı bir alanda mıyız (kıyas yasağı/dar yorum gerektiren alan var mı, ör. ceza)?

## Denetim şeması
1. **Lafzî yorumla başla.** Metnin olağan dil anlamını sapta (TMK m.1: önce kanunun "sözü").
   Açık ve tek anlamlı lafız varsa amaçsal yoruma zıt sonuç çıkarmaktan çekin.
2. **Sistematik + tarihsel + amaçsal yorumu ekle.** Normun kanun içindeki yerini, gerekçesini
   (tarihsel) ve koruduğu amacı (gai/teleolojik) değerlendir. TMK m.1: kanunun "özü/ruhu".
   Objektif-güncel ve sübjektif-tarihsel yorum gerilimini, hangisinin makul sonucu verdiğini
   tartışarak çöz.
3. **Mantıksal argümanları sırala.** Kıyas (benzer olaya benzer kural), evleviyet (a fortiori),
   aksi ile kanıt (a contrario) ve amaca aykırı genişlemeyi daraltan teleolojik redüksiyonu
   uygula. Ceza hukukunda kıyas yasağı (TCK m.2; Anayasa m.38 kanunilik) sınırını mutlaka gözet.
4. **Boşluk tespiti ve doldurma.** Norm yoksa: (a) örtülü boşluk-kasıtlı susma ayrımını yap;
   (b) kasıtlı susma ise a contrario; (c) gerçek boşluk ise önce örf-âdet hukuku (TMK m.1/II),
   sonra hâkimin hukuk yaratması (TMK m.1/II son cümle: "kendisi kanun koyucu olsaydı")
   devreye girer; (d) bu yaratma "bilimsel görüşlere ve yargı kararlarına" dayandırılır
   (TMK m.1/III). Ara sonuç: kanun → örf-âdet → hâkim hukuku sırası.
5. **İspat/gerekçe yükü.** Tercih edilen yorumun neden diğerlerine üstün olduğu gerekçelendirilir;
   dayanak doktrin/yerleşik içtihat ile desteklenir, künye doğrulanmadıkça [DOĞRULANMADI].

## Çıktı modülleri
- Yorum argümanları tablosu (lafzî/sistematik/tarihsel/amaçsal + sonuç).
- Boşluk tipi etiketi ve doldurma yolu (TMK m.1 sırasıyla).
- Karşı argümana cevap notu.
- Önerilen yorumun gerekçeli özeti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

