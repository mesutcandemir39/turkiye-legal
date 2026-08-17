---
argument-hint: ''
description: Mevduat/katılım hesabı, hesaptan yetkisiz çekim, havale-EFT hatası, dolandırıcılıkla
  yapılan transfer veya bankanın özen yükümlülüğü ihlali iddialarını değerlendirmek
  ve bankanın sorumluluğunu denetle
name: mevduat-havale-hesap
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
  requires_human_review: true
  risk_level: high
  sources:
  - ad: Bankacılık Kanunu
    numara: '5411'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Mevduat, Hesap ve Havale/EFT Uyuşmazlıkları

## Görev
Mevduat/hesap ilişkisinden doğan uyuşmazlıklarda (yetkisiz çekim, hatalı/dolandırıcılıkla yapılan havale-EFT, hesap bloke, faiz işletme) bankanın özen ve iade yükümlülüğünü, müşterinin kusurunu ve sorumluluğun dağılımını belirlemek.

## Soğuk başlangıç (intake)
- Hesap türü: vadesiz/vadeli mevduat, katılım fonu, ticari hesap?
- Olay: yetkisiz para çekme, sahte talimatla havale, EFT'nin yanlış hesaba gitmesi, internet/mobil bankacılık dolandırıcılığı mı?
- Müşterinin bilgi/şifre paylaşımı, ihmal veya talimatı var mı; banka bildirim/doğrulama yapmış mı?
- Zarar tutarı ve bankaya bildirim tarihi nedir?

## Denetim şeması
1. **İlişkinin niteliği**: Mevduat, banka açısından usulsüz tevdi/karz benzeri ilişkidir; banka parayı iade ve hesabı doğru tutma borcu altındadır. Banka, basiretli bir tacir gibi yüksek özen yükümlülüğü taşır (TTK m.18/2; TBK m.506/2 benzeri özen ölçütü).
2. **Yetkisiz işlem ve ispat**: Hesaptan çıkan parada bankanın geçerli bir talimata dayandığını ve kimlik/doğrulama kontrolünü yaptığını ispatı gerekir. Sahtecilik/yetkisiz işlemde kural, bankanın kusursuz sorumluluğa yakın ağır özen sorumluluğudur; Yargıtay yerleşik içtihadı bankanın objektif özen ölçüsüyle sorumlu tutulduğu yönündedir [doğrulanacak — karararama.yargitay.gov.tr, 11. HD].
3. **Müşterinin kusuru ve birlikte kusur**: Müşterinin şifre/OTP paylaşımı, oltalama bağlantısına bilgi girmesi gibi ağır kusuru varsa TBK m.52 uyarınca tazminattan indirim veya sorumluluğun kalkması gündeme gelir. Banka ile müşteri kusuru oranlanır.
4. **Havale/EFT (TBK m.555-560)**: Havalede bankanın talimata uygunluğu, yanlış hesaba transferde sebepsiz zenginleşen lehtara karşı iade (TBK m.77 vd.) ve bankanın aracı sorumluluğu değerlendirilir.
5. **Süre ve usul**: Sözleşmeden doğan iade talebinde zamanaşımı kural olarak TBK m.146 (10 yıl); haksız fiil unsuru varsa TBK m.72 süreleri. Ara sonuç olarak bankanın/müşterinin sorumluluk payını ve talep edilebilir tutarı yaz.

## Çıktı modülleri
- Sorumluluk ve birlikte kusur analizi.
- İspat yükü dağılımı tablosu (bankadan istenecek kayıtlar).
- Talep/dava ya da bankaya başvuru taslağı iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

