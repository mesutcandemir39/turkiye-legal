---
argument-hint: ''
description: Sermaye piyasası ilişkisinin nitelendirilmesi, ihraççı ve sermaye piyasası
  aracı tespiti, hangi rejimin (SPK madde, Kurul tebliği, BİST kuralı) uygulanacağının
  ve görevli mercinin belirlenmesi gerekti
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
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Sistematik

## Görev
Önündeki olayı sermaye piyasası hukuku süzgecinden geçirip doğru nitelendirmek; uygulanacak normu (SPK maddesi → Kurul tebliği → BİST/MKK/Takasbank prosedürü) ve görevli mercii (Kurul, idari yargı, adli yargı, tahkim) belirlemek.

## Soğuk başlangıç (intake)
- İlgili ortaklık halka açık mı, payları borsada işlem görüyor mu, yoksa halka kapalı ihraççı mı?
- Söz konusu araç nedir (pay, borçlanma aracı, yatırım fonu katılma payı, türev)?
- İşlem halka arz mı, tahsisli/nitelikli yatırımcıya satış mı, ikincil piyasa işlemi mi?
- Sorun ihraç, kamuyu aydınlatma, piyasa dürüstlüğü, kurumsal yönetim mi yoksa yaptırım boyutu mu?

## Denetim şeması
1. **İhraççı/halka açıklık sıfatı:** Pay sahibi sayısı veya borsada işlem görme üzerinden halka açık ortaklık niteliği (SPK m.16) belirlenir. Halka açıklık, sürekli yükümlülükleri (m.14-15) tetikler.
2. **Araç niteliği:** İşleme konu unsurun "sermaye piyasası aracı" (SPK m.3) olup olmadığı saptanır; değilse SPK rejimi dışıdır.
3. **İşlem tipi:** Halka arz mı (SPK m.4, izahname zorunluluğu) yoksa istisna kapsamında tahsisli satış mı (m.11 ve ilgili tebliğ) olduğu ayrılır; ara sonuç olarak izahname/ihraç belgesi gerekip gerekmediği netleşir.
4. **Görevli merci:** İdari yaptırım uyuşmazlıkları idari yargıda (İYUK m.2, m.7); izahname sorumluluğu/tazminat adli yargıda; piyasa suçları (m.106-107) ağır ceza mahkemesinde, Kurul mütalaası şartıyla (m.115); yatırımcı-aracı kurum uyuşmazlığında sözleşmesel tahkim/BİST yolu değerlendirilir.
5. **Norm güncelliği:** Atıf yapılan Kurul tebliğinin yürürlük ve değişiklik durumu doğrulanır; ispat yükü, iddia eden tarafa aittir (HMK m.190; idari işlemde idarenin gerekçelendirme yükü).

## Çıktı modülleri
- Nitelendirme notu: ortaklık/araç/işlem tipi ve uygulanacak rejim
- Görevli/yetkili merci tespiti ve süre uyarısı
- İlgili SPK maddeleri ve tebliğ atıfları listesi (güncellik kaydıyla)
- Sonraki adım önerisi ve uzman beceriye yönlendirme



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

