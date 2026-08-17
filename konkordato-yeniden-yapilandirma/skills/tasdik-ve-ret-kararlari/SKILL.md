---
argument-hint: ''
description: Konkordatonun tasdiki için aranan şartların denetimi, tasdik veya ret
  kararının sonuçları ve bu kararlara karşı kanun yollarının işletilmesi gerektiğinde
  kullanılır.
name: tasdik-ve-ret-kararlari
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
  - ad: İcra ve İflas Kanunu
    numara: '2004'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tasdik, Ret ve Kanun Yolları

## Görev
Konkordatonun mahkemece tasdiki için İİK m.305 şartlarını denetlemek, tasdik (m.306) ve ret (m.308) kararlarının sonuçlarını çözümlemek, kanun yollarını (istinaf/temyiz) işletmek.

## Soğuk başlangıç (intake)
- Komiserin esas hakkındaki raporu mahkemeye sunuldu mu?
- Çoğunluk sağlandı, depo şartları yerine getirildi mi?
- İmtiyazlı alacakların ödenmesi güvenceye bağlandı mı?
- Tasdik/ret kararı verildi mi, hangi tarihli?

## Denetim şeması
1. **Tasdik şartları (m.305).** (a) Teklifin borçlunun kaynaklarıyla orantılı olması (rehinli malların satışından veya devamlı işletmeden elde edilecek gelir gözetilir); (b) İİK m.206/1. sırada yer alan alacakların tam ödenmesinin güvenceye bağlanması (alacaklı vazgeçmedikçe); (c) yargılama giderleri ve konkordatonun yerine getirilmesi için gerekli giderlerin depo edilmesi.
2. **Tasdik kararı (m.306).** Mahkeme tasdik kararında alacaklıların hangi ölçüde alacaklarından vazgeçtiğini, ödeme takvimini ve gerekirse bir kayyım/denetim mekanizmasını gösterir. Tasdik kararı ilan ve tescil edilir.
3. **Tasdikin sonuçları (m.308/c-h).** Konkordato, tasdik edilmeyen alacaklar dâhil tüm alacaklılar için bağlayıcı hâle gelir (çekişmeli alacaklar ve rehinli/yakın istisnaları saklı). Rehinli alacaklılarla yapılan anlaşma ayrıca düzenlenir (m.308/h).
4. **Ret (m.308).** Şartlar yoksa talep reddedilir; borçlu iflasa tabi ise ve borca batıksa doğrudan iflasına karar verilebilir (m.308/son). İspat yükü: tasdik şartlarının varlığını borçlu ortaya koyar.
5. **Kanun yolları.** Tasdik/ret kararına karşı istinaf ve temyiz yolu (İİK ve HMK genel hükümleri çerçevesinde) açıktır; süreler titizlikle hesaplanır. Yargıtay 23. Hukuk Dairesi içtihadı esas alınır `[doğrulanacak — karararama.yargitay.gov.tr]`. Ara sonuç: hangi kanun yoluna, hangi sürede başvurulacağı.

## Çıktı modülleri
- Tasdik şartları denetim raporu.
- Tasdik/ret kararı sonuç analizi.
- İstinaf/temyiz dilekçesi taslağı (yer tutuculu) ve süre hesabı.
- Karar sonrası icra/tescil adımları listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

