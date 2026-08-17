---
argument-hint: ''
description: Vekâlet ücreti ve masrafların faturalanması, tahsil edilmesi, gecikmiş
  alacakların takibi ve avukatın hapis hakkı ile güvence stratejisi gerektiğinde kullanılır.
name: vekalet-ucreti-tahsilat
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
  - ad: Avukatlık Kanunu
    numara: '1136'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Vekâlet Ücreti Faturalama ve Tahsilat

## Görev
Hak edilen vekâlet ücreti ve masrafları doğru hesaplayıp faturalamak; tahsilatı yönetmek; gecikme halinde uygun hukuki yola (icra/dava) ve güvenceye karar vermek.

## Soğuk başlangıç (intake)
1. Sözleşmede ücret tipi (maktu/nispi/saatlik) ve ödeme planı ne; yazılı sözleşme var mı?
2. İş hangi aşamada bitti/kesildi; hak edilen tutar nedir, kısmi tahsilat oldu mu?
3. Karşı taraf vekâlet ücreti hükmedildi mi, tahsil edildi mi?
4. Müvekkil ödemede mi temerrütte; elde dosya/evrak (hapis hakkı) var mı?

## Denetim şeması
1. **Hak edilen ücretin tespiti (1136 m.163-164)**: Sözleşmedeki tutar; sözleşme yoksa Avukatlık Asgari Ücret Tarifesi. İşin tamamlanma derecesine göre hak ediş belirlenir.
2. **Karşı taraf vekâlet ücreti (1136 m.164/son)**: Yargılama gideri olarak hükmedilen tutar aksi kararlaştırılmadıkça avukata aittir; müvekkil bunu kendine mal edemez.
3. **Faturalama**: Serbest meslek makbuzu/fatura düzeni; KDV ve stopaj boyutu (mali müşavirle teyit). Masraflar ayrı kalemlenir.
4. **Temerrüt ve faiz (TBK m.117, 120)**: Muacceliyet/ihtar ile temerrüt; ticari/adi faiz ayrımı, sözleşmesel faiz şartı.
5. **Güvence — hapis hakkı (1136 m.166)**: Avukat, müvekkile ait olup elinde bulunan evrak ve değerler üzerinde ücret ve masraf alacağı için hapis hakkına sahiptir; sınırları gözetilerek kullanılır.
6. **Takip yolu**: Yazılı sözleşme/makbuz varsa ilamsız icra (İİK m.42 vd.) veya alacak davası; itiraz halinde itirazın iptali (İİK m.67, 1 yıl) değerlendirilir.
7. **Ara sonuç**: Hak ediş netse fatura kesilir, ödenmezse ihtar + uygun takip yolu seçilir.

## Çıktı modülleri
- Ücret/masraf hesap dökümü ve fatura kalemleri.
- İhtarname taslağı ([doldurulacak] tutar, vade, faiz).
- Takip yolu önerisi (icra/dava) ve hapis hakkı değerlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

