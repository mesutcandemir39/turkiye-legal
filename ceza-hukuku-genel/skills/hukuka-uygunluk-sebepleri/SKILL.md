---
argument-hint: ''
description: Meşru savunma, ilgilinin rızası, hak kullanma, kanun hükmü ve amirin
  emri gibi hukuka uygunluk sebeplerini ve sınırın aşılmasını değerlendirmek gerektiğinde
  kullanılır.
name: hukuka-uygunluk-sebepleri
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Hukuka Uygunluk Sebepleri

## Görev
Tipik bir fiilin hukuka aykırılığını ortadan kaldıran sebeplerin (TCK m.24-27) bulunup bulunmadığını ve sınırın aşılması hâlinin etkisini değerlendirmek.

## Soğuk başlangıç (intake)
- Fiil hangi hak/değer için ve hangi saldırıya karşı yapıldı?
- Saldırı haksız, mevcut/yakın ve devam ediyor muydu?
- Savunma ile saldırı arasında orantı var mıydı; başka çıkış yolu var mıydı?
- Rıza söz konusuysa, konu üzerinde tasarruf edilebilir miydi?

## Denetim şeması
1. **Kanun hükmü ve amirin emri (m.24):** Fiil kanunun verdiği yetki ya da bağlayıcı emrin yerine getirilmesiyle mi işlendi? Konusu suç olan emir yerine getirilemez; getirilse de sorumluluk doğar (m.24/3).
2. **Meşru savunma (m.25/1):** Şartlar — (a) haksız bir saldırı, (b) saldırının hâlen var/başlamak üzere/devam ediyor olması, (c) kendine veya başkasına yönelmesi, (d) savunmanın saldırı ile orantılı olması. Tümü varsa fiil hukuka uygundur.
3. **Zorunluluk hâli (m.25/2):** Ağır ve muhakkak tehlikeden korunmak için orantılı kaçınma; bu bir kusurluluğu kaldıran sebep olarak da tartışılır.
4. **Hakkın kullanılması ve rıza (m.26):** Hakkını kullanan kişi (örn. avukatın savunma dokunulmazlığı), üzerinde mutlak surette tasarruf edilebilen bir hakka ilişkin geçerli ve önceden açıklanmış rıza. Yaşam ve vücut bütünlüğünde rızanın sınırlarına dikkat.
5. **Sınırın aşılması (m.27):** Sınır kast olmaksızın (taksirle) aşılmışsa ve fiil taksirle de cezalandırılıyorsa indirimli ceza; meşru savunmada mazur görülebilecek heyecan/korku/telaşla aşılması cezasızlık sonucunu doğurabilir. Ara sonuç: aşma kasıtlı mı, mazur görülebilir mi?
6. **Ara sonuç:** Bir sebep tam ise fiil suç değildir; eksikse kusurluluk katmanına geçilir.

## Çıktı modülleri
- Sebep bazlı şart kontrol listesi (madde atıflı).
- Orantılılık ve başka çıkış yolu değerlendirmesi.
- Sınırın aşılması senaryosu ve sonuç (cezasızlık/indirim).
- Savunma stratejisi notu ve `[DOĞRULANMADI]` içtihat ihtiyacı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

