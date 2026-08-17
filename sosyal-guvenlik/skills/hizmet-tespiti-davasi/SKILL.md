---
argument-hint: ''
description: Kuruma hiç bildirilmemiş veya eksik bildirilmiş çalışma sürelerinin mahkemece
  tespiti istendiğinde; hak düşürücü süre, re'sen araştırma ve tanık-belge ispatının
  kritik olduğu durumlarda kullanılır.
name: hizmet-tespiti-davasi
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
  - ad: Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu
    numara: '5510'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Hizmet Tespiti Davası

## Görev
Sigortalının kuruma bildirilmemiş hizmetlerinin tespiti davasını kurmak, hak düşürücü süreyi ve ispat stratejisini yönetmek. Bu dava kamu düzenine ilişkindir; hâkim re'sen araştırma yapar.

## Soğuk başlangıç (intake)
- Tespiti istenen dönem hangi yıllar; işyeri hâlâ faal mi?
- SGK hizmet dökümünde bu dönem hiç mi yok, eksik mi (gün/kazanç eksikliği)?
- Aynı işyerinden kuruma bildirilmiş başka bir gün/dönem var mı?
- O işyerinde birlikte çalışan, tanıklık edebilecek kişiler var mı?

## Denetim şeması
1. Hukuki dayanak — 5510 m.86/9 (mülga 506 m.79/10): Kuruma bildirilmemiş çalışmanın tespiti mahkemeden istenir. Davalılar: işveren ve SGK.
2. Hak düşürücü süre: Hizmetin geçtiği yılın sonundan itibaren 5 yıl. Ancak işverence kuruma verilmiş herhangi bir belge (işe giriş bildirgesi, dönem bordrosu, müfettiş tutanağı) varsa hak düşürücü süre işlemez — bu istisna mutlaka araştırılır.
3. Re'sen araştırma: Mahkeme işyeri SGK sicil dosyasını, dönem bordrolarını, varsa müfettiş raporlarını getirtir; komşu işyeri tanıklarını dinler. İspat yükü davacıda olmakla birlikte hâkim resen delil toplar.
4. İspat hiyerarşisi: Önce yazılı/resmi belge (bordro, ücret tediye, SGK kaydı), sonra bordro tanıkları, en son komşu işyeri/resmi kurum tanıkları. Salt tanıkla tespitte güçlü/destekleyici delil aranır.
5. Ara sonuç: Tespit edilen dönem, gün sayısı ve prime esas kazanç belirlenir; karar SGK kayıtlarına işlenir.

## Çıktı modülleri
- Dava dilekçesi iskeleti (taraflar, dönem, talep sonucu, deliller).
- Delil ve tanık listesi; getirtilecek belgeler dizini.
- Hak düşürücü süre değerlendirme notu (istisna var/yok).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

