---
argument-hint: ''
description: Elektronik haberleşme hizmeti sunmak için bildirim veya kullanım hakkı
  türü yetkilendirme, işletmeci yükümlülükleri, kaynak tahsisi ve yetkilendirme iptali/iadesi
  değerlendirildiğinde ve BTK yetkilend
name: yetkilendirme-isletmeci-uyum
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
  - ad: Telekomunikasyon Kanunu
    numara: '5809'
    tur: kanun
  - ad: Elektronik Ticaretin Düzenlenmesine Dair Kanun
    numara: '5651'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yetkilendirme ve İşletmeci Uyum Şeması

## Görev
Bir elektronik haberleşme faaliyetinin doğru yetkilendirme türüne tabi olup olmadığını, işletmeci yükümlülüklerinin yerine getirilip getirilmediğini ve iptal/iade riskini denetleyerek BTK uyum yol haritası çıkarmak.

## Soğuk başlangıç (intake)
1. Sunulan hizmet türü nedir (sabit/mobil, internet servis sağlayıcılığı, altyapı, sanal mobil, katma değerli)?
2. Yetkilendirme türü: bildirime mi yoksa kullanım hakkına mı (frekans/numara/uydu pozisyonu kaynak tahsisi gerektiren) tabi?
3. Yetkilendirme alındı mı, hangi tarihli; kaynak tahsisi (frekans/numara) var mı?
4. BTK'ya bildirim, ücret ve raporlama yükümlülükleri güncel mi?

## Denetim şeması
1. **Yetkilendirme gerekliliği ve türü**: 5809 m.8-9 — kaynak tahsisi gerektirmeyen hizmetler bildirim, frekans/numara/uydu pozisyonu gibi sınırlı kaynak gerektirenler kullanım hakkı kapsamındadır. Yetkilendirme Yönetmeliği eşik ve usulü belirler. Ara sonuç: bildirim mi kullanım hakkı mı.
2. **Başvuru ve şartlar**: Bildirimde BTK'ya beyan; kullanım hakkında ihale/tahsis usulü, idari ücret ve kullanım hakkı ücreti. İspat ve belge yükü başvurucudadır; eksiklik ret/iade doğurur.
3. **Yükümlülükler**: 5809 — idari ücret, evrensel hizmet katkısı, raporlama, tüketici hakları (m.47-50) ve gizlilik (m.51) uyumu; tesis paylaşımı/arabağlantı (m.17-21) yükümlülükleri ilgili pazarda etkin piyasa gücüne (EPG) bağlı olabilir.
4. **Tadil/yenileme/iade**: Yetkilendirme süresi, yenileme ve devir BTK iznine tabi; kaynak iadesi ve hizmet sonlandırmada abone koruma yükümlülükleri gözetilir.
5. **İptal/sona erme**: Yükümlülük ihlali, ücret ödenmemesi veya kaynak amacına aykırı kullanım yetkilendirme iptalini doğurabilir; iptal idari işlem olduğundan İYUK m.7 süresinde dava ve m.27 yürütmenin durdurulması değerlendirilir.

İlkesel içtihat için BTK yetkilendirme/iptal uyuşmazlıklarında karararama.danistay.gov.tr (13. Daire ağırlıklı) taranır; künye doğrulanmadan [DOĞRULANMADI] işaretlenir.

## Çıktı modülleri
- Yetkilendirme uyum kontrol listesi (yükümlülük/durum/eksik).
- Kaynak tahsisi ve ücret riski tablosu.
- Tadil/yenileme başvurusu veya iptale karşı dava stratejisi taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

