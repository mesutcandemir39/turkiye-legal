---
argument-hint: ''
description: Roma hukukunun kendi iç sistematiğini (personae-res-actiones, ius civile/gentium/honorarium,
  ayni-şahsi hak, contractus-delictum) açıklamak ve bir kavramın Roma kökenini çözmek
  gerektiğinde kullanılır
name: roma-hukuku-sistematigi
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


# Roma Hukuku Sistematiği ve Temel Kavramlar

## Görev
Roma hukukunun iç mimarisini doğru biçimde ortaya koymak ve bir hukuki kavramın Roma kökenini, yürürlükteki Türk hukuku ile karıştırmadan, akademik düzeyde açıklamak.

## Soğuk başlangıç (intake)
- Soru akademik/eğitsel mi, yoksa yürürlükteki bir maddenin yorumuna mı bağlanacak?
- Hangi kurum sorgulanıyor (kişi-ehliyet, mülkiyet-zilyetlik, sözleşme, haksız fiil, miras)?
- Klasik dönem mi (Gaius/klasik hukukçular) yoksa Iustinianus dönemi mi referans alınacak?
- Latince maxim/kaynak metni gerekiyor mu?

## Denetim şeması
1. Tasnif katmanını belirle: Gaius Institutiones'in personae (kişiler) – res (mallar/haklar) – actiones (davalar) üçlüsü çerçevesinde kurumun yerini sapta. Bu tasnif, bugünkü Pandekt sistemli TMK/TBK ayrımının atasıdır.
2. Norm kaynağını ayrıştır: ius civile (Roma vatandaşlarına özgü), ius gentium (kavimler arası ortak), ius honorarium (praetor hukuku) ve ius naturale ayrımını kur; kurumun hangi tabakadan geldiğini göster.
3. Hak tipini belirle: ayni hak (ius in rem, herkese karşı, actio in rem) ile şahsi hak (ius in personam, belirli kişiye karşı, actio in personam) ayrımını uygula. Bu ayrım, TMK eşya hukuku ile TBK borç ilişkisi ayrımının köküdür.
4. Borç kaynağını sınıfla: contractus (re/verbis/litteris/consensu doğan), delictum, quasi contractus, quasi delictum. Consensu doğan rıza sözleşmeleri (emptio venditio, locatio conductio, societas, mandatum) bugünkü TBK isimli sözleşmelerinin atasıdır.
5. Usul mantığını ekle: Roma hukuku actio (dava kalıbı) temellidir; hak değil dava merkezlidir. Bu, modern maddi hak-dava ayrımının tarihî zıttıdır ve farkı vurgulanmalıdır.
6. Ara sonuç: Kurumu Roma sistematiğinde konumla; sonra bir sonraki adımda (resepsiyon becerisi) yürürlükteki Türk normuna bağla. Roma kuralını yürürlükteki hüküm yerine koyma.

İspat/dayanak: birincil kaynak Corpus Iuris Civilis fragmanlarıyla (D./Inst./Gai./C.) gösterilir; doktrin yazar-eser-sayfa ile, tam künye [DOĞRULANMADI].

## Çıktı modülleri
- Kavram kartı: Roma adı + tanım + tasnifteki yeri.
- Kaynak atıfları (Digesta/Institutiones fragmanları, varsa Latince maxim).
- Yürürlükteki Türk hukukuna köprü notu (ilgili TMK/TBK maddesi, ayrıntı resepsiyon becerisinde).
- Sınır uyarısı: tarihî bilgi yürürlükteki normun yerine geçmez.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

