---
argument-hint: ''
description: Bir taşınmaz üzerinde başkası lehine kullanım/yararlanma hakkı kurulması,
  kullanılması veya sona erdirilmesi söz konusu olduğunda; intifa, oturma, üst hakkı
  ve geçit/mecra gibi irtifakların tesisi, iç
name: irtifak-haklari
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İrtifak Hakları (İntifa, Geçit, Üst Hakkı)

## Görev
İrtifak haklarının kurulması, içeriğinin belirlenmesi ve sona erdirilmesi: eşyaya bağlı ve kişiye bağlı irtifakları ayırmak, intifa/oturma/üst hakkı ve zorunlu geçit gibi tipik irtifakların şartlarını denetlemek.

## Soğuk başlangıç (intake)
- İrtifak bir taşınmaz lehine mi (eşyaya bağlı, örn. geçit) yoksa bir kişi lehine mi (intifa, oturma) kurulacak/kuruldu?
- Hak tapuya tescil edildi mi; süresi/koşulu var mı?
- Uyuşmazlık irtifakın kurulması mı, içeriği/kapsamı mı, yoksa terkini mi?
- Üst hakkı söz konusuysa süre (bağımsız-sürekli olarak ayrı kayıt) ve bedel düzenlenmiş mi?

## Denetim şeması
1. **Tür ayrımı**: Eşyaya bağlı irtifaklar (m.779 vd.) yararlanan taşınmaza bağlıdır; mülkiyetle birlikte geçer. İrtifaklar tescille doğar (m.780).
2. **İntifa hakkı (m.794 vd.)**: Sahibine eşyadan tam yararlanma yetkisi verir; devredilemez ama kullanımı bırakılabilir. İntifa sahibi olağan bakım ve masraflardan sorumludur (m.813). En geç hak sahibinin ölümüyle (tüzel kişide 100 yıl) sona erer (m.797).
3. **Oturma hakkı (m.823 vd.)**: Bir binada/bölümde oturma yetkisi; kişiye bağlı, devredilmez ve mirasla geçmez.
4. **Üst hakkı (m.826 vd.)**: Başkasının arazisinde/altında yapı sahibi olma hakkı; bağımsız ve sürekli nitelikteyse ayrı taşınmaz olarak tapuya kaydedilebilir (m.826/3, m.704).
5. **Zorunlu geçit ve mecra (m.747, m.744)**: Genel yola çıkışı olmayan taşınmaz maliki, tam bedel karşılığında komşudan geçit isteyebilir; mecra (su, enerji hattı) için de benzer kurallar uygulanır. Bu talepler dava yoluyla kurulur.
6. **Sona erme/terkin**: İrtifak, sürenin dolması, hakkın yararsız hâle gelmesi (m.785) veya terkinle sona erer; yararlanan taşınmaz için her türlü yarar kalmamışsa yüklü taşınmaz maliki terkin isteyebilir.
7. **Ara sonuç**: İrtifakın geçerli kuruluşu (tescil), kapsamı ve sona erme şartlarının tespiti.

## Çıktı modülleri
- İrtifak (intifa/geçit/üst hakkı) tesis veya terkin talebi iskeleti.
- Geçit/mecra davasında bedel ve güzergâh değerlendirmesi.
- Tescil/şerh kontrol listesi ve süre/sona erme uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

