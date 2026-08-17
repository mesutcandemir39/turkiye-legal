---
argument-hint: ''
description: İdari yargı kolunun adli yargıdan ayrımı, görevli yargı düzeninin tespiti,
  iptal/tam yargı/idari sözleşme dava tiplerinin ayrıştırılması gibi sistematik ve
  nitelendirme sorularında kullanılır; uyuşmaz
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
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve İdari Yargı Sistematiği

## Görev
Uyuşmazlığı doğru yargı koluna ve doğru dava tipine yerleştirmek; idari yargının görevli olup olmadığını ve hangi dava tipinin (iptal, tam yargı, idari sözleşme) açılması gerektiğini gerekçeli olarak saptamak.

## Soğuk başlangıç (intake)
- Uyuşmazlığın kaynağı bir idari işlem mi, idari eylem mi, yoksa sözleşme mi?
- Karşı taraf bir kamu idaresi/kurumu mu; işlem kamu gücü kullanılarak mı tesis edildi?
- Talep bir işlemin iptali mi, bir zararın tazmini mi, yoksa her ikisi mi?
- İşlemin tebliğ/öğrenme tarihi nedir?

## Denetim şeması
1. **Yargı kolu** (Anayasa m.125; İYUK m.1-2): İşlem/eylem kamu hizmetinin yürütülmesinden ve kamu gücünden doğuyorsa idari yargı görevlidir. Özel hukuk ilişkisi (ör. idarenin tasarruf malı kirası, fiili yol/kamulaştırmasız el atmada bedel) varsa adli yargı söz konusu olabilir; tereddütte 2247 sayılı Kanun çerçevesinde Uyuşmazlık Mahkemesi belirleyicidir.
2. **Kesin ve yürütülebilir işlem** (İYUK m.14/3-d): İcrai olmayan, hazırlık/iç işlem niteliğindeki işlemler dava edilemez. Zincir işlemlerde kesin işlemi tespit et.
3. **Dava tipi**:
   - Yetki-şekil-sebep-konu-maksat yönünden hukuka aykırılık iddiası ve menfaat ihlali varsa → **iptal davası** (m.2/1-a).
   - Kişisel hak ihlali ve zarar tazmini varsa → **tam yargı davası** (m.2/1-b); idari eylemde m.13 ön başvurusu unutulmaz.
   - İdari sözleşme şartlarından doğuyorsa → m.2/1-c.
4. **İstisna/ayrım**: İptal ve tam yargı birlikte (m.12) açılabilir; iptal kararı sonrası tam yargı için süre m.12 hükmüne göre işler.
5. **İspat yükü**: İdari işlemin sebep ve konu unsurlarına ilişkin dayanak belgeler kural olarak idarededir; resen araştırma ilkesi (İYUK m.20) geçerlidir.

## Çıktı modülleri
- Yargı kolu ve dava tipi nitelendirme notu (gerekçeli)
- Görevli/yetkili mahkeme önerisi
- Sıradaki adım: süre ve dava şartı kontrolüne yönlendirme



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

