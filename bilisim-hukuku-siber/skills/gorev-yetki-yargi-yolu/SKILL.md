---
argument-hint: ''
description: Bilişim/siber bir uyuşmazlıkta hangi yargı koluna, hangi mahkemeye/mercie,
  hangi yetki kuralıyla başvurulacağını belirlemek; ceza-idari-hukuk yolları arasında
  doğru tercihi yapmak gerektiğinde kullanı
name: gorev-yetki-yargi-yolu
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Elektronik Ticaretin Düzenlenmesine Dair Kanun
    numara: '5651'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Görev, Yetki ve Yargı Yolu Haritası

## Görev
Bilişim/siber uyuşmazlıkta doğru yargı kolunu, görevli ve yetkili mercii ve başvuru yolunu belirlemek; eş zamanlı yürüyen süreçleri koordine etmek.

## Soğuk başlangıç (intake)
1. Talep ne? (ceza/şikâyet, idari yaptırım itirazı, tazminat, içerik kaldırma, uyum?)
2. Taraflar kim, biri tacir/tüketici mi, idare mi?
3. Olayın yeri/zararın doğduğu yer neresi?
4. Süre kısıtı veya acil tedbir ihtiyacı var mı?

## Denetim şeması
1. **Ceza yolu.** Bilişim suçlarında (TCK m.243-245) şikâyet/ihbar Cumhuriyet başsavcılığına yapılır; kovuşturmada görev kural olarak asliye ceza, ağırlaştırılmış hallerde ağır ceza mahkemesindedir. Yetki suçun işlendiği yer (CMK m.12). Soruşturma gizliliği ve koruma tedbirleri (CMK m.134) bu yolda işler.
2. **5651 tedbir yolu.** İçerik çıkarma/erişim engellemede görevli mercі sulh ceza hâkimliği (m.9), özel hayatta BTK (m.9/A); kararlara itiraz CMK itiraz usulüne tabidir.
3. **İdari yol (KVKK).** Kurul kararlarına (idari para cezası, ilgili kişi başvurusu sonucu) karşı dava idari yargıda açılır; idari para cezasına karşı yol ise niteliğine göre değerlendirilir (Kabahatler Kanunu/idari yargı tartışması). Dava açma süresi (2577 İYUK m.7) gözetilir.
4. **Hukuk yolu.** Tazminat ve sözleşme uyuşmazlıklarında görev: taraflar tacir ve iş ticari ise asliye ticaret (TTK m.4-5); tüketici işlemiyse tüketici mahkemesi/hakem heyeti; aksi halde asliye hukuk. Yetki HMK m.6 (genel) ve haksız fiilde HMK m.16 (haksız fiilin işlendiği/zararın doğduğu yer). Acil koruma için ihtiyati tedbir/delil tespiti (HMK m.389 vd., m.400 vd.).
5. **Ara sonuç.** Eş zamanlı işleyebilecek yollar (ceza + KVKK + tazminat) ve sıralaması, görev-yetki ve süreler tabloya bağlanır. İspat yükü her yolda ayrıca ele alınır.

## Çıktı modülleri
- Yargı yolu/görev/yetki tablosu (yol, mercі, kural, süre).
- Süre ve acil tedbir takvimi.
- Yol koordinasyon notu (eş zamanlı süreçler).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

