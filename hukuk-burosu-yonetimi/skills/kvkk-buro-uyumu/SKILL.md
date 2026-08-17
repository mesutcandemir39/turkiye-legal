---
argument-hint: ''
description: Hukuk bürosunun veri sorumlusu olarak KVKK yükümlülüklerini kurgularken;
  aydınlatma, saklama-imha, VERBİS, aktarım ve veri ihlali süreçlerini denetlerken
  kullanılır.
name: kvkk-buro-uyumu
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


# Büro KVKK Uyumu

## Görev
Hukuk bürosunun veri sorumlusu sıfatıyla kişisel veri işleme faaliyetlerini KVKK'ya uygun hale getirmek: işleme şartı, aydınlatma, güvenlik, saklama-imha, aktarım ve ihlal yönetimi.

## Soğuk başlangıç (intake)
1. Büro hangi veri kategorilerini işliyor (müvekkil, karşı taraf, tanık, çalışan; özel nitelikli veri var mı)?
2. Veriler nerede tutuluyor (UYAP harici sistem, bulut, fiziki dosya) ve kimlerle paylaşılıyor?
3. Aydınlatma metni, saklama-imha politikası, VERBİS kaydı mevcut mu?
4. Yurt dışına veri aktarımı (yurt dışı bulut, yabancı müvekkil) var mı?

## Denetim şeması
1. **İşleme şartı (KVKK m.5-6)**: Her işleme amacı bir hukuki sebebe bağlanır — vekâlet/sözleşmenin ifası, hukuki yükümlülük, meşru menfaat; özel nitelikli veride m.6 daha katı şartlar. Avukatlık faaliyetinde işleme çoğunlukla sözleşme ifası ve hukuki yükümlülüğe dayanır; açık rıza son çare kabul edilir.
2. **Aydınlatma (KVKK m.10)**: Müvekkil ve diğer ilgili kişilere kimliği, amaç, aktarım, toplama yöntemi ve haklar bildirilir. Vekâlet ilişkisinin sır niteliği (1136 m.36) ile uyum kurulur.
3. **Güvenlik (KVKK m.12)**: Teknik/idari tedbirler — erişim yetkisi, şifreleme, fiziki dosya güvenliği, çalışan gizlilik taahhüdü.
4. **Saklama-imha**: Her veri kategorisi için saklama süresi (dava/zamanaşımı/mevzuat gerekleri) ve süre sonunda imha/anonimleştirme planı.
5. **Aktarım (KVKK m.8-9)**: Bilirkişi, mahkeme, karşı vekil, mali müşavir aktarımları amaca uygun ve hukuki sebebe bağlı; yurt dışı aktarımda m.9 rejimi.
6. **İhlal (KVKK m.12/5)**: Veri ihlalinde Kurula ve etkilenen ilgili kişiye gecikmeksizin (Kurul kararıyla 72 saat ölçütü) bildirim süreci hazır tutulur.
7. **Ara sonuç**: Her kategori için şart + aydınlatma + saklama + güvenlik karşılanmışsa uyum sağlanmıştır; eksikler boşluk listesine yazılır.

## Çıktı modülleri
- Veri işleme envanteri (kategori, amaç, hukuki sebep, saklama, alıcı).
- Aydınlatma metni ve gerekirse açık rıza metni taslağı.
- Saklama-imha politikası ve ihlal müdahale akışı.
- Uyum boşluğu raporu ve eylem planı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

