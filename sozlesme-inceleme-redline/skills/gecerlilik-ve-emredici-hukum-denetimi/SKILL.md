---
argument-hint: ''
description: Bir maddenin veya bütün sözleşmenin emredici hükme, ahlaka veya kamu
  düzenine aykırı olup olmadığını, kısmi mi tam mı hükümsüz olduğunu değerlendirmek
  gerektiğinde kullanılır.
name: gecerlilik-ve-emredici-hukum-denetimi
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Geçerlilik ve Emredici Hüküm Denetimi

## Görev
Sözleşme hükümlerini geçerlilik süzgecinden geçirmek; kesin hükümsüz, iptal edilebilir veya yazılmamış sayılacak kayıtları ayıklamak ve kısmi butlanın metni nasıl etkilediğini belirlemek.

## Soğuk başlangıç (intake)
- Hangi madde şüpheli; emredici bir hükmü mü aşıyor (faiz tavanı, asgari işçi hakkı, tüketici koruması)?
- Edimin konusu baştan imkânsız veya hukuka aykırı mı?
- İrade sakatlığı (hata/hile/korkutma) veya gabin belirtisi var mı?
- Sözleşme matbu/standart mı (GİK denetimi gerekir)?

## Denetim şeması
1. **Konu denetimi**: TBK m.27/f.1 — kanunun emredici hükümlerine, ahlaka, kamu düzenine, kişilik haklarına aykırı veya konusu imkânsız sözleşme kesin hükümsüzdür. Örn. ölünceye kadar rekabet yasağı kişilik hakkını aşarsa, ölçüsüz münhasırlık.
2. **Kısmi butlan**: TBK m.27/f.2 — sakatlık yalnız bazı hükümleri etkiliyorsa kural olarak diğerleri ayakta kalır; ancak bu hükümler olmadan sözleşme yapılmayacağı anlaşılırsa tamamı geçersiz. "Severability/bölünebilirlik" kaydı bu sonucu yönlendirir.
3. **GİK içerik denetimi**: TBK m.21 (şaşırtıcı/beklenmedik kayıt yazılmamış sayılır), m.24 (tek taraflı değiştirme yasağı), m.25 (dürüstlüğe aykırı, karşı tarafı ağırlaştıran kayıt geçersiz). Tüketicide TKHK m.5 ek koruma.
4. **İrade sakatlığı/gabin**: TBK m.30-39 iptal hakkı (1 yıl, m.39); m.28 gabin (aşırı yararlanma).
5. **İspat yükü**: Hükümsüzlüğü ileri süren ispatla yükümlüdür (TMK m.6); kesin hükümsüzlük hâkimce resen dikkate alınır, ileri sürülmesi süreye bağlı değildir.
6. **Ara sonuç**: Geçersiz/yazılmamış kayıtların listesi ve metnin ayakta kalan kısmı; redline öncesi temizlik haritası.

## Çıktı modülleri
- Geçersiz/iptal edilebilir/yazılmamış sayılacak madde tablosu.
- Kısmi butlan etkisi ve bölünebilirlik kaydı önerisi.
- Emredici hüküm ihlali için düzeltme veya çıkarma talebi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

