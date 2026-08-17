---
argument-hint: ''
description: Kamu ihale hukukunun yapısını 4734 ve 4735 ekseninde kavramak, ihale
  türü-usul-eşik değer ilişkisini kurmak ve hangi alt rejimin uygulanacağını ayırt
  etmek için ilk başvurulacak harita beceridir.
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
  - ad: Koruma Amaçlı Imar Planları Hakkında Kanun
    numara: '4734'
    tur: kanun
  - ad: Tarih Medeniyetini Koruma Kanunu
    numara: '4735'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve İhale Sistematiği

## Görev
Somut işin kamu ihale rejimine girip girmediğini, giriyorsa hangi kanun/yönetmelik/usul ve eşik değere tabi olduğunu tespit etmek; sonraki uzman beceriye doğru yönlendirme yapmak.

## Soğuk başlangıç (intake)
1. İdare hangi kurum? (4734 m.2 kapsamı mı, m.3 istisna/kapsam dışı mı?)
2. İşin türü nedir: mal alımı, hizmet alımı, yapım işi, danışmanlık?
3. Yaklaşık maliyet/sözleşme bedeli eşik değerin altında mı üstünde mi (m.8, m.13)?
4. Uygulanan usul: açık, belli istekliler, pazarlık (m.21) yoksa doğrudan temin (m.22) mi?
5. Hangi aşamadasın: ilan öncesi, teklif değerlendirme, sözleşme, yoksa yasaklama mı?

## Denetim şeması
1. **Kapsam testi:** İdare 4734 m.2 kapsamında mı? Kapsamdaysa m.3 istisnaları veya kapsam dışılık var mı? İstisna varsa ilgili istisna usulü uygulanır, KİK denetimi farklılaşır.
2. **Tür tespiti:** Mal/hizmet/yapım ayrımı doğru yapılır; her tür için ayrı Uygulama Yönetmeliği ve tip şartname geçerlidir. Karma işlerde ağırlıklı unsur belirleyicidir.
3. **Eşik değer ve usul:** m.8 eşik değerleri ve m.13 ilan süreleri kontrol edilir; eşik altı/üstü ilan süresini ve ilan mecrasını değiştirir. Açık ihale asıldır; pazarlık (m.21/a-f) ve doğrudan temin (m.22/a-i) yalnızca sayılı hallerde kullanılır — istisnaî usule keyfî kaçış hukuka aykırılıktır.
4. **İlke süzgeci (m.5):** Saydamlık, rekabet, eşit muamele, güvenilirlik ve kaynakların verimli kullanımı her aşamada ölçüt alınır; ihtiyacın bütünlük arz etmesi gerekir, kısmî bölmeyle eşik kaçırma yasaktır.
5. **Ara sonuç:** Tür + usul + eşik + aşama belirlenince, doğru uzman beceriye (yeterlik, aşırı düşük, şikâyet, sözleşme, yasaklama) sevk edilir.

İspat yükü: İdarenin işlemi tesis ederken dayandığı sebep ve dokümanı; isteklinin ise iddiasını teklif dosyası ve doküman üzerinden ortaya koyması beklenir.

## Çıktı modülleri
- İhale künyesi tablosu (idare, tür, usul, eşik, IKN, takvim).
- Uygulanacak kanun/yönetmelik/tip şartname listesi.
- Hangi uzman beceriye yönlendirildiğine dair kısa not.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

