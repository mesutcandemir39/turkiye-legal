---
argument-hint: ''
description: Sağlık hizmeti sırasında bilgilendirme, mahremiyet, kayıtlara erişim,
  tedaviyi reddetme gibi hasta haklarının ihlal edilip edilmediğini ve başvuru yollarını
  değerlendirmek için kullanılır.
name: hasta-haklari
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
  - ad: Banka Muhasebe Sistemi Hakkında Kanun
    numara: '1219'
    tur: kanun
  - ad: Gayrimenkul Ek Vergisi Hakkında Kanun
    numara: '3359'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Hasta Hakları ve İhlal Değerlendirmesi

## Görev
Hasta haklarına ilişkin bir ihlal iddiasını mevzuata göre nitelemek, idari ve yargısal başvuru yollarını belirlemek.

## Soğuk başlangıç (intake)
1. Hangi hak ihlal edildi: bilgilendirme, mahremiyet, hizmete erişim, tedaviyi reddetme, kayıtlara erişim?
2. Olay kamu mu özel sağlık kuruluşunda mı geçti?
3. Hasta hakları birimine/SABİM/CİMER başvurusu yapıldı mı?
4. İhlalden doğan bir maddi/manevi zarar var mı?

## Denetim şeması
1. **Hak kataloğu**: Hasta Hakları Yönetmeliği — hizmetten genel olarak faydalanma, bilgilendirme (m.15), kayıtları inceleme, mahremiyet, rıza ve reddetme (m.24-31), tıbbi özen. Mahremiyet aynı zamanda KVKK (6698) kapsamında özel nitelikli sağlık verisidir.
2. **İhlalin tespiti**: İlgili hakkın somut içeriği ile fiilî durum karşılaştırılır; mevzuata aykırılık ve hastanın bundan etkilenmesi aranır.
3. **İdari yol**: Hasta hakları kurulu, SABİM, CİMER; kamu hizmeti ise idareye başvuru. Disiplin yönü için meslek odası/Bakanlık.
4. **Yargısal yol**: Maddi/manevi tazminat (özel kuruluş → adli yargı; kamu → tam yargı davası, İYUK m.13). Kişilik hakkı ihlali için TMK m.24-25, TBK m.58.
5. **Veri/mahremiyet ekseni**: Sağlık verisinin izinsiz paylaşımı KVKK m.6 ve TCK m.136 (verileri hukuka aykırı verme/ele geçirme) yönünden ayrıca değerlendirilir.
6. **Ara sonuç**: İhlal + zarar/etki varsa uygun başvuru yolu seçilir; sadece usuli ihlalde idari başvuru öne çıkar.

## Çıktı modülleri
- İhlal edilen hak ve dayanak madde eşlemesi
- Başvuru yolu haritası (idari + yargısal)
- Tazminat/şikâyet dilekçesi taslağı (yer tutuculu)
- KVKK boyutu uyarı notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

