---
argument-hint: ''
description: Basın ve medya hukukunun temel kavramlarını, mecra türlerini ve uygulanacak
  rejimi belirlemek; ifade özgürlüğü ile kişilik hakkı dengesinin genel çerçevesini
  kurmak gerektiğinde kullanılır.
name: temel-kavramlar-ve-sistem
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
  - ad: Basın Meslek İlkeleri ve Yapı İtibarı Hakkında Kanun
    numara: '5187'
    tur: kanun
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Sistematik

## Görev
Somut olayın hangi medya rejimine girdiğini saptamak, ifade-basın özgürlüğü (Anayasa m.26, m.28) ile kişilik hakkı (TMK m.24) ekseninde uygulanacak normları haritalamak ve doğru yol/merci seçimine zemin hazırlamak.

## Soğuk başlangıç (intake)
1. Yayın hangi mecrada çıktı: basılı eser, radyo/TV, internet haber sitesi, sosyal medya?
2. Yayın tarihi ve hâlâ erişilebilir mi (online ise URL)?
3. İçerik bir maddi vakıa iddiası mı yoksa değer yargısı/eleştiri mi?
4. Mağdur gerçek kişi mi, tüzel kişi mi, kamu görevlisi/siyasetçi mi?
5. Talep ne: düzeltme, içeriğin kaldırılması, tazminat, ceza şikâyeti?

## Denetim şeması
1. **Mecra tespiti**: Basılı/süreli yayın ise 5187 sayılı Basın Kanunu (m.2 tanımlar) devreye girer; işitsel-görsel ise 6112 sayılı Kanun; internet ise 5651 sayılı Kanun. Mecra, görevli mercii (sulh ceza hâkimliği, asliye hukuk, RTÜK) belirler.
2. **Koruma katmanı**: Her mecrada genel koruma da uygulanır — kişilik hakkı (TMK m.24-25), haksız fiil tazminatı (TBK m.49, m.58), ceza (TCK m.125 hakaret, m.134 özel hayat).
3. **Hukuka aykırılık ön süzgeci**: TMK m.24/II uyarınca üstün nitelikte özel/kamusal yarar, rıza veya kanunun verdiği yetki varsa ihlal hukuka uygun sayılır. Haber verme hakkı çerçevesinde gerçeklik, güncellik, kamu yararı ve öz-biçim dengesi aranır.
4. **Ara sonuç**: İhlal var ve hukuka uygunluk sebebi yoksa; mağdurun statüsüne (kamuya mal olmuş kişi katlanma eşiği yüksektir) göre yol/merci ve süre seçilir.

## Çıktı modülleri
- Mecra-rejim eşleştirme tablosu
- Uygulanacak normlar listesi (madde atıflı)
- Yol/merci ve süre özeti
- Bir sonraki uzman beceriye yönlendirme notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

