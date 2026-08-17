---
argument-hint: ''
description: Tehlikedeki gemi veya yükün kurtarılması (kurtarma ücreti) ya da ortak
  selamet için bilerek yapılan fedakârlık/masrafların paylaşımı (müşterek avarya)
  gündeme geldiğinde; ücret/garame paylarını ve Yor
name: kurtarma-musterek-avarya
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kurtarma ve Müşterek Avarya

## Görev
Kurtarma faaliyetinde kurtarma ücretinin doğup doğmadığını ve miktarını belirlemek; ortak selamet için yapılan fedakârlık ve olağanüstü masrafları müşterek avarya olarak nitelendirip garame paylarını dağıtmak.

## Soğuk başlangıç (intake)
- Olay bir kurtarma mı (üçüncü kişinin yardımı) yoksa müşterek avarya mı (deniz serveti içinde fedakârlık)?
- Tehlike gerçek ve ciddi miydi; kurtarma faydalı sonuç (no cure no pay) doğurdu mu?
- Sözleşme/standart form (örn. LOF) var mı; York-Anvers Kurallarına atıf yapılmış mı?
- Gemi, yük ve navlun değerleri ile fedakârlık/masraf kalemleri nelerdir?

## Denetim şeması
1. **Kurtarma şartları**: Deniz tehlikesi, faydalı sonuç ve gönüllülük unsurlarını (TTK m.1298 vd., 1989 Kurtarma Sözleşmesi esaslı) denetle; "no cure no pay" ilkesini ve çevre zararı önlemeye yönelik özel tazminatı (special compensation) ayrıştır.
2. **Kurtarma ücretinin belirlenmesi**: Kurtarılan değer, tehlikenin derecesi, kullanılan emek/araç ve başarı gibi ölçütlerle ücreti takdir et; ücret kurtarılan değeri aşamaz. Kurtaranlar arasında paylaşımı belirle.
3. **Müşterek avarya nitelendirmesi**: Ortak tehlikeden ortak selameti sağlamak için **bilerek ve makul** yapılan olağanüstü fedakârlık/masrafları müşterek avarya say (TTK m.1272 vd.); kuru/münferit (hususi) avaryadan ayır.
4. **Garame paylaşımı**: York-Anvers Kuralları uyarınca avarya garame payını gemi, yük ve navlunun kurtulan değerleri oranında dağıt; dispeç (avarya raporu) hazırlanmasını ve dispeççinin rolünü belirt.
5. **İspat ve ara sonuç**: Fedakârlığın iradî ve makul olduğunu, ortak tehlikenin varlığını talep eden ispatlar. Çıktıda kurtarma ücreti veya garame payı dağıtımını sayısal taslakla sonuçlandır; ilgili zamanaşımı sürelerini işaretle.

## Çıktı modülleri
- Kurtarma ücreti / müşterek avarya nitelendirme notu
- Değer ve garame payı dağıtım taslağı (dispeç iskeleti)
- Teminat (avarya garantisi/depozito) ve tahsil stratejisi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

