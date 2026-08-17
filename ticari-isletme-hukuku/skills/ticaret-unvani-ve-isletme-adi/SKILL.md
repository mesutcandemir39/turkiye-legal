---
argument-hint: ''
description: Ticaret unvaninin olusturulmasi, zorunlu/secimlik ekler, unvanin korunmasi
  ve unvana tecavuz; benzer unvan veya isletme adi kullanimina karsi tespit-men-tazminat
  talepleri gerektiginde kullanilir.
name: ticaret-unvani-ve-isletme-adi
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Ticaret Unvanı ve İşletme Adı

## Görev
Ticaret unvanının doğru oluşturulup oluşturulmadığını denetlemek ve unvan/işletme adına yönelik tecavüze karşı koruma araçlarını kurmak. Unvan, tacirin kimliği ve ticari itibarının taşıyıcısıdır.

## Soğuk başlangıç (intake)
1. Tacir gerçek kişi mi, hangi şirket türü mü (unvan çekirdeği değişir)?
2. Mevcut unvan zorunlu unsurları taşıyor mu?
3. Çakışan/benzer unvan veya işletme adı kim tarafından kullanılıyor, hangi tarihten beri?
4. İltibas (karıştırılma) ve zarar somut mu?

## Denetim şeması
1. **Unvanın oluşturulması:** TTK m.41-46 — gerçek kişi tacirde ad-soyad çekirdek; şirketlerde tür ve faaliyet konusu zorunlu (AŞ/Ltd. ibaresi şart, m.43-44). Ek ve sıfatlar gerçeğe aykırı, yanıltıcı, kamu düzenine aykırı olamaz (m.46). Unvan Türkçe esaslı kurulur.
2. **Tek unvan ve kullanma:** Her tacirin işletmesiyle ilgili işlemlerinde unvanını kullanma zorunluluğu (TTK m.39); belgelerde unvan, sicil numarası ve internet sitesi bilgisi (m.39/2). Unvan tescil ve ilan edilir (m.40).
3. **Unvanın korunması:** TTK m.50 — usulen tescil ve ilan edilen unvanı kullanma hakkı münhasıran sahibine aittir. TTK m.52 — unvana tecavüz edilen kişi: tespit, men (engelleme), tecavüzün sonucu olan maddi durumun ortadan kaldırılması (ref), kusur varsa maddi tazminat, ağır hal varsa manevi tazminat isteyebilir. Haksız rekabet hükümleriyle (TTK m.54 vd.) yarışma mümkündür.
4. **İşletme adı:** TTK m.53 — işletme adı işletmeyi tanıtır, tescil edilince benzer şekilde korunur.
5. **İspat:** Önceki tarihli tescil/kullanım, karıştırılma ihtimali ve zarar (tazminat için) ispatlanır. Ara sonuç: zorunlu unsur eksikse unvan düzeltilir; tecavüz varsa m.52 talepleri kurulur, ihtiyati tedbir istenebilir.

## Çıktı modülleri
- Unvan uygunluk denetim notu (zorunlu/yasak unsur kontrolü).
- Tecavüz halinde m.52 talep matrisi (tespit/men/ref/tazminat).
- İhtarname ve dava dilekçesi talep sonucu taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

