---
argument-hint: ''
description: Kişisel veri, veri sorumlusu, veri işleyen, ilgili kişi, açık rıza ve
  özel nitelikli veri ayrımlarının netleştirilmesi gereken her başlangıçta; rol ve
  kavram tespiti yapılırken kullanılır.
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
  sources:
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# KVKK Temel Kavramlar ve Sistematik

## Görev
KVKK uyuşmazlık veya uyum çalışmasının daha en başında kavramsal zemini doğru kurmak: kişisel veri/özel nitelikli veri ayrımı, veri sorumlusu/veri işleyen/ilgili kişi rolleri, işleme ve aktarım kavramları, açık rızanın gerçek hukuki yeri.

## Soğuk başlangıç (intake)
1. Hangi gerçek kişiye ait, hangi tür veriler söz konusu (kimlik, iletişim, sağlık, biyometrik, finansal)?
2. Müvekkil bu verilerin işlenmesinde kim — sorumlu mu, işleyen mi, ilgili kişi mi?
3. Veriler nereden geliyor, hangi amaçla işleniyor, kime aktarılıyor?
4. İşleme tek seferlik mi, süreklilik gösteren bir faaliyet mi?

## Denetim şeması
1. **Kişisel veri mi?** KVKK m.3/1-d: kimliği belirli veya belirlenebilir gerçek kişiye ilişkin her türlü bilgi. Tüzel kişi verisi KVKK kapsamı dışıdır; anonim hale getirilmiş veri kişisel veri değildir.
2. **Özel nitelikli mi?** KVKK m.6/1: ırk, etnik köken, siyasi düşünce, din-mezhep, kılık-kıyafet, dernek-vakıf-sendika üyeliği, sağlık, cinsel hayat, ceza mahkûmiyeti/güvenlik tedbiri, biyometrik ve genetik veriler. Bu liste sınırlıdır (numerus clausus); kıyasla genişletilmez.
3. **Rol tespiti** (m.3): Veri sorumlusu işleme amaç ve vasıtalarını belirleyen; veri işleyen onun adına işleyen kişidir. Yükümlülükler asıl olarak sorumluya yüklenir; aralarında m.12 uyarınca yazılı sözleşme zorunludur.
4. **İşleme şartı var mı?** Genel veride m.5, özel nitelikli veride m.6. Açık rıza tek değil, son çare şarttır — m.3/1-a anlamında özgür irade, belirli konu ve aydınlatmaya dayalı bilgi unsurlarını taşımalıdır; aksi halde geçersizdir.
5. **Ara sonuç**: Kavram ve rol netleşmeden m.4 ilkeleri ve yaptırım katmanına geçilmez.

İspat yükü: İşlemenin hukuka uygunluğunu (geçerli şarta dayandığını) veri sorumlusu ispatlar; açık rızanın varlığını da sorumlu kanıtlamak zorundadır.

## Çıktı modülleri
- Rol ve veri kategorisi tablosu (genel/özel nitelikli; sorumlu/işleyen).
- İşleme faaliyeti tanım fişi (amaç-veri-sebep-süre-aktarım).
- Açık rızanın gerekip gerekmediğine dair kısa değerlendirme notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

