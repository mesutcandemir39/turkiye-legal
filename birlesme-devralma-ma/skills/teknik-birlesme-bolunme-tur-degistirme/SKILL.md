---
argument-hint: ''
description: TTK m.134 vd. kapsamında devralma veya yeni kuruluş yoluyla birleşme,
  TTK m.159 bölünme ve TTK m.180 tür değiştirme işlemlerinin belge, organ kararı ve
  alacaklı koruma adımlarını yürütmek için kullanı
name: teknik-birlesme-bolunme-tur-degistirme
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  - ad: Rekabetin Korunması Hakkında Kanun
    numara: '4054'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Teknik Birleşme, Bölünme ve Tür Değiştirme

## Görev
TTK'daki yapısal değişiklik işlemlerinin (birleşme/bölünme/tür değiştirme) zorunlu belge ve organ kararı adımlarını ve alacaklı/ortak koruma mekanizmalarını uygulamak.

## Soğuk başlangıç (intake)
- İşlem birleşme mi, bölünme mi (tam/kısmi), tür değiştirme mi?
- Taraf şirketlerin türleri ve büyüklükleri ne?
- Küçük ölçekli şirketler için kolaylaştırılmış usul (TTK m.155-156) uygulanabilir mi?
- Ayrılma akçesi veya pay değişim oranı tartışmalı mı?

## Denetim şeması
1. **Birleşme**: TTK m.136 türler arası birleşme izni; birleşme sözleşmesi (TTK m.145-146), birleşme raporu (TTK m.147), inceleme hakkı (TTK m.149), genel kurul onayı (TTK m.151) ve gerekli nisaplar.
2. **Alacaklı koruması**: TTK m.157 — alacaklılara çağrı ve teminat talebi hakkı; m.158 ortakların kişisel sorumluluğunun devamı.
3. **Pay sahibi koruması**: Pay/ortaklık haklarının korunması (TTK m.140), ayrılma akçesi (TTK m.141); denkleştirme davası (TTK m.191).
4. **Bölünme**: TTK m.159 tam/kısmi bölünme; bölünme sözleşmesi/planı (TTK m.167), m.169 raporu; m.175 sorumluluk (müteselsil).
5. **Tür değiştirme**: TTK m.180-182; tür değiştirme planı (TTK m.185) ve raporu (TTK m.186); ortakların paylarının korunması (TTK m.183).
6. **Tescil ve ilan**: Ticaret siciline tescille hüküm doğar; külli halefiyet sonucu.
7. **İspat/dayanak**: Değişim oranı bilirkişi/değerleme raporu ile desteklenir.

## Çıktı modülleri
- İşlem türüne göre belge ve organ kararı kontrol listesi
- Birleşme/bölünme/tür değiştirme sözleşmesi-planı iskeleti
- Alacaklı çağrı metni ve süre takvimi
- Tescil dosyası içerik listesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

