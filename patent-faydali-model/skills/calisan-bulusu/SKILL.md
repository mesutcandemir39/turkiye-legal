---
argument-hint: ''
description: Bir çalışanın iş ilişkisi sırasında yaptığı buluşun hakkının kime ait
  olduğu, bildirim, hak talebi ve bedel sorunları gündeme geldiğinde kullanılır; işveren-çalışan
  dengesi ve şirket içi süreç tasarım
name: calisan-bulusu
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


# Çalışan Buluşları ve Hizmet Buluşu

## Görev
SMK m.113-120 çerçevesinde hizmet buluşu/serbest buluş ayrımını yapmak, bildirim ve hak talebi sürecini kurmak, çalışana ödenecek bedeli ve uyuşmazlık yolunu belirlemek.

## Soğuk başlangıç (intake)
1. Buluşu yapan kim; iş sözleşmesi/üniversite/kamu görevlisi statüsü ne?
2. Buluş iş yükümlülükleri kapsamında mı, işyeri deneyim/çalışmalarına mı dayanıyor?
3. Çalışan buluşu işverene yazılı bildirdi mi; işveren hak talebinde bulundu mu?
4. Bedel/karşılık konusunda anlaşma veya değerlendirme yapıldı mı?

## Denetim şeması
1. **Niteleme (SMK m.113).** Hizmet buluşu: çalışanın yükümlülüğü gereği gerçekleştirdiği ya da işyerinin deneyim ve çalışmalarına dayanan buluş. Bunun dışındakiler serbest buluştur. Ara sonuç: hizmet mi serbest mi?
2. **Bildirim (SMK m.114).** Çalışan, hizmet buluşunu gecikmeksizin yazılı olarak işverene bildirir; bildirim içeriği yönetmelikte belirlenir. Bildirimin yapılış/eksiklik sonuçlarını kontrol et.
3. **İşverenin hak talebi (SMK m.115).** İşveren tam veya kısmi hak talep edebilir; talep bildirimden itibaren süresinde yapılmazsa buluş serbest buluş niteliği kazanır. Tam hak talebinde buluş üzerindeki haklar işverene geçer.
4. **Bedel (SMK m.115/3 ve ilgili hükümler).** Tam/kısmi hak talebinde çalışana makul bedel ödenir; bedelin belirlenmesinde buluşun ekonomik değeri, çalışanın işteki konumu ve işletmenin payı esas alınır.
5. **Serbest buluş ve yükümlülük (SMK m.117-118).** Çalışan serbest buluşu da işverene bildirmek ve kanunda öngörülen hallerde öncelikli kullanım teklifinde bulunmakla yükümlü olabilir.
6. **Uyuşmazlık.** Bedel ve nitelik uyuşmazlıkları için tahkim/uzlaşma ve dava yolu; üniversite mensubu buluşları için özel rejim (SMK m.121) ayrıca değerlendirilir.

## Çıktı modülleri
- Hizmet/serbest buluş nitelemesi gerekçesi.
- Bildirim ve hak talebi zaman çizelgesi.
- Bedel değerlendirme çerçevesi.
- Sözleşme/iç yönetmelik için süreç ve şablon önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

