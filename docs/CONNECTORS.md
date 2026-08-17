# Harici Bağlayıcı (Connector) Sözleşmesi

> Bu belge, `turkiye-legal`'e gelecekte eklenebilecek harici veri kaynağı bağlayıcıları (MCP connector'ları — örn. içtihat veritabanı, Resmî Gazete beslemesi, UYAP entegrasyonu) için **ne "iyi" sayıldığını** tanımlar. Şu an depoda fiilen çalışan bir connector **yoktur** — bu belge, ROADMAP Q3'teki connector çalışmasından önce yazılan bir tasarım sözleşmesidir, böylece ilk connector eklenirken rastgele/tutarsız bir yaklaşım benimsenmez.

## 1. Neden bu belge var

`sources/mevzuat/kanunlar.yaml` gibi statik kaynak defterleri, bu projenin halüsinasyon savunmasının temelidir. Ancak statik defterler doğası gereği güncelliğini kaybeder — yeni bir içtihat, yeni bir Kurul kararı veya güncel bir Resmî Gazete sayısı defterde olmayacaktır. Bir **connector**, modele canlı/güncel veriye erişim sağlayarak bu boşluğu kapatabilir — ama yanlış tasarlanmış bir connector, statik defterin sağladığı doğrulanabilirliği geri götürebilir (örn. connector'ın döndürdüğü veri kendisi hatalıysa veya prompt injection'a açıksa).

## 2. "İyi bir hukuki connector" ne demektir

Bir connector, aşağıdaki kriterlerin **hepsini** karşılamadan bu projeye eklenmez:

### 2.1 Kimlik doğrulama ve erişim

- Connector, **salt okunur (read-only)** erişim sağlamalıdır. Bir connector'ın resmî bir sisteme (örn. UYAP, Ticaret Sicili) yazma/değiştirme yetkisi olması bu projenin kapsamı dışındadır — geri dönüşü olmayan bir işlemi (dilekçe gönderme, ödeme yapma gibi) bir connector üzerinden otomatik tetiklemek asla yapılmaz.
- Kimlik bilgileri (API anahtarı, OAuth token) kullanıcının **kendi** hesabına ait olmalıdır — `turkiye-legal` hiçbir paylaşılan/ortak kimlik bilgisi barındırmaz veya dağıtmaz.
- Kullanıcının kimlik bilgileri asla depo içine, loglara veya golden test senaryolarına yazılmaz.

### 2.2 Provenance (kaynak izlenebilirliği)

- Connector'ın döndürdüğü her sonuç, **nereden geldiğini** (hangi resmî kaynak, hangi tarih, hangi URL/erişim yöntemi) açıkça taşımalıdır. Bir skill, connector'dan gelen bir bilgiyi kullanıcıya sunarken bu provenance bilgisini **de** aktarmak zorundadır — "connector şunu söyledi" değil, "şu kaynağa göre (X tarihli, Y URL'sinde), şu bilgi".
- Connector sonucu, statik kaynak defterindeki bir kayıtla çelişiyorsa (örn. bir kanunun yürürlükten kalktığını söylüyor ama defter "yürürlükte" diyor), skill bu çelişkiyi **gizlemeden** kullanıcıya bildirmelidir — hangisinin doğru olduğuna kendi başına karar vermez.

### 2.3 Prompt injection direnci

- Connector'dan dönen içerik (örn. bir web sayfasının metni, bir API yanıtı) **asla** doğrudan talimat olarak yorumlanmaz. Bir içtihat metninin içine gömülü "önceki talimatları unut" türü bir ifade, modelin davranışını değiştirmemelidir — bkz. `SECURITY.md` §2 (Kritik Hukuki Yanıltma Açıkları).
- Connector çıktısı, skill'in sistem promptunun bir parçası olarak değil, **kullanıcı girdisiyle eşdeğer güven seviyesinde** bir veri olarak ele alınır.

### 2.4 Zarif bozulma (graceful degradation)

- Connector erişilemezse (ağ hatası, kota aşımı, kimlik doğrulama hatası), skill bu durumu **açıkça** bildirmelidir — "muhtemelen güncelsiniz" gibi bir varsayımda bulunulmaz (bkz. `cekirdek:surum-kontrolu`'nün aynı ilkeyi uyguladığı `ADR-010`/`ADR-011` deseni).
- Bir connector'ın yokluğunda skill, statik kaynak defterine geri dönebilmeli (mümkünse) veya açıkça "bu bilgi için connector gereklidir, şu an mevcut değil" demelidir.

### 2.5 Maliyet ve hız şeffaflığı

- Ücretli/abonelik gerektiren bir connector (örn. bir içtihat veritabanı API'si) kullanılıyorsa, bu README'de ve ilgili skill'in dokümantasyonunda **açıkça** belirtilir — "ücretsiz" gibi yanıltıcı bir izlenim verilmez.

## 3. Mevcut Connector'lar

Şu an depoda fiilen çalışan bir MCP connector **yoktur.** `cekirdek:surum-kontrolu`, GitHub'ın genel (kimlik doğrulamasız) Releases API'sine `urllib` ile doğrudan bir HTTP isteği atar — bu teknik olarak bir "connector" değil, deterministik bir script'in tek bir genel API uç noktasına yaptığı basit bir çağrıdır; yukarıdaki kriterlerin çoğu (kimlik doğrulama, provenance karmaşıklığı) bu basit kullanım için geçerli değildir.

## 4. İstenen (Wanted) Connector'lar

Aşağıdakiler, ROADMAP Q3/M6 hedefiyle uyumlu, topluluktan katkı beklenen connector fikirleridir — hiçbiri taahhüt değildir:

| Connector fikri | Hangi boşluğu kapatır | Not |
|---|---|---|
| Ücretsiz/kamuya açık içtihat kaynağı | `sources/ictihat/`'ın en büyük yapısal boşluğu (bkz. ROADMAP M6) | Türkiye'de ücretsiz, makine-okunabilir, kapsamlı bir kamu içtihat API'si şu an bilinmiyor — bu, bir fizibilite araştırması gerektirir |
| Resmî Gazete günlük besleme | `mevzuat-takip/agents/resmi-gazete-gunluk.md` şu an `NOT_IMPLEMENTED` | resmigazete.gov.tr'nin resmî bir API'si olup olmadığı araştırılmalı |
| KVKK Kurulu / Rekabet Kurulu duyuru beslemesi | `mevzuat-takip:kurul-karari-takibi`'nin "yalnız verilen metni işler" sınırını genişletebilir | kvkk.gov.tr / rekabet.gov.tr'de yapılandırılmış bir besleme var mı araştırılmalı |
| UYAP entegrasyonu | Avukatın kendi dosyalarına erişim | Yalnız salt-okunur, kullanıcının kendi UYAP kimlik bilgileriyle; yazma/gönderme işlemi **asla** otomatikleştirilmez |

## 5. Bir Connector Önerisi Nasıl Sunulur

`CONTRIBUTING.md`'deki "✨ Yeni Skill / Agent / Routine Talebi" issue şablonunu kullanın ve şunları ekleyin: connector'ın hangi resmî/güvenilir kaynağa bağlandığı, kimlik doğrulama modeli, yukarıdaki §2 kriterlerinin her birine nasıl uyduğu. Kriterlerden birini karşılamayan bir connector önerisi, gerekçesi ne olursa olsun bu depoya eklenmez.
