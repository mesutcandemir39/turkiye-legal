---
argument-hint: ''
description: Dağınık bir dava dosyasından künye, talep, taraflar ve aşamayı tek sayfalık
  yapılandırılmış özete dönüştürmek gerektiğinde; yeni gelen veya devralınan dosyaya
  hızlı hâkim olmak için kullan.
name: dosya-ozeti-cikarma
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dosya Özeti Çıkarma

## Görev
Bir dava dosyasının dağınık evrakını; künye, taraflar, talep, aşama ve sıradaki iş kalemlerini içeren tek sayfalık, Excel'lenebilir bir özete indirgemek. Amaç dosyaya 5 dakikada hâkim olmayı sağlamaktır.

## Soğuk başlangıç (intake)
- Dosya hangi yargı koluna ait: hukuk (HMK), ceza (CMK), icra (İİK), idari (İYUK)?
- Elinde hangi evrak var (dava/iddianame, cevap, bilirkişi raporu, tensip, ara karar, UYAP dökümü)?
- Mahkeme ve esas numarası ile tarafların adları belli mi?
- Özet kimin için: hâkim olmak için mi, müvekkile rapor için mi, devir için mi?

## Denetim şeması
1. Künye kalemi: mahkeme adı, esas no, dava türü, dava tarihi, talep sonucu. HMK m.119 zorunlu unsurları (taraflar, talep, vakıalar, hukuki sebep, deliller) dosyada mevcut mu, eksik unsur var mı denetle. Eksikse [doldurulacak].
2. Taraf kalemi: davacı/davalı (ceza dosyasında şüpheli-sanık-müşteki-katılan), vekilleri, tebligat adresleri. Vekâletname dosyada mı; yoksa eksik listesine yaz.
3. Talep ve dayanak: dava dilekçesindeki talep sonucu ile hukuki sebepleri evraktan birebir aktar; yorum ekleme.
4. Aşama tespiti: dilekçeler aşaması mı, ön inceleme (HMK m.137) mi, tahkikat mı, istinaf mı? Son işlem tarihinden çıkar.
5. Ara sonuç: bir sonraki kritik adım (duruşma, cevap süresi, rapora itiraz) ve son günü ile birlikte not et; her veri kaynağına (evrak + tarih + sayfa) bağlanır. Belgede olmayan bilgi uydurulmaz.

## Çıktı modülleri
- Tek sayfalık künye tablosu (mahkeme, esas no, taraflar, talep, aşama).
- Sıradaki iş kalemleri listesi (ne, ne zaman, dayanak madde).
- Eksik evrak ve [doldurulacak] alanları listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

