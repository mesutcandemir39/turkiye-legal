---
argument-hint: ''
description: İdare hukukunun temel kavramlarını ve yapısını oturtmak; idari işlem,
  idari eylem, idari sözleşme, kamu hizmeti ve yargı yolu ayrımını netleştirmek için
  kullanılır; dosyanın hangi rejime tabi olduğu b
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Sistematik

## Görev
İdare hukukunun çerçevesini kurmak: önündeki ilişkinin idari mi özel hukuk mu olduğunu, idari işlem/eylem/sözleşme ayrımını ve buradan doğan yargı yolunu (idari/adli) belirlemek. Bu beceri, sonraki tüm denetimlerin zeminini hazırlar.

## Soğuk başlangıç (intake)
1. İşlemi/eylemi yapan makam kim; kamu gücü mü kullanıyor yoksa özel hukuk kişisi gibi mi hareket ediyor?
2. Elinde tek yanlı bir karar mı (işlem), maddi bir faaliyet/davranış mı (eylem), yoksa bir sözleşme mi var?
3. Karar kesin ve yürütülebilir mi, yoksa hazırlık/iç işlem mi?
4. Tebliğ/öğrenme tarihi nedir?

## Denetim şeması
1. **İdarilik testi.** İlişki bir kamu makamının kamu gücü ayrıcalığıyla tesis ettiği bir ilişki mi? Anayasa m.123 (idarenin kanuniliği) ve m.125 (yargı yolu) çerçevesinde değerlendir. İdarenin özel hukuk ilişkileri (kira, satım, eser) kural olarak adli yargıda görülür.
2. **İdari işlem unsurları.** Tek yanlılık, icrailik, kesinlik. İYUK m.14/d uyarınca kesin ve yürütülebilir olmayan işlem dava edilemez; hazırlık işlemleri, görüş, mütalaa, iç genelge kural olarak icrai değildir.
3. **İşlem türünü ayır.** Bireysel-düzenleyici (yönetmelik/genelge), bağlı-takdiri, basit-zincirleme işlem ayrımını yap; düzenleyici işlemlere karşı dava açma süresi ve yetkili mahkeme farklılaşır.
4. **İdari sözleşme mi?** Konusu kamu hizmeti, tarafı idare ve içinde kamu gücü ayrıcalığı/üstün hükümler varsa idari sözleşmedir (imtiyaz, hizmet sözleşmesi); bunlar idari yargıdadır.
5. **Yargı yolu sonucu.** İdari işlem/eylem/idari sözleşme → idari yargı (İYUK). Aksi → adli yargı. **Ara sonuç:** dosyanın rejimi ve gidilecek mahkeme.
6. **İspat yükü.** İdari yargıda re'sen araştırma ilkesi geçerlidir (İYUK m.20); yine de işlemin dayanağı belgeleri ve hukuka aykırılık iddialarını davacı somutlaştırmalıdır.

## Çıktı modülleri
- İlişkinin nitelendirilmesi (idari/özel hukuk) tablosu.
- İşlem/eylem/sözleşme ayrımı ve gerekçesi.
- Yargı yolu ve muhtemel görevli mahkeme önerisi.
- Bir sonraki adım: hangi alt-beceriye geçileceği (iptal denetimi, sorumluluk, kamulaştırma vb.).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

