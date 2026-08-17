---
argument-hint: ''
description: Göç işlemlerinde dava/itiraz/başvuru sürelerinin hesaplanması veya kaçırma
  riskinin değerlendirilmesi gerektiğinde; özellikle sınır dışı ve idari gözetimin
  kısa süreleri için kullanılır.
name: sureler-ve-zamanasimi
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


# Süreler ve Hak Düşürücü Süreler

## Görev
Göç ve yabancılar alanındaki tüm idari ve yargısal sürelerin başlangıcını, uzunluğunu ve son gününü doğru hesaplamak; süre kaçırma riskini önceden tespit edip uyarmak.

## Soğuk başlangıç (intake)
1. Hangi işlemin süresi hesaplanacak (sınır dışı, gözetim, ikamet ret, çalışma ret, vatandaşlık ret)?
2. Tebliğ veya öğrenme tarihi tam olarak nedir, tebligat usulü ne (elden, e-tebligat, ilanen)?
3. Arada idari itiraz/komisyon başvurusu yapıldı mı?
4. Süre uzatan/durduran bir durum (adli tatil, mücbir sebep) var mı?

## Denetim şeması
1. **Başlangıç**: Süre kural olarak tebliğ/öğrenmeyle başlar. Tebligatın usulüne uygunluğu (Tebligat Kanunu) denetlenir; usulsüz tebligat süreyi başlatmaz.
2. **Süre uzunlukları**:
   - Genel iptal davası: İYUK m.7 — 60 gün.
   - Sınır dışı kararına karşı dava: YUKK m.53'teki özel kısa süre; bu süre genel 60 günden farklıdır ve titizlikle uygulanır.
   - İdari gözetime itiraz: YUKK m.57 — sulh ceza hâkimliğine; ayrıca gözetimin periyodik (aylık) değerlendirilmesi.
   - İdari itiraz/komisyon yolu varsa işlemeye etkisi (İYUK m.11) değerlendirilir.
3. **Durma/uzama**: İYUK m.8 — sürenin son günü adli tatile/resmî tatile rastlarsa uzama; idari yargıda çalışmaya ara verme dönemi etkisi.
4. **Sonuç tipi**: Bu süreler hak düşürücüdür; geçirilmesi davanın süre yönünden reddine yol açar ve telafisi yoktur.
**Ara sonuç**: Her işlem için tek bir kesin son gün ve güvenli iç hatırlatma (son günden birkaç gün önce) belirlenir.

## Çıktı modülleri
- İşlem bazlı süre takvimi (başlangıç, uzunluk, dayanak, son gün).
- Risk uyarısı: yaklaşan/kaçırılmış süreler.
- Tebligat geçerliliği kısa değerlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

