---
argument-hint: ''
description: Avukatlığın hukuki niteliği, kaynak hiyerarşisi (1136 sayılı Kanun, TBB
  Meslek Kuralları, yönetmelikler, tarife) ve meslek-müvekkil-baro üçlüsü hakkında
  genel çerçeve ve yön bulma için kullanılır.
name: avukatlik-temel-kavramlar
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


# Avukatlık Mesleğinin Temel Kavramları ve Sistematiği

## Görev
Avukatlık hukukunun temel kavramlarını, kaynak hiyerarşisini ve sistematiğini ortaya koymak;
bir soruyu doğru norm katmanına ve doğru alt-beceriye yönlendirmek.

## Soğuk başlangıç (intake)
1. Soru avukatın hak/yetkileri mi, müvekkille iç ilişki (sözleşme-ücret-sır) mı, yoksa
   disiplin/baro boyutu mu?
2. Kişi avukat mı, stajyer mi, müvekkil mi, karşı taraf mı?
3. Olayda menfaat çatışması veya sır riski görünüyor mu?
4. Uyuşmazlık hangi aşamada (danışma, sözleşme, dava, azil, disiplin şikâyeti)?

## Denetim şeması
1. **Niteliği belirle.** Avukatlık hem kamu hizmeti hem serbest meslektir; yargının kurucu
   unsuru ve bağımsız savunmadır (Av. K. m.1-2). Bu nitelik, bağımsızlık ve sır gibi tüm
   meslek kurallarının temel gerekçesidir.
2. **Kaynak hiyerarşisini kur.** Çekirdek: 1136 sayılı Avukatlık Kanunu. Üstüne TBB Meslek
   Kuralları, Avukatlık Kanunu Yönetmeliği, TBB Reklam Yasağı Yönetmeliği ve yıllık TBB
   Avukatlık Asgari Ücret Tarifesi gelir. Müvekkil ilişkisinin maddi temeli vekâlet
   sözleşmesidir (TBK m.502 vd.).
3. **Genel davranış normunu uygula.** Avukat görevini özenle, doğrulukla ve onurla yapar;
   meslek kurallarına uyar (Av. K. m.34, TBB Meslek Kuralları m.3-4). Ara sonuç: somut
   davranış bu genel normla bağdaşıyor mu?
4. **Doğru alt-beceriye yönlendir.** Sır → sir-saklama; çatışma → cikar-catismasi; ücret →
   vekalet-ucreti; disiplin → disiplin-sorumlulugu; arama/dokunulmazlık → avukatin-yetkileri;
   tarife/karşı taraf vekâlet ücreti → ücret becerisi. İspat yükü genel kuralda davacıdadır
   (TMK m.6), disiplinde kovuşturmayı yürüten organdadır.

## Çıktı modülleri
- Sorunu doğru norm katmanına yerleştiren kısa harita.
- İlgili madde atıfları listesi (Av. K. + TBB Meslek Kuralları + tarife yılı).
- Önerilen alt-beceri ve eksik bilgi soruları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

