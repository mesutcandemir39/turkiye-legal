---
argument-hint: ''
description: Bir sözleşmenin geçerli kurulup kurulmadığı, şekil şartına tabi olup
  olmadığı veya tek taraflı dayatılan standart maddelerin denetimi söz konusu olduğunda
  kullanılır.
name: sozlesmenin-kurulusu-ve-sekil
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


# Sözleşmenin Kurulması, Şekil ve Genel İşlem Koşulları

## Görev
Bir sözleşmenin kurulup kurulmadığını, kuruluş anını, şekle uygunluğunu ve standart/dayatılmış maddelerin geçerliliğini denetlemek.

## Soğuk başlangıç (intake)
- Öneri ve kabul nasıl, ne zaman ve hangi içerikle gerçekleşti?
- Sözleşme bir şekle tabi mi (taşınmaz satışı, kefalet, vekâletten azil)?
- Metin matbu/standart mı; karşı taraf maddeleri müzakere edebildi mi?
- Tarafların esaslı noktalarda tam uyuşması var mı?

## Denetim şeması
1. Öneri-kabul: TBK m.1-2; esaslı noktalarda uyuşma şart, ikincil noktalar boş bırakılırsa hâkim doldurur (m.2/f.2). Süreli/süresiz öneri ve bağlayıcılık (m.3-5).
2. Şekil: Kural serbestî (m.12). Kanunen öngörülen şekil geçerlilik şartıdır; aksi hâlde kesin hükümsüzlük. Taşınmaz satışı resmî şekle (TMK m.706, Tapu K.), kefalet yazılı + el yazısı miktar/tarih (m.583), genel vekâletten azil serbest. İradi şekil kararlaştırılmışsa adi yazılı varsayılır (m.17).
3. Genel işlem koşulları: m.20-25. Yazılmamış sayılma (beklenmeyen/şaşırtıcı kayıt, m.21), yorumda aleyhe yorum, değiştirme yasağı (m.24), dürüstlüğe aykırı içerik denetimi (m.25). Tüketici işlemlerinde 6502 s.K. m.5 ek koruma.
4. Muvazaa: Görünürdeki ve gizli işlem ayrımı (TBK m.19); nispi muvazaada gizli işlem geçerli şekil şartını taşıyorsa ayakta kalır.
5. İspat yükü: Sözleşmenin kurulduğunu iddia eden ispatlar; senede karşı senetle ispat kuralı (HMK m.201) ve şekil şartına tabi işlemlerde tanık sınırı.
6. Ara sonuç: Sözleşme geçerli kuruldu mu, hangi maddeler yazılmamış sayılır?

## Çıktı modülleri
- Kuruluş analizi ve şekil uygunluk tablosu.
- Yazılmamış/geçersiz GİK maddeleri listesi.
- Eksik veya riskli kayıtlar için düzeltme önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

