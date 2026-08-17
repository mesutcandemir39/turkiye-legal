---
argument-hint: ''
description: Maddi vakıayı hukuk kuralının soyut şartlarına tek tek yerleştirerek
  gerekçeli ara sonuç üretmek gerektiğinde kullanılır; mütalaanın hukuki değerlendirme
  bölümünün çekirdek yöntemidir.
name: altlama-subsumption-teknigi
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


# Altlama (Subsumption) Tekniği

## Görev
Hukuk kuralının her bir şartını (unsurunu) tek tek alıp somut vakıaya uygulamak ve "bu şart gerçekleşti / gerçekleşmedi" ara sonuçlarını gerekçeyle vermek. Altlama, mütalaayı keyfi kanaatten ayıran asıl yöntemdir: büyük önerme (kural) + küçük önerme (olay) → sonuç.

## Soğuk başlangıç (intake)
- Uygulanacak temel norm hangi madde? (Tam metni ve unsurları çıkarıldı mı?)
- Bu normun unsurları (şartları) nelerdir, kaç tane?
- Her unsur için elde hangi vakıa/delil var?
- Tanımlanması gereken belirsiz kavram var mı? (Ör. ağır kusur, basiretli tacir, dürüstlük)

## Denetim şeması
1. Kuralı unsurlarına ayır: Madde metni cümle cümle çözülür ve kümülatif/seçimlik şartlar listelenir. Örnek — haksız fiil (TBK m.49): (a) hukuka aykırı fiil, (b) kusur, (c) zarar, (d) illiyet bağı. Dördü birlikte aranır.
2. Her unsuru olaya uygula: Unsur → ilgili vakıa → gerçekleşip gerçekleşmediği. Belirsiz kavram varsa önce tanımlanır (içtihat/doktrin ölçütüyle), sonra olaya uygulanır.
3. İspat yükü kontrolü: Her unsuru kim ispatlamalı (TMK m.6, HMK m.190)? Karine veya ispat yükü tersine çevrilen haller (ör. TBK m.66 adam çalıştıranın sorumluluğunda kurtuluş beyyinesi, TBK m.112 ifa etmeme karinesi) ayrıca not edilir.
4. İstisna ve def'iler: Kuralın istisnaları, hukuka uygunluk sebepleri, zamanaşımı def'i gibi karşı argümanlar aynı titizlikle altlanır.
5. Ara sonuç birleştirme: Tüm unsurlar gerçekleşiyorsa hukuki sonuç doğar; bir unsur eksikse talep dayanaktan yoksundur. Çekişmeli unsurda koşullu sonuç ("X ispatlanırsa...") kurulur.
6. Karşıt görüş testi: Aynı vakıaya alternatif nitelendirme mümkün mü? (Ör. fiil hem haksız fiil hem sözleşmeye aykırılık — yarışma) tartışılır.

## Çıktı modülleri
- Unsur tablosu (unsur | olaydaki karşılığı | ispat yükü | ara sonuç)
- Belirsiz kavram tanımı ve uygulanışı
- Def'i/istisna değerlendirmesi
- Birleştirilmiş hukuki sonuç (koşullu varyantlarıyla)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

