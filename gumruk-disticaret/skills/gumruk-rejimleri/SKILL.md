---
argument-hint: ''
description: Dahilde işleme, antrepo, geçici ithalat, transit ve hariçte işleme gibi
  rejimlerin şartları, kapatılması ve ihlal sonuçlarını analiz etmek gerektiğinde;
  rejim ihlalinden doğan yükümlülük ve cezaları d
name: gumruk-rejimleri
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
  - ad: Gümrük Müsait Müşterek Gümrük Bölgeleri Hakkında Kanun
    numara: '4458'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Gümrük Rejimleri ve Şartlı Muafiyet

## Görev
Ekonomik etkili ve şartlı muafiyet rejimlerinin (dahilde işleme, antrepo, geçici ithalat, transit, hariçte işleme, gümrük kontrolü altında işleme) şartlarını, izin yükümlülüklerini, kapatma sürelerini ve ihlal sonuçlarını analiz etmek.

## Soğuk başlangıç (intake)
- Hangi rejim ve hangi izin (DİİB, antrepo izni, geçici ithalat izni) söz konusu?
- İzin süresi/kapatma süresi nedir; süre aşıldı mı, taahhütler yerine getirildi mi?
- Eşya işlendi, ihraç edildi, yeniden ihraç edildi mi; fire/zayiat oranı uygun mu?
- İdare ihlal mi tespit etti, yoksa rejim usulüne uygun mu kapatılacak?

## Denetim şeması
1. Rejim seçimi ve izin: Şartlı muafiyet rejimleri izne tabidir (4458 m.80 vd.). İznin kapsamı, süresi ve taahhütleri belirleyicidir; izinsiz veya kapsam dışı işlem ihlaldir.
2. Dahilde işleme: Eşya işlenip ihraç edilmek üzere vergileri askıya alınarak (DİİB) ithal edilir; ihracat taahhüdü süresinde gerçekleşmezse askıdaki vergiler ek tahakkukla doğar. İkincil işlem görmüş ürün, fire ve verimlilik oranları denetlenir.
3. Antrepo: Eşya antrepoda gümrük gözetiminde tutulur; antrepodan izinsiz çekme, sayım noksanlığı veya kayıt uyumsuzluğu yükümlülük ve ceza doğurur (m.236 ilgili hükümleri).
4. Geçici ithalat: Tam/kısmi muafiyetle belirli süre için ithal edilen eşya süresinde yeniden ihraç edilmeli; aksi halde serbest dolaşıma giriş vergileri ve cezası gündeme gelir.
5. Yükümlülüğün doğumu: Rejim ihlalinde yükümlülük 4458 m.182-184 çerçevesinde doğar; doğum anı oran/kur ve zamanaşımı (m.197) için saptanır.
6. İspat yükü: Rejim şartlarına uygunluğu (ihracatın gerçekleştiği, sürenin tutulduğu, fire oranının makul olduğu) izin sahibi belgelerle ispatlar; idare ihlali somut tespitle ortaya koyar.
7. Ara sonuç: Rejimin doğru kapatılıp kapatılmadığı, ihlal varsa doğan vergi ve cezanın dayanağı belirlenir; telafi edici düzeltme imkânları değerlendirilir.

## Çıktı modülleri
- Rejim-izin-taahhüt uyum kontrol listesi
- İhlal halinde yükümlülük hesabı ve savunma notu
- Rejim kapatma/düzeltme başvuru taslağı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

