---
argument-hint: ''
description: Fazla çalışma, ulusal bayram-genel tatil, hafta tatili ücreti ve yıllık
  izin alacaklarının doğup doğmadığını ve tutarını çözmek gerektiğinde; çalışma sürelerini,
  zamları ve takdiri indirimi kapsayan a
name: iscilik-alacaklari-fazla-mesai-izin
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İşçilik Alacakları — Fazla Çalışma, UBGT, Hafta Tatili, Yıllık İzin

## Görev
Ücret dışı işçilik alacaklarını (fazla çalışma, fazla sürelerle çalışma, UBGT, hafta tatili, yıllık izin ücreti) doğru zam ve hesap esaslarıyla belirlemek.

## Soğuk başlangıç (intake)
1. Günlük/haftalık fiili çalışma saatleri ve düzeni nasıldı?
2. Bayram-genel tatil ve hafta tatillerinde çalışıldı mı?
3. Yıllık izinler kullandırıldı mı; izin defteri/imzalı belge var mı?
4. Bordrolarda fazla çalışma/tatil tahakkuku görünüyor mu?

## Denetim şeması
1. **Çalışma süresi (m.63):** Haftalık çalışma 45 saat. Aşan kısım fazla çalışmadır.
2. **Fazla çalışma / fazla sürelerle çalışma (m.41):** 45 saati aşan çalışma fazla çalışma → saat ücreti **%50 zamlı**. Sözleşmeyle haftalık süre 45'in altında belirlenmişse, bu süre ile 45 arasındaki çalışma fazla sürelerle çalışma → **%25 zamlı**. Yıllık fazla çalışma 270 saatle sınırlıdır (sınır aşımı çalışmayı geçersiz kılmaz, fazlasını da hak doğurur).
3. **UBGT (m.47):** Ulusal bayram ve genel tatil günü çalışılırsa, çalışılmayan o gün için bir günlük ücret zaten ödenir; çalışıldığında ayrıca her gün için bir günlük ücret daha → o günkü çalışma toplam iki yevmiye.
4. **Hafta tatili (m.46):** Tatilde çalışmadan bir günlük ücret hak edilir. Hafta tatilinde çalışıldıysa Yargıtay uygulamasında çalışılan gün için ilave 1,5 yevmiye doğar.
5. **Yıllık izin (m.53, 59):** Hizmet süresine göre 1-5 yıl 14 gün, 5-15 yıl 20 gün, 15+ yıl 26 gün (asgari, 18 yaş altı ve 50 yaş üstü en az 20 gün). Kullandırılmayan izin sözleşme sonunda **son ücret** üzerinden ücrete dönüşür (m.59). İspat yükü kullandırıldığına dair işverende (imzalı izin belgesi).
6. **İspat ve indirim:** Fazla çalışma işçide ispat; tanıkla ispatta ve uzun süreli/günlük çalışmalarda hakkaniyet/takdiri indirim uygulanabilir. İmzalı bordroda tahakkuk varsa o aylar dışlanır.

## Çıktı modülleri
- Alacak kalemleri tablosu (zam oranı + dönem + tutar mantığı).
- İspat yükü ve delil durumu notu.
- Takdiri indirim öngörüsü.
- Zamanaşımı uyarısı (ücret nitelikli alacaklarda 5 yıl).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

