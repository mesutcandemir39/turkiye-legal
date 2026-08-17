---
argument-hint: ''
description: Patent/faydalı model hakkına tecavüz edilip edilmediği, hangi fiillerin
  tecavüz sayıldığı ve hangi taleplerin ileri sürülebileceği değerlendirildiğinde
  kullanılır; hak sahibinin saldırı stratejisi içi
name: tecavuz-tespiti-ve-talepler
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Patent Hakkına Tecavüz Tespiti ve Talepler

## Görev
SMK m.141 kapsamında tecavüz fiilini saptamak ve SMK m.149-151 uyarınca ileri sürülebilecek talepleri (tespit, men, ref, tazminat, el koyma, imha) belirlemek.

## Soğuk başlangıç (intake)
1. Hakka konu patent/faydalı model geçerli ve ayakta mı (yıllık ücretler ödendi mi)?
2. Karşı tarafın fiili ne: üretim, satış, kullanım, ithalat, stoklama, dolaylı tecavüz?
3. Tecavüz iddiası hangi istem(ler)e dayanıyor; eşdeğer mi literal mi?
4. Zarar/yoksun kazanç verisi, lisans bedeli emsali var mı?

## Denetim şeması
1. **Hakkın geçerliliği ve ayakta olması.** Belge verilmiş, hükümsüz kılınmamış ve yıllık ücretleri ödenmiş olmalı (SMK m.101). Faydalı modelde tecavüz davası açılırken araştırma raporu talebi gerekebileceğini değerlendir.
2. **Tecavüz fiili (SMK m.141).** İzinsiz üretim, satışa sunma, satma, kullanma, ithalat, ticari amaçla elde bulundurma; usul patentinde usulün kullanımı ve doğrudan elde edilen ürün; ayrıca dolaylı/araç sağlama yoluyla tecavüz. Ara sonuç: fiil m.141 kapsamında mı?
3. **Kapsam denetimi.** Fiil, istem yorumu (SMK m.89) ile koruma kapsamına giriyor mu? Bu, istem-ürün eşleştirmesiyle yapılır (bkz. istem yorumu becerisi).
4. **Savunma süzgeci.** Önceki kullanım hakkı (SMK m.87), tüketilme (SMK m.152), hükümsüzlük def'i, deneme amaçlı/özel kullanım istisnaları (SMK m.85/3) karşı tarafın elinde mi?
5. **Talepler (SMK m.149).** Tespit, muhtemel tecavüzün önlenmesi, durdurma (men), giderme (ref), tazminat (maddi/manevi), el koyma/imha, kararın ilanı. Tazminatta yoksun kalınan kazanç SMK m.151 üç yöntemden biriyle (lisans analojisi dahil) hesaplanır.

## Çıktı modülleri
- Tecavüz fiili nitelendirmesi (m.141 hangi bent).
- İstem-ürün kapsam eşleştirmesi özeti.
- Karşı tarafın savunma/def'i envanteri.
- Talep listesi ve tazminat hesap yöntemi önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

