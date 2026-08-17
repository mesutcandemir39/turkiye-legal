---
argument-hint: ''
description: Bir KVKK uyum taraması başlatılırken kapsamın, denetlenecek birim ve
  sistemlerin, rol tespitinin ve denetim yönteminin sabitlenmesi gerektiğinde kullanılır.
name: denetim-kapsami-ve-yontem
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Denetim Kapsamı ve Yöntem Belirleme

## Görev
KVKK uyum taramasının iskeletini kurmak: neyin, hangi rol bakımından, hangi kanıtlarla ve hangi skorlama mantığıyla denetleneceğini yazılı olarak sabitlemek. Kapsamı tanımlanmamış denetim, bulgu üretmez.

## Soğuk başlangıç (intake)
1. Denetlenen kuruluşun sektörü, çalışan sayısı ve işlediği başlıca veri kategorileri nedir?
2. Tarama tüm kuruluşu mu, yoksa belirli birim/süreçleri (İK, pazarlama, müşteri hizmetleri) mi kapsıyor?
3. Kuruluş bu süreçlerde veri sorumlusu mu, veri işleyen mi?
4. Daha önce denetim yapıldı mı, açık bulgu var mı, hangi belgeler hazır?

## Denetim şeması
1. **Rol tespiti (KVKK m.3)**: Kapsamdaki her faaliyet için veri sorumlusu/veri işleyen sıfatı belirlenir; yükümlülükler asıl olarak sorumluya düşer, işleyene m.12 sözleşmesiyle aktarılan kısımlar ayrı izlenir.
2. **Kapsam matrisi**: Birim × süreç × sistem (CRM, İK yazılımı, web sitesi, çağrı merkezi, bulut/SaaS) tablosu çıkarılır; her hücre denetim kalemine dönüşür.
3. **Kanıt kuralı**: Her kontrol maddesi için beyan değil belge istenir (politika, ekran görüntüsü, log, sözleşme). Belge yoksa bulgu "Uygunsuz" kabul edilir; hesap verebilirlik ispat yükü veri sorumlusundadır (m.4 — accountability).
4. **Skorlama tanımı**: Her madde "Uygun / Kısmen / Uygunsuz / Kapsam dışı"; risk = olasılık × etki (yaptırım m.18 + itibar + ilgili kişi zararı).
5. **Ara sonuç**: Kapsam, rol ve skorlama mantığı yazıya dökülmeden kanıt toplamaya geçilmez; aksi halde bulgular karşılaştırılamaz.

İspat yükü: Uyumu belgelerle ispat yükümlülüğü veri sorumlusundadır; denetçi yokluk halinde uygunsuzluk lehine karine kurar.

## Çıktı modülleri
- Denetim kapsam ve rol tanımı belgesi.
- Birim/süreç/sistem kapsam matrisi.
- Skorlama ve kanıt kuralı tanım sayfası.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

