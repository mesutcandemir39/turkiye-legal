---
argument-hint: ''
description: Kullanıcı mahkemeye verilecek dava dilekçesini yazmak istediğinde, talep
  sonucunu netleştirmek, vakıaları sıralamak ve delilleri bağlamak istediğinde kullanılır.
name: dava-dilekcesi-hazirlama
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dava Dilekçesi Hazırlama (HMK m.119)

## Görev
HMK m.119'a uygun, eksiksiz, talep sonucu net ve delilleri bağlanmış bir dava dilekçesi iskeleti üretmek.

## Soğuk başlangıç (intake)
- Tarafların tam ad, T.C. kimlik no ve adresleri nedir?
- Tam olarak ne talep ediyorsunuz (para ise tutar, fer'iler dâhil)?
- Olay nasıl gelişti (tarih sırasıyla)?
- Her iddianızı hangi belge/tanıkla ispatlayacaksınız?
- Zorunlu arabuluculuk/ön başvuru yapıldıysa belgesi var mı?

## Denetim şeması
1. **Zorunlu unsurlar (HMK m.119):** Mahkeme adı; tarafların ad-soyad, TCKN, adres; varsa kanuni temsilci; davanın konusu ve değeri; **açık talep sonucu**; dayanılan vakıaların sıra numarasıyla açık özeti; her vakıanın hangi delille ispatlanacağı (vakıa-delil bağlantısı); dayanılan hukuki sebepler; imza. Eksik unsurda hâkim bir haftalık kesin süre verir (m.119/2); giderilmezse dava açılmamış sayılabilir.
2. **Talep sonucu:** Net ve infaza elverişli olmalı. Belirsiz alacak davası açılacaksa şartları (HMK m.107) ayrıca değerlendirilir; aksi halde kısmî/tam talep tercihi yapılır.
3. **Vakıa-delil eşlemesi (m.119/1-e,f ve m.194 somutlaştırma yükü):** Her maddi vakıa somut anlatılır; soyut iddia yetersizdir.
4. **Ek belgeler:** Deliller dilekçeye eklenir veya nerede olduğu gösterilir; tanık varsa ad-adres bildirilir. Harç ve gider avansı (m.120) yatırılmadan dava işleme alınmaz.
5. **İddianın genişletilmesi yasağı (m.141):** Dava açıldıktan sonra serbestçe yeni vakıa/talep eklenemeyeceği için ilk dilekçe kapsamlı olmalıdır.
6. **Ara sonuç:** Unsurlar tam + talep net + deliller bağlı + harç/avans hazır ise dava açılmaya hazırdır.

## Çıktı modülleri
- m.119 başlıklarına oturtulmuş dava dilekçesi taslağı.
- Vakıa-delil eşleme tablosu.
- Harç/gider avansı ve ek belge kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

