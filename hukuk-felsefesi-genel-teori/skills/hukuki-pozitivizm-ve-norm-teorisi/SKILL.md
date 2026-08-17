---
argument-hint: ''
description: Bir normun nereden bağlayıcılık aldığı, üst norma aykırı alt normun akıbeti
  veya geçerlilik-meşruiyet ayrımı tartışıldığında; Kelsen ve Hart çizgisinde norm
  geçerliliğini Türk norm hiyerarşisine bağla
name: hukuki-pozitivizm-ve-norm-teorisi
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Hukuki Pozitivizm ve Norm Geçerliliği

## Görev
Bir normun geçerliliğini (bağlayıcılığını) kaynağına dayalı olarak analiz etmek; Kelsen'in
saf hukuk teorisi (temel norm/basamak teorisi) ve Hart'ın tanıma kuralı çerçevesini Türk
pozitif norm hiyerarşisine (Anayasa m.11, m.90/son) bağlamak.

## Soğuk başlangıç (intake)
- Sorun bir alt normun (yönetmelik/tüzük) üst norma (kanun/Anayasa) aykırılığı mı?
- Norm yürürlükte ama içeriği "haksız" mı görünüyor (geçerlilik mi, meşruiyet mi sorusu)?
- Milletlerarası bir andlaşma ile kanun çatışması var mı (m.90/son devrede mi)?
- İddia akademik mi yoksa norm denetimi/iptal argümanı üretmeye mi yönelik?

## Denetim şeması
1. **Geçerlilik ölçütünü belirle.** Pozitivizmde bir norm, üst normun öngördüğü usul ve
   yetkiyle konulmuşsa geçerlidir; içeriğin "adil" olması geçerlilik şartı değildir
   (geçerlilik ≠ meşruiyet). Bunu açıkça ayır.
2. **Basamağı kur.** Anayasa m.11 (Anayasanın bağlayıcılığı/üstünlüğü) ve m.90/son (temel
   hak andlaşmalarının kanuna üstünlüğü) ile somut normu hiyerarşide konumla. Tanıma kuralı
   (Hart) burada "Türkiye'de hangi normlar hukuktur" sorusunun pozitif cevabıdır.
3. **Aykırılığın akıbetini ayır.** Kanunun Anayasaya aykırılığı → AYM norm denetimi
   (Anayasa m.148 vd.); yönetmeliğin kanuna/Anayasaya aykırılığı → idari yargıda iptal
   (2577 İYUK) ve Anayasa m.124 düzenleme yetkisi sınırı. Geçersizlik kendiliğinden değil,
   yetkili merci kararıyla tespit edilir.
4. **Geçerlilik-meşruiyet gerilimini işaretle.** Norm geçerli ama içeriksel olarak ağır
   adaletsizse, salt pozitivist cevap yetersiz kalır; bu noktada doğal hukuk/Radbruch
   tartışmasına köprü kur (ayrı beceriye yönlendir). Ara sonuç: geçerli ≠ her durumda uygulanmalı.
5. **Dayanak.** Kelsen (Saf Hukuk Teorisi) ve Hart (Hukuk Kavramı) ile Türk anayasa öğretisine
   atıf yap; sayfa [DOĞRULANMADI]. Norm denetimi kararı zikredilecekse künye
   kararlarbilgibankasi.anayasa.gov.tr üzerinden teyit edilir, doğrulanmadıkça [DOĞRULANMADI].

## Çıktı modülleri
- Norm hiyerarşisi şeması (somut norm yerleştirilmiş).
- Geçerlilik/meşruiyet ayrım notu.
- Aykırılık halinde başvurulacak denetim yolu (AYM / idari yargı) ve madde atfı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

