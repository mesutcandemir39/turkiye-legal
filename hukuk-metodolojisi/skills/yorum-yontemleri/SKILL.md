---
argument-hint: ''
description: Bir kanun hükmünün ne anlama geldiği tartışmalı olduğunda; lafzı belirsiz,
  çok anlamlı ya da amacıyla çatışır göründüğünde dört yorum yöntemini sırayla uygulamak
  için kullanılır.
name: yorum-yontemleri
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
    madde: '1'
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yorum Yöntemleri (Lafzî, Sistematik, Tarihsel, Amaçsal)

## Görev
Bir normun anlamını TMK m.1 çerçevesinde, kabul gören dört yorum yöntemini birlikte kullanarak ortaya koymak; lafız ile amaç çatıştığında gerekçeli bir tercih yapmak.

## Soğuk başlangıç (intake)
- Hangi kanunun hangi madde/fıkra/bendi tartışmalı? Tam metni elimizde mi?
- Tereddüt nereden doğuyor: kelimenin çok anlamlılığı mı, sessizlik mi, başka hükümle çelişki mi?
- Bu bir özel hukuk normu mu, ceza/idare gibi yorum yasaklarının sıkı olduğu bir alan mı?
- Tarafların savunduğu iki rakip okuma nedir?

## Denetim şeması
1. **Lafzî (sözel) yorum** — TMK m.1: önce metnin olağan dil anlamı ve hukuk dilindeki teknik anlamı. Hükmün "açık" görünmesi yorumu bitirmez; lafız sadece başlangıç ve dış sınırdır.
2. **Sistematik yorum** — Hükmü bulunduğu kanun içindeki yerine, başlık/kenar başlığına, yollamalara (örn. TMK m.5 ile genel hükümlerin yayılması) ve üst normlara göre oku. Çelişkide *lex specialis*, *lex superior*, *lex posterior* kurallarını uygula.
3. **Tarihsel yorum** — Madde gerekçesi, kanunun hazırlık çalışmaları, İsviçre/Alman kaynak hükümle karşılaştırma ve önceki düzenlemeyle fark. Kaynak kanun yorumu yol gösterir ama bağlamaz.
4. **Amaçsal (gai/teleolojik) yorum** — Normun koruduğu menfaat ve güttüğü amaç (ratio legis). Menfaatler içtihadı ile çatışan menfaatleri tart. Anayasaya ve AİHS'e uygun yorum (Anayasa m.11, m.90/5) tercih edilir.
5. **Sentez ve sınır** — Yöntemler çatışırsa amaçsal sonuç genellikle üstün tutulur; ancak lafzın olası anlamı aşılırsa bu artık yorum değil hukuk yaratma/kıyas olur (ayrı beceri). Ceza ve vergi gibi kanunilik ağır basan alanlarda lafzın dışına çıkan genişletici yorumdan kaçın (TCK m.2).

## Çıktı modülleri
- Tartışılan hüküm ve iki rakip okumanın tablosu.
- Dört yöntemin her birinin sonucu ve ağırlığı.
- Gerekçeli tercih + karşı argümana cevap.
- Atıf taslağı: ilke + `[DOĞRULANMADI]` künye yeri (karararama.yargitay.gov.tr).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

