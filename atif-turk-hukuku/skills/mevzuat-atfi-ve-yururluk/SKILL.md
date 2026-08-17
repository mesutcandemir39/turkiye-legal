---
argument-hint: ''
description: Bir kanun, kararname veya yönetmelik hükmüne atıf yapılırken; madde-fıkra-bent
  doğruluğunu, hükmün güncel/mülga/değişik olup olmadığını ve yürürlük tarihini denetlemek
  için kullanılır.
name: mevzuat-atfi-ve-yururluk
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


# Mevzuat Atfı ve Yürürlük Kontrolü

## Görev
Bir mevzuat hükmüne, doğru madde/fıkra/bent ile ve yürürlük durumu teyit edilmiş biçimde atıf yapmak; mülga veya değişmiş hükme dayanarak hatalı sonuç üretmeyi önlemek.

## Soğuk başlangıç (intake)
- Hangi kanun/kararname/yönetmelik, hangi madde-fıkra-bent?
- Hüküm güncel mi, yoksa değişmiş/yürürlükten kalkmış olabilir mi?
- Olayın tarihi ile hükmün yürürlük tarihi uyumlu mu (zaman bakımından uygulama)?
- Bu bir özel kanun mu, genel kanun mu (lex specialis ilişkisi var mı)?

## Denetim şeması
1. **Tam atıf** — Kanun adı veya numarası + madde + fıkra + bent: "TBK m.49/1", "HMK m.119/1-(e)", "İİK m.67/1". Kısaltma standardı tutarlı kullanılır (TMK 4721, TBK 6098, TTK 6102, TCK 5237, CMK 5271, HMK 6100, İYUK 2577, İİK 2004).
2. **Yürürlük/değişiklik** — mevzuat.gov.tr karşılaştırmalı/güncel metni esas alınır; "Mülga" veya "(Değişik: …)" ibaresi kontrol edilir. Eski metne dayanılıyorsa açıkça belirtilir.
3. **Zaman bakımından uygulama** — Olay tarihi ile hüküm tarihi çatışıyorsa hangi kanunun uygulanacağı (geçmişe etkisizlik, derhal uygulama, geçiş hükmü; ceza için lehe kanun, TCK m.7) ayrıca değerlendirilir.
4. **Hiyerarşi ve yetki** — Yönetmelik/tebliğ kanuna aykırı olamaz (Anayasa m.124); alt düzenleme kanunsuz hak/yük getiremez. Atıfta üst normla uyum denetlenir.
5. **Yollama zinciri** — Madde başka maddeye yolluyorsa (örn. "… hükümleri kıyasen uygulanır") zincir izlenir; atıf, asıl uygulanacak hükme yapılır.
6. **Yanlış numara riski** — Madde numarası benzer kanunlarla (örn. eski-yeni TBK/BK) karışabilir; numara daima güncel kanuna göre teyit edilir.

## Çıktı modülleri
- Tam mevzuat atfı (madde/fıkra/bent).
- Yürürlük durumu: güncel / değişik / mülga + tarih.
- Zaman bakımından uygulama notu (gerekirse).
- Hiyerarşi/yollama uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

