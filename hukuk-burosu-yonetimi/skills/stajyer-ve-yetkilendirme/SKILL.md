---
argument-hint: ''
description: Stajyer avukat veya yardımcı personele görev verirken, yetki sınırlarını
  ve sorumluluk-gizlilik çerçevesini belirlerken ve süpervizyon kurarken kullanılır.
name: stajyer-ve-yetkilendirme
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Stajyer Yönetimi ve Görev Yetkilendirmesi

## Görev
Stajyer avukat ve yardımcı personele verilecek görevleri meslek hukuku sınırları içinde tanımlamak; gizlilik ve süpervizyon çerçevesini kurmak; büronun sorumluluğunu yönetmek.

## Soğuk başlangıç (intake)
1. Görev kime verilecek (stajyer avukat / sekreter / paralegal) ve niteliği ne?
2. Görev bağımsız temsil mi gerektiriyor yoksa hazırlık/araştırma işi mi?
3. Stajyerin yetki belgesi/durumu ve gözetimi sağlayacak avukat kim?
4. Görevde gizli müvekkil bilgisi ve çıkar çatışması riski var mı?

## Denetim şeması
1. **Yetki sınırı (1136 m.23-26 staj rejimi)**: Stajyer avukatın yetkileri kanunla sınırlıdır; belirli işler yanında bulunduğu avukatın gözetiminde yürütülür, bağımsız ve sınırsız temsil söz konusu değildir. Görev bu sınıra göre tanımlanır.
2. **Süpervizyon**: Her görev için sorumlu/gözeten avukat atanır; çıktı kalite kontrolünden geçer (özen — TBK m.506).
3. **Gizlilik (1136 m.36)**: Stajyer ve personel sır saklama yükümlülüğü kapsamındadır; yazılı gizlilik taahhüdü ve erişim sınırlaması (KVKK m.12) uygulanır.
4. **Çıkar çatışması**: Görevlendirme öncesi ilgili kişinin o dosyada çatışması olmadığı teyit edilir (1136 m.38).
5. **Sorumluluk**: Stajyer/personel hatasının büroyu bağladığı bilinciyle, riskli işlerde çift kontrol konur.
6. **Ara sonuç**: Yetkiye uygun görev + atanmış süpervizör + gizlilik + çatışma teyidi sağlanınca görev verilebilir.

## Çıktı modülleri
- Görev tanım ve yetki sınırı notu.
- Gizlilik/veri erişim taahhüdü taslağı.
- Süpervizyon ve kontrol akışı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

