---
argument-hint: ''
description: İş kazası tazminat dava dilekçesi, idari ceza itirazı, SGK işlemlerine
  itiraz ve İSG dokümantasyonu (uyarı, tutanak) taslaklarını üretmek için kullanılır.
name: dilekce-tutanak-taslaklari
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
  - ad: İş Sağlığı ve Güvenliği Kanunu
    numara: '6331'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dilekçe, Tutanak ve Başvuru Taslakları

## Görev
İSG dosyasının türüne uygun taslak üretmek: iş kazası tazminat dava dilekçesi, idari para cezası itirazı, SGK işlemine itiraz/dava, ve işveren tarafı için savunma/uyarı/tutanak metinleri. Eksik bilgiler `[doldurulacak]` yer tutucularıyla işaretlenir.

## Soğuk başlangıç (intake)
- Hangi taslak isteniyor (tazminat dilekçesi / ceza itirazı / SGK itirazı / İSG tutanağı)?
- Taraflar, sıfatları ve husumet (asıl işveren-alt işveren) netleşti mi?
- Talep sonucu sayısallaştı mı (fazlaya ilişkin haklar saklı, belirsiz alacak mı)?
- Dayanak deliller ve madde atıfları hazır mı?

## Denetim şeması
1. **Dava dilekçesi mimarisi (HMK m.119):** Mahkeme, taraflar, konu, açık talep sonucu, vakıalar, hukuki sebepler (TBK m.417, m.49-56; 6331 ilgili madde), deliller ve imza. İş kazası tazminatında belirsiz alacak/kısmi dava tercihini ve fazlaya ilişkin hakların saklı tutulmasını ekle.
2. **İdari ceza itirazı:** Sulh ceza hâkimliğine hitap, 5326 m.27 dayanağı, on beş günlük süre vurgusu, ceza-madde uyumsuzluğu ve usul sakatlığı gerekçeleri, iptal/indirim talebi.
3. **SGK işlemine itiraz/dava:** İlgili işleme (rücu, gelir, tespit) göre iş mahkemesine; idari aşamada SGK'ya itiraz gerekiyorsa onu da ele.
4. **İşveren tarafı dokümanları:** İSG kuralına aykırılık savunma tutanağı, uzman/hekim yazılı uyarı metni, KKD zimmet tutanağı, eğitim katılım formu şablonu — ileride ispat için tarih/imza alanlarıyla.
5. **Disiplin:** Madde atıflarını doğru ver; içtihat zikredilecekse künyeyi `[DOĞRULANMADI]` işaretle, uydurma numara yazma. **Ara sonuç:** Taslağı yer tutucularla eksiksiz iskelete oturt.

## Çıktı modülleri
- İstenen tür için tam dilekçe/başvuru taslağı.
- Eksik bilgi `[doldurulacak]` listesi.
- Ekler ve delil dizini önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

