---
argument-hint: ''
description: Bir kişinin yaptığı hukuki işlemin ehliyet yönünden geçerli olup olmadığı;
  küçüğün, kısıtlının veya ayırt etme gücü tartışmalı kişinin işleminin akıbeti sorgulandığında
  kullanılır.
name: ehliyet-ve-temsil
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


# Hak ve Fiil Ehliyeti, Sınırlı Ehliyetsiz İşlemleri

## Görev
Bir hukuki işlemin ehliyet süzgecinden geçip geçmediğini belirlemek: işlemi yapanın hangi ehliyet katmanına düştüğünü saptayıp işlemin geçerli, kesin hükümsüz, askıda hükümsüz (icazete bağlı) ya da iptal edilebilir olduğunu gerekçelendirmek.

## Soğuk başlangıç (intake)
- İşlemi yapanın yaşı ve durumu: ergin mi, kaç yaşında, vesayet/kısıtlılık var mı?
- İşlem anında ayırt etme gücü var mıydı (akıl hastalığı, sarhoşluk, geçici bilinç kaybı iddiası)?
- İşlem türü: borç altına sokuyor mu, karşılıksız kazandırma mı, kişiye sıkı sıkıya bağlı hak mı?
- Yasal temsilci (veli/vasi) onayı/izni var mı; varsa önceden mi sonradan mı?

## Denetim şeması
1. **Ayırt etme gücü** — TMK m.13: yaş, akıl hastalığı/zayıflığı, sarhoşluk veya benzer sebeple makul davranma yeteneğinden yoksun olmayan kişi ayırt etme gücüne sahiptir. Yoklukta (m.15) işlem kural olarak kesin hükümsüzdür (m.14-15).
2. **Katman belirleme** — Tam ehliyetli: işlem geçerli. Tam ehliyetsiz (m.14-15): kişisel olarak hak kuramaz, işlemleri hükümsüz. Sınırlı ehliyetsiz (m.16): ayırt etme gücü olan küçük/kısıtlı.
3. **Sınırlı ehliyetsizin işlemi** — TMK m.16: yasal temsilcinin rızası olmadıkça borç altına giremez; ancak (a) karşılıksız kazanma ve (b) kişiye sıkı sıkıya bağlı hakları tek başına kullanabilir. Borçlandırıcı işlem temsilcinin rızasına bağlıdır; rıza yoksa işlem askıda hükümsüzdür ve icazetle (TBK m.451 vd. kıyasen onam) geçerli hâle gelebilir.
4. **Sorumluluk** — TMK m.16/2: yasal temsilcinin rızası dışında borçlanan sınırlı ehliyetsiz, sebepsiz zenginleşme (TBK m.77 vd.) ölçüsünde veya kasten ehliyetsizliğine güveni boşa çıkarmışsa sorumlu olur.
5. **Tüzel kişide** — TMK m.49-50: tüzel kişi organları aracılığıyla fiil ehliyetini kullanır; organların hukuki işlemleri ve kusurları tüzel kişiyi bağlar.
6. **Dürüstlük denetimi** — TMK m.2: ehliyetsizliğin kötüniyetle/çelişkili biçimde ileri sürülmesi korunmaz.

## Çıktı modülleri
- Ehliyet katmanı tespiti + işlemin akıbeti (geçerli/butlan/askıda/iptal).
- İcazet veya yasal temsilci onayı için yapılması gerekenler.
- İspat yükü notu (ayırt etme gücü yokluğunu iddia eden ispatlar — m.6).
- İlkesel içtihat atfı, künye `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

