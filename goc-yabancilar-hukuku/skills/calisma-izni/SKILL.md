---
argument-hint: ''
description: Yabancının çalışma izni başvurusu, uzatması, ret/iptali veya izinsiz
  çalışma yaptırımı söz konusu olduğunda; 6735 sayılı Kanun kapsamında izin türü ve
  usulünü saptamak için kullanılır.
name: calisma-izni
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
  - ad: Yabancılar ve Uluslararası Koruma Kanunu
    numara: '6458'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Çalışma İzni ve Uluslararası İşgücü

## Görev
Yabancının çalışma iznini 6735 sayılı Uluslararası İşgücü Kanunu çerçevesinde yapılandırmak, doğru izin türünü ve başvuru kanalını belirlemek, ret/iptal ve izinsiz çalışma yaptırımlarına karşı strateji geliştirmek.

## Soğuk başlangıç (intake)
1. İşveren üzerinden mi (bağımlı), bağımsız mı yoksa Turkuaz Kart yoluyla mı çalışma planlanıyor?
2. Yabancının mevcut ikamet izni ve Türkiye'de bulunma süresi nedir?
3. İşveren şirketin durumu (sermaye, mevcut Türk personel sayısı) nedir?
4. Ret, iptal veya idari para cezası tebliğ edildi mi, tarihi?

## Denetim şeması
1. **İzin türleri**: 6735 m.10 — süreli çalışma izni (kural olarak ilk başvuruda belirli işveren/işyeri ve süre bağlı), süresiz çalışma izni, bağımsız çalışma izni; Turkuaz Kart (m.11 — nitelikli işgücü/yatırım için süresiz hak veren belge).
2. **Çalışma izni-ikamet ilişkisi**: m.13 — geçerli çalışma izni ve Turkuaz Kart ikamet izni yerine geçer; ayrıca ikamet izni aranmaz.
3. **Başvuru usulü**: Yurt içinden geçerli ikamet izni varsa doğrudan, yurt dışından ise temsilcilik üzerinden; başvuru Çalışma ve Sosyal Güvenlik Bakanlığına yapılır, değerlendirme kriterleri (uluslararası işgücü politikası, istihdam etkisi) uygulanır.
4. **Ret/iptal**: m.15-16 — politika kriterlerine uymama, sahte/eksik belge, fiilen çalışmama, iznin amacı dışında kullanımı. İşlem idari nitelikte olup İYUK yolu açıktır.
5. **İzinsiz çalışma yaptırımı**: m.23 — izinsiz çalışan yabancıya ve çalıştıran işverene idari para cezası; tekrarda artış; yabancı için sınır dışı riski (YUKK m.54 ile bağlantı).
**İspat yükü**: İzin şartlarını ve fiilî çalışmayı başvuran/işveren ispatlar; idari para cezasının maddi dayanağını (tespit tutanağı) idare ortaya koyar.

## Çıktı modülleri
- İzin türü seçim matrisi ve başvuru belge listesi.
- Ret kararına karşı iptal davası dilekçe iskeleti.
- İdari para cezasına karşı itiraz/dava ve yaptırım-risk notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

