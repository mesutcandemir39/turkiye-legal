---
argument-hint: ''
description: Bir menfaatin gerçekten sübjektif hak olup olmadığı, hak türleri (mutlak-nispi,
  yenilik doğuran, def'i-itiraz) ve hak-yetki-yükümlülük ilişkileri çözümlenmek istendiğinde;
  Hohfeld ve menfaat/irade teo
name: hak-ve-yukumluluk-teorisi
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


# Hak, Yükümlülük ve Hukuki İlişki Teorisi

## Görev
Sübjektif hak kavramını analiz etmek; bir talebin gerçek bir hak mı, yetki/beklenti mi
olduğunu ayırmak; hak türlerini ve karşı kavramları (yükümlülük, def'i, itiraz) sistematize
etmek. Bu çözümleme dava dilekçesinde "talep sonucu" ve "hukuki sebep" kurarken doğrudan işe yarar.

## Soğuk başlangıç (intake)
- İddia edilen şey bir sübjektif hak mı, yoksa korunan basit bir menfaat/beklenti mi?
- Hak mutlak mı (herkese karşı, ör. mülkiyet) nispi mi (belirli kişiye karşı, ör. alacak)?
- Talep, yenilik doğuran (kurucu/değiştirici/bozucu) bir hakka mı dayanıyor?
- Karşı tarafın elinde def'i mi (ör. zamanaşımı) yoksa itiraz mı (ör. ödeme) var?

## Denetim şeması
1. **Hak teorisini seç.** İrade teorisi (hak = korunan irade gücü) ile menfaat teorisi
   (hak = hukuken korunan menfaat, Jhering) arasında somut menfaate uygun olanı kullan; çoğu
   Türk doktrini karma yaklaşımı benimser.
2. **Hohfeld dörtlüsünü uygula.** Talep hakkı–yükümlülük, özgürlük/serbesti–hak yokluğu,
   yetki (kudret)–tâbilik, bağışıklık–yetersizlik ilişkilerini ayır. "Hak" denilen şeyin
   hangi kutucuğa düştüğünü belirle; bu, kime karşı ne talep edilebileceğini netleştirir.
3. **Hak türünü sınıfla.** Mutlak/nispi; ayni/şahsi; yenilik doğuran (TMK ve TBK'da örnekler:
   bozucu yenilik doğuran fesih hakkı gibi); devredilebilir/kişiye sıkı bağlı. Mutlak hak,
   üçüncü kişilere karşı korunma (haksız fiil/istihkak) imkânı verir.
4. **Karşı kavramı tespit et.** Def'i (hakkı ileri sürmeye bağlı, ör. zamanaşımı def'i,
   TBK m.161; hâkim re'sen dikkate almaz) ile itiraz (hakkın doğmadığını/sona erdiğini
   gösteren, hâkim re'sen dikkate alır) ayrımını yap. Ara sonuç: ispat yükü ve usul sonucu buradan çıkar.
5. **İspat yükü.** Hakkı iddia eden, hakkın doğum vakıalarını; karşı taraf, sona erme/engelleyici
   vakıaları ispatla yükümlüdür (TMK m.6; HMK m.190). Bunu hak teorisi sonucuyla hizala.

## Çıktı modülleri
- Hak nitelendirme notu (gerçek hak mı / menfaat mi).
- Hohfeld ilişki tablosu (talep–yükümlülük vb.).
- Hak türü etiketi ve sonuçları (mutlak/nispi, yenilik doğuran).
- Def'i/itiraz ayrımı ve ispat yükü dağılımı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

