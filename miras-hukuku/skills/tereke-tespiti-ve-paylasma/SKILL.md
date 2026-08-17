---
argument-hint: ''
description: Terekenin envanterini çıkarmak, mirasçılık belgesi almak ve elbirliği
  mülkiyetini sona erdirip paylaşmayı veya ortaklığın giderilmesini sağlamak gerektiğinde;
  iştirak halinin çözümü, paylaşma sözleşme
name: tereke-tespiti-ve-paylasma
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
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tereke Tespiti, Mirasçılık Belgesi ve Paylaşma

## Görev
Terekeyi tespit ve koruma altına almak, mirasçılık belgesini temin etmek ve mirasçılar arasındaki elbirliği mülkiyetini paylaşma sözleşmesi veya ortaklığın giderilmesi davasıyla tasfiye etmek (TMK m.640-676).

## Soğuk başlangıç (intake)
- Mirasçılar belli mi? Mirasçılık belgesi (veraset ilamı) alındı mı?
- Tereke kalemleri neler? (taşınmaz, banka, araç, şirket payı, alacak)
- Mirasçılar paylaşmada anlaşıyor mu, anlaşmazlık mı var?
- Taşınmaz fiilen bölünebilir mi, yoksa satış mı gerekir?
- Denkleştirilecek sağlararası kazandırma var mı (m.669)?

## Denetim şeması
1. **Mirasçılık belgesi (m.598):** Sulh hukuk mahkemesinden veya noterden; çekişme varsa mahkeme. Belge mirasçı sıfatını ve payları gösterir, aksi ispatlanana dek karine teşkil eder.
2. **Tereke tespiti/koruma (m.589-592):** Sulh hukuk mahkemesinden defter tutma, mühürleme, terekenin yönetimi; mirasçı belirsizse temsilci atanması.
3. **Elbirliği mülkiyeti (m.640, m.701 vd.):** Miras ortaklığı elbirliği mülkiyetidir; mirasçılar terekeye birlikte malik olup birlikte tasarruf ederler. Oybirliği gerekir.
4. **Paylaşmaya geçiş (m.642-647):** Her mirasçı paylaşmayı isteyebilir (m.642); sözleşmeyle paylaşma yazılı şekle tabidir (m.676). Anlaşma sağlanamazsa ortaklığın giderilmesi davası açılır.
5. **Ortaklığın giderilmesi (m.642 vd., HMK m.4 — sulh hukuk):** Önce aynen taksim araştırılır; mümkün değilse satış suretiyle giderme. Denkleştirme talepleri burada karşılanır (m.669).
6. **Ara sonuç:** mirasçılık belgesi + envanter + paylaşma yolu (sözleşme/dava). İspat: tapu, banka, sicil kayıtları; pay kesirleri belge ile (m.6).

## Çıktı modülleri
- Mirasçılık belgesi talebi dilekçesi
- Tereke envanteri tablosu (aktif/pasif, değer)
- Paylaşma sözleşmesi taslağı (yazılı şekilli)
- Ortaklığın giderilmesi (izale-i şuyu) dava dilekçesi taslağı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

