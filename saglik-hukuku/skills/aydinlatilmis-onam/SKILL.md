---
argument-hint: ''
description: Bir tıbbi müdahalede rızanın geçerli olup olmadığını ve aydınlatmanın
  yeterliğini denetlemek için kullanılır; onam kusurunun başlı başına sorumluluk doğurup
  doğurmadığını değerlendirir.
name: aydinlatilmis-onam
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
  - ad: Banka Muhasebe Sistemi Hakkında Kanun
    numara: '1219'
    tur: kanun
  - ad: Gayrimenkul Ek Vergisi Hakkında Kanun
    numara: '3359'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Aydınlatılmış Onam Denetimi

## Görev
Tıbbi müdahaleye verilen rızanın hukuken geçerli, aydınlatmanın ise içerik ve usul olarak yeterli olup olmadığını saptamak ve onam kusurunun sonuçlarını belirlemek.

## Soğuk başlangıç (intake)
1. Müdahale öncesi yazılı/sözlü aydınlatma yapıldığını gösteren belge var mı?
2. Hastaya hangi riskler, alternatifler ve başarısızlık olasılığı anlatıldı?
3. Hasta reşit/ehliyetli miydi; acil durum/bilinç kaybı var mıydı?
4. Onam formu matbu mu, müdahaleye özgü mü, makul süre öncesinde mi alındı?

## Denetim şeması
1. **Rızanın hukuki temeli**: TCK m.26 (ilgilinin rızası — hukuka uygunluk sebebi), Hasta Hakları Yönetmeliği m.24-31, Biyotıp Sözleşmesi (5013) m.5, 1219 m.70. Rıza yoksa müdahale kural olarak hukuka aykırıdır.
2. **Aydınlatmanın kapsamı**: Tanı, önerilen tedavi, başarı/başarısızlık olasılığı, riskler ve ciddi komplikasyonlar, alternatif yöntemler, hiç tedavi edilmeme sonucu. Estetik gibi zorunlu olmayan müdahalelerde aydınlatma yükü ağırlaşır.
3. **Usul ve zamanlama**: Hastanın karar vermesine yetecek makul süre, anlayabileceği dil, baskısız ortam. Ameliyat masasında alınan onam zayıftır.
4. **Ehliyet ve temsil**: Küçük/kısıtlı için veli/vasi onamı; acil ve bilinç kaybında varsayılan rıza/zorunluluk hâli (TCK m.25).
5. **İspat yükü**: Aydınlatmanın yapıldığını ve onamın alındığını hekim/hastane ispatlar (karine davacı/hasta lehine).
6. **Ara sonuç**: Aydınlatma eksikse, müdahale teknik olarak kusursuz olsa dahi gerçekleşen komplikasyondan hekim sorumlu olabilir; çünkü hasta o riski üstlenmemiş sayılır.

## Çıktı modülleri
- Onam geçerlilik kontrol listesi
- Aydınlatma içerik boşluğu raporu
- İspat durumu ve belge eksikliği notu
- Müdahaleye özgü onam metni taslağı (yer tutuculu)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

