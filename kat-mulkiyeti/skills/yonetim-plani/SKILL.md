---
argument-hint: ''
description: Sitenin anayasası niteliğindeki yönetim planının düzenlenmesi, bir hükmünün
  yorumlanması, değiştirilmesi ya da yönetim planına aykırı uygulamaların tartışılması
  gündeme geldiğinde; bağlayıcılık, değiş
name: yonetim-plani
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
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yönetim Planı — İçerik, Değişiklik ve Yorum

## Görev
Anagayrimenkulün yönetimini düzenleyen yönetim planının hukuki niteliğini, bağlayıcılığını ve içerik sınırlarını belirlemek; bir hükmün yorumu, değiştirilmesi veya plana aykırı uygulama uyuşmazlıklarını çözmek.

## Soğuk başlangıç (intake)
- Yürürlükteki yönetim planı tapuya tescilli mi; tarihi ve son değişikliği nedir?
- Uyuşmazlık planın bir hükmünün anlamına mı, plana aykırı bir uygulamaya mı, yoksa plan değişikliğine mi ilişkin?
- Tartışılan konu KMK'nın emredici bir hükmüyle (örn. oybirliği gereken haller) çelişiyor mu?
- Plan değişikliği için gerekli nisap sağlanmış mı; karşı çıkan malik var mı?

## Denetim şeması
1. **Hukuki nitelik (KMK m.28)**: Yönetim planı, anagayrimenkulün yönetim tarzını, kullanma maksat ve şeklini, yönetici ve denetçilerin alacağı ücreti ve yönetime ilişkin diğer hususları düzenleyen **sözleşme** niteliğinde belgedir. Bütün kat maliklerini, onların külli/cüzi haleflerini ve yöneticileri bağlar (m.28/1).
2. **Bağlayıcılık ve aleniyet**: Yönetim planı ve değişiklikleri, bağımsız bölüm maliklerini bağlamak için tapu kütüğüne işlenir; sonradan malik olanlar da bilgisi olmasa dahi bağlıdır.
3. **Değişiklik nisabı (m.28/3)**: Yönetim planının değiştirilmesi için **bütün kat maliklerinin beşte dördünün (4/5) oyu** şarttır. Bu nitelikli çoğunluk sağlanmadan yapılan değişiklik geçersizdir; aykırılık karar iptali yoluyla ileri sürülür.
4. **Emredici hükümlerle sınır**: Yönetim planı KMK'nın emredici hükümlerine aykırı düzenleme getiremez. Örneğin oybirliği aranan haller (m.19/2 anataşınmazda değişiklik, m.44 ilave inşaat, m.45 ortak yer devri) plan ile çoğunluğa indirilemez.
5. **Yorum yöntemi**: Plan hükmü TMK m.1-2 ve sözleşme yorumu ilkeleriyle (dürüstlük kuralı, amaçsal yorum) yorumlanır; açık hüküm yoksa KMK'nın tamamlayıcı hükümleri uygulanır.
6. **Ara sonuç**: Hüküm geçerli ve bağlayıcı mı; değişiklik 4/5 nisabını sağlıyor mu; aykırı uygulama için karar iptali/eksikliğin giderilmesi (m.33) gerekli mi?

## Çıktı modülleri
- Yönetim planı hüküm analizi ve yorum notu.
- Değişiklik için nisap (4/5) ve usul kontrol listesi.
- Emredici hükümle çatışma taraması ve geçersizlik değerlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

