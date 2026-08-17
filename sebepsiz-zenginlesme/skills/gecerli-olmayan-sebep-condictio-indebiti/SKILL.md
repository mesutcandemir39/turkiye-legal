---
argument-hint: ''
description: Borç olmadığı halde veya geçersiz bir sözleşmeye dayanarak yapılan ödeme/edimin
  geri istenmesi söz konusu olduğunda; hata ile ödeme ve isteyerek ödeme ayrımını
  çözmek için kullanılır.
name: gecerli-olmayan-sebep-condictio-indebiti
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


# Geçerli Olmayan Sebep — Borçlanılmayanın İfası

## Görev
Hiç var olmayan veya geçersiz/iptal edilmiş bir borca dayanarak yapılan edimin iadesini TBK m.77/2 ve m.78 çerçevesinde denetlemek; "yanılarak ödeme" ile "borçlu olmadığını bilerek ödeme" ayrımını netleştirmek, çünkü ikincisi iadeyi kapatır.

## Soğuk başlangıç (intake)
- Ödeme/edim hangi borca dayanıyordu; o borç hiç var mıydı, geçersiz miydi, iptal mi edildi?
- Ödeyen, ödeme anında borçlu olmadığını biliyor muydu, yanılarak mı ödedi?
- Çifte ödeme, fazla ödeme, baştan geçersiz sözleşme gibi tipik bir durum var mı?
- Borç zamanaşımına uğramış mıydı veya ahlaki bir ödev miydi?

## Denetim şeması
1. **Geçersiz/yok borç tespiti.** Sözleşme kesin hükümsüz (TBK m.27), iptal edilmiş (irade sakatlığı m.39), şekil eksik (m.12) veya borç hiç doğmamışsa, ona dayalı ifa sebepsizdir (m.77/2).
2. **Yanılarak ödeme şartı (m.78/1).** Borçlanmadığı şeyi ifa eden, ancak **yanılarak** (borçlu olduğunu sanarak) ödediğini ispat ederse geri isteyebilir. Bu kuruma özgü ek ispat yüküdür.
3. **İsteyerek ödeme engeli (m.78/1).** Ödeyen, ödeme anında borçlu olmadığını **biliyorsa**, ödediğini geri isteyemez (bilinçli ifa bağışlama/ibra gibi yorumlanır). Baskı altında/ihtirazi kayıtla ödeme bu engelin dışındadır.
4. **İstisnalar (m.78/2).** Zamanaşımına uğramış borcun ifası ve ahlaki ödevin yerine getirilmesi geri istenemez; bunlar geçerli sebep sayılır.
5. **İade kapsamı.** Para ise anapara; semere/faiz için zenginleşenin iyiniyeti m.79'a göre belirlenir. Geçersiz sözleşmede karşılıklı ifalar varsa her iki tarafın iadesi birlikte (tasfiye) ele alınır.
6. **İspat ve ara sonuç.** Borcun yokluğunu ve yanılgıyı ödeyen; bilerek ödendiğini iade borçlusu ileri sürer ve ispatlar. Ara sonuç: iade hakkı var/yok + kapsam + faiz başlangıcı.

## Çıktı modülleri
- Geçersizlik + yanılgı altlama notu.
- İade talebi/ihtarname taslağı (ihtirazi kayıt vurgusuyla).
- İsteyerek ödeme engeli risk değerlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

