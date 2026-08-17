---
argument-hint: ''
description: Karşı taraf markayı uzun süredir kullanmıyorsa veya size karşı kullanmama
  itirazı/def'i ileri sürüldüyse; beş yıllık ciddi kullanım koşulu ve ispat yükünü
  m.9-m.19/2 üzerinden yönetmek için kullanılır
name: kullanmama-defi-ve-ispati
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
  version: 0.1.0
user-invocable: true
---


# Kullanmama Def'i ve Kullanımın İspatı

## Görev
Markanın "kullan ya da kaybet" ilkesini işletmek: tescilden sonra beş yıl içinde Türkiye'de ciddi biçimde kullanılmayan markanın itiraz/dava dayanağı olmasını engellemek (m.19/2 def'i; iptal için m.26/1-a, m.9). İspat yükü kural olarak marka sahibindedir.

## Soğuk başlangıç (intake)
- Dayanak marka kaç yıldır tescilli (beş yıl doldu mu)?
- Hangi mal/hizmette kullanım iddia ediliyor?
- Kullanım Türkiye'de, ciddi ve tescil edildiği biçimde mi?
- Kullanmama için haklı sebep var mı (idari engel, ithalat yasağı)?

## Denetim şeması
1. **Beş yıllık süre.** Tescil tarihinden (veya son ciddi kullanımdan) itibaren kesintisiz beş yıl kullanmama aranır (m.9/1).
2. **Def'i hakkı (m.19/2).** Yayına itirazda, itiraz dayanağı marka beş yıldır tescilliyse başvuru sahibi kullanım ispatı isteyebilir; ispatlanamazsa itiraz o markaya dayanılarak reddedilir.
3. **Ciddi kullanım ölçütü.** Pazarda gerçek ticari amaçla, markanın esas işlevine uygun, somut ve süreklilik gösteren kullanım; sırf hakkı korumak için sembolik kullanım yeterli değildir.
4. **Kapsam.** Kullanım, tescilli mal/hizmetin hangileri için ispatlandıysa koruma o kapsamla sınırlanır; kısmî kullanmama kısmî iptal/etkisizlik doğurur.
5. **Ayırt ediciliği değiştirmeyen kullanım.** Markanın ayırt edici karakterini değiştirmeyen farklı unsurlarla kullanım da kullanım sayılır (m.9/2).
6. **Haklı sebep.** Marka sahibinin iradesi dışındaki engeller (ruhsat bekleme, ithalat yasağı) kullanmamayı mazur gösterebilir.

## Çıktı modülleri
- Beş yıllık süre ve kullanım dönemi cetveli.
- Ciddi kullanım delil listesi (fatura, katalog, reklam, ambalaj — tarihli).
- Def'i/iptal talebi taslağı ve ispat yükü notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

