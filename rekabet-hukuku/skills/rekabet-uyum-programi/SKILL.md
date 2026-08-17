---
argument-hint: ''
description: Teşebbüsler için önleyici rekabet uyumu kurmak; fiyatlandırma, dağıtım,
  bilgi paylaşımı, rakip temasları ve yerinde inceleme hazırlığı gibi alanlarda risk
  taraması ve iç politika tasarlamak istendiğin
name: rekabet-uyum-programi
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
  - ad: Rekabetin Korunması Hakkında Kanun
    numara: '4054'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Rekabet Uyum Programı ve Risk Önleme

## Görev
Bir teşebbüsün rekabet hukuku ihlal riskini ihlal gerçekleşmeden azaltmak; ticari uygulamaları (fiyat, dağıtım, bilgi paylaşımı, ihale, rakip temasları) m.4/m.6 süzgecinden geçirerek iç politika, eğitim ve yerinde inceleme protokolü kurmak.

## Soğuk başlangıç (intake)
- Teşebbüsün pazardaki konumu hâkim/lider mi, yoksa pazar payı düşük mü?
- Rakiplerle temas alanları: dernek/birlik üyeliği, ortak ihaleler, kıyaslama (benchmarking), tedarik?
- Dağıtım modeli: bayilik, tek satıcılık, online satış kısıtları, fiyat tavsiyesi var mı?
- Daha önce soruşturma/şikâyet geçmişi var mı?

## Denetim şeması
1. **Yatay risk taraması (m.4)** — rakiplerle fiyat, kapasite, gelecek strateji, müşteri/bölge bilgisi paylaşımı kırmızı çizgidir; dernek toplantıları, kıyaslama çalışmaları ve ihale işbirlikleri ayrı ayrı taranır. Rekabete duyarlı bilginin akışı sınırlandırılır.
2. **Dikey risk taraması (m.4 + 2002/2 Tebliğ)** — yeniden satış fiyatının belirlenmesi (RSF) ve mutlak bölgesel koruma ağır kısıtlamadır; tavsiye fiyat/azami fiyat ile RSF ayrımı netleştirilir, online satış ve platform kısıtları gözden geçirilir.
3. **Hâkim durum riski (m.6)** — pazar payı yüksekse münhasırlık, sadakat indirimi, fiyat sıkıştırması, ayrımcılık ve bağlama uygulamaları nesnel haklılık ekseninde değerlendirilir; hâkim teşebbüsün özel sorumluluğu vurgulanır.
4. **Birleşme/işbirliği kontrolü (m.7)** — gelecek işlemler için bildirim eşiği erken kontrol; gun-jumping önleme.
5. **Yerinde inceleme (dawn raid) protokolü** — m.15 incelemesinde kapıda davranış, yasal danışmana ulaşma, belgelerin korunması, engelleme yasağı (silme/saklama nispi ceza ve karine riski); çalışan eğitimi.
6. **Pişmanlık refleksi** — ihlal tespit edilirse Pişmanlık Yönetmeliği kapsamında ilk başvuran avantajının iç prosedüre yerleştirilmesi.

## Çıktı modülleri
- Risk ısı haritası (yatay/dikey/hâkim durum/işlem).
- İç politika ve kırmızı-çizgi rehberi taslağı.
- Yerinde inceleme (dawn raid) eylem protokolü.
- Eğitim ve periyodik denetim takvimi önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

