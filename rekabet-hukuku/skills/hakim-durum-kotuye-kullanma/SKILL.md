---
argument-hint: ''
description: Bir teşebbüsün pazar gücüne dayanarak dışlayıcı (yıkıcı fiyat, fiyat
  sıkıştırması, münhasırlık, bağlama, ayrımcılık) veya sömürücü davranışta bulunduğu
  iddialarını 4054 m.6 çerçevesinde değerlendirmek
name: hakim-durum-kotuye-kullanma
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


# Hâkim Durumun Kötüye Kullanılması (m.6)

## Görev
Önce ilgili pazarda hâkim durumun varlığını tespit etmek, ardından söz konusu tek taraflı davranışın 4054 m.6 anlamında kötüye kullanma oluşturup oluşturmadığını ve nesnel haklılık savunmasını değerlendirmek.

## Soğuk başlangıç (intake)
- Teşebbüsün ilgili pazardaki yaklaşık payı ve konumu nedir; rakip ve giriş engeli durumu?
- İddia edilen davranış: yıkıcı/aşırı fiyat, fiyat sıkıştırması, münhasırlık, bağlama, mal vermeyi reddetme, ayrımcılık mı?
- Davranış dışlayıcı mı (rakip dışlama) yoksa sömürücü mü (müşteri sömürüsü)?
- Müvekkil hâkim teşebbüs mü, yoksa dışlanan rakip/şikâyetçi mi?

## Denetim şeması
1. **İlgili pazar + hâkimlik (m.3, m.6)** — ilgili pazar tanımlanır; hâkim durum, pazarda rakiplerden ve müşterilerden bağımsız hareket edebilme gücüdür. Yüksek pazar payı kuvvetli gösterge olmakla birlikte tek başına belirleyici değildir; giriş engelleri, dengeleyici alıcı gücü ve dikey bütünleşme birlikte değerlendirilir.
2. **Davranışın nitelendirilmesi** — m.6 bentleri örnek niteliğindedir:
   - Dışlayıcı: yıkıcı fiyat, fiyat sıkıştırması (marj sıkıştırması), münhasır alım/satım, sadakat indirimleri, bağlama-paketleme, mal/hizmet vermeyi reddetme (zorunlu unsur doktrini), ayrımcı koşullar.
   - Sömürücü: aşırı/adil olmayan fiyat ve haksız ticari koşullar dayatma.
3. **Etki analizi** — kötüye kullanma için kural olarak pazarı kapama/dışlama etkisi veya tüketici zararı gösterilmelidir; uygun rakip (as-efficient competitor) testi gibi iktisadi araçlar kullanılır.
4. **Nesnel haklılık ve etkinlik savunması** — davranışın nesnel olarak haklı olduğu veya etkinlik kazanımı sağladığı ileri sürülebilir; ispat yükü bu noktada teşebbüse geçer.
5. **Ara sonuç ve yaptırım** — hâkimlik yoksa m.6 uygulanmaz (davranış m.4 açısından incelenebilir). Hâkimlik + kötüye kullanma + etki varsa ihlal; ceza ciro üzerinden (m.16), ayrıca özel hukukta tazminat (m.57-58).

## Çıktı modülleri
- Hâkimlik analizi (pay, engeller, bağımsız hareket gücü).
- Davranış-tip eşleştirmesi ve dışlama/sömürü ayrımı.
- Nesnel haklılık savunması taslağı veya saldırı argümanları.
- Doğrulanacak Kurul/Danıştay kararı atıfları `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

