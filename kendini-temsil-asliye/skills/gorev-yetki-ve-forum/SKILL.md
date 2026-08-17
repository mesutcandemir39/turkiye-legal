---
argument-hint: ''
description: Kullanıcı davayı hangi mahkemede ve hangi yerde açacağını bilmek istediğinde,
  sulh-asliye-tüketici ayrımı veya yetkili yer (yerleşim, sözleşme, haksız fiil yeri)
  sorusu gündeme geldiğinde kullanılır.
name: gorev-yetki-ve-forum
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Görev, Yetki ve Doğru Mahkemenin Belirlenmesi

## Görev
Davanın hangi tür mahkemede (görev) ve hangi yerdeki mahkemede (yetki) açılacağını doğru saptamak; yanlış mahkemede açıp süre ve harç kaybetmeyi önlemek.

## Soğuk başlangıç (intake)
- Uyuşmazlığın konusu ve yaklaşık değeri nedir?
- Karşı tarafın yerleşim yeri/adresi neresi?
- Bir sözleşme var mı, varsa ifa yeri neresi?
- Haksız fiil/zarar nerede gerçekleşti?
- Taşınmaz söz konusu mu?

## Denetim şeması
1. **Görev (tür):** Görev kamu düzenindendir, re'sen incelenir (HMK m.114/1-c). Sulh hukukun görevi HMK m.4'te sayılıdır (kira ilişkisinden doğan davalar, paydaşlığın/ortaklığın giderilmesi, zilyetliğin korunması, taşınır/taşınmaz teslimi). Sayılmayan işlerde genel görevli asliye hukuktur (m.2). Tüketici işlemiyse tüketici mahkemesi/hakem heyeti (6502 sayılı Kanun); iş ilişkisiyse iş mahkemesi.
2. **Yetki (yer) — genel kural:** Davalının yerleşim yeri mahkemesi (HMK m.6). Birden fazla davalı varsa herhangi birinin yerleşim yeri (m.7).
3. **Özel/seçimlik yetki:** Sözleşmeden doğan davada sözleşmenin ifa yeri (HMK m.10); haksız fiilde fiilin işlendiği veya zararın doğduğu yer (m.16); taşınmaza ilişkin ayni hak ve zilyetlik davalarında taşınmazın bulunduğu yer **kesin yetkilidir** (m.12). Tüketici, kendi yerleşim yeri tüketici hakem heyetine de başvurabilir.
4. **İspat yükü/itiraz:** Yetki itirazı, kesin yetki yoksa, ilk itiraz olarak cevap dilekçesinde ileri sürülür (HMK m.116, 117); süresinde yapılmazsa yetki kesinleşir. Görev ise her aşamada incelenir.
5. **Ara sonuç:** Görevli mahkeme türü + yetkili yer kombinasyonu netleşir; kesin yetki varsa seçimlik yetki kapanır.

## Çıktı modülleri
- Forum kararı (görevli mahkeme + yetkili yer + gerekçe maddesi).
- Alternatif yetkili yerler listesi (seçimlik yetkide).
- Yanlış forum riski ve görevsizlik/yetkisizlik kararının sonuçları (HMK m.20 süre/dosya gönderme) notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

