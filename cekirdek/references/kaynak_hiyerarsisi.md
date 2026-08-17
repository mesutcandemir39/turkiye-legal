# Hukuki Kaynak Hiyerarşisi

Tüm `turkiye-legal` skill'leri, hukuki bir sonuca varırken aşağıdaki hiyerarşiyi izler. Üstteki bir kaynak alttakiyle çelişirse üsttaki bağlayıcıdır.

```
1. Anayasa
2. Kanun
3. Cumhurbaşkanlığı Kararnamesi
4. Yönetmelik
5. Tebliğ / Genelge
6. Yargıtay İçtihadı Birleştirme Kararı (İBK)  — BAĞLAYICI
   Yargıtay Daire Kararı, Danıştay Kararı, AYM Kararı — YOL GÖSTERİCİ, bağlayıcı DEĞİL
7. Doktrin (bilimsel görüş) — en zayıf bağlayıcılık, yalnız yorum desteği
```

## Uygulama kuralı

Bir skill bir hukuki sonuca ulaştığında, dayandığı kaynağı **bu hiyerarşideki konumuyla birlikte** belirtir. Örnek:

> KVKK m.10 (Kanun) gereği veri sorumlusu kimliği aydınlatma metninde açıkça belirtilmelidir. Bu konuda [Yargıtay Y. Karar No] emsal teşkil eder ancak bağlayıcı değildir; somut olayda farklı değerlendirilebilir.

## İBK ile daire kararı ayrımı

Bu ayrım özellikle önemlidir çünkü sık karıştırılır:

- **İçtihadı Birleştirme Kararı (İBK):** Yargıtay Genel Kurulu tarafından, çelişen daire kararlarını birleştirmek için verilir. **Tüm mahkemeleri ve Yargıtay dairelerini bağlar** (2797 sayılı Yargıtay Kanunu m.45).
- **Daire kararı:** Tek bir Yargıtay dairesinin verdiği karardır. Emsal niteliğindedir ama **bağlayıcı değildir** — aynı konuda başka bir daire veya aynı daire farklı bir tarihte farklı karar verebilir.

Bir skill bu ikisini ayırt etmeden "Yargıtay şöyle karar vermiştir, bu nedenle kesindir" ifadesini **kullanamaz**.

## Kaynak: sources/ kayıt defteri ile ilişki

Bu hiyerarşi *hangi kaynağın diğerine üstün olduğunu* belirler; `sources/mevzuat/kanunlar.yaml` ise *bir kaynağın gerçekten var olup olmadığını* (uydurma olmadığını) doğrular. İkisi birbirini tamamlar — bkz. ``CREDITS.md`` ADR-005.
