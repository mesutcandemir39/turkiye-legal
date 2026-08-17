---
argument-hint: ''
description: Karmaşık bir uyuşmazlığı cevaplanabilir alt hukuki sorulara bölmek, doğru
  hukuk dalı ve normları belirleyip değerlendirme sırasını kurmak gerektiğinde kullanılır;
  mütalaanın yol haritasını oluşturur.
name: hukuki-sorunun-cercevelenmesi
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


# Hukuki Sorunun Çerçevelenmesi

## Görev
Maddi olaydan doğan hukuki uyuşmazlığı, sistematik olarak cevaplanabilir alt sorulara ayırmak ve hangi normların hangi sırayla uygulanacağını belirlemek. İyi çerçevelenmemiş bir soru, dağınık ve sonuçsuz bir mütalaa üretir.

## Soğuk başlangıç (intake)
- Müvekkilin asıl öğrenmek istediği nihai soru ne? (Talep haklı mı / borçlu muyum / dava açayım mı?)
- Olay hangi hukuk dal(lar)ına giriyor? (Birden çok dal kesişiyor olabilir.)
- Birbirine bağlı ön sorunlar var mı? (Önce geçerlilik, sonra ifa gibi)
- İstenen yalnızca hukuki nitelendirme mi, yoksa strateji önerisi mi?

## Denetim şeması
1. Nihai sorudan alt sorulara: Üst soru mantıksal bileşenlerine ayrılır. Örnek (sözleşmeden cayma): (a) Sözleşme geçerli kuruldu mu? (b) Geçerliyse, fesih/dönme şartları gerçekleşti mi? (c) Gerçekleştiyse, talep edilebilecek tazminat ne? (d) Talep zamanaşımına uğradı mı?
2. Mantıksal sıralama: Ön sorun sonraki sorunun cevabını belirliyorsa önce ele alınır (geçersiz sözleşmede ifa tartışılmaz; sebepsiz zenginleşme/TBK m.77 devreye girer).
3. Hukuk dalı eşlemesi: Her alt soru ilgili dala ve başat norma bağlanır (borç ilişkisi → TBK; ayni hak → TMK; ticari iş → TTK; usul → HMK/İYUK/CMK). Kesişen alanlarda özel hükmün genel hükme üstünlüğü gözetilir.
4. Emredici/yedek hüküm taraması: Tarafların aksini kararlaştıramayacağı emredici normlar belirlenir; bunlar değerlendirmenin sınırıdır.
5. Zaman bakımından uygulama: Olaya yürürlükteki mi yoksa mülga mevzuatın mı uygulanacağı, geçici maddeler kontrol edilir.
6. Ara sonuç: Numaralandırılmış alt soru listesi + her sorunun norm dayanağı + değerlendirme sırası.

## Çıktı modülleri
- Nihai soru → alt sorular ağacı
- Her alt soru için başat norm eşlemesi
- Değerlendirme sırası gerekçesiyle
- Emredici hüküm uyarı kutusu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

