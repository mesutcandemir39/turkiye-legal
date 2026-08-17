# Yönetişim (Governance)

## 1. Roller

| Rol | Yetki | Şu an |
|---|---|---|
| **Lead Maintainer** | Nihai karar mercii; lisans, güvenlik ve yönetişim dosyalarında tek onay yetkisi | Mesut Can Demir ([@mesutcandemir39](https://github.com/mesutcandemir39)) |
| **Dev Maintainers** | `scripts/`, `.github/workflows/`, `.devcontainer/` üzerinde onay yetkisi | Henüz atanmadı (bkz. not aşağıda) |
| **Legal Maintainers** | `skills/`, `agents/`, `sources/`, `evaluations/golden/` üzerinde onay yetkisi | Henüz atanmadı |
| **Katkıcı (Contributor)** | PR açabilir, issue açabilir, tartışmaya katılabilir | Herkes |

> **Not:** Bu depo **public** ve açık kaynaktır, ancak hâlâ kişisel bir hesap altındadır (organizasyon değil). GitHub Teams (`@turkiye-legal/dev-maintainers` vb.) kişisel hesaplarda çalışmaz; bu nedenle `.github/CODEOWNERS`'daki takım referansları depo bir organizasyona taşınana kadar fiilen devre dışıdır ve tüm onaylar Lead Maintainer'dan geçer. İlk dış bakımcılar katıldığında ve/veya depo bir organizasyona taşındığında bu bölüm güncellenecektir.

## 2. Karar Alma

Günlük kararlar (PR onayı, issue triyajı, küçük düzeltmeler) ilgili CODEOWNERS bölgesinin bakımcısı tarafından alınır. Mimari değişiklikler (yeni bir ADR gerektiren kararlar) Lead Maintainer onayı gerektirir ve `CREDITS.md`'ye yeni bir ADR olarak işlenir — mevcut bir ADR asla sessizce değiştirilmez.

## 3. Hukuki Yorum Uyuşmazlıkları (Legal Conflict Resolution)

Türk hukukunda yargı kararları çelişebilir, doktrin görüşleri ayrışabilir ve aynı madde farklı yorumlanabilir. Bu, bir hata değil hukukun doğasıdır — ancak bir açık kaynak PR'ının bir mahkeme salonu tartışmasına dönüşmesine izin verilmez.

**Kural:**

1. Bir PR'da veya issue'da hukuki bir yorum uyuşmazlığı çıkarsa, taraflar önce kaynaklarını (kanun maddesi, Yargıtay/Danıştay kararı, doktrin referansı) net şekilde ortaya koyar.
2. Tartışma **iki round** içinde netleşmelidir. Üçüncü round'a geçmeden önce şu iki seçenekten biri uygulanır:
   - **(a) Çift görüşlü format zorunluluğu:** İlgili `SKILL.md` veya `references/` dosyası, tek bir "doğru" cevap sunmak yerine iki (veya daha fazla) görüşü açıkça ayrıştırarak sunacak şekilde yeniden yazılır. Örnek format:
     ```
     ⚖️ Bu konuda doktrinde/içtihatta görüş ayrılığı bulunmaktadır:
     - Görüş A: ... (Kaynak: ...)
     - Görüş B: ... (Kaynak: ...)
     Somut olaya uygulanacak görüş için mutlaka bir avukata danışın.
     ```
   - **(b) Lead Maintainer nihai kararı:** Çift görüşlü format teknik olarak uygun değilse (örn. bir süre hesabı gibi tek bir doğru sonucu olması gereken bir konuda), Lead Maintainer ilgili kaynakları inceleyip nihai kararı verir ve gerekçesini PR'a yazar.
3. Hiçbir tartışma bir katkıcıyı susturmak veya küçümsemek için kullanılamaz — bkz. `CODE_OF_CONDUCT.md`.

## 4. Bakımcı Devri (Bus Factor)

Proje şu an tek bakımcıya bağımlıdır. Bu riski azaltmak için:

- DCO (Developer Certificate of Origin) kullanılır, CLA değil — katkı eşiği düşük tutulur.
- İlk 3 düzenli katkıcı (5+ merge edilmiş PR) `dev-maintainers` veya `legal-maintainers` rolüne davet edilir.
- Lead Maintainer uzun süre (90+ gün) aktif olmazsa, aktif bakımcılar arasından geçici bir "acting maintainer" belirlenir — bu durum `docs/` altında ayrıca belgelenecektir.

## 5. Değişiklik Süreci

Bu `GOVERNANCE.md` dosyasındaki kurallar bir PR ile değiştirilebilir; ancak böyle bir PR en az 7 gün açık kalmalı ve Lead Maintainer onayı gerektirir.
