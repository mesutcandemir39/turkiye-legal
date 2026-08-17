---
argument-hint: ''
description: Sözleşmede kararlaştırılan ceza koşulu, pey akçesi veya cayma parasının
  türü, geçerliliği, indirilmesi ve asıl borçla ilişkisi değerlendirilirken kullanılır.
name: cezai-sart-ve-teminat
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


# Cezai Şart, Bağlanma Parası ve Cayma Parası

## Görev
Sözleşmedeki ceza koşulunu (cezai şart) türüne göre nitelendirmek, geçerliliğini ve fahiş cezanın indirilmesini değerlendirmek; bağlanma/cayma parasından ayırmak.

## Soğuk başlangıç (intake)
- Sözleşmede ceza/tazminat kaydı nasıl düzenlenmiş?
- Alacaklı hem asıl edimi hem cezayı mı istiyor, yoksa seçimlik mi?
- Ceza miktarı edime göre aşırı/fahiş mi?
- Borçlu tacir mi (indirim talebi sınırı için)?

## Denetim şeması
1. Cezai şart türleri: TBK m.179 — (a) seçimlik cezai şart: alacaklı ya ifayı ya cezayı ister; (b) ifaya eklenen cezai şart: gecikme veya belirli yerde ifa için, hem ifa hem ceza istenebilir; (c) dönme cezası (m.179/f.3): borçlu cezayı ödeyerek sözleşmeden dönebilir.
2. Asıl borca bağlılık: m.182 — geçersiz asıl borçta ceza da istenemez; ceza asıl borcun fer'idir. Asıl alacak zamanaşımına uğrarsa ceza da etkilenir.
3. Aşan zarar: Alacaklı cezayı aşan zararını ancak borçlunun kusurunu ispatla isteyebilir (m.180/f.2).
4. Fahiş cezanın indirilmesi: m.182/f.3 — hâkim aşırı bulduğu cezayı resen indirir. Ancak tacirler bakımından TTK m.22 — tacir, cezanın fahiş olduğu gerekçesiyle indirim isteyemez (sınırlı istisnalar).
5. Bağlanma parası (pey akçesi) ve cayma parası: m.177-178 — bağlanma parası sözleşmenin yapıldığının kanıtıdır, kural olarak ifada mahsup edilir; cayma parası ise dönme hakkının karşılığıdır. Nitelendirme sonuçları değiştirir.
6. İspat yükü: Cezanın kararlaştırıldığını alacaklı; fahişliği ve indirim sebebini borçlu ileri sürer.

## Çıktı modülleri
- Ceza koşulu nitelendirme tablosu (tür ve sonuç).
- Fahiş ceza/indirim analizi (tacir ayrımıyla).
- Sözleşmeye uygun ceza maddesi taslağı önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

