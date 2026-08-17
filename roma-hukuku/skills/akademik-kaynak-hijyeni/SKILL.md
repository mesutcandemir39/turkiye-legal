---
argument-hint: ''
description: Roma hukuku metni veya akademik çalışma için birincil kaynak (Corpus
  Iuris Civilis), Latince maxim ve doktrin atıflarının doğru künyeyle verilmesi gerektiğinde
  kullanılır; uydurma fragman, sahte künye
name: akademik-kaynak-hijyeni
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


# Roma Hukuku Kaynak ve Atıf Hijyeni

## Görev
Roma hukuku ve hukuk tarihi metinlerinde birincil kaynak, Latince maxim ve doktrin atıflarının doğru ve doğrulanabilir biçimde verilmesini sağlamak; uydurma fragman, sahte künye ve hatalı Latince kullanımını önlemek.

## Soğuk başlangıç (intake)
- Çıktı akademik metin mi, ders notu mu, mütalaa eki mi?
- Birincil Roma kaynağı (Digesta/Institutiones/Codex) atfı gerekli mi?
- Latince maxim kullanılacak mı; tam lafız mı isteniyor?
- Doktrin künyesi tam mı, yoksa ilkesel atıf mı yeterli?

## Denetim şeması
1. Birincil kaynak atıf standardını uygula:
   - Digesta: D. kitap.başlık.fragman.paragraf (ör. D.41.1.20).
   - Institutiones (Iustinianus): Inst. kitap.başlık.paragraf; Gaius için Gai. kitap.paragraf (ör. Gai. 2.12).
   - Codex: C. kitap.başlık.fragman; Novellae: Nov. numara.
   Fragman numarasından emin değilsen numara uydurma; kurumu anlat ve atfı [DOĞRULANMADI] olarak işaretle.
2. Latince maximi doğru lafızla yaz: tam ve klasik biçimde; eksik/uydurma Latince kullanma. Çeviriyi mutlaka ekle ve yürürlükteki maddeyle bağla.
3. Doktrin atfını düzenle: Türk Roma hukuku literatüründe başlıca eserler ilkesel olarak anılabilir (Ziya Umur — Roma Hukuku Lügatı/Ders Notları; Türkân Rado — Roma Hukuku Dersleri; Belgin Erdoğmuş; Bülent Tahiroğlu/Belgin Erdoğmuş). Tam künye (baskı, sayfa) gerekiyorsa [DOĞRULANMADI] işareti koy; sayfa numarası uydurma.
4. Yürürlükteki norm ile tarihî kaynağı ayrı tut: tarihî bilgi yürürlükteki hukukun yerine geçmez. Çıktıda yürürlükteki madde (TMK/TBK) ile Roma kaynağını farklı katmanlarda göster.
5. İçtihat gerekirse: tarihî-sistematik yorumun mahkemece kullanıldığı kararları karararama.yargitay.gov.tr veya karararama.danistay.gov.tr üzerinden doğrula; esas/karar numarası asla uydurma, doğrulanmamışsa ilkesel atıfla yetin ve [DOĞRULANMADI] işaretle.
6. Ara sonuç: her atfı kaynak türüne göre standartlaştır; doğrulanmamış olanları açıkça etiketle.

İspat/dayanak: birincil kaynak fragman standardıyla; doktrin yazar-eser ile; yürürlükteki norm madde ile.

## Çıktı modülleri
- Atıf listesi (birincil kaynak / doktrin / yürürlükteki norm ayrı bloklar).
- Doğrulama notları ([DOĞRULANMADI] etiketli kalemler).
- Latince maxim sözlüğü (lafız + çeviri + madde bağı).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

