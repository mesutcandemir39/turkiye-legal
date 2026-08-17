---
argument-hint: ''
description: Sigortacıya ön başvuru, Sigorta Tahkim Komisyonu başvurusu, dava veya
  cevap dilekçesi gibi sigorta uyuşmazlığına özgü belgelerin taslaklanması istendiğinde
  kullanılır; doğru hukuki sebep ve talep mima
name: dilekce-basvuru-taslagi
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  - ad: Bankalar Kanunu
    numara: '5684'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Başvuru ve Dilekçe Taslakları (Sigortacıya Başvuru, Tahkim, Dava)

## Görev
Sigorta uyuşmazlığına özgü belgeleri usulüne uygun taslaklamak: sigortacıya zorunlu ön başvuru, Sigorta Tahkim Komisyonu başvurusu, dava dilekçesi veya cevap dilekçesi; vakıa-hukuki sebep-talep mimarisini kurmak.

## Soğuk başlangıç (intake)
1. Hangi belge isteniyor (ön başvuru / tahkim / dava / cevap)?
2. Taraflar, poliçe bilgileri, riziko ve talep tutarı belli mi?
3. Forum seçildi mi (tahkim/ticaret/tüketici) ve başvuru şartı tamam mı?
4. Hangi deliller mevcut (poliçe, eksper raporu, kaza tutanağı, ödeme kanıtı)?

## Denetim şeması
1. **Belge türü ve dayanak.** Ön başvuru için KTK m.97 / 5684 m.30 başvuru şartı; tahkim için 5684 m.30; dava için HMK m.119 zorunlu unsurları. Ara sonuç: hangi format ve zorunlu unsurlar?
2. **Vakıa ve hukuki sebep.** Riziko, teminat ve ihlal vakıaları kronolojik; hukuki sebepler madde atıflı (örn. TTK m.1409/1421 teminat, m.1459 tazminat, m.1472 halefiyet, KTK m.91/97 doğrudan hak).
3. **Talep sonucu.** Net, miktar belirten talep; alacak likitse kesin, değilse belirsiz alacak/kısmi dava tercihi (HMK m.107-109); faiz başlangıcı ve türü (temerrüt/avans faizi).
4. **Delil bağlama.** Her vakıayı bir delile bağla; bilirkişi ve eksper raporu talebi; eksik belgeler için `[doldurulacak]` yer tutucu.
5. **Usul kontrolü.** Görev-yetki, harç/gider, zamanaşımı/hak düşürücü süre, başvuru şartı tamamlığı son kez doğrulanır.

## Çıktı modülleri
- İstenen belgenin tam taslağı (başlık, taraflar, açıklamalar, hukuki sebepler, deliller, talep sonucu).
- Madde atıflı hukuki sebep listesi.
- Delil dizini ve `[doldurulacak]` eksik belge listesi.
- Süre/usul uyarı notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

