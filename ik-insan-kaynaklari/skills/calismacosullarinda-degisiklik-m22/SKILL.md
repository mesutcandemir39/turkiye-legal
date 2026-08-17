---
argument-hint: ''
description: Ücret, görev yeri, görev tanımı, çalışma saatleri gibi koşullarda değişiklik
  yapılacaksa veya yapılan değişikliğe işçi itirazı varsa, m.22 usulünü ve değişiklik
  feshini denetlemek için kullanılır.
name: calismacosullarinda-degisiklik-m22
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
  - ad: İş Kanunu
    numara: '4857'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Çalışma Koşullarında Esaslı Değişiklik (m.22)

## Görev
İşverenin çalışma koşullarında yapacağı esaslı değişikliği (görev yeri, ücret, unvan, vardiya) hukuka uygun usulle gerçekleştirmek; reddedilen değişikliğin "değişiklik feshine" dönüşmesini doğru yönetmek.

## Soğuk başlangıç (intake)
1. Hangi koşul değişiyor (yer, ücret, görev, çalışma süresi) ve neden?
2. Sözleşmede/iç yönetmelikte işverene değişiklik (nakil) yetkisi veren saklı kayıt var mı?
3. Değişiklik çalışan aleyhine esaslı mı, yoksa yönetim hakkı kapsamında mı?
4. Çalışanın yazılı muvafakati alınacak mı?

## Denetim şeması
1. **Esaslılık testi**: Yönetim hakkı kapsamındaki tâli değişiklikler (m.22 dışı) ile çalışan aleyhine **esaslı** değişiklik ayrılır. Esaslı olanlar m.22 usulüne tabidir.
2. **Yazılı bildirim ve muvafakat (m.22/1)**: Esaslı değişiklik **yazılı** bildirilir; çalışan **6 işgünü** içinde yazılı kabul etmezse değişiklik onu bağlamaz. Sözlü/zımni kabul yeterli sayılmaz.
3. **Saklı kayıt**: Sözleşmede işverene nakil/değişiklik yetkisi tanınmışsa, bu yetki **dürüstlük kuralı** ve hakkın kötüye kullanılmaması sınırında kullanılabilir.
4. **Değişiklik feshi (m.22/2)**: Çalışan kabul etmezse işveren, değişikliğin geçerli sebebe dayandığını **yazılı** açıklayarak bildirim sürelerine uyup feshedebilir; bu fesih iş güvencesi denetimine tabidir (m.18-21).
5. **İspat**: Değişikliğin geçerli sebebe dayandığı ve usule uyulduğu işverence ispatlanır.
6. **Ara sonuç**: Muvafakatsiz dayatma → değişiklik işçiyi bağlamaz; usulsüz değişiklik feshi → işe iade riski.

## Çıktı modülleri
- Esaslı değişiklik bildirim (m.22) yazısı taslağı.
- Muvafakatname taslağı.
- Reddi halinde değişiklik feshi gerekçeli bildirim taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

