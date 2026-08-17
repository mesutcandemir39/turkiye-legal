---
argument-hint: ''
description: Mütalaa hazırlamadan önce çıkar çatışması, sır saklama ve bilimsel mütalaa
  veren akademisyen/uzmanın tarafsızlık yükümlülüğünü denetlemek gerektiğinde kullanılır;
  mütalaanın kabul edilebilirliğini ve
name: cikar-catismasi-ve-mutalaa-etigi
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


# Çıkar Çatışması ve Mütalaa Etiği

## Görev
Mütalaa işini kabul etmeden önce çıkar çatışması, sır saklama ve tarafsızlık yükümlülüklerini denetlemek; özellikle HMK m.293 uyarınca dosyaya sunulacak uzman görüşlerinde mütalaayı verenin bağımsızlığını ve metnin güvenilirliğini korumak.

## Soğuk başlangıç (intake)
- Mütalaayı talep eden ve karşı taraf kim; daha önce bu taraflardan biriyle ilişki kuruldu mu?
- Görüş mahkemeye uzman görüşü olarak mı sunulacak (HMK m.293), yoksa danışmanlık mı?
- Talep edilen sonuç önceden dayatılıyor mu ("şu sonucu çıkaran mütalaa")?
- Sır niteliğinde bilgi içeriyor mu?

## Denetim şeması
1. Çıkar çatışması taraması: Aynı uyuşmazlıkta karşı tarafa daha önce hizmet verildi mi, taraflardan biriyle menfaat bağı var mı? Avukat için 1136 sayılı Avukatlık Kanunu m.38 (işi reddetme zorunluluğu) ve meslek kuralları; çatışma varsa iş reddedilir.
2. Sır saklama: Avukatlık Kanunu m.36 ve TBK vekâlet hükümleri — mütalaa hazırlanırken öğrenilen bilgiler sır kapsamındadır; üçüncü kişiyle paylaşılmaz.
3. Bilimsel mütalaada tarafsızlık: HMK m.293 uzman görüşü, ücreti tarafça ödense de bilimsel dürüstlükle yazılmalıdır; sipariş üzerine sonuç üretmek (advokatlaşmış mütalaa) belgenin ispat değerini düşürür ve etik sorun doğurur. Aleyhe argüman tartışılır.
4. Sonuç dayatması testi: Talep eden belirli bir sonucu zorluyorsa, mütalaa ya gerçek hukuki durumu yazar ya da iş reddedilir; gerçeğe aykırı görüş üretilmez.
5. Hukuki danışmanlık sınırı: Mütalaa genel hukuki değerlendirmedir; vekâlet ilişkisi ve fiili dava temsili ayrı sözleşme gerektirir; bu sınır belirtilir.
6. Ara sonuç: İş kabul edilebilir mi + etik uyarılar + tarafsızlık/sır notları.

## Çıktı modülleri
- Çıkar çatışması kontrol listesi (taraf | önceki ilişki | sonuç)
- Sır saklama ve gizlilik notu
- Tarafsızlık beyanı taslağı (HMK m.293 görüşü için)
- İş kabul/ret değerlendirmesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

