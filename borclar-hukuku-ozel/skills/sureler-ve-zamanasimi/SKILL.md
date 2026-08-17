---
argument-hint: ''
description: Hangi talep için hangi zamanaşımı veya hak düşürücü sürenin işlediğini,
  başlangıcını ve kesilme-durma hallerini belirlemek gerektiğinde; her sözleşme tipinin
  özel sürelerini genel kuraldan ayırmak içi
name: sureler-ve-zamanasimi
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İsimli Sözleşmelerde Süreler ve Zamanaşımı

## Görev
Talep bazında doğru süreyi (genel/özel zamanaşımı veya hak düşürücü ihbar süresi), başlangıç anını ve kesilme/durma hallerini belirlemek; sürenin niteliğini (zamanaşımı mı, hak düşürücü mü) ayırmak çünkü sonuçları farklıdır.

## Soğuk başlangıç (intake)
- Talebin türü ve hukuki dayanağı (ayıp, ücret, tazminat, iade)?
- Olayların tarihleri (teslim, kabul, ifa, fark etme)?
- Adi mi ticari mi tüketici işlemi mi?
- Kesen işlem var mı (dava, takip, ikrar)?

## Denetim şeması
1. **Genel zamanaşımı (m.146-147).** Kural 10 yıl; m.147 istisnaları 5 yıl: kira bedeli, vekâlet/komisyon/simsarlık ücreti, eser sözleşmesinden doğan alacaklar (bazı haller), serbest meslek/zanaatkâr alacakları. Önce talebin bu listeye girip girmediğine bakılır.
2. **Satışta ayıp (m.231).** 2 yıl; taşınmaz yapıda 5 yıl; satıcı ağır kusurlu/hileli ise süreyle korunmaz.
3. **Eserde ayıp (m.478).** 2 yıl; taşınmaz yapı 5 yıl; yüklenici ağır kusurlu ise 20 yıl.
4. **İhbar/hak düşürücü süreler.** Satışta gözden geçirme-ihbar (m.223), eserde m.477, ticari satışta TTK m.23/c (2/8 gün) hak düşürücüdür; geçirilirse kabul sayılır ve hâkim resen dikkate alır. Bunlar zamanaşımından ayrıdır.
5. **Başlangıç anı.** Zamanaşımı alacağın muaccel olduğu anda işler (m.149); ayıpta teslim/kabul; tazminatta zarar ve failin öğrenilmesi ilgili tipe göre belirlenir.
6. **Kesilme/durma (m.153-156).** Dava, takip, ikrar, hakeme başvuru keser; kesilince yeni süre işler. Durma halleri (m.153) sınırlı. İspat: zamanaşımı def'ini ileri süren taraf; kesilme/durmayı buna dayanan taraf ispatlar. Ara sonuç: her talep için tek bir nihai süre/tarih.

## Çıktı modülleri
- Talep-süre-başlangıç-kesilme tablosu.
- Zamanaşımı def'i / def'e cevap notu.
- Risk uyarısı (yakın dolan süreler için aksiyon listesi).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

