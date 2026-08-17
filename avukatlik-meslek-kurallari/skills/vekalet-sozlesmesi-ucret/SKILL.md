---
argument-hint: ''
description: Avukatlık ücret sözleşmesinin kurulması, ücret türleri ve sınırları,
  asgari ücret tarifesi, karşı tarafa yüklenen vekâlet ücreti ve ücret alacağının
  takibi söz konusu olduğunda kullanılır.
name: vekalet-sozlesmesi-ucret
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
  version: 0.1.0
user-invocable: true
---


# Avukatlık Sözleşmesi ve Vekâlet Ücreti

## Görev
Avukatlık ücret sözleşmesini geçerlilik ve sınırlar yönünden kurmak/denetlemek; akdi ve
yargısal (karşı tarafa yüklenen) vekâlet ücretini ayırt etmek; ücret alacağını yapılandırmak.

## Soğuk başlangıç (intake)
1. Ücret nasıl kararlaştırıldı (maktu, nispi, yüzde, başarı koşullu)?
2. Yazılı sözleşme var mı; iş değeri/dava değeri ne?
3. İş tamamlandı mı; haksız azil/istifa var mı?
4. Tartışma akdi ücret mi, yoksa karşı tarafa yüklenecek yargılama gideri vekâlet ücreti mi?

## Denetim şeması
1. **Sözleşmenin kurulması.** Avukatlık sözleşmesi serbestçe düzenlenir, yazılı yapılmaması
   geçersizlik sebebi değildir ama yazılılık ispat ve ücret için önemlidir (Av. K. m.163,
   TBK m.502 vd.). Belirlenmemişse ücret, tarife esas alınarak ve emeğe göre takdir edilir.
2. **Ücretin sınırları (emredici).** Ücret, dava konusu para veya değerin %25'ini aşamaz;
   yüzde belirlenen işlerde sınır bu orandır (Av. K. m.164/2). Dava konusu şeyin aynının
   ücret olarak kararlaştırılması (sonuca ortaklık) yasaktır. Ara sonuç: sözleşme bu sınırı
   aşıyor mu? Aşan kısım geçersizdir.
3. **Asgari tarife tabanı.** Kararlaştırılan ücret, yürürlükteki TBB Avukatlık Asgari Ücret
   Tarifesi'nin altında olamaz (m.164/4). Tarife her yıl Resmî Gazete'de yayımlanır; yıl/tarih
   belirt.
4. **Karşı tarafa yüklenen vekâlet ücreti.** Dava sonunda haksız çıkan tarafa yüklenen
   vekâlet ücreti yargılama giderindendir (HMK m.323/1-ğ) ve tarifeye göre hesaplanır; bu
   ücret kural olarak avukata aittir (Av. K. m.164/son), akdi ücretten ayrıdır.
5. **Azil/istifa ve müteselsil sorumluluk.** Haksız azilde ücretin tamamı muaccel olur; haklı
   sebeple azilde indirim gündeme gelir (Av. K. m.174). Karşı yan vekille sulh/feragat halinde
   ücret koruması ve müteselsil sorumluluk (m.165) gözetilir; avukatın hapis hakkı (m.166)
   ve örnek üzerinde alıkoyma değerlendirilir.
6. **Takip ve zamanaşımı.** Ücret alacağı vekâlet ilişkisinden doğar; zamanaşımı TBK m.147/5
   uyarınca beş yıldır. İlamsız icra/dava yolu seçilir; ispat yükü ücreti talep edendedir
   (TMK m.6).

## Çıktı modülleri
- Sözleşmenin geçerlilik/sınır denetimi (aşan/geçersiz şart tespiti).
- Akdi ve yargısal vekâlet ücreti ayrım tablosu.
- Ücret sözleşmesi ve ücret alacağı ihtar/talep taslağı ([doldurulacak] yer tutucularla).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

