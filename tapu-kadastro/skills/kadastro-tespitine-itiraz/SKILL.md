---
argument-hint: ''
description: Kadastro çalışması sırasında veya askı ilanından sonra tespit edilen
  malik, sınır, yüzölçüm ya da nitelik hatasına itiraz edilirken; kadastro tutanağının
  kesinleşmesi, 10 yıllık hak düşürücü süre ve k
name: kadastro-tespitine-itiraz
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
  - ad: Tapu Kanunu
    numara: '3402'
    tur: kanun
  - ad: Kat Özel Koşulu Olmak Üzere Yapılan Satış Mukavelelerine Dair Kanun
    numara: '2644'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kadastro Tespitine İtiraz ve Kadastro Davası

## Görev
Kadastro tespitindeki malik/sınır/yüzölçüm hatasına karşı doğru zaman, mercii ve dayanakla itiraz/dava kurmak; tutanağın kesinleşip kesinleşmediğini ve hangi yolun açık olduğunu belirlemek.

## Soğuk başlangıç (intake)
- Kadastro çalışması hangi aşamada: tespit anı mı, 30 günlük askı ilanı mı, tutanak kesinleşmiş mi?
- İtiraz neye: malik tespiti mi, sınır/yüzölçüm mü, niteliğe (mera, yol, orman) mı?
- Taşınmaz tapulu mu, tapusuz zilyetlik mi; dayanak kayıt/zilyetlik var mı?
- Tutanağın kesinleşme tarihi ve üzerinden geçen süre nedir?

## Denetim şeması
1. **Aşamayı belirle.** Tespite itiraz kadastro teknisyenliğine/komisyona; askı ilanı 30 gün (3402 sayılı Kanun m.11). İlana itiraz çözülmezse iş kadastro mahkemesine taşınır (m.25 vd.).
2. **Tespit dayanağını denetle.** Kayda dayalı tespit (m.13), kayıt dışı/zilyetliğe dayalı tespit (m.14): 20 yıl çekişmesiz nizasız malik sıfatıyla zilyetlik, vergi kaydı, kültür arazisi 40 dönüm / sulu-kuru sınırları; kamu malları kadastro dışı (m.16, m.18).
3. **Kesinleşme ve hak düşürücü süreyi kontrol et.** Kadastro tutanağının kesinleştiği tarihten itibaren 10 yıl geçmedikçe önceki hukuki sebebe dayanan iddia dinlenir; 10 yıl geçtikten sonra kadastrodan önceki sebebe dayanılarak dava açılamaz (3402 m.12/3). Bu süre hak düşürücüdür, re'sen gözetilir.
4. **Görev ve husumet.** Kesinleşmeden önce kadastro mahkemesi münhasıran görevli (m.25); kesinleştikten sonra genel mahkemede tapu iptali-tescil. Husumet kayıt malikine, Hazineye veya ilgili kamu idaresine yöneltilir.
5. **İspat planı.** Eski tapu/zabıt kaydı, vergi kaydı, keşif + fen bilirkişisi (sınır/yüzölçüm), yerel bilirkişi ve tanık (zilyetliğin süresi/niteliği), hava fotoğrafı; orman/mera niteliğinde uzman bilirkişi.
6. **Ara sonuç.** Açık yol (komisyon itirazı / kadastro mahkemesi / genel mahkeme) ve süre durumu netleştirilir.

## Çıktı modülleri
- Aşama–mercii–süre tablosu (hangi yol, hangi süre, hak düşürücü mü).
- İtiraz/dava dilekçesi iskeleti, talep sonucu ve delil listesi.
- 10 yıllık hak düşürücü süre risk notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

