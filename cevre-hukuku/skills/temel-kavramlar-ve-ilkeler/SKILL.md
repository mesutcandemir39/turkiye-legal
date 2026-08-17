---
argument-hint: ''
description: Çevre hukukunun sistematiğini, kirleten öder ve ihtiyat ilkelerini, idari/özel/ceza
  eksenlerinin ayrımını ve uygulanacak normlar piramidini kurmak gerektiğinde; bir
  çevre uyuşmazlığını ilk kez çerçeve
name: temel-kavramlar-ve-ilkeler
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
  - ad: Çevre Kanunu
    numara: '2872'
    tur: kanun
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve İlkeler

## Görev
Çevresel bir olguyu doğru hukuki eksene oturtmak, uygulanacak normlar bütününü ve yol haritasını belirlemek; idari, özel hukuk ve ceza katmanlarını ayırt etmek.

## Soğuk başlangıç (intake)
1. Müvekkil hangi konumda: yatırımcı/işletme, idare, yoksa kirliliğe maruz kalan/itiraz eden mi?
2. Ortada somut bir idari işlem (ÇED kararı, izin, yaptırım) var mı; varsa tarihi ve tebliği nedir?
3. Talep ne: işlem iptali, tazminat, faaliyetin durdurulması, yoksa ceza riskini yönetmek mi?
4. Faaliyet hangi sektör/tesis; hangi çevresel unsur (hava, su, atık, gürültü) etkileniyor?

## Denetim şeması
1. **İlkeleri uygula**: 2872 sayılı Çevre Kanunu m.3 — önleme, ihtiyat, kirleten/bozan öder, işbirliği ve katılım ilkeleri yorum ölçütüdür. Anayasa m.56 sağlıklı ve dengeli çevrede yaşama hakkını güvence altına alır.
2. **Ekseni belirle**: İzin/ÇED/yaptırım işlemleri → idari eksen (2577 sayılı İYUK). Kirlilikten doğan zarar → özel hukuk ekseni (TBK m.49 vd.; el atma için TMK m.683). Kasten/taksirle kirletme → ceza ekseni (TCK m.181-182).
3. **Sorumluluk türünü tespit et**: 2872 m.28 uyarınca kirletenin sorumluluğu kusura bağlı değildir; birden çok kirleten varsa müteselsil sorumluluk gündeme gelir. İdari yaptırımlarda ise m.20-23 cetveli ve 5326 sayılı Kanun genel rejimi uygulanır.
4. **Norm hiyerarşisini kur**: Kanun (2872, 3194) → yönetmelik (ÇED, Çevre İzin ve Lisans, alan yönetmelikleri) → genelge/kılavuz. Yönetmelik kanuna, genelge yönetmeliğe aykırı olamaz; aykırılık iptal sebebidir.
5. **Ara sonuç**: İlgili norm, yargı yolu, süre durumu ve ispat ihtiyacı tek paragrafta sabitlenir.

## Çıktı modülleri
- Eksen ve yargı yolu haritası (idari/özel/ceza)
- Uygulanacak normlar listesi (madde + yürürlükteki yönetmelik sürümü)
- İlkesel değerlendirme ve ilk risk notu
- Sonraki adım önerisi (hangi beceriye geçilecek)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

