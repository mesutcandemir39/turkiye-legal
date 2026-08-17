---
argument-hint: ''
description: Vasiyetname veya miras sözleşmesi düzenlenmesi, yorumu, şekil ve ehliyet
  denetimi gerektiğinde; resmi/el yazılı/sözlü vasiyet, mirasçı atama, belirli mal
  bırakma (muayyen mal vasiyeti) ve koşul-yüklem
name: olume-bagli-tasarruflar-vasiyet-miras-sozlesmesi
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
  version: 0.1.0
user-invocable: true
---


# Ölüme Bağlı Tasarruflar — Vasiyetname ve Miras Sözleşmesi

## Görev
Bir ölüme bağlı tasarrufun türünü, şeklini, ehliyet ve içerik geçerliliğini denetlemek; mirasçı atama, muayyen mal vasiyeti, art/yedek mirasçı, koşul ve yükleme kurmak ya da yorumlamak.

## Soğuk başlangıç (intake)
- Tasarruf vasiyetname mi, miras sözleşmesi mi? Tarihi ve düzenleniş şekli?
- Resmi (noter/sulh hâkimi), el yazılı mı, sözlü mü düzenlendi?
- Tasarruf anında mirasbırakanın yaşı ve ayırt etme gücü?
- İçerik: mirasçı atama mı, belirli mal bırakma mı, koşul/yükleme var mı?
- Sonradan değiştirildi/geri alındı mı? Sonraki tasarruf var mı?

## Denetim şeması
1. **Tür ve şekil:** Vasiyetname tek taraflı, her zaman dönülebilir (m.542 geri alma). Şekiller: resmi (m.532-537), el yazılı — baştan sona el yazısı, tarih, imza (m.538), sözlü — olağanüstü hal, iki tanık (m.539-541). Miras sözleşmesi iki taraflı, daima resmi şekilde (m.545); olumlu/olumsuz (feragat) olabilir.
2. **Ehliyet:** Vasiyet için ayırt etme gücü + 15 yaş (m.502); miras sözleşmesi için ayırt etme gücü + ergin + kısıtlı olmama (m.503).
3. **İrade sakatlığı:** Yanılma, aldatma, korkutma, zorlama varsa iptal sebebi (m.557/3, m.504). Hatalı saik açık ve belirleyiciyse dikkate alınır (m.504/2).
4. **İçerik denetimi:** Mirasçı atama (m.516), muayyen mal vasiyeti (m.517), art mirasçı (m.521-523), yedek mirasçı (m.520), koşul ve yükleme (m.515), vakıf kurma (m.526). Hukuka/ahlaka aykırı, imkânsız koşul yazılmamış sayılır (m.515/2).
5. **Yorum:** Mirasbırakanın gerçek iradesi esas (m.504, lehe yorum); muayyen mal vasiyeti mi mirasçı atama mı ayrımı pay sonuçlarını değiştirir.
6. **Ara sonuç:** Geçerlilik haritası; iptal sebebi varsa iptal davası becerisine, saklı pay aşımı varsa tenkis becerisine yönlendir.

## Çıktı modülleri
- Vasiyetname/miras sözleşmesi taslağı (şekil şartlı, [doldurulacak] yer tutuculu)
- Geçerlilik/şekil denetim çizelgesi
- Yorum notu ve tür tayini (atama vs. muayyen mal)
- Geri alma/değiştirme metni taslağı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

