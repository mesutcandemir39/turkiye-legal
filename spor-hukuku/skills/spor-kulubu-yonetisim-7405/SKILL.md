---
argument-hint: ''
description: Spor kulübü veya spor anonim şirketi kuruluşu, organları, mali denetim,
  yönetici sorumluluğu ve ibra konularını 7405 sayılı Kanun çerçevesinde ele almak
  gerektiğinde kullanın.
name: spor-kulubu-yonetisim-7405
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
  - ad: Çalışma ve Sosyal Güvenlik Bakanlığı Kuruluş ve Görevleri Hakkında Kanun
    numara: '7405'
    tur: kanun
  - ad: Tıbbi Deontoloji Tüzüğü Hakkında Kanun
    numara: '6222'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Spor Kulüpleri, Spor AŞ ve Yönetişim (7405)

## Görev
Spor kulübü ve spor anonim şirketinin kuruluş, organ, mali denetim ve yönetici sorumluluğu konularını 7405 sayılı Kanun ve TTK çerçevesinde değerlendirmek; yönetişim uyumu ve sorumluluk riskini haritalamaktır.

## Soğuk başlangıç (intake)
1. Yapı ne: dernek statüsündeki spor kulübü mü, spor anonim şirketi mi, ikisi birlikte mi?
2. Sorun ne: kuruluş/dönüşüm, genel kurul, mali denetim, yönetici sorumluluğu, ibra?
3. Borçlanma/harcama sınırı aşıldı mı; mali tablo durumu nedir?
4. Hangi federasyona bağlı; lisans/finansal kriter yükümlülüğü var mı?
5. İhtilaf taraf(lar)ı kim?

## Denetim şeması
1. **Hukuki yapı**: Kulübün dernek mi, 7405 kapsamında spor kulübü mü olduğu; spor anonim şirketine dönüşüm ve kurumsal yapı (TTK 6102 ile birlikte) belirlenir.
2. **Organlar ve genel kurul**: Genel kurul, yönetim ve denetim kurulu işleyişi; çağrı, nisap ve karar usulleri (dernek mevzuatı/TTK karması) kontrol edilir.
3. **Mali denetim ve sınırlar**: 7405, kulüp yöneticilerine harcama ve borçlanma sınırı getirir; sınırı aşan borçlanmadan **yöneticilerin kişisel/müteselsil sorumluluğu** doğabilir. Mali tabloların bağımsız denetimi ve şeffaflık yükümlülüğü değerlendirilir.
4. **Yönetici sorumluluğu ve ibra**: Sorumluluğun şartları, ibranın kapsamı ve ibranın sorumluluğu kaldırma etkisi; sorumluluk davasında ispat yükü ve zamanaşımı.
5. **Federasyon uyumu**: Kulüp lisans, finansal fair play ve federasyon mali kriterlerine uyum; ihlalin idari/sportif yaptırımı (puan silme, transfer yasağı) gündeme gelir.
6. **Ara sonuç**: Yönetişim boşlukları, sorumluluk riski ve düzeltici adımlar listelenir.

## Çıktı modülleri
- Yönetişim ve sorumluluk risk haritası
- Genel kurul/karar usulü kontrol listesi
- Yönetici sorumluluğu değerlendirme notu
- Uyum açığı ve eylem planı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

