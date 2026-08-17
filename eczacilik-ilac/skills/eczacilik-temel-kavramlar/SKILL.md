---
argument-hint: ''
description: Eczacılık-ilaç alanına ilk girişte hangi katmanda (meslek, ürün, geri
  ödeme) olunduğunu ve görevli yargı yolunu belirlemek; kavram ve norm haritası kurmak
  gerektiğinde kullanılır.
name: eczacilik-temel-kavramlar
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
  - ad: Hemşirelik Kanunu
    numara: '6197'
    tur: kanun
  - ad: Mimar ve Mühendisler Hakkında Kanun
    numara: '1262'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Eczacılık ve İlaç Hukuku Temel Kavramları

## Görev
Önündeki olayı ilaç-eczacılık hukukunun doğru katmanına yerleştirmek, başat normu ve görevli yargı yolunu seçmek, sonraki uzman beceriye yönlendirmek.

## Soğuk başlangıç (intake)
- Uyuşmazlık kişiye mi (eczacı, mesul müdür, ecza deposu), ürüne mi (ruhsat, fiyat, tanıtım), ödemeye mi (SGK/MEDULA kesintisi) ilişkin?
- Karşı taraf kim: TİTCK, SGK, eczacı odası, ecza deposu, hasta/tüketici, bir başka eczacı?
- Ortada bir idari işlem (ruhsat reddi/iptali, ceza, kesinti) veya bir sözleşme/alacak mı var?
- Elinizde denetim tutanağı, idari yaptırım kararı, sözleşme, ihbarname var mı; tebliğ tarihi nedir?

## Denetim şeması
1. **Katman tespiti.** Meslek icrası → 6197 sayılı Kanun ve Eczaneler Yönetmeliği (RG 12.04.2014). Ürün → 1262 sayılı Kanun + Beşeri Tıbbi Ürünler Ruhsatlandırma Yönetmeliği (RG 11.12.2021) + TİTCK düzenlemeleri (663 sayılı KHK dayanağı). Geri ödeme → 5510 m.63 + SUT.
2. **Yargı yolu.** TİTCK/SGK/oda gibi kamu işlemleri idari yargıda (2577 İYUK); eczane devri, muvazaa, depo-eczane cari hesabı, alacak adli yargıda; 1262 m.18-19, TCK m.187 ceza yargısında; hasta-eczane ilişkisi koşullara göre tüketici mahkemesinde.
3. **Norm hiyerarşisi.** İdari işlemin dayanağı tebliğ/yönetmelik üst normu aşıyorsa Anayasa m.124 ve İYUK çerçevesinde normun uygulanmaması savı kurulur. Ara sonuç: dayanak norm geçerli mi, işlem yetki-şekil-sebep-konu-maksat yönünden sakat mı (idari işlem unsurları).
4. **Süre kapısı.** İdari işlemde İYUK m.7 (60 gün); idari para cezasında özel kanun yoksa 5326 sayılı Kabahatler Kanunu; SGK kesintisinde önce sözleşmesel itiraz kademesi. İspat yükü: idari işlemin sebep unsurunu (denetim bulgusu) idare; iptal sebebini davacı ortaya koyar.

## Çıktı modülleri
- Katman ve yargı yolu tespit notu.
- Uygulanacak normlar listesi (madde/RG tarihiyle).
- Hangi uzman beceriye geçileceğine dair yönlendirme ve eksik bilgi listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

