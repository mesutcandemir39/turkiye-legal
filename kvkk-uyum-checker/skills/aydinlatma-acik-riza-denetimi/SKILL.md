---
argument-hint: ''
description: Mevcut aydınlatma metinlerinin ve açık rıza beyanlarının m.10, Aydınlatma
  Tebliği ve Rıza Tebliği'ne uygunluğu denetlenirken ya da bu metinler taslaklanırken
  kullanılır.
name: aydinlatma-acik-riza-denetimi
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Aydınlatma ve Açık Rıza Metni Denetimi

## Görev
Kuruluşun aydınlatma metinlerini ve açık rıza beyanlarını madde madde denetlemek; zorunlu unsur, zamanlama ve ikisinin birbirinden ayrı tutulması kurallarına uygunluğu test edip eksikleri bulgu listesine bağlamak.

## Soğuk başlangıç (intake)
1. Hangi kanallarda aydınlatma yapılıyor (web formu, işe alım, sözleşme, çağrı merkezi, kamera tabelası)?
2. Her kanal için ayrı metin var mı, yoksa tek genel metin mi kullanılıyor?
3. Açık rıza alınıyor mu; alınıyorsa aydınlatmadan ayrı bir onay olarak mı?
4. Rızanın geri alınması için bir mekanizma var mı?

## Denetim şeması
1. **Zorunlu unsur testi (m.10/1)**: Her metinde (a) veri sorumlusu/temsilci kimliği, (b) işleme amaçları, (c) aktarılan alıcı grupları ve amacı, (ç) toplama yöntemi ve hukuki sebebi, (d) m.11 hakları bulunmalı. "vb.", "gerektiğinde" gibi muğlak ifadeler eksiklik sayılır (Aydınlatma Tebliği).
2. **Zamanlama**: Aydınlatma, verinin elde edildiği anda yapılmalı; sonradan yapılan aydınlatma ihlaldir.
3. **Ayrılık ilkesi**: Aydınlatma ile açık rıza tek metinde/tek onay kutusunda birleştirilemez; aydınlatma rıza şartına bağlanamaz. Birleşik kullanım kırmızı bulgudur.
4. **Açık rızanın geçerliliği (m.3/1-a)**: Rıza özgür irade + belirli konu + bilgilendirme unsurlarını taşımalı; ön işaretli kutu, hizmet şartına bağlı rıza ("rıza vermezsen hizmet yok") geçersizdir.
5. **Hukuki sebebin doğru gösterimi**: Metinde her amaç için m.5/m.6 sebebi açık rıza ile karıştırılmadan gösterilmeli.
6. **Ara sonuç**: Eksik/geç aydınlatma m.18/1-a yaptırım riski; geçersiz rıza ise işlemenin tümünü hukuka aykırı kılar.

İspat yükü: Aydınlatmanın usulüne uygun yapıldığını ve rızanın geçerli alındığını veri sorumlusu kayıt/onay loguyla ispatlar.

## Çıktı modülleri
- Metin başına m.10 unsur kontrol listesi (Uygun/Eksik).
- Aydınlatma–açık rıza ayrımı uygunsuzluk raporu.
- Kanal bazlı düzeltilmiş aydınlatma/rıza taslakları ([doldurulacak] yer tutucularıyla).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

