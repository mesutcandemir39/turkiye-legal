---
argument-hint: ''
description: Tapu veya mülkiyet ispatı olmaksızın fiilî hâkimiyetin gasp ya da saldırı
  ile bozulduğu durumlarda; zilyetlik karinesi, gaspta geri alma, saldırıyı durdurma
  davaları ve kısa hak düşürücü süreler için
name: zilyetlik-ve-korunmasi
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
  version: 0.1.0
user-invocable: true
---


# Zilyetlik ve Zilyetliğin Korunması

## Görev
Mülkiyet ispatına girmeden, eşya üzerindeki fiilî hâkimiyetin (zilyetliğin) gasp veya saldırı yoluyla bozulmasına karşı hızlı koruma sağlamak; zilyetlik karinelerini ve dava yollarını işletmek.

## Soğuk başlangıç (intake)
- Müvekkil eşyayı fiilen elinde mi tutuyordu; doğrudan mı dolaylı zilyet mi (kiraya vermiş, emanet etmiş)?
- Zilyetlik nasıl bozuldu: zorla/gizlice alındı (gasp) mı, yoksa tecavüz/rahatsız etme (saldırı) mı?
- Fiili ve faili ne zaman öğrendi; üzerinden ne kadar süre geçti?
- Müvekkil sadece zilyetliğe mi dayanmak istiyor, yoksa mülkiyet de ispatlanabilir mi?

## Denetim şeması
1. **Zilyetliğin tanımı**: Eşya üzerinde fiilî hâkimiyet (TMK m.973). Aslî/fer'î, doğrudan/dolaylı zilyetlik ayrımı husumeti belirler.
2. **Karineler**: Taşınır zilyedi onun maliki sayılır (m.985); önceki zilyet de o sıradaki malik karinesinden yararlanır (m.986). Bu karineler ispat yükünü tersine çevirir.
3. **Gasptan korunma (m.981-982)**: Zilyetliği gasp edilen kişi kuvvet kullanarak (m.981) ya da dava yoluyla eşyayı geri isteyebilir; taşınmazda el koyanı çıkarıp yeniden zilyet olabilir (m.982).
4. **Saldırının önlenmesi (m.983)**: Zilyetliğine saldırılan, saldırının önlenmesini ve sebebinin giderilmesini isteyebilir.
5. **Hak düşürücü süre (m.984)**: Dava, fiilin ve failin öğrenilmesinden başlayarak 2 ay ve her hâlde fiilden itibaren 1 yıl içinde açılmalıdır. Bu süre kesin olup re'sen gözetilir.
6. **Sınır**: Zilyetlik davasında hakkın esası (mülkiyet) tartışılmaz; yalnızca fiilî durum korunur. Esasa ilişkin iddialar ayrı dava (istihkak/el atma) gerektirir.
7. **Ara sonuç**: Süre içindeyse hızlı koruma (geri verme/saldırının durdurulması); süre geçmişse mülkiyete dayalı dava yoluna geçiş.

## Çıktı modülleri
- Zilyetlik davası dilekçesi iskeleti ve süre uyarısı (2 ay / 1 yıl).
- Gasp/saldırı nitelendirme tablosu.
- Mülkiyet davasına geçiş için köprü notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

