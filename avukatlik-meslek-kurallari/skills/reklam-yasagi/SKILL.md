---
argument-hint: ''
description: Avukatın web sitesi, sosyal medya, tabela, ilan, iş takipçiliği ve tanıtım
  faaliyetlerinin meslek kurallarına uygunluğu değerlendirildiğinde kullanılır.
name: reklam-yasagi
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


# Reklam Yasağı ve Mesleki Tanıtım Sınırları

## Görev
Bir tanıtım/iletişim faaliyetinin reklam yasağı ve meslek kurallarına uygun olup olmadığını
saptamak; uyumlu hale getirmek.

## Soğuk başlangıç (intake)
1. Mecra ne (tabela, web sitesi, sosyal medya, gazete/ilan, rehber, arama motoru reklamı)?
2. İçerik hangi bilgileri veriyor ( unvan, uzmanlık iddiası, başarı/oran, fiyat, müvekkil adı)?
3. İş sağlama/aracı kullanma veya iş takipçiliği unsuru var mı?
4. Karşılaştırmalı/abartılı ifade veya müvekkil referansı içeriyor mu?

## Denetim şeması
1. **Yasağın temeli.** Avukat iş elde etmek için reklam sayılabilecek her türlü teşebbüs ve
   harekette bulunamaz (Av. K. m.55; TBB Avukatlık Meslek Kuralları m.7-8; TBB Reklam Yasağı
   Yönetmeliği). Amaç, mesleğin onuru ve haksız rekabetin önlenmesidir.
2. **İzin verilen bilgilendirme.** Ad-soyad, unvan, iletişim, çalışma alanları (uzmanlık
   "iddiası" değil bilgilendirme düzeyinde), büro bilgileri ölçülü biçimde verilebilir.
   Ara sonuç: içerik "bilgilendirme" sınırında mı, yoksa "iş celbi/reklam" düzeyine mi geçti?
3. **Yasak içerik kalıpları.** Başarı oranı/kazanılmış dava reklamı, müvekkil adı/işi ifşası
   (sır yükümü m.36 ile çakışır), karşılaştırmalı üstünlük, fiyat reklamı, arama motorunda
   meslektaş adına/kayırıcı anahtar kelime, panel/aracı yoluyla iş sağlama yasaktır.
4. **Sosyal medya ve web.** Mecraya özgü değil içeriğe özgü değerlendirilir; takipçi
   kazanmaya yönelik abartılı/teşvik edici paylaşım yasak kapsamına girer.
5. **Yaptırım.** İhlal disiplin suçudur (m.34, m.135); ayrıca haksız rekabet boyutu
   (TTK m.55 vd.) gündeme gelebilir.

## Çıktı modülleri
- İçerik bazında "uyumlu / düzeltilmeli / yasak" işaretlemesi.
- Uyumlu tabela/web/sosyal medya metni önerisi.
- Düzeltme ve risk notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

