---
argument-hint: ''
description: Taşınmaza haksız tecavüz/işgal olduğunda, geçmiş işgal bedeli (ecrimisil)
  istendiğinde ya da paydaşlar arası ortaklık sona erdirilmek istendiğinde; el atmanın
  önlenmesi, ecrimisil ve izale-i şuyu dava
name: el-atma-ecrimisil-ortakligin-giderilmesi
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# El Atmanın Önlenmesi, Ecrimisil ve Ortaklığın Giderilmesi

## Görev
Taşınmaz üzerindeki fiilî uyuşmazlıkları çözmek: haksız müdahaleyi durdurmak (el atmanın önlenmesi), haksız işgal dönemi için kullanım bedeli almak (ecrimisil) ve birlikte mülkiyeti sona erdirmek (ortaklığın giderilmesi/izale-i şuyu).

## Soğuk başlangıç (intake)
- Müdahale ne biçimde: fiilî işgal, sınır/taşkın yapı, izinsiz kullanım mı?
- Taşınmaz tek malikte mi, paylı/elbirliği mülkiyette mi?
- Ecrimisil isteniyorsa işgal süresi ve emsal kira/getiri verisi var mı?
- Talep müdahalenin durdurulması mı, ortaklığın tamamen giderilmesi mi?

## Denetim şeması
1. **El atmanın önlenmesi (TMK m.683/2)**: Malik, taşınmazına haklı sebep olmaksızın yapılan her müdahalenin önlenmesini ister. Unsurlar: davacının malik (veya ayni hak sahibi) olması, müdahalenin varlığı/sürmesi ve haksızlığı. Yapı varsa kal (yıkım) talebi eklenir; iyiniyetli taşkın yapıda m.725 dengesi gözetilir.
2. **Paylı mülkiyette husumet**: Her paydaş tek başına el atmanın önlenmesi isteyebilir (koruma işlemi, m.693); elbirliği mülkiyetinde koruyucu davaların tek mirasçıca açılabileceği kabul edilir [doğrulanacak — karararama.yargitay.gov.tr].
3. **Ecrimisil (haksız işgal tazminatı)**: Kötüniyetli/haksız zilyetten, işgal süresince kullanım bedeli istenir; talep geriye dönük olup zamanaşımına (TBK m.146, 10 yıl; haksız fiil yönüyle m.72 değerlendirmesi) ve emsal getiri-keşfe dayanır. Paydaşlar arası ecrimisilde önceden intifadan men koşulu (kural olarak) aranır [ilkeler için karararama.yargitay.gov.tr].
4. **Ortaklığın giderilmesi (m.698-699)**: Her paydaş, aksine engel yoksa her zaman paylaşma isteyebilir. Mahkeme önce **aynen taksimi** (m.699/2) araştırır; mümkün değilse **satış suretiyle paylaştırma** (açık artırma, m.699/3) yapar. Elbirliği mülkiyetinde tüm ortaklar davaya dahil edilir (zorunlu dava arkadaşlığı); muhdesat ve takyidat bedel paylaşımında dikkate alınır.
5. **Ara sonuç**: Müdahale varsa men (+ gerekirse kal) ve ecrimisil; birlikte mülkiyette aynen taksim ya da satış.

## Çıktı modülleri
- El atmanın önlenmesi + ecrimisil dava dilekçesi iskeleti.
- Ortaklığın giderilmesi dilekçesi (paydaş listesi, pay oranları, aynen taksim/satış talebi).
- Görev/yetki notu: el atma asliye hukuk, ortaklığın giderilmesi sulh hukuk (HMK m.4), yetki taşınmazın yeri (HMK m.12).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

