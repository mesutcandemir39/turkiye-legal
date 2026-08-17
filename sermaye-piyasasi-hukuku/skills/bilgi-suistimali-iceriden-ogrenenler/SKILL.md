---
argument-hint: ''
description: İçsel bilgiye dayalı işlem, içsel bilginin yetkisiz aktarımı veya tavsiye
  yoluyla kullanılması iddiası ve SPK m.106 kapsamındaki cezai sorumluluk değerlendirileceğinde
  kullanılır.
name: bilgi-suistimali-iceriden-ogrenenler
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
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Bilgi Suistimali (İçeriden Öğrenenlerin Ticareti)

## Görev
İçsel bilgiye dayalı işlem (insider trading) iddiasını SPK m.106 unsurları üzerinden çözümlemek; failin sıfatı, içsel bilginin niteliği ve işlem-bilgi ilişkisini kurarak ceza ve idari sorumluluk riskini değerlendirmek.

## Soğuk başlangıç (intake)
- İşlemi yapan kim: yönetici, çalışan, danışman, hâkim ortak mı; bilgiye nasıl ulaştı?
- İşleme konu içsel bilgi nedir, ne zaman oluştu ve ne zaman kamuya açıklandı?
- İşlemler bilgi açıklanmadan önce mi yapıldı; kazanç/zarardan kaçınma var mı?
- Müvekkil şüpheli/sanık mı, yoksa savunma/Kurul incelemesine yanıt mı hazırlanıyor?

## Denetim şeması
1. **Fail çevresi:** SPK m.106; içsel bilgiye sıfat veya görev nedeniyle ulaşanlar (yönetici, denetçi, hizmet ilişkisi, hâkim ortak) ile bu bilgiyi bunlardan edinenler kapsamı belirlenir.
2. **İçsel bilgi niteliği:** Bilginin kamuya açıklanmamış, belirli, fiyatı/yatırım kararını önemli ölçüde etkileyebilir nitelikte olduğu saptanır; değilse suç oluşmaz.
3. **Fiil:** Bilgiye dayalı olarak sermaye piyasası aracında işlem yapmak, başkasına yaptırmak, bilgiyi yetkisiz aktarmak veya tavsiyede bulunmak unsurları aranır. Ara sonuç: hangi seçimlik hareketin gerçekleştiği belirlenir.
4. **Manevi unsur ve illiyet:** Kast aranır; işlemin içsel bilgiye dayandığı, emir/işlem kayıtları, zamanlama ve bilgiye erişen listesiyle bağlanır. İspat yükü iddia makamındadır (CMK m.217; şüpheden sanık yararlanır).
5. **Yaptırım ve usul:** Cezai yaptırım m.106; soruşturma/kovuşturma Kurul'un başvurusu/mütalaası şartına bağlıdır (m.115); etkin pişmanlık (m.109) ve aynı fiilin idari yaptırım boyutu ayrıca değerlendirilir. İçtihat için Yargıtay bankası taranır, künye `[DOĞRULANMADI]`.

## Çıktı modülleri
- Unsur unsur suç analizi tablosu (m.106)
- İçsel bilgi-işlem zamanlama kronolojisi
- Savunma/iddia stratejisi ve etkin pişmanlık değerlendirmesi
- Kurul mütalaası/usul yol haritası



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

