---
argument-hint: ''
description: Aynı olayda sebepsiz zenginleşme yanında istihkak, haksız fiil, sözleşmesel
  iade veya vekâletsiz iş görme talebi de mümkün olduğunda hangi talebin öncelikli
  ve avantajlı olduğunu belirlemek için kulla
name: yarisma-ve-talep-secimi
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Diğer Taleplerle Yarışma ve Talep Seçimi

## Görev
Sebepsiz zenginleşmenin tali (ikincil) niteliğini gözeterek, aynı maddi olayda mümkün olan diğer taleplerle (aynî istihkak, sözleşmesel iade, haksız fiil, vekâletsiz iş görme) yarışmayı çözmek ve müvekkil için en avantajlı talebi seçmek. Yanlış talep seçimi süre, faiz ve ispat dezavantajı doğurur.

## Soğuk başlangıç (intake)
- Olayda ayakta bir sözleşme veya geçersiz sözleşmenin tasfiyesi var mı?
- İade konusu hâlâ aynen mevcut, belirli bir şey mi (istihkak mümkün mü)?
- Karşı tarafın kusurlu/hukuka aykırı fiili var mı (haksız fiil mümkün mü)?
- Bir kişi başkasının işini yetkisiz mi gördü (vekâletsiz iş görme)?

## Denetim şeması
1. **Tali nitelik kuralı.** Sebepsiz zenginleşme, başka bir talep mümkünse kural olarak geri planda kalır; mümkün olan diğer talep yoksa veya tükenmişse devreye girer. Önce öncelikli talepler taranır.
2. **Aynî istihkak (TMK m.683).** İade konusu belirli bir şey ve mülkiyet devredilmemişse, malik istihkakla aynen iade isteyebilir; bu talep süre ve aynen iade bakımından avantajlıdır. Zamanaşımına da kural olarak tâbi değildir.
3. **Sözleşmesel iade/dönme.** Geçersiz veya dönülmüş sözleşmede iade çoğu kez sözleşmenin kendi tasfiye rejimiyle (TBK m.125/2 dönme) çözülür; bu daha geniş tazminat imkânı sağlayabilir.
4. **Haksız fiil (TBK m.49 vd.).** Karşı tarafın kusurlu ve hukuka aykırı fiili zarara yol açtıysa haksız fiil tazminatı zenginleşmeden bağımsız ve genellikle daha geniş kapsamlıdır; ölçü "zarar"dır, "zenginleşme" değil.
5. **Vekâletsiz iş görme (TBK m.526-531).** Bir kişi başkasının işini onun menfaatine/iradesine göre yetkisiz görmüşse, sebepsiz zenginleşme yerine bu özel hükümler uygulanır.
6. **Seçim ve ara sonuç.** Süre, faiz başlangıcı, ispat kolaylığı ve talep miktarı karşılaştırılır; gerekiyorsa terditli (kademeli) talep kurulur. Ara sonuç: birincil talep + yedek sebepsiz zenginleşme talebi.

## Çıktı modülleri
- Talep karşılaştırma matrisi (süre/faiz/ispat/miktar).
- Terditli talep kurgusu önerisi.
- Seçilen talep gerekçe notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

