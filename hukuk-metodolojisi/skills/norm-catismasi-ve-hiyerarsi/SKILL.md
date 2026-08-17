---
argument-hint: ''
description: Aynı olaya birden fazla kural uygulanabiliyor ve bunlar farklı sonuçlar
  veriyorsa; özel-genel, önceki-sonraki, üst-alt norm çatışmasını ve Anayasa/AİHS
  üstünlüğünü çözmek için kullanılır.
name: norm-catismasi-ve-hiyerarsi
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
  - ad: Türk Medeni Kanunu
    madde: '1'
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Norm Çatışması ve Hiyerarşi Çözümü

## Görev
Bir olaya uygulanabilir görünen rakip normlar arasında geçerli/öncelikli olanı, normlar hiyerarşisi ve çatışma kuralları aracılığıyla belirlemek.

## Soğuk başlangıç (intake)
- Çatışan normlar hangileri (kanun-kanun, kanun-tüzük/yönetmelik, kanun-Anayasa, kanun-AİHS)?
- Normlardan biri diğerine göre daha özel mi, daha yeni mi, daha üst mü?
- Konu temel hak alanına giriyor mu (AİHS m.90/5 devreye girer mi)?
- Çatışma görünüşte mi (yorumla giderilebilir) yoksa gerçek mi?

## Denetim şeması
1. **Önce yorumla uzlaştır** — Görünüşteki çatışmalar çoğu kez sistematik/amaçsal yorumla giderilir; iki norm farklı kapsamları düzenliyor olabilir. Gerçek çatışma ancak uzlaştırma imkânsızsa kabul edilir.
2. **Hiyerarşi (lex superior derogat inferiori)** — Anayasa (m.11: bağlayıcı ve üstün) > kanun > Cumhurbaşkanlığı kararnamesi (alanına göre) > yönetmelik. Alt norm üst norma aykırıysa uygulanmaz; idari düzenleme için idari yargıda iptal/itiraz yolu açıktır.
3. **Anayasaya uygun yorum** — Kanun birden çok okumaya açıksa Anayasa'ya uygun olanı seçilir; kanunun Anayasa'ya aykırılığı ciddi ise itiraz yoluyla AYM'ye başvuru (Anayasa m.152) düşünülür. AYM kararları bağlayıcıdır (m.153).
4. **Milletlerarası sözleşme üstünlüğü** — Anayasa m.90/5: usulüne göre yürürlüğe konmuş temel hak ve özgürlüklere ilişkin milletlerarası sözleşmeler (özellikle AİHS) ile kanunlar çatışırsa sözleşme esas alınır.
5. **Özel-genel (lex specialis derogat generali)** — Özel hüküm, genel hükmü kendi alanında bertaraf eder; genel hüküm boşlukta tamamlayıcı kalır.
6. **Önceki-sonraki (lex posterior derogat priori)** — Aynı düzeydeki normlarda sonraki, önceki ile çatıştığı ölçüde onu zımnen ilga eder; ancak sonraki genel, önceki özeli kural olarak ilga etmez.

## Çıktı modülleri
- Çatışan normların ve sonuçların tablosu.
- Uygulanan çatışma kuralı zinciri.
- Anayasa/AİHS denetimi gerekiyorsa yol önerisi.
- Sonuç + `[DOĞRULANMADI]` AYM/Yargıtay künyesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

