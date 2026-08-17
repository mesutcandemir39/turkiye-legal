---
argument-hint: ''
description: Hacizli malın borçluya değil üçüncü kişiye ait olduğu iddiası (istihkak)
  ya da başka alacaklının hacze iştiraki gündeme geldiğinde; istihkak prosedürü, ispat
  yükü, mülkiyet karinesi ve sıraya katılma
name: istihkak-ve-hacze-istirak
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
  - ad: İcra ve İflas Kanunu
    numara: '2004'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İstihkak ve Hacze İştirak

## Görev
Haczedilen mal üzerinde üçüncü kişinin mülkiyet/rehin iddiasını (istihkak, m.96-99) çözmek; takibe sonradan katılan alacaklının hacze iştirakini (m.100, m.101) ve sıraya etkisini yönetmek.

## Soğuk başlangıç (intake)
- İstihkak iddiasında bulunan kim; mal kimin elinde haczedildi (zilyetlik)?
- Mal borçlu ile aynı çatı/işyerinde mi (karine yönü)?
- İddia haciz sırasında mı, sonra mı ileri sürüldü (3 günlük bildirim)?
- İştirak eden alacaklının ilk haciz tarihiyle ilişkisi nedir?

## Denetim şeması
1. **Zilyetlik karinesi (m.97/a)**: Haciz sırasında malı elinde bulunduran lehine mülkiyet karinesi vardır. Mal borçlunun elinde haczedilmişse istihkak iddia eden üçüncü kişi mülkiyetini ispatla yükümlüdür; üçüncü kişinin elinde haczedilmişse ispat yükü alacaklıdadır.
2. **Usul (m.96-99)**: İstihkak iddiası icra dairesine bildirilir; icra müdürü dosyayı icra mahkemesine gönderir. Takibin devamı/talikine mahkeme karar verir (m.97). İstihkak davası süresinde açılmazsa iddiadan vazgeçilmiş sayılır.
3. **Hacze iştirak (m.100)**: Borçluya karşı önce takip yapan alacaklının haczine, belirli belgelere dayanan diğer alacaklılar adi olarak iştirak edebilir; iştirak sırayı ve paylaşımı etkiler.
4. **İmtiyazlı iştirak (m.101)**: Eş, çocuk, vasi/kayyım gibi kişilerin belirli alacakları için özel iştirak imkânı denetlenir.
5. **İspat ve karine çatışması**: Muvazaa iddiası (özellikle aile/şirket içi devirler) ayrıca incelenir; gerektiğinde tasarrufun iptali becerisine geçilir.
6. **Ara sonuç**: İstihkakın akıbeti ve iştirakle oluşacak yeni sıra/dağıtım belirlenir.

## Çıktı modülleri
- İstihkak davası/itiraz dilekçesi iskeleti.
- İspat yükü ve karine yönü analizi.
- Hacze iştirak talebi ve sıraya etki notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

