---
argument-hint: ''
description: Bir yatırım veya devralma öncesi girişimin hukuki durum tespiti (due
  diligence) yapılırken; kurumsal, sözleşmesel, fikri mülkiyet, iş hukuku, vergi ve
  KVKK risklerinin taranması, bulguların raporlanma
name: hukuki-durum-tespiti-due-diligence
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Hukuki Durum Tespiti (Due Diligence)

## Görev
Yatırım/devralma öncesi girişimin hukuki risklerini sistematik taramak; kapanış öncesi giderilmesi gereken (condition precedent) ve fiyata/garantiye yansıması gereken bulguları ayırmak; DD raporu üretmek.

## Soğuk başlangıç (intake)
1. İşlem tipi: azınlık yatırımı mı, kontrol devri/M&A mi?
2. Şirketin yaşı, çalışan sayısı, fikri mülkiyet ağırlığı ne?
3. Hangi başlıklar kritik: IP, iş hukuku, vergi/teşvik, sözleşmeler, KVKK?
4. Daha önce yatırım turu/SAFE/borç var mı (cap table karmaşası)?
5. Süre ve veri odası (data room) erişimi hazır mı?

## Denetim şeması
1. Kurumsal: Esas sözleşme, pay defteri (TTK m.499), GK/YK kararları, ticaret sicili kayıtları; cap table'ın belgelerle örtüşmesi; geçmiş artırım/devirlerin geçerliliği (m.456, m.490).
2. Sözleşmesel: Müşteri/tedarikçi sözleşmelerinde kontrol değişikliği (change of control) ve devir yasağı; SAFE/dönüştürülebilir enstrümanların dönüşüm etkisi; SHA çakışması.
3. Fikri mülkiyet: Ürün/kod/markanın şirkete ait olduğunun teyidi — kurucu ve çalışan IP devir sözleşmeleri (6769 SMK; çalışan buluşu hükümleri; 5846 FSEK eser/mali hak devri); açık kaynak lisans uyumu.
4. İş hukuku: İş sözleşmeleri, fazla mesai/kıdem riskleri (4857), SGK uyumu (5510), ESOP/danışman ilişkilerinin niteliği (işçi mi serbest mi).
5. Vergi/teşvik: VUK uyumu, TGB/Ar-Ge teşvik şartlarının fiilen sağlanması (4691/5746), olası geçmiş dönem riskleri.
6. KVKK: Veri envanteri, aydınlatma/açık rıza, VERBİS, veri ihlali geçmişi (6698 m.10-12); DD sırasında veri aktarımının kendisi m.8-9 ile altlanır.
7. Red flag ve çıkış: Bulguları "kapanış ön şartı / fiyat düzeltmesi / beyan-tekeffül-tazminat" olarak sınıfla; düzeltilemez riskte işlemden çekilme önerisi.

## Çıktı modülleri
- Veri odası talep listesi (başlık başlık).
- DD bulgu/risk raporu (önem derecesi ve madde atıflı).
- Red flag listesi ve kapanış ön şartı/garanti önerileri.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

