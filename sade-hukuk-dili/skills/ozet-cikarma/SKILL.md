---
argument-hint: ''
description: Uzun bir dava dosyasını, bilirkişi raporunu, sözleşmeyi veya yazışma
  zincirini hukukçu olmayan bir karar verici için kısa, yalın ve doğru yönetici özetine
  indirgemek gerektiğinde kullanılır.
name: ozet-cikarma
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Belge Özeti ve Yönetici Özeti Çıkarma

## Görev
Uzun ve teknik bir hukuki belgeyi (dosya, rapor, sözleşme, yazışma) hukukçu olmayan bir okuyucunun
hızlıca kavrayacağı kısa bir yönetici özetine indirgemek; kritik bilgiyi düşürmeden, gereksiz
ayrıntıyı eleyerek.

## Soğuk başlangıç (intake)
1. Özetlenecek belge ve uzunluğu?
2. Karar verici kim ve özetten ne bekliyor (onay, risk değerlendirmesi, durum bilgisi)?
3. İstenen uzunluk (yarım sayfa, bir sayfa)?
4. Vurgulanması gereken karar noktaları var mı?

## Denetim şeması
1. ÇEKİRDEK BİLGİYİ AYIR: Belgeden taraf/konu, talep/sonuç, kritik tarih-süre, parasal büyüklük ve
   risk çıkarılır; bunlar özetin omurgasıdır ve asla düşürülmez.
2. PİRAMİT DİZİLİŞ: Sonuç/öneri en üste, gerekçe altına, ayrıntı en sona konur (ters piramit).
3. KARAR NOKTALARINI İŞARETLE: Okuyucunun aksiyon alması gereken hususlar (imza, onay, süre,
   bütçe) ayrıca belirginleştirilir.
4. DOĞRULUK SÜZGECİ (ispat/sadakat): Özet, kaynaktaki hiçbir şartı veya çekinceyi yanlış
   mutlaklaştırmaz; sayılar ve süreler kaynakla birebir doğrulanır.
5. BELİRSİZLİK İŞARETİ: Kaynakta açık olmayan veya teyit gereken noktalar "[DOĞRULANMADI]" /
   "[doldurulacak]" ile bırakılır, tahminle doldurulmaz.
6. ARA SONUÇ: Özet, karar verici için yeterli ve doğru mu; kritik bir tarih/tutar/risk atlanmış mı.

## Çıktı modülleri
- Tek paragraf yönetici özeti (sonuç önce).
- Anahtar bilgiler tablosu (taraflar / konu / tutar / kritik tarih / risk).
- Karar/aksiyon noktaları listesi.
- Ayrıntı için asıl belgeye yönlendirme ve "[DOĞRULANMADI]" notları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

