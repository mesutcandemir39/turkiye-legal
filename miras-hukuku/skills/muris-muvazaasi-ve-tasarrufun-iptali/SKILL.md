---
argument-hint: ''
description: Mirasbırakanın mirasçıdan mal kaçırmak için yaptığı görünüşte satış/devir
  işlemlerine ya da geçersiz vasiyetnameye karşı iptal/butlan davası kurarken; muvazaa,
  ehliyetsizlik, şekil sakatlığı ve irade
name: muris-muvazaasi-ve-tasarrufun-iptali
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
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Muris Muvazaası ve Ölüme Bağlı Tasarrufun İptali

## Görev
Mirastan mal kaçırma amaçlı muvazaalı sağlararası işlemleri ve geçersiz ölüme bağlı tasarrufları geçersiz kılmak; muris muvazaası (TBK m.19) ile vasiyet iptali (TMK m.557-559) yollarını ayırmak.

## Soğuk başlangıç (intake)
- İhtilaflı işlem sağlararası devir mi (tapuda satış/bağış), ölüme bağlı tasarruf mu?
- Devir bedeli gerçekten ödendi mi? Alıcının ödeme gücü ve akrabalık?
- Davacı saklı paylı mı, yoksa tüm mirasçı mı? (muvazaada herkes, tenkiste yalnız saklı paylı)
- Vasiyette şekil sakatlığı, ehliyetsizlik veya irade fesadı iddiası var mı?
- İşlemin/ölümün tarihi ve öğrenme tarihi?

## Denetim şeması
1. **Muris muvazaası (TBK m.19; 1.4.1974 t. 1/2 İBK çerçevesi):** Mirasbırakan, mirasçıdan mal kaçırmak için taşınmazı görünüşte satar ama gerçekte bağışlar. Görünüşteki sözleşme muvazaadan, gizli bağış şekil eksikliğinden geçersizdir; tapu iptali ve tescil istenir. Süreye/saklı pay şartına tabi değildir; tüm mirasçılar açabilir.
2. **Muvazaa ölçütleri:** Mirasbırakanın kaçırma saiki, bedel-değer dengesizliği, satış için makul ihtiyaç yokluğu, taraflar arası ilişki, ödeme delili yokluğu. Yargıtay yerleşik içtihadına bakılır — künyeler doğrulanmadan zikredilmemeli, karararama.yargitay.gov.tr'den `[DOĞRULANMADI]`.
3. **Tenkisten ayır:** Gerçek (gizleme amacı olmayan) bağışta muvazaa değil tenkis yolu işler. Sıralamada: önce muvazaa, başarısızsa terditli tenkis.
4. **Vasiyet iptali (m.557):** Ehliyetsizlik, irade sakatlığı (yanılma-aldatma-korkutma), hukuka/ahlaka aykırı içerik, şekle aykırılık. Hak düşürücü süre (m.559): iptal sebebi ve ölümün öğrenilmesinden 1 yıl, her hâlde iyiniyetlilere karşı 10, kötüniyetlilere 20 yıl.
5. **Ara sonuç:** doğru dava türü (iptal-tescil / vasiyet iptali / terditli tenkis), görev (asliye hukuk), yetki (taşınmaz — HMK m.12).

## Çıktı modülleri
- Tapu iptali ve tescil (muris muvazaası) dava dilekçesi taslağı
- Terditli tenkis talebi entegrasyonu
- Muvazaa karine ve delil listesi (tanık, ödeme, banka)
- Vasiyetnamenin iptali dava taslağı (süre uyarılı)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

