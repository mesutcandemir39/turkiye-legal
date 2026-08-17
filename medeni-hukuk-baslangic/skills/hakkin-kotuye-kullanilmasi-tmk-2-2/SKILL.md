---
argument-hint: ''
description: Lafzen haklı görünen bir talep veya savunma somut olayda hakkaniyete
  açıkça aykırı düştüğünde; çelişkili davranış, hakkın geç kullanılması, salt zarar
  verme veya menfaat dengesizliği iddiası gündeme g
name: hakkin-kotuye-kullanilmasi-tmk-2-2
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
  version: 0.1.0
user-invocable: true
---


# Hakkın Kötüye Kullanılması Yasağı (TMK m.2/2)

## Görev
Bir hakkın kullanımının somut olayda açıkça kötüye kullanma teşkil edip etmediğini denetlemek ve "bir hakkın açıkça kötüye kullanılmasını hukuk düzeni korumaz" sonucunu (TMK m.2/2) gerekçelendirmek.

## Soğuk başlangıç (intake)
- Hangi hak/yetki kullanılıyor ve karşı taraf hangi davranışı kötüye kullanma sayıyor?
- Hak sahibi daha önce aksi yönde davranıp güven yarattı mı (çelişkili davranış)?
- Hak çok geç mi kullanılıyor; karşı tarafta haklı bir güven oluştu mu?
- Hakkın kullanımında meşru bir menfaat var mı, yoksa salt zarar verme mi?

## Denetim şeması
1. **Önce hakkı tespit et** — TMK m.2/2 mevcut bir hakkın kullanımını sınırlar; önce hakkın varlığı ve kapsamı özel normla belirlenir. Süzgeç, kuralın sonucunu düzeltir.
2. **"Açıkça" eşiği** — Her dengesizlik değil, yalnızca *açık* kötüye kullanma korunmaz. Eşik yüksektir; sıradan menfaat çatışması yetmez.
3. **Tipoloji** — (a) Çelişkili davranış (*venire contra factum proprium*); (b) hakkın çok geç kullanılması ve yaratılan güvene aykırılık; (c) meşru menfaat yokluğu / salt başkasına zarar verme; (d) edimler arası aşırı oransızlık; (e) kendi hukuka aykırı davranışından yarar sağlama; (f) hakkın amacından saptırılması.
4. **İspat** — TMK m.6 / HMK m.190: kötüye kullanmayı iddia eden ispatla yükümlüdür. Ancak açık kötüye kullanma kamu düzenini ilgilendirdiğinden hâkimce re'sen gözetilebilir.
5. **Sonuç ve ölçülülük** — Açıkça kötüye kullanılan hak korunmaz: talep reddedilir, def'i etkisizleşir veya hak sınırlanır. Hakkın tümden düşürülmesi son çaredir; ölçülü ve gerekli olanla yetinilir.
6. **m.3 ile fark** — m.2/2 davranış denetimi, m.3 bilgisizliğin (iyiniyet) korunmasıdır; karıştırılmaz.

## Çıktı modülleri
- Hakkın tespiti + kötüye kullanma tipi eşleştirmesi.
- Güven/çelişki kronolojisi (tarih sırasıyla).
- "Açıklık" eşiği değerlendirmesi.
- Sonuç önerisi (ret/sınırlama) + ilkesel içtihat `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

