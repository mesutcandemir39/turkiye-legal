---
argument-hint: ''
description: Personel yönetmeliği, disiplin yönetmeliği, etik kod, uzaktan çalışma
  veya kılık-kıyafet politikası gibi iç düzenlemeler hazırlanacak veya mevcutları
  gözden geçirilecekse kullanılır.
name: isyeri-yonetmelikleri-ve-politikalar
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


# İşyeri Yönetmelikleri ve İK Politikaları

## Görev
İşverenin iç düzenlemelerini (personel/disiplin yönetmeliği, etik kod, izin, uzaktan çalışma politikası) hukuken bağlayıcı ve dava dayanağı oluşturacak biçimde kurgulamak; bunların çalışma koşulu hâline gelmesini ve değiştirilmesini doğru yönetmek.

## Soğuk başlangıç (intake)
1. Hangi politika hazırlanıyor (disiplin, etik, uzaktan çalışma, bilgi güvenliği)?
2. Yönetmelik sözleşmenin eki mi, yoksa tek taraflı işveren talimatı mı olacak?
3. Çalışanlara nasıl tebliğ ve kabul ettirilecek?
4. Mevcut bir yönetmelik değiştiriliyor mu (kazanılmış koşul riski)?

## Denetim şeması
1. **Hukuki nitelik**: İç yönetmelik, çalışana tebliğ edilip kabul gördüğünde veya sözleşmeye atıfla **çalışma koşulu** hâline gelir; bu durumda lehe hükümler kazanılmış hak doğurur, aleyhe değişiklik m.22'ye tabi olur.
2. **Disiplin yönetmeliği**: Ceza skalası, fiil-yaptırım eşleşmesi ve orantılılık içermeli; ölçütsüz/keyfî yaptırım eşit davranma borcuna (m.5) ve fesih denetimine takılır.
3. **Talimat hakkı sınırı**: Yönetmelik, emredici hükümlere (asgari ücret, çalışma süresi, izin, fazla mesai sınırı) aykırı olamaz; aykırı kayıt geçersizdir.
4. **Uzaktan çalışma (m.14)**: Yazılı yapılma, ekipman/gider, iletişim ve veri koruma kayıtları; İSG yükümlülüğü uzaktan çalışmada da sürer.
5. **Tebliğ ve ispat**: Politikanın çalışana ulaştığı imza/KEP/sistem kaydıyla ispatlanmalı; aksi halde fesihte dayanak olamaz.
6. **KVKK kesişimi**: İzleme/bilgi güvenliği politikaları KVKK aydınlatmasıyla uyumlu olmalı.
7. **Ara sonuç**: Tebliğ edilmemiş veya emredici hükme aykırı yönetmelik dava dayanağı olmaz.

## Çıktı modülleri
- Politika/yönetmelik taslağı (kapsam + yaptırım skalası + yürürlük).
- Tebliğ-kabul formu taslağı.
- Emredici hükme uygunluk ve değişiklik usulü notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

