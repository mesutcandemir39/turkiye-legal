---
argument-hint: ''
description: Sebepsiz zenginleşmenin ne olduğunu, hangi borç kaynağına girdiğini ve
  haksız fiil ile sözleşmeden farkını netleştirmek gerektiğinde; bir uyuşmazlığın
  gerçekten sebepsiz zenginleşme olup olmadığını il
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Sistematik

## Görev
Eldeki malvarlığı kaymasının sebepsiz zenginleşme borç ilişkisi (TBK m.77 vd.) doğurup doğurmadığını teşhis etmek; bu kurumu sözleşme, haksız fiil ve vekâletsiz iş görmeden ayırarak doğru hukuki çerçeveyi kurmak. Yanlış çerçeve, ölçüyü (zenginleşme mi, zarar mı), süreyi ve faizi kökünden değiştirir.

## Soğuk başlangıç (intake)
- Bir malvarlığı değeri bir taraftan diğerine mi geçti; ne (para, mal, emek, kullanım yararı)?
- Bu geçişin arkasında geçerli bir sebep (sözleşme, kanun, mahkeme kararı) var mı?
- Taraflar arasında hâlâ ayakta bir sözleşme ilişkisi mevcut mu?
- Kayma kimin fiiliyle oldu (fakirleşenin ödemesi mi, zenginleşenin müdahalesi mi)?

## Denetim şeması
1. **Borç kaynağını ayır.** Sebepsiz zenginleşme, sözleşme ve haksız fiilin yanında üçüncü bağımsız kaynaktır (TBK m.77). Amacı denkleştirici adalet; ceza veya zarar tazmini değil. Ölçü daima "zenginleşme miktarı"dır.
2. **Dört unsuru sına (m.77/1).** (a) Zenginleşme (aktif artışı veya pasif azalması), (b) fakirleşme (malvarlığından veya emeğinden), (c) ikisi arasında illiyet bağı, (d) haklı sebebin yokluğu. Dördü birlikte aranır.
3. **Talep türünü belirle.** Edim sebepsiz zenginleşmesi (fakirleşenin bilinçli kazandırması) ile müdahale (haksız kullanım, başkasının malını harcama) sebepsiz zenginleşmesini ayır; ispat yükü ve kapsam farklılaşır.
4. **Yarışmayı kontrol et (tali nitelik).** Aynî istihkak (TMK m.683), sözleşmenin ifası veya haksız fiil (TBK m.49) talebi mümkünse kural olarak ona öncelik verilir; sebepsiz zenginleşme ikincil/tamamlayıcıdır. Vekâletsiz iş görme (TBK m.526 vd.) varsa onun özel hükümleri uygulanır.
5. **Ara sonuç.** Uygulanacak madde bloğu (m.77-82), talebin tipi ve görevli mahkeme netleşir; ispat yükü genel kural TMK m.6 ile dağıtılır: haklı sebebin yokluğunu iade isteyen ispatlar.

## Çıktı modülleri
- Nitelendirme notu (kaynak + tip + dayanak madde + gerekçe).
- Yarışma analizi (öncelikli talep var mı tablosu).
- Yanlış çerçeve riski uyarısı (zarar/zenginleşme ölçü farkı).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

