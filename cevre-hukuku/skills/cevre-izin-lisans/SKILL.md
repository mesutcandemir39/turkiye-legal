---
argument-hint: ''
description: Emisyon, deşarj, gürültü gibi çevre izinleri ile geri kazanım/bertaraf
  lisanslarının alınması, askıya alınması veya iptaline ilişkin işlem ve uyuşmazlıklarda;
  EÇBS/e-Çevre süreçlerinde ve izinsiz faal
name: cevre-izin-lisans
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
  - ad: Çevre Kanunu
    numara: '2872'
    tur: kanun
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Çevre İzin ve Lisansları

## Görev
Bir tesisin tabi olduğu çevre izni/lisansını belirlemek, başvuru ve yenileme sürecini yönetmek, izin işlemlerine veya izinsiz faaliyet yaptırımlarına karşı strateji kurmak.

## Soğuk başlangıç (intake)
1. Tesis hangi faaliyet kolunda; çevreye etki bakımından hangi sınıfta yer alıyor?
2. Hangi izin konuları gerekli: hava emisyonu, atıksu deşarjı, gürültü, derin deniz deşarjı, tehlikeli madde?
3. Geçici faaliyet belgesi veya çevre izni/lisansı mevcut mu; süresi/yenileme durumu?
4. İdari yaptırım (durdurma, para cezası) uygulandı mı?

## Denetim şeması
1. **Yükümlülüğün kaynağı**: 2872 m.11 ve m.12, faaliyet sahibine arıtma/önleme ve izin yükümlülüğü yükler. Çevre İzin ve Lisans Yönetmeliği tesisleri çevresel etkilerine göre sınıflandırır ve izin konularını belirler.
2. **Süreç**: Başvuru EÇBS/e-Çevre üzerinden yapılır; geçici faaliyet belgesi sonrası belirli sürede çevre izni alınması gerekir. Süreye uyulmaması belgenin iptali ve faaliyet durdurma sonucunu doğurabilir.
3. **İzinsiz faaliyet sonucu**: 2872 m.15 faaliyetin durdurulmasını, m.20-23 idari para cezalarını öngörür; izinsiz deşarj/emisyon ağırlaştırıcıdır.
4. **İşleme itiraz**: İznin verilmemesi, askıya alınması veya iptali ile durdurma/ceza kararları idari işlemdir; iptal davası 2577 sayılı İYUK'a tabidir (süre kural olarak 60 gün, yürütmenin durdurulması talep edilebilir).
5. **İspat ve ara sonuç**: Ölçüm raporları, emisyon/deşarj analizleri ve EÇBS kayıtları esastır; usulüne uygun olmayan numune/ölçüm ceza işlemini sakatlayabilir.

## Çıktı modülleri
- İzin/lisans kapsam tablosu (konu + dayanak)
- Başvuru/yenileme yol haritası ve süre takvimi
- İzin işlemine veya durdurma kararına karşı dava iskeleti
- Ölçüm/numune usul denetimi notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

