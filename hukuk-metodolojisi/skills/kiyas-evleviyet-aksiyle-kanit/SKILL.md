---
argument-hint: ''
description: İki olayın benzerliği nedeniyle bir kuralın taşınıp taşınmayacağı, ya
  da kuralın yalnızca metindeki hâlle sınırlı olup olmadığı tartışıldığında mantıksal
  yorum argümanlarını doğru seçmek için kullanıl
name: kiyas-evleviyet-aksiyle-kanit
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
    madde: '1'
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kıyas, Evleviyet ve Aksiyle Kanıt

## Görev
Bir hükmün metinde sayılmayan bir olaya uygulanıp uygulanmayacağını, klasik yorum/boşluk doldurma argümanları (analoji, *a fortiori*, *a contrario*) arasından doğrusunu seçerek gerekçelendirmek.

## Soğuk başlangıç (intake)
- Eldeki olay, kuralın düzenlediği olaya hangi yönden benziyor; benzerlik kuralın amacı bakımından mı yoksa yüzeysel mi?
- Kanun bir liste/sayım mı yapıyor (tahdidi mi, tadadi mi)?
- Alan kıyasa açık mı (özel hukuk) yoksa kapalı mı (ceza TCK m.2, vergi, istisna hükümleri, emredici sınırlamalar)?
- Rakip taraf hangi argümanı (a contrario) öne sürüyor?

## Denetim şeması
1. **Kıyas (analoji)** — Şartlar: (i) kanunda doğrudan hüküm yok; (ii) düzenlenen olay ile eldeki olay, kuralın amacı (ratio) bakımından özsel olarak benzer; (iii) farklı muameleyi haklı kılan bir ayrım yok. Sağlanırsa kuralın hukuki sonucu eldeki olaya taşınır. Tek olaya değil, bir ilkeye dayanan kıyas "hukuk kıyası"dır.
2. **Evleviyet (a fortiori)** — *A maiore ad minus*: çok için geçerli olan, evleviyetle az için de geçerlidir (yetki/hak hâlleri). *A minore ad maius*: az için yasak olan, çok için evleviyetle yasaktır (yasak/yük hâlleri). Amaç ölçeği aynı yönde işlemelidir.
3. **Aksiyle kanıt (a contrario)** — Kanun bir hâli düzenleyip diğerini bilinçle dışarıda bıraktıysa, dışarıdakine zıt sonuç bağlanır. Ancak susmanın "bilinçli tercih" mi yoksa "boşluk" mu olduğu önce belirlenmelidir; yanlış a contrario, boşluğu örter.
4. **Çatışma çözümü** — Aynı olayda kıyas ve a contrario ters sonuç verir; tercih, normun amacına (teleolojik) göre yapılır. İstisna ve sınırlayıcı hükümler dar yorumlanır, kural kıyasa kapalıdır (*exceptiones non sunt extendendae*).
5. **Yasak alan kontrolü** — Ceza (TCK m.2), vergi ve idari yaptırımlarda aleyhe kıyas ve kıyasa varan genişletici yorum yasaktır; bu alanda yalnızca lehe/teknik kıyas tartışılabilir.

## Çıktı modülleri
- Benzerlik analizi tablosu (ratio temelli).
- Seçilen argüman + neden diğerinin reddedildiği.
- Yasak alan uyarısı (gerekiyorsa).
- İlkesel içtihat atfı, künye `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

