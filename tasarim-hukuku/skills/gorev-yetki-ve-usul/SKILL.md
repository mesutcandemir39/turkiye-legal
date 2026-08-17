---
argument-hint: ''
description: Tasarım uyuşmazlıklarında görevli ve yetkili mahkemenin, idari/adli yol
  ayrımının ve dava şartlarının SMK m.156 ile HMK çerçevesinde belirlenmesi; doğru
  mahkemede doğru davanın açılması ve dava şartı
name: gorev-yetki-ve-usul
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


# Görev, Yetki ve Usul Haritası

## Görev
Tasarım uyuşmazlığını doğru mecraya yerleştirmek: görevli mahkeme, yetkili yer, idari yol (TÜRKPATENT/YİDD) ile adli yol ayrımı, dava şartları ve arabuluculuk ön koşulunu netleştirmek.

## Soğuk başlangıç (intake)
1. Uyuşmazlık türü nedir (tescil/itiraz idari süreci, hükümsüzlük, tecavüz, tazminat, devir)?
2. Tarafların yerleşim yeri ve tecavüzün/işlemin yapıldığı yer neresi?
3. Talep parasal mı (tazminat → ticari dava → arabuluculuk şartı olabilir)?
4. İlgili ilde FSHHM var mı, yoksa görevlendirilen asliye mi?

## Denetim şeması
1. Görevli mahkeme (SMK m.156/1): SMK'den doğan hukuk davalarında Fikrî ve Sınai Haklar Hukuk Mahkemesi görevlidir; bulunmayan yerlerde HSK'nin belirlediği asliye hukuk mahkemesi bu sıfatla bakar. Ceza boyutu için Fikrî ve Sınai Haklar Ceza Mahkemesi.
2. İdari/adli ayrımı: Tescil, yayın, itiraz ve YİDD kararları idari süreçtir; YİDD'nin nihai kararına karşı 2 ay içinde Ankara FSHHM'de iptal davası açılır (SMK m.67). Hükümsüzlük ve tecavüz ise doğrudan adli davadır.
3. Yetki (SMK m.156/3-5): Hak sahibinin açacağı davalarda davacının yerleşim yeri veya tecavüzün/fiilin işlendiği yahut etkilerinin görüldüğü yer mahkemesi yetkilidir; üçüncü kişilerin hak sahibine açacağı davalarda davalının (sicildeki) yerleşim yeri. TÜRKPATENT aleyhine davada Ankara mahkemeleri.
4. Dava şartı arabuluculuk: Konusu para olan ticari davalarda (TTK m.5/A, HMK çerçevesi) tazminat talepleri için dava şartı arabuluculuk işletilir; tecavüzün tespiti/men gibi taleplerle birlikte yapı kurulur. Hükümsüzlük gibi münhasıran mahkeme yetkisindeki talepler arabuluculuğa elverişli değildir.
5. Dava şartları ve süre: Görev resen incelenir (HMK m.114/1-c); zamanaşımı (tazminatta TBK m.72), tedbirde 2 haftalık esas dava süresi (HMK m.397) kontrol edilir.
6. Ara sonuç: Görevli/yetkili mahkeme, idari mi adli mi, arabuluculuk gerekip gerekmediği net yazılır.

## Çıktı modülleri
- Yol haritası tablosu (idari/adli, görevli mahkeme, yetkili yer).
- Dava şartı kontrol listesi (görev, yetki, arabuluculuk, süre).
- Talep türüne göre arabuluculuk elverişlilik notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

