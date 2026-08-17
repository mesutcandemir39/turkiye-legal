---
argument-hint: ''
description: Vergi uyuşmazlığının türünü (tarh, tahakkuk, tahsil, ceza) ve doğru yargı
  yolunu belirlemek, idari aşama ile dava aşaması arasındaki ilişkiyi kurmak için
  ilk başvurulacak çerçeve beceridir.
name: temel-kavramlar-ve-vergi-yargisi
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
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Vergi Yargısı Sistematiği

## Görev
Müvekkilin elindeki belgeden hareketle uyuşmazlığı doğru sınıflandırmak, hangi normun (maddi vergi kanunu, VUK, AATUHK) ve hangi yargı yolunun devrede olduğunu saptamak, idari çözüm ile dava arasındaki tercihi çerçevelemek.

## Soğuk başlangıç (intake)
1. Elinizde tam olarak hangi belge var: vergi/ceza ihbarnamesi mi, ödeme emri mi, düzeltme/şikâyet reddi mi, ihtiyati haciz/tahakkuk yazısı mı?
2. Belge size ne zaman tebliğ edildi (eline geçti)? Tebligat usulü ne?
3. Uyuşmazlık verginin aslına mı, cezaya mı, faize/gecikme zammına mı yoksa tahsil aşamasına mı ilişkin?
4. Daha önce uzlaşma, düzeltme veya izaha davet süreci işletildi mi?

## Denetim şeması
1. **İşlem türünü belirle.** Tarh işlemi (ihbarname) → dava süresi İYUK m.7 ve VUK m.377 uyarınca 30 gün. Tahsil işlemi (ödeme emri) → AATUHK m.58 uyarınca 7 gün. Düzeltme-şikâyet reddi → VUK m.124 sonrası dava.
2. **Tarh türünü ayır.** Beyana dayalı (VUK m.378, kural olarak dava yok, istisna ihtirazi kayıt), ikmalen (m.29), re'sen (m.30) veya idarece tarh (m.29). Re'sen tarhda takdir sebebi ve yöntemi denetime tabidir.
3. **Görev-yetkiyi yerleştir.** Esasen vergi mahkemesi görevli; İYUK m.37 uyarınca uyuşmazlık konusu işlemi yapan dairenin bulunduğu yerdeki vergi mahkemesi yetkili.
4. **İdari aşama-dava ilişkisini kur.** Uzlaşma (VUK Ek m.1 vd.) ve düzeltme-şikâyet (VUK m.116 vd.) dava süresini etkiler; bunlardan birini seçmek diğerini kapatabilir. Ara sonuç: hangi yolun ceza indirimi, süre ve ispat avantajı sağladığını tablola.
5. **Otomatik durma etkisini not et.** Tarhiyata karşı dava İYUK m.27/4 gereği tahsili kendiliğinden durdurur; ödeme emrine ve ihtirazi kayıtlı davada bu etki yoktur, ayrı YD talebi gerekir.

## Çıktı modülleri
- Uyuşmazlık sınıflandırma tablosu (işlem türü / norm / süre / mahkeme).
- İdari yol vs. dava yolu karşılaştırması (avantaj-risk).
- Bir sonraki adım ve süre uyarısı listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

