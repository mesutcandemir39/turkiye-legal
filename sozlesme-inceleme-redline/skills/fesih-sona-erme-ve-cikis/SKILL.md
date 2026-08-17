---
argument-hint: ''
description: Fesih sebepleri, bildirimli/haklı fesih, dönme-fesih ayrımı, otomatik
  yenileme ve sözleşme sonrası yükümlülükler incelendiğinde kullanılır.
name: fesih-sona-erme-ve-cikis
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


# Fesih, Sona Erme ve Çıkış Hükümleri

## Görev
Sözleşmenin nasıl ve hangi sonuçlarla sona ereceğini denetlemek; fesih haklarının dengesini, bildirim usulünü, geçmişe/ileriye etki ayrımını ve çıkış sonrası yükümlülükleri belirlemek.

## Soğuk başlangıç (intake)
- Sözleşme ani edimli mi (dönme) yoksa sürekli mi (ileriye etkili fesih)?
- Fesih hakları kimde, tek taraflı mı; bildirim süresi/şekli ne?
- Haklı sebeple derhal fesih ve sözleşmeden dönme şartları net mi?
- Sona erme sonrası gizlilik, rekabet yasağı, iade, devir yükümlülükleri var mı?

## Denetim şeması
1. **Dönme/fesih ayrımı**: Ani edimli sözleşmede temerrüt hâlinde TBK m.125 — alacaklı ya ifa+gecikme tazminatı, ya ifadan vazgeçip müspet zarar, ya da dönüp menfi zarar isteyebilir. Sürekli borç ilişkisinde sona erme kural olarak **ileriye etkilidir** (fesih), geçmiş tasfiye edilmez.
2. **Haklı sebeple fesih**: Sürekli ilişkilerde dürüstlük kuralı gereği haklı/önemli sebeple derhal fesih hakkı emredici nitelikte kabul edilir; sözleşmeyle tümüyle kaldırılamaz. Tetikleyiciler somut ve ölçülebilir yazılmalı.
3. **Bildirim usulü**: Süre, şekil (yazılı/noter/KEP), ihtar şartı (TBK m.117 temerrüt için, kira/eser özel hükümleri) ve "cure period" (düzeltme süresi) denetlenir.
4. **Otomatik yenileme/erken çıkış**: Sessiz yenileme, asgari taahhüt süresi ve erken fesih cezası (cezai şart denetimine bağlanır) müvekkil aleyhineyse işaretlenir.
5. **Sona erme sonuçları**: İade, hesap kapama, lisans/erişim sonlandırma, geçiş desteği; ayakta kalan hükümler (survival): gizlilik, rekabet yasağı (ölçülülük: süre-yer-konu), sorumluluk, uyuşmazlık.
6. **İspat/usul**: Fesih sebebini ve usulüne uygunluğunu fesheden taraf ispatlar; haksız fesih müspet zarar doğurabilir.

## Çıktı modülleri
- Fesih hakları denge tablosu (kim, hangi sebeple, hangi usulle).
- Bildirim ve düzeltme süresi (cure) lafız önerisi.
- Survival (ayakta kalan hüküm) ve çıkış yükümlülükleri kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

