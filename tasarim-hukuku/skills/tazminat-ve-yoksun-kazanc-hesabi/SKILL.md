---
argument-hint: ''
description: Tasarım tecavüzünde maddi/manevi tazminatın ve yoksun kalınan kazancın
  SMK m.150-151 yöntemleriyle hesaplanması, itibar tazminatı ve faiz başlangıcının
  belirlenmesi; tecavüzün parasal sonuçlarının tal
name: tazminat-ve-yoksun-kazanc-hesabi
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


# Tazminat ve Yoksun Kalınan Kazanç Hesabı

## Görev
Tasarım tecavüzünün parasal sonucunu kurmak: fiili zarar, yoksun kalınan kazanç, manevi ve itibar tazminatı kalemlerini SMK'ye uygun hesap yöntemiyle ortaya koymak ve bilirkişi denetimine hazır hâle getirmek.

## Soğuk başlangıç (intake)
1. Tecavüz fiili ve süresi belirli mi (üretim/satış adetleri, dönem)?
2. Hak sahibinin kâr marjı, lisans bedeli emsalleri veya satış kaybı verisi var mı?
3. Tasarımın ürünün talebini yaratmadaki ekonomik önemi (m.151/3) nedir?
4. Manevi/itibar zararı doğuran somut olgu var mı (kalitesiz taklitle itibar kaybı)?

## Denetim şeması
1. Kalemler (SMK m.150/1): Maddi tazminat = fiili zarar + yoksun kalınan kazanç. Ayrıca manevi tazminat (genel hükümler) ve itibar tazminatı (SMK m.150/2 — taklidin kötü üretimi/uygunsuz kullanımı hakkın itibarına zarar verdiğinde) istenebilir.
2. Yoksun kalınan kazanç yöntem seçimi (SMK m.151/2): Hak sahibi üç yöntemden birini seçer: (a) tecavüz olmasaydı elde edilebilecek muhtemel gelir, (b) tecavüz edenin elde ettiği net kazanç, (c) lisans verilseydi istenecek makul lisans bedeli. Seçim davacıya aittir; verisi en güçlü yöntemi seçin.
3. Tasarımın katkı payı (SMK m.151/3): Tasarımın ürüne olan ekonomik katkısı belirleyiciyse, kazanç hesaplanırken bu etken dikkate alınır (ürün talebinin tasarımdan kaynaklanma oranı).
4. İspat ve veri: Karşı tarafın ticari defter/satış kayıtları (delil tespiti/sunma yükümlülüğü), gümrük/üretim kayıtları; bilirkişiye yöntemi ve verileri net biçimde sunun.
5. Faiz ve zamanaşımı: Faiz başlangıcı haksız fiil/temerrüt esaslarına göre; tazminat talebi SMK m.157 yollamasıyla TBK haksız fiil zamanaşımına (TBK m.72: ıttıladan itibaren 2 yıl ve her hâlde 10 yıl) tabidir.
6. Ara sonuç: Seçilen yöntem, hesap tablosu, faiz ve zamanaşımı durumu net yazılır.

## Çıktı modülleri
- Tazminat hesap tablosu (kalem, yöntem, veri kaynağı, tutar).
- Yöntem seçimi gerekçesi ve katkı payı analizi.
- Faiz başlangıcı ve zamanaşımı kontrol notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

