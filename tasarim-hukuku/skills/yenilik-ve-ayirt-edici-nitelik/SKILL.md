---
argument-hint: ''
description: Bir tasarımın SMK m.56-58 uyarınca yeni ve ayırt edici olup olmadığının
  bilgilenmiş kullanıcı ve seçenek özgürlüğü ölçütleriyle değerlendirilmesi; tescil
  başvurusu öncesi veya hükümsüzlük tartışmasınd
name: yenilik-ve-ayirt-edici-nitelik
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


# Yenilik ve Ayırt Edici Nitelik Denetimi

## Görev
Tasarımın korumaya değer olup olmadığını belirleyen iki maddi şartı denetlemek: yenilik (SMK m.56/4) ve ayırt edici nitelik (SMK m.56/5, m.57). Bu, hem başvuru stratejisinin hem de hükümsüzlük/tecavüz savunmasının çekirdeğidir.

## Soğuk başlangıç (intake)
1. İncelenen tasarımın tüm görselleri ve hangi ürüne uygulandığı elimizde mi?
2. Karşılaştırılacak önceki tasarım(lar) — kamuya sunma tarihi ve kaynağı nedir?
3. İlgili sektörde tasarımcının seçenek özgürlüğü ne kadar geniş (teknik kısıt yoğunluğu)?
4. Tasarım sahibinin kendi açıklaması var mı (12 aylık grace period uygulanır mı)?

## Denetim şeması
1. Başvuru/rüçhan tarihini sabitle (SMK m.56/6): Karşılaştırma anı budur. Rüçhan varsa rüçhan tarihi esas alınır.
2. Yenilik (SMK m.56/4): Aynı tasarım, başvuru/rüçhan tarihinden önce dünyanın herhangi bir yerinde kamuya sunulmamış olmalı. "Yalnızca küçük ayrıntılarda farklılık" aynılık sayılır. İspat yükü yeniliğin yokluğunu iddia edende (hükümsüzlük davacısı).
3. Kamuya sunmanın istisnası (SMK m.58/3): Başvurudan önceki 12 ay içinde tasarımcının/halefinin/kötüye kullananın açıklaması yeniliği bozmaz (grace period). Bu süreyi titizlikle hesaplayın.
4. Ayırt edici nitelik (SMK m.56/5, m.57/1): Bilgilenmiş kullanıcıda bıraktığı genel izlenim, önceki tasarımların bıraktığından farklı olmalı. Değerlendirme bütünsel genel izlenime göre yapılır; ayrıntı farkları tek başına yetmez.
5. Seçenek özgürlüğü (SMK m.57/2): Tasarımcının seçenek özgürlüğü dar olan sektörlerde küçük farklar ayırt ediciliği sağlayabilir; geniş olduğunda daha belirgin fark aranır. Teknik/standart kısıtları belgeleyin.
6. Koruma dışı: Teknik zorunluluğun dayattığı görünüm ve zorunlu ara bağlantı (SMK m.58/4) yenilik/ayırt edicilikten önce eler.
7. Ara sonuç: Her iki şart için ayrı ayrı "karşılanıyor/karşılanmıyor" ve gerekçe; bilgilenmiş kullanıcının kim olduğu mutlaka tanımlanır.

## Çıktı modülleri
- Yenilik ve ayırt edicilik kontrol cetveli (önceki tasarım vs. dava konusu, fark analizi).
- Bilgilenmiş kullanıcı profili ve seçenek özgürlüğü değerlendirmesi.
- Grace period takvimi ve sonuç notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

