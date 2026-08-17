---
argument-hint: ''
description: Bir uyuşmazlıkta dava açmadan önce zorunlu (dava şartı) arabuluculuğa
  başvurulması gerekip gerekmediğini saptamak; ticari, iş, tüketici ve genişleyen
  kapsam, son tutanak ve dava şartı eksikliğinin son
name: dava-sarti-arabuluculuk
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dava Şartı Arabuluculuk Kapsam Denetimi

## Görev
Dava açılmadan önce zorunlu arabuluculuk gerekip gerekmediğini belirlemek; gerekiyorsa son tutanağı dava şartı olarak dosyaya bağlamak, gerekmiyorsa boşa süreç işletilmesini önlemek.

## Soğuk başlangıç (intake)
- Uyuşmazlık türü ne? (ticari alacak, işçi-işveren, tüketici, kira, ortaklığın giderilmesi?)
- Talep konusu para alacağı/tazminat mı, yoksa kapsam dışı bir talep mi?
- Daha önce arabuluculuğa başvuruldu mu, son tutanak var mı?
- Karşı tarafa ulaşılabiliyor mu (anlaşamama tutanağı seçeneği)?

## Denetim şeması
1. **Ticari uyuşmazlıklar** (TTK m.5/A): Konusu bir miktar paranın ödenmesi olan alacak ve tazminat talepleri bakımından dava şartı arabuluculuk; dava açmadan son tutanak alınmalıdır.
2. **İş uyuşmazlıkları** (7036 sayılı İş Mahkemeleri Kanunu m.3): İşçi-işveren arasındaki kıdem/ihbar/fazla mesai gibi alacak ve işe iade taleplerinde dava şartı arabuluculuk; **iş kazası/meslek hastalığından kaynaklanan maddi-manevi tazminat** istisnası kontrol edilir.
3. **Tüketici uyuşmazlıkları** (6502 sayılı Kanun): Belirli parasal sınır üstündeki tüketici uyuşmazlıklarında dava şartı arabuluculuk; hakem heyeti zorunluluğu olan alt sınır ayrıca kontrol edilir.
4. **Genişleyen kapsam**: Kira ilişkisinden doğan uyuşmazlıklar, taşınır/taşınmaz ortaklığının giderilmesi, komşuluk hukuku ve kat mülkiyetinden doğan belirli uyuşmazlıklar da kademeli olarak dava şartı arabuluculuk kapsamına alınmıştır — **güncel kapsam ve yürürlük tarihleri mevzuattan teyit edilir.**
5. **Sonuç** (dava şartı): Kapsamdaki uyuşmazlıkta son tutanak (anlaşma/anlaşamama) dosyaya konmadan dava açılırsa, dava **usulden reddedilir** (HMK m.115; ilgili özel hükümler). Karşı tarafın katılmaması durumunda anlaşamama tutanağı dava şartını karşılar.
6. **Süre etkisi**: Arabuluculuğa başvuru, zamanaşımını durdurur ve hak düşürücü süreyi işlemekten alıkoyar; bu koruma esastır.

Ara sonuç: "Kapsamda mı + hangi norm + son tutanak gerekli mi + zamanaşımı etkisi" özeti.

## Çıktı modülleri
- Kapsam kararı (norm atıflı, istisna kontrollü).
- Eksik son tutanak halinde usulden ret uyarısı.
- Başvurunun zamanaşımı/hak düşürücü süreye etkisi notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

