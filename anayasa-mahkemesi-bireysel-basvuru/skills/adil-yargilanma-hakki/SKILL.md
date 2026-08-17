---
argument-hint: ''
description: Mahkemeye erişim, gerekçeli karar, silahların eşitliği, makul sürede
  yargılanma, çelişmeli yargılama, masumiyet karinesi gibi adil yargılanma güvencelerinin
  ihlali iddia edildiğinde kullanılır.
name: adil-yargilanma-hakki
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  - ad: Anayasa Mahkemesinin Kuruluşu ve Yargılama Usulü Hakkında Kanun
    numara: '6216'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Adil Yargılanma Hakkı İhlali

## Görev
Anayasa m.36 ve AİHS m.6 kapsamındaki adil yargılanma güvencelerinden hangisinin somut olayda ihlal edildiğini tespit etmek ve kanun yolu şikâyetinden ayırmak.

## Soğuk başlangıç (intake)
- Hangi yargılamada, hangi güvence ihlal edildi (erişim, gerekçe, eşitlik, süre)?
- Mahkeme esaslı iddialarınızı/delillerinizi gerekçeyle karşıladı mı?
- Yargılama ne kadar sürdü; gecikme kime atfedilebilir?
- Şikâyetiniz sonucun yanlışlığına mı, usulün adilliğine mi ilişkin?

## Denetim şeması
1. Uygulanabilirlik — m.36: medeni hak ve yükümlülükler ile suç isnadı uyuşmazlıklarında güvence devreye girer.
2. Mahkemeye erişim — aşırı harç, katı süre/şekil yorumu, fiilî engeller erişim hakkını ölçüsüzce sınırlıyorsa ihlal doğar (m.13 ölçülülük süzgeci).
3. Gerekçeli karar hakkı — mahkeme, davanın sonucuna etkili, esaslı iddiaları karşılamak zorundadır; susulan esaslı itiraz ihlal nedeni olabilir. Her argümana ayrı yanıt aranmaz.
4. Silahların eşitliği ve çelişmeli yargılama — taraflardan birine tanınan usuli üstünlük, sunulan görüş/delile yanıt imkânının verilmemesi ihlaldir.
5. Makul süre — uyuşmazlığın karmaşıklığı, tarafların ve yargı makamlarının tutumu, başvurucu için önem ölçütleriyle değerlendirilir; yargı kaynaklı uzun gecikme ihlaldir.
6. Masumiyet karinesi ve diğer ceza güvenceleri — m.38 ile birlikte değerlendirilir.

Sınır: Delil takdiri ve hukuk kuralının yorumu kural olarak kanun yolu şikâyetidir; ancak takdir "açık keyfîlik / bariz takdir hatası" düzeyindeyse anayasal denetime girer.

İspat yükü: ihlali oluşturan usuli kusuru ve sonuca etkisini başvurucu gösterir.

Ara sonuç: ihlal edilen alt güvence(ler) ve dayanak.

## Çıktı modülleri
- İhlal edilen güvence başlıkları ve gerekçe.
- Kanun yolu şikâyeti / anayasal şikâyet ayrımı notu.
- Makul süre hesabı (varsa).
- AYM/AİHM ilke ölçütlerine atıf [DOĞRULANMADI].



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

