---
argument-hint: ''
description: Bir kişinin 4/a, 4/b veya 4/c kapsamında olup olmadığını, sigortalılığın
  başlangıç-bitişini ve hangi sigorta kolunun devreye girdiğini belirlemek gerektiğinde;
  her sosyal güvenlik dosyasının ilk adımı
name: sigortalilik-statusu-ve-sistem
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


# Sigortalılık Statüsü ve Sistem Haritası

## Görev
Kişinin sosyal güvenlik sistemindeki yerini (statü, dönem, sigorta kolu) doğru saptamak ve uyuşmazlığı sistematik olarak konumlandırmak. Yanlış statü tespiti, tüm emeklilik/prim/dava değerlendirmesini geçersiz kılar.

## Soğuk başlangıç (intake)
- Kişi hizmet akdiyle mi (işçi), kendi nam ve hesabına mı (esnaf/şirket ortağı), yoksa kamu görevlisi olarak mı çalışıyor/çalıştı?
- Çalışma dönemi(leri) hangi tarih aralığında; 2008 Ekim öncesi (mülga kanun) dönem var mı?
- İşe giriş bildirgesi verilmiş mi, SGK hizmet dökümünde kaydı var mı?
- Uyuşmazlık emeklilik, prim, hizmet tespiti, iş kazası mı yoksa GSS mi?

## Denetim şeması
1. Statü tayini — 5510 m.4: Hizmet akdi varsa 4/a; bağımsız çalışma (esnaf, şirket ortağı, tarım) 4/b; kamu görevlisi 4/c. Şirket ortaklığında m.4/1-b ve ortaklık türü (limited ortağı, AŞ yönetim kurulu üyesi) ayrımı yapılır.
2. Sigortalı sayılmayanlar — m.6: İstisna haller (örn. bazı aile çalışmaları) elenir.
3. Başlangıç/bitiş — m.7 ve m.9: 4/a'da fiilen işe başlama, 4/b'de tescil/kayıt belirleyicidir. Ara sonuç: sigortalılık dönemleri çıkarılır.
4. Geçiş hükümleri: 2008/Ekim öncesi için 506/1479/5434 ve 5510 geçici maddeleri uygulanır; emeklilik koşulu kademeli geçişe tâbidir.
5. Sigorta kolu ayrımı: kısa vade (m.13-18) / uzun vade (m.25-37) / GSS (m.60). İspat yükü: sigortalılık iddiasında kural olarak iddia eden tarafta; kuruma bildirilmiş kayıt aksini ispata kadar esas alınır.

## Çıktı modülleri
- Statü ve dönem tablosu (statü / tarih aralığı / dayanak madde).
- Uygulanacak mevzuat (5510 mi, mülga kanun mu) tespiti.
- Devreye giren sigorta kolu ve sonraki uzman beceriye yönlendirme.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

