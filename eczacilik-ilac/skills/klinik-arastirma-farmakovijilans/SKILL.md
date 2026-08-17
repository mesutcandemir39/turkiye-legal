---
argument-hint: ''
description: Klinik araştırma izinleri, gönüllü onamı, etik kurul ve advers etki/farmakovijilans
  yükümlülükleri ile bunlara bağlı sorumluluk konularında kullanılır.
name: klinik-arastirma-farmakovijilans
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
  - ad: Hemşirelik Kanunu
    numara: '6197'
    tur: kanun
  - ad: Mimar ve Mühendisler Hakkında Kanun
    numara: '1262'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Klinik Araştırma ve Farmakovijilans

## Görev
Klinik araştırmanın izin, etik ve gönüllü koruması boyutlarını ve ruhsat sahibinin farmakovijilans (advers etki izleme) yükümlülüklerini denetlemek.

## Soğuk başlangıç (intake)
- Konu klinik araştırma izni/yürütülmesi mi, yoksa pazardaki ürünün advers etki bildirimi mi?
- Araştırmada faz, etik kurul onayı, gönüllü bilgilendirilmiş onamı durumu nedir?
- Farmakovijilansta: ciddi advers etki bildirim süresi kaçırıldı mı, PSUR/risk yönetim planı var mı?
- TİTCK denetimi/yaptırımı veya gönüllü zararı iddiası var mı?

## Denetim şeması
1. **Dayanak.** İlaç ve Biyolojik Ürünlerin Klinik Araştırmaları Hakkında Yönetmelik ve İyi Klinik Uygulamaları kılavuzu; farmakovijilans için ilgili TİTCK düzenlemesi; etik temelde Anayasa m.17 (kişinin maddi-manevi varlığı, rızası olmadan deneye tabi tutulamama).
2. **Klinik araştırma denetimi.** TİTCK izni + etik kurul onayı + geçerli bilgilendirilmiş gönüllü onamı zorunlu. Ara sonuç: üç katman da tamam mı; onam aydınlatma ölçütünü karşılıyor mu?
3. **Gönüllü koruması ve sorumluluk.** Gönüllü sigortası, zarar halinde tazminat; haksız fiil sorumluluğu (TBK m.49 vd.) ve aydınlatma kusuru değerlendirilir.
4. **Farmakovijilans yükümlülüğü.** Ruhsat sahibinin ciddi advers reaksiyonları süresinde bildirme, PSUR/PBRER ve risk yönetim planı sunma yükümlülüğü; ihlalde TİTCK idari yaptırımı (birel işlem → İYUK m.7).
5. **Eşgüdüm.** İhlal hem idari yaptırım hem ürün sorumluluğu (zarar gören hasta) doğurabilir; süreçler ayrı yürür.

## Çıktı modülleri
- İzin/etik/onam üçlü uygunluk kontrol listesi.
- Farmakovijilans yükümlülük takvimi ve eksik bildirim analizi.
- Yaptırıma karşı dava veya tazminat değerlendirme notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

