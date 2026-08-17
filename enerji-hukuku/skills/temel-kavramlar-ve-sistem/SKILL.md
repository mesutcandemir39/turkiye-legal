---
argument-hint: ''
description: Enerji dosyasını piyasa (elektrik 6446, doğal gaz 4646, yenilenebilir
  5346) ve katman (lisans-düzenleyici, sözleşmesel, idari yargı) ekseninde konumlandırıp
  doğru kanun, yönetmelik ve mercii belirleme
name: temel-kavramlar-ve-sistem
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
  - ad: Elektrik Piyasası Kanunu
    numara: '6446'
    tur: kanun
  - ad: Mühendislik ve Mimarlık Meslek Kanunu
    numara: '4646'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Enerji Hukuku Temel Kavramlar ve Sistematik

## Görev
Enerji dosyasını doğru piyasaya ve hukuki katmana oturtmak; uygulanacak kanun (6446/4646/5346/5015/5307), ilgili ikincil mevzuat ve görevli mercii hızlıca tespit ederek sonraki uzman becerilere doğru giriş kapısını açmak.

## Soğuk başlangıç (intake)
1. Hangi enerji türü/piyasa: elektrik, doğal gaz, yenilenebilir, akaryakıt, LPG?
2. Müvekkilin sıfatı: üretici/önlisans sahibi, tedarikçi, dağıtım/iletim, OSB üreticisi, tüketici, yatırımcı, EPC yüklenicisi?
3. Uyuşmazlık türü: lisans/düzenleyici uyum, EPDK yaptırımı, tarife/uzlaştırma alacağı, sözleşmesel (PPA/EPC) mi?
4. Lisans/önlisans var mı, hangi tarihli; lisanssız üretim kapsamında mı?
5. Bir EPDK işlemi/yaptırımı tebliğ edildi mi, tebliğ tarihi nedir?

## Denetim şeması
1. **Piyasa tespiti**: Elektrik için 6446 ve Elektrik Piyasası Lisans Yönetmeliği; doğal gaz için 4646; yenilenebilir destek için 5346; akaryakıt için 5015; LPG için 5307. Faaliyet birden çok kanunu ilgilendirebilir (ör. yenilenebilir üretim hem 6446 lisansı hem 5346 desteği).
2. **Faaliyet/lisans türü**: 6446 m.5 lisans gerektiren faaliyetler (üretim, iletim, dağıtım, toptan/perakende satış, OSB, piyasa işletim); m.14 ve Lisanssız Elektrik Üretimi Yönetmeliği kapsamında lisanssız üretim eşikleri ve mahsuplaşma. Ara sonuç: lisanslı mı lisanssız mı rejim.
3. **Katman ayrımı**: (a) Düzenleyici uyum — EPDK Kurul kararı/yönetmelik; (b) Sözleşmesel — bağlantı anlaşması, sistem kullanım anlaşması, PPA, EPC, TBK 6098; (c) İdari yargı — EPDK işlemine karşı iptal/tam yargı (İYUK).
4. **Görev-yetki ve süre**: EPDK işlemleri idari işlem; idari yargıda dava (İYUK m.7, kural 60 gün). Sözleşmesel uyuşmazlıkta tahkim şartı varsa adli yargı/tahkim ayrımını netleştir.
5. **Tarih kilidi**: Olay tarihindeki yürürlük halini ve YEKDEM/tarife versiyonunu sabitlemeden değerlendirme yapma.

## Çıktı modülleri
- Dosya konumlandırma notu (piyasa + katman + uygulanacak norm seti).
- Görevli merci ve süre uyarısı.
- Hangi uzman beceriye geçileceğine dair yönlendirme.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

