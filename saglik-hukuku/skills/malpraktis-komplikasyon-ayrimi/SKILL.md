---
argument-hint: ''
description: İstenmeyen tıbbi sonucun önlenebilir bir kusur (malpraktis) mu yoksa
  öngörülen ama kaçınılmaz bir komplikasyon mu olduğunu ayırmak için kullanılır; komplikasyon
  yönetimi kusurunu da değerlendirir.
name: malpraktis-komplikasyon-ayrimi
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
  - ad: Banka Muhasebe Sistemi Hakkında Kanun
    numara: '1219'
    tur: kanun
  - ad: Gayrimenkul Ek Vergisi Hakkında Kanun
    numara: '3359'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Malpraktis ve Komplikasyon Ayrımı

## Görev
İstenmeyen sonucun hukuki niteliğini belirlemek: önlenebilir özen ihlali (malpraktis/sorumluluk doğurur) mu, yoksa özenli davranışa rağmen ortaya çıkan komplikasyon (kural olarak sorumluluk doğurmaz) mu.

## Soğuk başlangıç (intake)
1. İstenmeyen sonuç literatürde bu müdahalenin bilinen komplikasyonu mu?
2. Müdahale endikasyona ve tıbbi standarda uygun yapıldı mı?
3. Komplikasyon ortaya çıktığında zamanında teşhis ve müdahale edildi mi?
4. Hasta bu komplikasyon riski hakkında önceden aydınlatıldı mı?

## Denetim şeması
1. **Standarda uygunluk testi**: Müdahale tekniği, endikasyonu ve zamanlaması tıbbın güncel verilerine uygun mu? Uygunsa malpraktis ihtimali zayıflar.
2. **Öngörülebilirlik/kaçınılabilirlik**: Komplikasyon, dikkatli bir hekimce öngörülebilir ama somut olayda kaçınılmaz mıydı? Kaçınılabilir bir sonuç önlenmemişse bu malpraktistir (TBK m.49, TCK m.22 taksir).
3. **Komplikasyon yönetimi kusuru**: Komplikasyon meşru olsa bile, geç teşhis, yanlış sevk, takipsizlik veya yetersiz müdahale bağımsız bir kusur oluşturur ve sorumluluk doğurur.
4. **Aydınlatma bağlantısı**: Komplikasyon riski önceden bildirilmemişse, sonuç hukuken hastaya yüklenemez (bkz. Aydınlatılmış Onam Denetimi).
5. **İspat ve bilirkişi**: Ayrım maddi-teknik bir sorundur; ATK ve uzmanlık dalı bilirkişisi belirleyicidir. Rapor metodolojisi ayrıca denetlenmelidir.
6. **Ara sonuç**: Standarda uygun + öngörülen + iyi yönetilen + aydınlatılmış sonuç = komplikasyon (sorumluluk yok). Aksi her hâlde malpraktis tartışması açılır.

## Çıktı modülleri
- Malpraktis/komplikasyon ayrım tablosu (kriter bazlı)
- Komplikasyon yönetimi kusuru kontrolü
- Bilirkişiye sorulacak teknik sorular taslağı
- İlkesel içtihat atfı (Yargıtay 12. CD / 3. HD) [DOĞRULANMADI]



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

