---
argument-hint: ''
description: Bir şirket için sıfırdan KVKK uyum programı kurulurken ya da mevcut uyumda
  boşluk analizi yapılırken; envanter, politika seti, sözleşme zinciri ve rol yapısı
  bütüncül tasarlanırken kullanılır.
name: uyum-programi-tasarimi
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


# Kurumsal KVKK Uyum Programı Tasarımı

## Görev
Veri sorumlusu kuruluş için uçtan uca KVKK uyum programını tasarlamak: kişisel veri envanterinden politika setine, sözleşme zincirinden eğitim ve denetime kadar bütünsel uyum mimarisi kurmak.

## Soğuk başlangıç (intake)
1. Kuruluşun sektörü, ölçeği ve işlediği başlıca veri kategorileri nedir?
2. Mevcutta hangi belgeler var (aydınlatma, rıza, politika, VERBİS)?
3. Veri işleyen/alt yüklenici zinciri ve yurt dışı aktarım var mı?
4. İç organizasyon nasıl — irtibat kişisi, komite, sorumluluk dağılımı var mı?

## Denetim şeması
1. **Envanter — temel taş**: Kişisel veri işleme envanteri çıkarılır (faaliyet, veri kategorisi, amaç, hukuki sebep m.5/m.6, alıcı, aktarım, saklama süresi). Tüm diğer belgeler envanterle tutarlı olmak zorundadır.
2. **Hukuki sebep haritalama (m.4-5-6)**: Her işleme bir geçerli şarta bağlanır; açık rızaya gereksiz bağımlılık azaltılır, meşru menfaat için denge testleri belgelenir.
3. **Belge seti**: Aydınlatma metinleri (m.10), gerektiğinde açık rıza beyanları, Saklama ve İmha Politikası, Kişisel Veri İşleme ve Koruma Politikası, ilgili kişi başvuru prosedürü, veri ihlali müdahale planı (m.12).
4. **Sözleşme zinciri**: Veri işleyenlerle m.12 sözleşmeleri; yurt dışı aktarımda m.9 standart sözleşme/güvenceler; çalışan ve tedarikçi taahhütleri.
5. **VERBİS ve organizasyon**: m.16 kayıt yükümlülüğü kontrolü, irtibat kişisi atanması, iç rol ve yetki matrisi, periyodik eğitim ve denetim döngüsü.
6. **Ara sonuç**: Boşluk analizi her başlık için "var/eksik/güncelleme gerekli" olarak skorlanır ve önceliklendirilmiş eylem planına bağlanır.

İspat yükü (hesap verebilirlik): Veri sorumlusu, m.4 ilkelerine ve tüm yükümlülüklere uyumu belgelerle ispatlayabilmelidir; uyum, kâğıt değil işleyen süreç olarak kurulur.

## Çıktı modülleri
- Boşluk analizi (gap analysis) skor tablosu ve eylem planı.
- Politika ve belge seti yapılandırma listesi.
- Sözleşme zinciri ve aktarım haritası.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

