---
argument-hint: ''
description: Rekabet hukukunun yapısını, 4054 sayılı Kanunun üç ekseni ile temel kavramları
  (teşebbüs, hâkim durum, ilgili pazar) anlamak ve bir olayı doğru eksene yerleştirmek
  istendiğinde kullanılır; ilk teşhis
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
  - ad: Rekabetin Korunması Hakkında Kanun
    numara: '4054'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Sistematik

## Görev
Rekabet hukuku sorununu 4054 sayılı Kanunun sistematiğine oturtmak; teşebbüs, ilgili pazar, hâkim durum gibi temel kavramları somut olaya uygulayarak doğru denetim eksenini (m.4 / m.6 / m.7) belirlemek.

## Soğuk başlangıç (intake)
- Sorun bir anlaşma/işbirliği mi, tek bir teşebbüsün tek taraflı davranışı mı, yoksa bir birleşme/devralma işlemi mi?
- Taraflar kim; teşebbüs sıfatı taşıyorlar mı; faaliyet gösterilen mal/hizmet ve coğrafi alan nedir?
- Yaklaşık pazar payları ve rakipler biliniyor mu?
- Talep eden konumu: müvekkil ihlalci taraf mı, mağdur/şikâyetçi mi, işlem yapan mı?

## Denetim şeması
1. **Teşebbüs sıfatı (4054 m.3)** — ekonomik faaliyet yürüten her birim teşebbüstür; hukuki forma bakılmaz. Aynı ekonomik bütünlük içindeki şirketler tek teşebbüs sayılabilir (grup içi anlaşmalar m.4 kapsamı dışıdır).
2. **Üç eksenden hangisi?**
   - Birden çok teşebbüs arası irade uyuşması/koordinasyon → **m.4** (anlaşma, uyumlu eylem, teşebbüs birliği kararı).
   - Tek teşebbüsün pazar gücüne dayalı davranışı → **m.6** (hâkim durum testi sonrası).
   - Kontrol değişikliği doğuran yoğunlaşma → **m.7** (eşik kontrolü).
3. **İlgili pazar tanımı** — İlgili Pazarın Tanımlanmasına İlişkin Kılavuz uyarınca ürün pazarı (talep/arz ikamesi, SSNIP mantığı) ve coğrafi pazar. Pazar dar tanımlanırsa pay yükselir; bu nedenle her tarafça stratejik bir adımdır.
4. **Pazar gücü göstergeleri** — pazar payı, giriş engelleri, alıcı gücü, HHI yoğunlaşması. Hâkim durum (m.6) ve yoğunlaşma değerlendirmesi (m.7) bu göstergelere dayanır.
5. **Ara sonuç** — olayın hangi eksende, hangi ilgili pazarda ve hangi pay/güç düzeyinde olduğu netleştirilir; ispat yükü kural olarak ihlal iddiasında bulunan/Kurul'dadır, muafiyet iddiasında ise teşebbüstedir (m.5).

## Çıktı modülleri
- Olay-eksen eşleştirme tablosu (m.4/m.6/m.7).
- Ön ilgili pazar taslağı ve pay tahmini.
- Sonraki adım önerisi: ilgili uzman beceriye yönlendirme (kartel, hâkim durum, birleşme, muafiyet, usul).
- Açık veri eksiklikleri ve doğrulanacak hususlar listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

