---
argument-hint: ''
description: Davanın hangi mahkemede (sulh hukuk, asliye hukuk, tüketici, iş, ticaret,
  aile, kadastro) ve hangi yer mahkemesinde açılacağını belirlemek; kesin yetki halleri,
  yetki sözleşmesi ve görevsizlik/yetkisi
name: gorev-yetki-belirleme
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Görev ve Yetki Tayini

## Görev
Davanın görevli mahkemesini ve yetkili yer mahkemesini doğru saptamak; kesin görev/yetki ile düzenleyici yetki ayrımını kurmak.

## Soğuk başlangıç (intake)
- Uyuşmazlığın konusu ve tarafları kim? (tüketici, işçi, tacir, eş, taşınmaz?)
- Dava değeri/konusu özel görevli mahkeme gerektiriyor mu?
- Davalının yerleşim yeri ve uyuşmazlık bağlantı yeri neresi?
- Geçerli bir yetki sözleşmesi var mı (tacirler/kamu tüzel kişileri arasında)?

## Denetim şeması
1. **Genel görev**: HMK m.2 uyarınca asliye hukuk mahkemesi asıl görevli; sulh hukukun görevi m.4'te sayılan işlerle (kira ilişkisinden doğan davalar dâhil belli işler, taksim, ortaklığın giderilmesi vb.) sınırlıdır.
2. **Özel görevli mahkemeler**: tüketici uyuşmazlıkları → tüketici mahkemesi (6502 sayılı Kanun); iş uyuşmazlıkları → iş mahkemesi (7036); ticari davalar → asliye ticaret mahkemesi (TTK m.4-5); aile → aile mahkemesi (4787); kadastro → kadastro mahkemesi; fikri haklar → FSHHM. Görev kamu düzenindendir, re'sen gözetilir (HMK m.1, m.114/1-c).
3. **Genel yetki**: Davalının yerleşim yeri mahkemesi (HMK m.6).
4. **Özel/seçimlik yetki**: Sözleşmeden doğan davada ifa yeri (m.10); haksız fiilde fiilin işlendiği/zararın doğduğu yer (m.16); taşınmazın aynına ilişkin davada taşınmazın bulunduğu yer **kesin yetki** (m.12).
5. **Kesin yetki halleri** sözleşmeyle değiştirilemez; **yetki sözleşmesi** (m.17-18) yalnızca tacir/kamu tüzel kişileri arasında ve kesin yetki olmayan hallerde geçerlidir.
6. **Görevsizlik/yetkisizlik kararı** (m.20): Kararın kesinleşmesinden itibaren iki hafta içinde dosyanın görevli/yetkili mahkemeye gönderilmesi istenmezse dava açılmamış sayılır — bu süre kritiktir.

Ara sonuç: "Görevli mahkeme + yetkili yer + kesin mi seçimlik mi" çıktısı.

## Çıktı modülleri
- Görevli mahkeme gerekçesi (madde atıflı).
- Yetkili yer mahkemesi seçenekleri ve kesin/seçimlik etiketi.
- Görevsizlik/yetkisizlik halinde iki haftalık gönderme uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

