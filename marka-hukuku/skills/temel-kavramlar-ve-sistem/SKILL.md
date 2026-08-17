---
argument-hint: ''
description: Marka hukukuna ilk girişte; markanın hukuki niteliği, hak sahipliği,
  koruma kapsamı ve SMK'nın tescil-koruma-tasarruf ekseninin haritalanması gerektiğinde
  uyuşmazlığı doğru kanala yerleştirmek için ku
name: temel-kavramlar-ve-sistem
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve SMK Sistematiği

## Görev
Somut sorunu 6769 sayılı SMK'nın doğru ekseninde (tescil/idari süreç, hükümsüzlük-iptal, tecavüz, sözleşme) konumlandırmak; markanın tanımı (m.4), hakkın doğumu (tescil ilkesi) ve kapsamının (m.7) çerçevesini kurmak. Yanlış kanal seçimi süre ve görev hatasına yol açar; bu yüzden ilk filtre budur.

## Soğuk başlangıç (intake)
- İşaret tescilli mi, başvuru aşamasında mı, tescilsiz kullanım mı?
- Hangi mal/hizmetler (Nice sınıfları) söz konusu?
- Talep ne: tescil/itiraz, hükümsüzlük/iptal, tecavüzün önlenmesi, tazminat, lisans/devir?
- Karşı tarafın hakkı/önceliği var mı, tarih sırası nedir?

## Denetim şeması
1. **Marka olabilirlik (m.4).** İşaret ayırt edici mi ve sicilde açık-kesin gösterilebiliyor mu (kelime, şekil, renk, ses, üç boyutlu). Olamıyorsa hiç tescil edilmemeli.
2. **Hakkın doğumu.** Türk sisteminde marka hakkı kural olarak tescille doğar (m.7/1). Tescilsiz işaret için m.6/3 (eskiye dayalı kullanım) ve haksız rekabet (TTK m.54-55) yolu ayrıca değerlendirilir.
3. **Koruma kapsamı (m.7).** Aynı işaret-aynı mal; benzer işaret-benzer mal + karıştırılma; tanınmış markada farklı sınıf koruması. Yasaklama yetkisinin kapsamı buradan çıkar.
4. **Sınırlar.** Dürüst kullanım (m.7/5), hakkın tüketilmesi (m.152), kullanmama def'i (m.19/2), sessiz kalma (m.25/6) hakkın kullanımını sınırlar.
5. **Ara sonuç.** Uyuşmazlığın türü (idari/adli), görevli merci (TÜRKPATENT/FSHHM) ve uygulanacak ana norm bloğu (m.5-6 / m.25-26 / m.29-150) belirlenir; süre riski işaretlenir.

## Çıktı modülleri
- Uyuşmazlık türü ve doğru kanal haritası.
- İşaret-mal/hizmet (Nice sınıfı) tablosu.
- Uygulanacak ana norm bloğu ve süre uyarı listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

