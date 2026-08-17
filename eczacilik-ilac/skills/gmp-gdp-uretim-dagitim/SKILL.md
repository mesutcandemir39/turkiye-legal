---
argument-hint: ''
description: İlaç üretim ve dağıtım denetimleri, GMP/GDP uygunsuzlukları, soğuk zincir,
  ecza deposu ve geri çekme süreçlerinde TİTCK denetim ve yaptırımlarına karşı kullanılır.
name: gmp-gdp-uretim-dagitim
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
  - ad: Hemşirelik Kanunu
    numara: '6197'
    tur: kanun
  - ad: Mimar ve Mühendisler Hakkında Kanun
    numara: '1262'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İyi Üretim ve Dağıtım Uygulamaları (GMP/GDP)

## Görev
Üretim yerinin GMP, ecza deposu/dağıtımın GDP uygunluğunu denetim raporu üzerinden değerlendirmek; uygunsuzluk yaptırımına ve geri çekme kararlarına karşı strateji kurmak.

## Soğuk başlangıç (intake)
- İhlal üretimde mi (GMP) dağıtımda mı (GDP, ecza deposu)?
- Denetim sonucu: kritik/major/minor bulgu sınıflandırması nedir; CAPA verildi mi?
- Soğuk zincir/sahte ilaç/karekod (İTS) ihlali var mı?
- TİTCK kararı: sertifika askısı, üretim/satış durdurma, geri çekme, idari para cezası mı?

## Denetim şeması
1. **Dayanak.** İlaçların GMP ve GDP kılavuzları (TİTCK), 1262 sayılı Kanun ve Ecza Depoları Yönetmeliği; İlaç Takip Sistemi (İTS/karekod) mevzuatı.
2. **Bulgu sınıflandırma.** Kritik bulgu (hasta güvenliği riski) → ağır yaptırım; major/minor → CAPA ile giderim. Ara sonuç: bulgunun sınıfı yaptırımla orantılı mı (ölçülülük)?
3. **İşlem denetimi.** Sertifika askısı/üretim durdurma/geri çekme birel idari işlemdir; yetki-sebep-konu yönünden incelenir. İspat: idare bulguyu denetim raporu ve numune analiziyle; firma CAPA ve düzeltici kanıtla karşılar.
4. **Geri çekme.** Sınıf 1/2/3 geri çekme; bildirim ve toplama yükümlülüğü; eksik geri çekme ek yaptırım ve TCK m.187 (bozulmuş/sahte ilaç) ceza riski doğurur.
5. **Yargı yolu.** İdari yaptırıma karşı iptal + yürütmeyi durdurma (İYUK m.7, m.27); telafisi güç zarar (tesis kapanması) somutlaştırılır. Sözleşmesel zarar (fason üretim, tedarik) adli yargıda TBK çerçevesinde ele alınır.

## Çıktı modülleri
- Denetim bulgusu-yaptırım orantılılık analizi.
- CAPA ve düzeltici kanıt dosyası planı.
- İptal + yürütmeyi durdurma dilekçe iskeleti [doldurulacak].



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

