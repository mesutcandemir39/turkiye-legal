---
argument-hint: ''
description: Aile hukuku dosyasına ilk girişte statü, ilişki ve uygulanacak rejim
  haritasını çıkarmak; hangi alt-konunun (evlilik, boşanma, velayet, nafaka, mal rejimi,
  soybağı, koruma) devreye gireceğini ayırt et
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  - ad: Ailenin Korunması ve Kadına Karşı Şiddetin Önlenmesine Dair Kanun
    numara: '6284'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Aile Hukuku Temel Kavramlar ve Sistematik

## Görev
Olayı TMK İkinci Kitap sistematiğine yerleştirmek; evlilik hukuku, hısımlık (soybağı/velayet/nafaka) ve vesayet eksenlerinden hangisinin devreye girdiğini, görevli mahkemeyi ve uygulanacak mal rejimini belirleyerek doğru alt-beceriye yönlendirmek.

## Soğuk başlangıç (intake)
1. Taraflar evli mi, nişanlı mı, evlilik dışı birliktelik mi; evliyse evlenme tarihi nedir?
2. Müşterek çocuk var mı, varsa yaşları ve kiminle yaşıyor?
3. Talep ne: boşanma, nafaka, velayet, mal paylaşımı, soybağı mı yoksa şiddet/koruma mı?
4. Açılmış dava/başvuru, geçici tedbir kararı veya yurt dışı/yabancı unsur var mı?

## Denetim şeması
1. **İlişki tipi.** Evlilik geçerli ve devam ediyorsa TMK m.185 vd. (evlilik birliği) uygulanır; butlan iddiası varsa mutlak (m.145) / nispi (m.148) butlan ayrımı yapılır. Evlilik dışı ilişkide soybağı (m.295, m.301) ve velayet (m.337) ekseni öne çıkar.
2. **Mal rejimi tespiti.** 01.01.2002 sonrası evliliklerde yasal rejim edinilmiş mallara katılmadır (m.202). Daha eski evliliklerde 4722 sK. yürürlük hükümleri ve eski mal ayrılığı dönemi dikkate alınır. Eşler sözleşmeyle (m.203) başka rejim seçmiş olabilir; tarih ve rejim türü hesabın temelidir.
3. **Çocuk varsa.** Velayet (m.335-336), kişisel ilişki (m.182-183) ve iştirak nafakası (m.182, m.328) birlikte değerlendirilir; çocuğun üstün yararı (m.339 vd.) süzgeçtir.
4. **Aciliyet.** Şiddet/tehdit varsa 6284 sK. tedbirleri (m.4, m.5, m.8) önceliklidir; boşanma davasıyla paralel yürür.
5. **Görev-yetki ara sonucu.** Görevli mahkeme aile mahkemesidir (4787 sK.); yetki boşanmada TMK m.168'e göre saptanır.

## Çıktı modülleri
- Statü ve ilişki haritası (evlilik/çocuk/mal rejimi/tarih tablosu).
- İlgili alt-beceri yönlendirmesi ve görev-yetki notu.
- Aciliyet bayrağı (6284 gerekiyor mu) ve ilk süre uyarıları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

