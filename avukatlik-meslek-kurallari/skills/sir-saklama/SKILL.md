---
argument-hint: ''
description: Avukatın sır saklama yükümü, kapsamı, istisnaları, tanıklıktan çekinme
  ve büroda arama-elkoyma rejimi söz konusu olduğunda; sır ihlali riskinin değerlendirilmesinde
  kullanılır.
name: sir-saklama
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
  - ad: Avukatlık Kanunu
    numara: '1136'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Mesleki Sır ve Sır Saklama Yükümlülüğü

## Görev
Avukatın sır saklama yükümlülüğünün kapsamını, istisnalarını ve usul güvencelerini somut
olaya uygulamak; sır ihlali riskini değerlendirmek.

## Soğuk başlangıç (intake)
1. Sır, müvekkilden mi öğrenildi, yoksa görev dolayısıyla başkasından mı?
2. İfşa kime, hangi amaçla yapılacak (mahkeme, baro, üçüncü kişi, medya)?
3. Müvekkilin açık muvafakati var mı?
4. Büroda/dosyada arama veya elkoyma tehdidi mi söz konusu?

## Denetim şeması
1. **Yükümlülüğün kaynağı ve kapsamı.** Avukat, kendisine tevdi edilen veya mesleğin
   icrası dolayısıyla öğrendiği hususları açığa vuramaz (Av. K. m.36/1, TBB Meslek Kuralları
   m.37). Yükümlülük müvekkilin ölümü/azilden sonra da sürer ve büro çalışanlarını da kapsar.
2. **Tanıklıktan çekinme.** Avukat bu konularda tanıklıktan çekinebilir; rızası olsa dahi
   sır sahibi izin vermedikçe tanıklık edemez (Av. K. m.36/2; CMK m.46; HMK m.249-250
   çerçevesinde). Ara sonuç: çekinme hak mı, yükümlülük mü? Sır sahibinin izni belirleyicidir.
3. **İstisnalar.** Müvekkilin açık izni; avukatın kendisine yöneltilen suçlama veya ücret
   alacağı davasında savunma için zorunlu açıklama; kanunen bildirim yükümlülüğü (örn. 5549
   sayılı Kanun kapsamı, ancak avukatın salt savunma faaliyeti için sınırları gözetilir).
   İstisna dar yorumlanır; ifşa, amaçla orantılı ve asgari olmalıdır.
4. **Arama-elkoyma rejimi.** Avukat bürosunda arama, ancak mahkeme kararıyla ve kararda
   belirtilen olayla sınırlı; arama sırasında baro başkanı/temsilcisi hazır bulunur; el
   konulmak istenen şeyin sır kapsamında olduğu ileri sürülürse o şey mühürlenip hâkime
   gönderilir (CMK m.130). İspat yükü: sır kapsamı iddiasını ileri süren değerlendirme için
   somutlaştırmalıdır; nihai karar sulh ceza hâkimliğindedir.
5. **İhlalin sonucu.** Sır ihlali disiplin suçudur ve TCK m.239 (ticari sır/müşteri sırrı)
   ile ceza sorumluluğu doğurabilir; ayrıca müvekkile karşı tazminat sorumluluğu (TBK m.49,
   m.502 vd.).

## Çıktı modülleri
- İfşanın hukuka uygun olup olmadığına dair gerekçeli değerlendirme.
- Arama/elkoyma anında uygulanacak adım listesi (baro temsilcisi, mühürleme, hâkim).
- Müvekkil bilgilendirme/muvafakat metni taslağı ([doldurulacak] yer tutucularla).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

