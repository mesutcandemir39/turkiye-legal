---
argument-hint: ''
description: Sığınma, mülteci, ikincil veya geçici koruma talebi söz konusu olduğunda;
  koruma başvurusunun statü tespiti, başvuru usulü, geri gönderme yasağı ve ret kararına
  itiraz için kullanılır.
name: uluslararasi-koruma
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


# Uluslararası ve Geçici Koruma

## Görev
Yabancının koruma ihtiyacını YUKK koruma rejimine yerleştirmek, doğru statüyü (mülteci, şartlı mülteci, ikincil koruma, geçici koruma) belirlemek, başvuru ve itiraz sürecini yönetmek; geri gönderme yasağını her aşamada güvence altına almak.

## Soğuk başlangıç (intake)
1. Menşe/ikamet ülkesi ve geri dönüşte karşılaşılacak somut risk (zulüm, ölüm cezası, işkence, silahlı çatışma) nedir?
2. Türkiye'ye giriş tarihi ve koruma talebi kayda alındı mı (kayıt tarihi)?
3. Suriye uyruklu/vatansız mı (geçici koruma kapsamı) yoksa diğer uyruk mu?
4. Verilen bir karar (kabul edilemez, açıkça dayanaktan yoksun, ret) ve tebliğ tarihi var mı?

## Denetim şeması
1. **Statü ayrımı**: Mülteci — Avrupa ülkesi kaynaklı olaylar nedeniyle (YUKK m.61, coğrafi sınırlama). Şartlı mülteci — Avrupa dışı kaynaklı zulüm korkusu (m.62). İkincil koruma — m.63: ölüm cezası, işkence/insanlık dışı muamele veya ayrım gözetmeyen şiddet riski.
2. **Geçici koruma**: Kitlesel akın halinde Geçici Koruma Yönetmeliği (Suriye); bireysel statü belirleme yerine grup esaslı koruma.
3. **Başvuru usulü**: m.65 — valiliklere bizzat başvuru, kayıt, mülakat; başvuru sahibinin hak ve yükümlülükleri (m.67-69).
4. **Geri gönderme yasağı (non-refoulement)**: m.4 ve m.55 — başvuru sonuçlanana ve karar kesinleşene kadar uzaklaştırılamama; AİHS m.3 ile birlikte mutlak nitelik.
5. **Karar ve itiraz**: Kabul edilemez başvuru (m.72), açıkça dayanaktan yoksunluk (m.79), ret kararları. İtiraz — Uluslararası Koruma Değerlendirme Komisyonu ve/veya idare mahkemesine dava; sürelere dikkat.
**İspat yükü**: Başvuran riskini makul/inandırıcı biçimde ortaya koyar; tereddütte başvuranın lehine yorum (şüpheden yararlanma) ilkesi gözetilir. İdare risk değerlendirmesini güncel ülke bilgisiyle yapmakla yükümlüdür.

## Çıktı modülleri
- Statü belirleme analizi ve dayanak madde tablosu.
- Başvuru/mülakat hazırlık notu ve risk anlatısı taslağı.
- Ret/kabul edilemezlik kararına karşı itiraz/dava dilekçesi iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

