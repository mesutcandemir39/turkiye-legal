---
argument-hint: ''
description: Müvekkile davanın/işin durumunu, seçeneklerini ve sonraki adımları anlatan
  yazılı bilgilendirme metni üretmek; aydınlatma yükümlülüğünü yalın ama eksiksiz
  yerine getirmek gerektiğinde kullanılır.
name: muvekkil-bilgilendirme-metni
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Müvekkil Bilgilendirme ve Aydınlatma Metni

## Görev
Müvekkile sürecin neresinde olunduğunu, hangi seçeneklerin bulunduğunu, olası sonuçları ve
sonraki adımları anlatan yapılandırılmış bir bilgilendirme metni hazırlamak; vekilin aydınlatma
borcunu (TBK m.506; Avukatlık K. m.34, TBB Meslek Kuralları m.3-4) sade ama eksiksiz karşılamak.

## Soğuk başlangıç (intake)
1. İş hangi aşamada (danışma, dava açma, tahkikat, karar, icra)?
2. Müvekkile sunulacak karar/seçenek var mı (sulh, istinaf, vazgeçme)?
3. Maliyet, süre ve başarı ihtimali hakkında beklenti yönetimi gerekiyor mu?
4. Acil bir süre veya talimat alınması gereken nokta var mı?

## Denetim şeması
1. DURUM TESPİTİ: İşin bugünkü hukuki durumu yalın dille özetlenir (ne yaptık, nerede duruyoruz).
2. SEÇENEKLER VE SONUÇLARI: Her seçeneğin olası sonucu, maliyeti ve riski dengeli sunulur; vekil
   abartılı başarı vaadinden kaçınır (meslek kuralları, dürüstlük). Olasılık dili kullanılır:
   "garanti" yerine "lehimize güçlü/zayıf gerekçe".
3. SÜRE VE TALİMAT (kritik sonuç): Müvekkilin karar vermesi gereken son tarih takvimle yazılır;
   kanun yolu süreleri (örn. istinaf/temyiz iki hafta) ve hak düşürücü süreler ayrıca uyarılır.
4. MALİYET ŞEFFAFLIĞI: Vekâlet ücreti, harç, gider ve karşı vekâlet ücreti riski açıkça belirtilir;
   beklenti yönetimi yapılır.
5. ONAY/TALİMAT İZİ (ispat): Müvekkilin onayını gerektiren konularda yazılı talimat istenir; bu,
   ileride uyuşmazlıkta vekilin lehine ispat aracıdır.
6. ARA SONUÇ: Metin müvekkili yanıltıcı kesinlik içermeden, tüm seçenekleri ve süreleri kapsıyor mu.

## Çıktı modülleri
- "Bugün neredeyiz" özeti.
- Seçenekler / sonuç / maliyet / risk tablosu.
- Karar verilmesi gereken konular ve son tarih.
- Onay/talimat istenen satır ve hukuki tavsiye notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

