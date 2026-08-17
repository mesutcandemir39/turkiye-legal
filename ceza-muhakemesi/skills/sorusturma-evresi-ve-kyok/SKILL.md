---
argument-hint: ''
description: Soruşturmanın başlaması, savcının delil toplaması, ifade/şüpheli hakları,
  iddianame veya takipsizlik kararı ile takipsizliğe itiraz süreçlerinde kullanılır.
name: sorusturma-evresi-ve-kyok
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
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Soruşturma Evresi ve Kovuşturmaya Yer Olmadığı Kararı

## Görev
Soruşturmanın hukuka uygun yürütülüp yürütülmediğini denetlemek; şüpheli/müşteki lehine talepleri belirlemek; iddianame ya da kovuşturmaya yer olmadığı (KYOK) kararına karşı strateji üretmek.

## Soğuk başlangıç (intake)
- Soruşturma neyle başladı: ihbar, şikâyet, suçüstü, resen?
- Şüpheli ifadesi alındı mı, müdafi hazır mıydı?
- Hangi deliller toplandı, eksik delil/araştırma var mı?
- Şikâyete bağlı suç mu (süre işliyor olabilir, TCK m.73)?
- KYOK verildiyse tebliğ tarihi nedir (itiraz süresi için)?

## Denetim şeması
1. **Başlama ve yürütme.** Savcı, ihbar veya şikâyetle suç şüphesini öğrenince soruşturmaya başlar ve maddi gerçeği araştırır; şüphelinin lehine delilleri de toplamak zorundadır (CMK m.158, m.160/2). Kolluk savcının emrinde çalışır (m.161).
2. **Şüpheli hakları.** İfade alınmadan önce haklar hatırlatılır: susma hakkı, müdafi, yakınına haber verme (m.147). Hukuka aykırı yöntemlerle alınan ifade delil olamaz (m.148).
3. **Şikâyet ve süre.** Şikâyete bağlı suçlarda fail ve fiilin öğrenilmesinden itibaren 6 ay içinde şikâyet gerekir (TCK m.73); aksi halde soruşturma şartı yoktur.
4. **Sonuç kararı.** Yeterli şüphe varsa iddianame düzenlenir (m.170); yoksa kovuşturmaya yer olmadığına karar verilir (m.172). Yeni delil olmadıkça aynı fiilden yeniden soruşturma açılamaz (m.172/2).
5. **KYOK'a itiraz.** Karara karşı tebliğden itibaren 15 gün içinde sulh ceza hâkimliğine itiraz edilir (m.173); hâkimlik kovuşturmaya yer olduğuna karar verirse savcı iddianame düzenler.
6. **Ara sonuç.** Eksik soruşturma, hak ihlali veya hatalı takipsizlik tespit edilirse itiraz dilekçesi; aksi halde kovuşturma savunması hazırlığına geçilir.

## Çıktı modülleri
- Soruşturma kronolojisi ve eksik işlem/delil listesi.
- Ek soruşturma/delil toplama talep dilekçesi taslağı.
- KYOK'a itiraz dilekçesi iskeleti (gerekçe + dayanak m.173).
- Şikâyet/zamanaşımı süresi uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

