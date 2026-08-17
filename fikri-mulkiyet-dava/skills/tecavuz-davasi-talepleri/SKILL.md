---
argument-hint: ''
description: Tecavüzün tespiti, durdurulması, giderilmesi, ürünlere el konulması,
  imha ve kararın ilanı taleplerini SMK m.149 ve FSEK m.66-70 çerçevesinde doğru ve
  eksiksiz kurgulamak gerektiğinde kullanılır.
name: tecavuz-davasi-talepleri
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tecavüz Davası ve Talep Mimarisi

## Görev
Tecavüz davasının talep sonucunu eksiksiz, infaza elverişli ve madde dayanaklı biçimde kurmak; sınai (SMK) ve telif (FSEK) rejimine göre talep paketini ayarlamak.

## Soğuk başlangıç (intake)
- Hangi hak ihlal edildi ve ihlal devam ediyor mu?
- Talep sadece durdurma mı, tazminat da var mı, imha/ilan isteniyor mu?
- Karşı tarafın elinde tecavüz ürünü/üretim aracı var mı?
- Manevi tazminat (itibar zedelenmesi) gündemde mi?

## Denetim şeması
1. Tespit ve durdurma: Tecavüzün tespiti, durdurulması ve giderilmesi (SMK m.149/1-a,b,c; FSEK m.66 ref', m.69 men'). Talep, fiili ve sonuçlarını kapsayacak şekilde somutlaştırılır.
2. El koyma ve imha: Tecavüz oluşturan ürünlere, bunların üretiminde münhasıran kullanılan araç/cihazlara el konulması ve imhası (SMK m.149/1-ç,d; m.149/1-e mülkiyetin tanınması). Ölçülülük gözetilir.
3. Tazminat: Maddi tazminat (yoksun kalınan kazanç) ve istenirse itibar tazminatı (SMK m.150) ile manevi tazminat (TBK m.58 atfıyla). FSEK'te m.68 (bedelin üç katına kadar) ve m.70 (maddi-manevi) seçenekleri.
4. Hesaplama yöntemi: SMK m.151 — davacının seçimine göre (a) lisans verseydi elde edeceği gelir, (b) tecavüz edenin elde ettiği kazanç, (c) sözleşme yapılsaydı ödenecek lisans bedeli. Seçim bilinçli yapılır; defter-kayıt ibrazı talep edilir.
5. İlan: Masrafı tecavüz edene ait olmak üzere hükmün ilanı (SMK m.149/1-f). Haklı menfaat şartı.
6. İspat yükü: Tecavüz ve zarar davacıda; tecavüz edenin kazancı için defterlerin sunulması ve bilirkişi. Ara sonuç: tedbir + esas + tazminat birlikte ama ayrı ayrı gerekçelendirilir.

## Çıktı modülleri
- Talep sonucu (numaralı, infaza elverişli) taslağı.
- Tazminat seçeneği ve hesap yöntemi notu (SMK m.151).
- Manevi tazminat ve ilan gerekçesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

