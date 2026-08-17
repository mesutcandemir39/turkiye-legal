---
argument-hint: ''
description: Tarife uygulaması, dağıtım/sistem kullanım bedelleri, son kaynak tedarik
  tarifesi, dengeleme ve uzlaştırma (DUY) alacak-borç uyuşmazlıkları ele alındığında
  kullanılır.
name: tarife-uzlastirma-piyasa
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
  - ad: Elektrik Piyasası Kanunu
    numara: '6446'
    tur: kanun
  - ad: Mühendislik ve Mimarlık Meslek Kanunu
    numara: '4646'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tarifeler, Dengeleme ve Uzlaştırma

## Görev
Tarife ve uzlaştırma kaynaklı bedel/alacak uyuşmazlıklarını çözmek; EPDK tarife metodolojisi ile EPİAŞ uzlaştırma verisini birlikte değerlendirerek doğru tutarı ve itiraz yolunu belirlemek.

## Soğuk başlangıç (intake)
1. Hangi bedel tartışmalı: dağıtım, iletim, sistem kullanım, son kaynak, dengeleme?
2. Müvekkil üretici mi, tedarikçi mi, serbest/serbest olmayan tüketici mi?
3. Tartışmalı fatura/uzlaştırma dönemi ve tutar nedir?
4. EPİAŞ/EPDK nezdinde itiraz/düzeltme başvurusu yapıldı mı?

## Denetim şeması
1. **Tarife dayanağı**: 6446 m.17 ve ilgili Tarifeler Yönetmelikleri — tarife türleri (bağlantı, iletim, dağıtım, perakende satış, son kaynak) ve Kurul onaylı tarifelerin bağlayıcılığı. Ara sonuç: uygulanan bedel onaylı tarifeye uygun mu.
2. **Son kaynak tedarik tarifesi**: 6446'da 6719 sayılı Kanun değişikliği sonrası rejim; belirli tüketim eşiği üstü tüketicilere uygulanan SKTT esasları doğru tüketici grubuna uygulanmış mı.
3. **Dengeleme ve uzlaştırma**: Dengeleme ve Uzlaştırma Yönetmeliği (DUY) — gün öncesi/dengeleme güç piyasası, dengesizlik tutarları, uzlaştırma hesapları. Tutar EPİAŞ verisiyle ve bilirkişi hesabıyla doğrulanır.
4. **İspat ve veri**: Sayaç/ölçüm verisi, uzlaştırmaya esas veri ve EPİAŞ bildirimleri esas delildir; ispat yükü bedeli talep/itiraz eden taraftadır.
5. **İtiraz yolu**: Önce EPİAŞ/ilgili tüzel kişiye düzeltme/itiraz; EPDK işlemi söz konusuysa İYUK m.7 süresinde idari dava; salt özel hukuk alacağı ise adli yargı/tahkim ayrımı yapılır.

## Çıktı modülleri
- Tarife/uzlaştırma uygunluk ve fark hesabı.
- İtiraz/düzeltme başvuru taslağı.
- Dava/ tahkim için tutar ve delil dizini.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

