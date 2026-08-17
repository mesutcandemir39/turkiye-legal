---
argument-hint: ''
description: Bir talebin hâlâ ileri sürülebilir olup olmadığını, zamanaşımı veya hak
  düşürücü süre dolup dolmadığını ve kesilme-durma etkilerini değerlendirmek gerektiğinde
  kullanılır.
name: zamanasimi-ve-sure-hesabi
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
  - ad: Avukatlık Kanunu
    numara: '1136'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Zamanaşımı ve Hak Düşürücü Süre Hesabı

## Görev
Somut bir talep için zamanaşımı/hak düşürücü süre durumunu hesaplamak; başlangıç anını, süreyi, kesilme ve durma sebeplerini değerlendirip talebin canlı olup olmadığını belirlemek.

## Soğuk başlangıç (intake)
1. Talebin hukuki niteliği nedir (sözleşme alacağı, haksız fiil tazminatı, sebepsiz zenginleşme, işçilik alacağı vb.)?
2. Talebin doğduğu/muaccel olduğu tarih nedir; haksız fiilde fail ve zarar ne zaman öğrenildi?
3. Bu arada dava, takip, ihtarname, borç ikrarı veya kısmi ödeme oldu mu?
4. Tarafların tacir/şirket olup olmadığı ve özel bir kanunun (İş K., TKHK, sigorta) uygulanıp uygulanmadığı?

## Denetim şeması
1. **Süre tipi ayrımı**: Zamanaşımı def'i ileri sürülünce dikkate alınır; hak düşürücü süre re'sen gözetilir ve kesilmez/durmaz. Önce talebin hangi rejime tabi olduğu belirlenir.
2. **Süre uzunluğu**: Genel zamanaşımı TBK m.146 — 10 yıl; periyodik edimler/kira/faiz vb. TBK m.147 — 5 yıl; haksız fiil TBK m.72 — fiil ve failin öğrenilmesinden 2, her halde 10 yıl (ceza zamanaşımı daha uzunsa o); sebepsiz zenginleşme TBK m.82 — 2/10 yıl. İş Kanunu, TKHK, sigorta (TTK), taşıma gibi özel süreler önceliklidir.
3. **Başlangıç**: Kural olarak alacağın muaccel olduğu an (TBK m.149); haksız fiilde öğrenme anı.
4. **Kesilme (TBK m.154)**: Borçlunun ikrarı, kısmi ödeme, dava/takip, ihtilafın mahkemeye/hakeme götürülmesi süreyi keser; kesilmeden sonra yeni süre işler (m.156).
5. **Durma (TBK m.153)**: Belirli ilişkilerde (örn. evlilik, vesayet) süre durur.
6. **Ara sonuç**: Başlangıç + süre − kesilme/durma hesabıyla son tarih bulunur; dolduysa talebin riski, dolmadıysa kalan süre raporlanır.

## Çıktı modülleri
- Zamanaşımı hesap tablosu (nitelik, dayanak, başlangıç, kesilmeler, sonuç tarihi).
- Risk notu (dolmuş/dolmak üzere/canlı) ve önerilen acil aksiyon.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

