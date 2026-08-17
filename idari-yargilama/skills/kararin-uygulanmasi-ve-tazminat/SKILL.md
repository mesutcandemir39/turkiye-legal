---
argument-hint: ''
description: İdarenin lehe kararı uygulamaması, kararın gereğinin yerine getirilmesi
  ve uygulamama nedeniyle tazminat talebi gündeme geldiğinde kullanılır; iptal kararının
  geriye yürür etkisi ve idarenin tesis etm
name: kararin-uygulanmasi-ve-tazminat
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
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İptal Kararının Uygulanması ve Tazminat

## Görev
Lehe sonuçlanan idari davanın gereğinin idarece eksiksiz ve süresinde yerine getirilmesini sağlamak; uygulamama hâlinde başvurulacak yolları ve tazminat imkânını kurgulamak.

## Soğuk başlangıç (intake)
- Karar hangi işlemi iptal etti; idarenin tesis etmesi gereken yeni işlem ne?
- Karar idareye tebliğ edildi mi; üzerinden ne kadar süre geçti?
- İdare kararı uygulamadı mı, eksik mi uyguladı, yoksa şeklen uygulayıp aynı sonucu mu doğurdu?
- Uygulamama nedeniyle doğan zarar var mı?

## Denetim şeması
1. **Uygulama zorunluluğu ve süre** (Anayasa m.138/4; İYUK m.28/1): İdare, idari yargı kararlarının gereğini **gecikmeksizin** ve kararın tebliğinden itibaren en geç **30 gün** içinde yerine getirmek zorundadır. Bu süre kamu düzenine ilişkindir.
2. **İptal kararının etkisi**: İptal kararı işlemi tesis edildiği andan itibaren (geçmişe etkili) ortadan kaldırır; idare iptalden önceki hukuki duruma dönmek ve kararın gerekçesine uygun işlem tesis etmekle yükümlüdür. Kararın etrafından dolanan (aynı sakatlıkla yeniden işlem) tutum hukuka aykırıdır.
3. **Uygulamama hâlinde tazminat** (İYUK m.28/3): Kararın gereği yerine getirilmezse ilgili, idare aleyhine maddi ve manevi tazminat davası açabilir. Ayrıca kararı kasten yerine getirmeyen kamu görevlilerinin kişisel sorumluluğu gündeme gelebilir (İYUK m.28 ilgili fıkrası); kişisel kusurla devlet aleyhine rücu ilişkisi gözetilir.
4. **Parasal kararların infazı** (İYUK m.28/2): Tazminat ve vergi davalarında hükmedilen tutar için genel hükümler ve idarenin ödeme süresi uygulanır; idare aleyhine ilamların icrasında özel sınırlamalar gözetilir.
5. **Ara sonuç**: Uygulamama yazılı olarak idareye hatırlatılır (başvuru/ihtar) ve tarih ispatlanır; gerekirse yeni işlem yine iptal davasına konu edilir.

## Çıktı modülleri
- İdarenin yapması gereken işlem/eylem listesi (karar gerekçesine bağlı)
- Uygulama süresi takibi ve ihtar metni
- Tazminat davası seçeneği değerlendirmesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

