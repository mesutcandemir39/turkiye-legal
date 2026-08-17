---
argument-hint: ''
description: Eldeki deniz ticareti belgelerini (konişmento, çarter parti, sörvey/ekspertiz
  raporu, gemi jurnali, protesto) hızla okuyup riskli kayıtları, çelişkileri ve eksik
  delilleri çıkarmak gerektiğinde kullan
name: belge-konismento-carter-inceleme
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Belge İnceleme (Konişmento, Çarter ve Sörvey)

## Görev
Deniz ticareti dosyasındaki belgeleri sistemli biçimde okuyup riskli/asimetrik kayıtları, çelişkileri ve eksik delilleri tespit etmek; sözleşmesel pozisyonu ve ispat durumunu hızla çıkarmak.

## Soğuk başlangıç (intake)
- Hangi belgeler mevcut (konişmento, çarter parti, manifesto, ordino, sörvey, gemi jurnali, protesto/rezerv)?
- Belgeler tutarlı mı; konişmento ile çarter parti çatışıyor mu?
- Sözleşmede tahkim, yetki, yabancı hukuk, sorumluluk ve sürastarya kayıtları nasıl?
- Eksik veya okunamayan kritik belge var mı?

## Denetim şeması
1. **Konişmento denetimi**: Zorunlu içeriği (TTK m.1228 vd.) ve türünü (nama/emre/hamiline) belirle; "temiz/clean" mi yoksa rezerv kayıtlı mı olduğunu, yükün durumuna ilişkin karine etkisini (taşıyan aleyhine/lehine) değerlendir.
2. **Çarter parti kayıtları**: Navlun, FIOST, starya/sürastarya, off-hire, tahkim ve uygulanacak hukuk klozlarını çıkar; konişmentoya atıf (incorporation) yoluyla hangi kayıtların yük ilgilisine karşı ileri sürülebileceğini değerlendir.
3. **Sörvey/ekspertiz ve protesto**: Sörvey raporunun bağımsızlığını, hasar tespiti ve nedensellik açıklamasını denetle; ziya/hasar ihbar ve protestolarının süresinde ve usulünce yapılıp yapılmadığını kontrol et.
4. **Çelişki ve boşluk taraması**: Belgeler arası tutarsızlıkları (ağırlık, koli sayısı, tarih, taraf adı) listele; ispat bakımından eksik delilleri ([gemi jurnali], [VDR kaydı], [yükleme fotoğrafı] gibi) işaretle.
5. **İspat ve ara sonuç**: Her belgenin kimin lehine karine/delil oluşturduğunu belirt; çıktıda sözleşmesel pozisyonu güçlü/zayıf yönleriyle özetle ve hangi belgenin temin edilmesi gerektiğini öner. Belirsiz alanlara `[DOĞRULANMADI]` notu düş.

## Çıktı modülleri
- Belge envanteri ve eksik belge listesi
- Riskli/asimetrik kayıtlar tablosu (kloz bazında)
- Çelişki/ispat haritası ve temin edilecek deliller notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

