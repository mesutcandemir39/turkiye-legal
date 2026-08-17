---
argument-hint: ''
description: Mütalaa konusu talebin zamanaşımı, hak düşürücü süre veya dava/başvuru
  süresi yönünden hâlâ kullanılabilir olup olmadığını denetlemek gerektiğinde kullanılır;
  her mütalaada zorunlu bir kontrol noktası
name: sureler-ve-zamanasimi-denetimi
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Süreler ve Zamanaşımı Denetimi

## Görev
Mütalaa edilen hakkın veya talebin süre yönünden hâlâ ileri sürülebilir olup olmadığını saptamak; zamanaşımı, hak düşürücü süre ve dava/başvuru sürelerini ayırt etmek. Esasen haklı bir talep, süre geçmişse pratikte değersizdir; bu denetim atlanamaz.

## Soğuk başlangıç (intake)
- Talebin hukuki niteliği ne? (Sözleşme, haksız fiil, sebepsiz zenginleşme, idari işlem iptali, ceza şikâyeti)
- Sürenin başladığı an hangi olay? (Muacceliyet, zarar/failin öğrenilmesi, tebliğ, ifa)
- Süreyi kesen/durduran bir işlem yapıldı mı? (Dava, takip, ihtar, kısmi ödeme)
- Karşı taraf zamanaşımı def'ini ileri sürer mi?

## Denetim şeması
1. Süre türü tayini: Zamanaşımı def'i olarak ileri sürülmeli ve hakkı sona erdirmez (borç eksik borca döner); hak düşürücü süre re'sen gözetilir ve hakkı sona erdirir. Bu ayrım sonucu kökten değiştirir.
2. Genel zamanaşımı süreleri: TBK m.146 genel on yıl; TBK m.147 beş yıllık istisnalar (kira, ücret, vekâlet vb.); haksız fiilde TBK m.72 — fiil ve failin öğrenilmesinden iki yıl ve her hâlde on yıl; sebepsiz zenginleşmede TBK m.82 — iki/on yıl. Ticari ve özel kanun süreleri (TTK, İş K., 6502, SMK) ayrıca kontrol edilir.
3. Başlangıç anı: Süre muacceliyet/öğrenme/tebliğ anından işler; her talep için bu an ayrı belirlenir.
4. Kesilme/durma: TBK m.154 (dava, takip, ihtar, borç ikrarı zamanaşımını keser) ve m.153 (durma sebepleri) uygulanır; kesilmeyle süre yeniden işler.
5. Dava/başvuru süreleri (hak düşürücü nitelikte): İdari davada İYUK m.7 (genel altmış gün); işe iade başvurusu İş K. m.20/m.21 (fesih tebliğinden bir ay); AYM bireysel başvuru otuz gün; bunlar re'sen gözetilir.
6. Ara sonuç: Süre türü + dolup dolmadığı + kesen/durduran işlem etkisi + "geçmişse hangi alternatif kalır" notu.

## Çıktı modülleri
- Süre hesap tablosu (talep | süre türü | başlangıç | bitiş | durum)
- Kesilme/durma değerlendirmesi
- Re'sen gözetilen süreler uyarısı
- Süre dolmuşsa kalan hukuki imkânlar



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

