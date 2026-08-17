---
argument-hint: ''
description: Bir hukuki argümanda Latin maximi (pacta sunt servanda, nemo plus iuris,
  in dubio pro reo, lex specialis) doğru biçimde kullanılacak, çevrilecek ve yürürlükteki
  maddeye bağlanacaksa kullanılır; uydurm
name: latin-maximleri
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


# Latin Hukuk Maximleri ve Doğru Kullanımı

## Görev
Hukuki metinlerde Latin maximlerini doğru lafız, doğru çeviri ve doğru yürürlükteki madde bağlantısıyla kullanmak; maximin bağlayıcı norm değil yardımcı argüman olduğu sınırını korumak.

## Soğuk başlangıç (intake)
- Hangi argüman için maxim aranıyor (sözleşme, ayni hak, ceza, yorum, usul)?
- Maxim mütalaa/dilekçeye mi girecek yoksa açıklama amaçlı mı?
- Yürürlükteki hangi maddeyle bağlanacak?

## Denetim şeması
1. Maximi doğru lafızla seç ve çevir (uydurma Latince yazma):
   - pacta sunt servanda — sözleşmeler bağlayıcıdır (TBK m.1, m.26 ile bağla).
   - nemo plus iuris ad alium transferre potest quam ipse haberet — kimse sahip olduğundan fazlasını devredemez (TMK m.683 devir, m.1023 istisna).
   - clausula rebus sic stantibus — şartların değişmezliği kaydı; aşırı ifa güçlüğü (TBK m.138).
   - res perit domino / periculum est emptoris — hasara mülkiyet sahibi katlanır; satışta yürürlükteki kural TBK m.208 olarak sabit, maximi mutlak kural saymadan kullan.
   - lex specialis derogat legi generali — özel norm genel normu bertaraf eder (norm çatışması, TMK m.1 sistematik yorum).
   - lex posterior derogat legi priori — sonraki kanun öncekini ilga eder.
   - in dubio pro reo — şüpheden sanık yararlanır (CMK 5271 ispat ve masumiyet karinesi, Anayasa m.38).
   - nulla poena sine lege / nullum crimen sine lege — kanunsuz suç ve ceza olmaz (TCK m.2, Anayasa m.38 kanunilik).
   - audiatur et altera pars — diğer taraf da dinlenir (hukuki dinlenilme hakkı, HMK m.27).
   - nemo iudex in causa sua — kimse kendi davasına hâkim olamaz (hâkimin reddi/yasaklılığı, HMK m.34 vd.).
   - in dubio contra stipulatorem / contra proferentem — şüphede düzenleyen aleyhine yorum (genel işlem koşulları, TBK m.23).
2. Maximi yürürlükteki maddeye altla: maxim tek başına gerekçe değildir; ilgili madde ile birlikte ve onu açıklayan yardımcı argüman olarak konumla.
3. İstisna ve sapmayı işaretle: maximin mutlak olmadığı, yürürlükteki normun farklı dengelediği halleri (ör. iyiniyetli üçüncü kişi korumasının nemo plus iuris'i sınırlaması) belirt.
4. Ceza ve usul maximlerinde anayasal dayanağı ekle (Anayasa m.38, m.36). Ara sonuç: maxim + çeviri + yürürlükteki madde + sınır üçlüsünü tamamla.

İspat/dayanak: yürürlükteki madde atfı ile; maxim klasik lafzıyla; Latince kaynak gerekirse fragman [DOĞRULANMADI].

## Çıktı modülleri
- Maxim kartı: Latince lafız / Türkçe çeviri / yürürlükteki madde / sınır notu.
- Argümana yerleştirme önerisi (yardımcı argüman uyarısıyla).
- Yanlış kullanım uyarıları (uydurma Latince, mutlaklaştırma).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

