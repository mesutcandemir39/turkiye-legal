---
argument-hint: ''
description: Avukatın meslektaşlarına, karşı taraf vekiline, mahkemeye ve adli mercilere
  karşı davranış kuralları, mektuplaşma gizliliği ve dürüstlük yükümü söz konusu olduğunda
  kullanılır.
name: meslektas-mahkeme-iliskileri
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


# Meslektaşlar Arası İlişkiler ve Mahkemeyle İletişim

## Görev
Avukatın meslektaşları, karşı taraf ve yargı mercileriyle ilişkilerinde uyması gereken
nezaket, dürüstlük ve gizlilik kurallarını somut olaya uygulamak.

## Soğuk başlangıç (intake)
1. Uyuşmazlık meslektaşla mı (karşı vekil, devir alınan dosya) yoksa mahkemeyle mi?
2. Karşı vekille yapılan sulh görüşmesi/yazışması gizli kaydıyla mı yürütüldü?
3. Mahkemeye/karşı tarafa yönelik bir beyan dürüstlük/saygı sınırında mı?
4. Devralınan dosyada önceki meslektaşın ücreti çözüldü mü?

## Denetim şeması
1. **Meslektaşa saygı ve dürüstlük.** Avukatlar birbirine ve mesleğe karşı dürüst ve saygılı
   davranmakla yükümlüdür (Av. K. m.34; TBB Meslek Kuralları m.5, m.11 vd.). Meslektaşı
   küçük düşüren beyan disiplin suçudur. Ara sonuç: beyan eleştiri mi, kişisel saldırı mı?
2. **Sulh görüşmesi gizliliği.** "Gizli/sulh amaçlı" kaydıyla yapılan yazışma ve görüşmeler,
   karşı tarafın muvafakati olmadan mahkemeye delil olarak sunulamaz (TBB Meslek Kuralları
   m.27). Bu kural müzakere serbestisini korur.
3. **Dosya devri ve önceki vekilin hakkı.** Bir işi başka avukattan devralan avukat, önceki
   meslektaşın ücret hakkı ve durumu konusunda meslek kurallarını gözetir (TBB Meslek
   Kuralları m.38); devir öncesi bilgilendirme beklenir.
4. **Mahkemeye karşı yükümlülük.** Avukat mahkemeye saygı gösterir, yanıltıcı beyandan
   kaçınır; usule uygun, doğru ve özenli savunma yapar (Av. K. m.34; HMK m.29 dürüstlük ve
   doğruyu söyleme yükümü). Duruşma düzenine ve hâkime saygı esastır.
5. **Yaptırım.** İhlaller disiplin sorumluluğu (m.135) doğurur; mahkemeye karşı taşkınlık
   ayrıca duruşma düzeni ve ilgili usul yaptırımlarını gündeme getirir.

## Çıktı modülleri
- Davranışın kural uygunluğu değerlendirmesi (meslektaş/mahkeme ekseninde).
- "Gizli/sulh amaçlı" yazışma şerhi şablonu.
- Dosya devir bilgilendirme yazısı taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

