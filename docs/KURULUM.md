# Kurulum ve Güncelleme Rehberi

Bu rehber, `turkiye-legal`'i Claude Code üzerinden kurmak, kullanmak ve güncel tutmak isteyen herkes (özellikle hiç terminal deneyimi olmayan avukatlar) için yazıldı. Adımları sırayla takip etmeniz yeterli.

---

## 1. Ön Koşul: Claude Code kurulu olmalı

`turkiye-legal`, bağımsız bir uygulama değildir — [Claude Code](https://code.claude.com) üzerinde çalışan bir **plugin paketidir**. Önce Claude Code'un kurulu ve çalışır durumda olduğundan emin olun. Claude Code'u nasıl kuracağınızı bilmiyorsanız [resmî dokümantasyona](https://code.claude.com) bakın.

Kurulum tamamlandığında terminalde şu komutu çalıştırıp bir hata almadığınızı doğrulayın:

```bash
claude --version
```

---

## 2. `turkiye-legal` marketplace'ini ekleyin

Bu, yalnızca **bir kez** yapmanız gereken bir adımdır. Terminali açın (Mac/Linux'ta Terminal, Windows'ta PowerShell) ve şunu yazın:

```bash
claude plugin marketplace add https://github.com/mesutcandemir39/turkiye-legal
```

Bu komut, `turkiye-legal` deposunu Claude Code'a "buradan plugin kurabilirsin" olarak tanıtır. Henüz hiçbir şey kurmaz.

---

## 3. İhtiyacınız olan plugin'leri kurun

Her plugin ayrı ayrı kurulur — yalnızca ilginizi çeken hukuk alanlarını kurmanız yeterlidir, hepsini kurmak zorunda değilsiniz.

```bash
# KVKK / veri koruma ile ilgileniyorsanız
claude plugin install kvkk-uyum@turkiye-legal

# İş hukuku ile ilgileniyorsanız
claude plugin install is-hukuku@turkiye-legal

# Sözleşme incelemesiyle ilgileniyorsanız
claude plugin install sozlesme@turkiye-legal

# İcra-iflas ile ilgileniyorsanız
claude plugin install icra-iflas@turkiye-legal

# Mevzuat takibiyle ilgileniyorsanız
claude plugin install mevzuat-takip@turkiye-legal

# Dava takibiyle ilgileniyorsanız
claude plugin install dava-takip@turkiye-legal

# Ticaret/şirketler hukukuyla ilgileniyorsanız
claude plugin install ticaret-sirketler@turkiye-legal

# Fikri mülkiyet/OSS lisans konularıyla ilgileniyorsanız
claude plugin install fikri-mulkiyet@turkiye-legal

# İdare/vergi hukukuyla ilgileniyorsanız
claude plugin install idare-vergi@turkiye-legal
```

**Öneri:** `cekirdek` plugin'ini de kurun — süre hesaplama, veri maskeleme ve sürüm kontrolü gibi diğer tüm plugin'lerin dayandığı paylaşılan altyapıyı içerir:

```bash
claude plugin install cekirdek@turkiye-legal
```

Hangi plugin'in hangi skill'leri içerdiğini görmek için ana [`README.md`](../README.md)'deki "Plugin haritası" tablosuna bakın.

---

## 4. Bir skill'i kullanın

Kurulum tamamlandıktan sonra, Claude Code içinde `/` yazarak veya doğrudan skill adını belirterek çağırabilirsiniz:

```
/kvkk-uyum:aydinlatma-review dosya.md
```

veya bir dosya yüklemeden, doğrudan konuşarak:

```
Bu aydınlatma metnini KVKK açısından incele: [metni buraya yapıştırın]
```

Claude Code, isteğinizin içeriğine göre ilgili skill'i otomatik olarak tanıyıp devreye alabilir.

---

## 5. Kurulu sürümünüzü kontrol edin

Hangi plugin'lerin kurulu olduğunu ve hangi sürümde olduklarını görmek için:

```bash
claude plugin list
```

`turkiye-legal`'in kendisinin bir **sürüm kontrol skill'i** de vardır — kurulu sürümünüzü GitHub'daki en son Stable sürümle karşılaştırır ve güncelleme varsa çalıştırmayı dener:

```
/cekirdek:surum-kontrolu
```

Bu skill'in davranışı Claude Code oturumunuzun **izin moduna** bağlıdır:

- **Varsayılan/kısıtlı mod:** Güncelleme tespit edilirse `claude plugin update` komutunu çalıştırmadan önce **size sorulur.**
- **`auto`/`bypass` modu:** Siz zaten Claude'a araçları onay istemeden kullanma izni verdiğiniz için, güncelleme **sessizce ve otomatik olarak** gerçekleşir.

Bkz. aşağıdaki "Neden otomatik güncelleme yok?" bölümü — bu, iki modun neden farklı davrandığının gerekçesidir.

---

## 6. Güncelleme

**Önemli: Güncellemeler otomatik gelmez.** Claude Code, bir plugin'i kurduğunuz anda o anki sürüme sabitler. Biz depoda yeni bir skill eklesek veya bir hatayı düzeltsek bile, sizin kurulu kopyanız **kendiliğinden değişmez.**

Güncel kalmak için düzenli olarak (örn. her ay bir kez, veya `surum-kontrolu` skill'i size bir güncelleme olduğunu söylediğinde) şunu çalıştırın:

```bash
claude plugin update <plugin-adı>@turkiye-legal
```

Örnek:

```bash
claude plugin update kvkk-uyum@turkiye-legal
```

Kurduğunuz her plugin'i ayrı ayrı güncellemeniz gerekir.

### Neden otomatik güncelleme, izin modunuza bağlı?

Bilinçli bir tasarım: bir avukatın kullandığı hukuki bir aracın, kendisi fark etmeden davranışının değişmesi (yeni bir yorum, farklı bir kural uygulaması) **kabul edilemez bir risktir.** Ama "onay" zaten Claude Code'un kendi izin sisteminde var — `turkiye-legal` bunun üzerine ikinci bir onay katmanı icat etmek yerine bu sisteme güvenir:

- Oturumunuzu varsayılan/kısıtlı modda tutarsanız, her güncelleme öncesi size sorulur — davranış tam olarak "otomatik güncelleme yok" ile aynıdır.
- Oturumunuzu bilinçli olarak `auto`/`bypass` moduna alırsanız, bu zaten "Claude'un araçları onay istemeden kullanmasına izin veriyorum" demektir — güncelleme de bu genel iznin doğal bir parçası olur.

Detaylı gerekçe: ``CREDITS.md`` ADR-010 ve ADR-011.

---

### Haftalık otomatik kontrol kurmak isterseniz

`/cekirdek:surum-kontrolu`'nü her hafta elle çağırmak istemiyorsanız, Claude Code'a şunu söyleyebilirsiniz:

```
Sürüm kontrolünü haftada bir otomatik çalıştır.
```

Claude, Claude Code'un **zamanlanmış görev** özelliğini kullanarak (kullanıcının kendi makinesinde saklanan, cron ifadesiyle tetiklenen bir görev) haftalık bir kontrol kurar. **Önemli sınır:** bu, bir işletim sistemi cron'u değildir — yalnızca Claude Code uygulaması açıkken veya bir sonraki açılışında çalışır; bilgisayarınız veya uygulama kapalıyken arka planda çalışmaz. Gerçekten kesintisiz bir arka plan kontrolü istiyorsanız, işletim sisteminizin kendi zamanlayıcısına (`cron`, Windows Görev Zamanlayıcı) `claude -p "/cekirdek:surum-kontrolu"` gibi headless bir komut eklemeniz gerekir — Claude bu komutu size gösterebilir ama sizin adınıza kurmaz.

Detaylı gerekçe: `CREDITS.md` ADR-012.

## 7. Yeni bir sürüm çıktığını nasıl öğrenirim?

Üç yol:

1. **`/cekirdek:surum-kontrolu` skill'ini çalıştırın** — en pratik yöntem.
2. **[Releases](https://github.com/mesutcandemir39/turkiye-legal/releases) sayfasını takip edin** — her yeni Stable sürüm burada duyurulur, "Watch" butonuyla bildirim alabilirsiniz.
3. **[`CHANGELOG.md`](../CHANGELOG.md)'ye göz atın** — her sürümde nelerin değiştiğinin tam listesi burada.

Her durumda: **gerçek hukuki işlerinizde daima yalnızca "Stable / Latest Release" etiketli sürümleri kullanın**, `alpha`/`beta`/`rc` etiketli test sürümlerini değil.

---

## 8. Bir plugin'i kaldırmak isterseniz

```bash
claude plugin uninstall <plugin-adı>@turkiye-legal
```

---

## 9. Claude Cowork'te kullanmak isterseniz

`turkiye-legal`, standart **Claude Code plugin formatını** (`.claude-plugin/plugin.json` + `skills/` + `agents/`) kullanır — bu, Claude Cowork'ün de tanıdığı aynı formattır. Yani bu depodaki plugin'ler **ek bir uyarlama gerekmeden** Cowork'te de çalışır:

1. Cowork uygulamasında **Customize** → **Browse plugins** yolunu izleyin.
2. Marketplace URL'si olarak `https://github.com/mesutcandemir39/turkiye-legal` girin (Claude Code'daki `claude plugin marketplace add` komutuyla aynı adres).
3. İstediğiniz plugin'i (örn. `kvkk-uyum`) seçip kurun.

Kurulumdan sonra skill'leri Claude Code'daki gibi (`/kvkk-uyum:aydinlatma-review`) çağırabilirsiniz. **Tek fark:** bu depodaki skill'lerin hepsi metin tabanlı analiz/triyaj üretir (görsel dashboard/rapor üretmez), bu yüzden Cowork'e özgü bir "satır içi görsel render" davranışı beklemeyin — çıktı her iki yüzeyde de aynı biçimde (metin) görünür. `cekirdek:surum-kontrolu`'nün haftalık otomatik kontrol özelliği (bkz. §6) yalnızca Claude Code'un zamanlanmış görev aracını kullanır; Cowork'te bu özelliğin bir eşdeğeri olup olmadığını kendi Cowork sürümünüzden kontrol edin.

---

## Sorun mu yaşıyorsunuz?

- Kurulum veya kullanım sırasında bir hatayla karşılaşırsanız: [Issues](https://github.com/mesutcandemir39/turkiye-legal/issues/new/choose) üzerinden "🐛 Teknik Hata Bildirimi" formunu doldurun.
- Bir skill'in yanlış hukuki bilgi verdiğini düşünüyorsanız: aynı sayfadan "⚖️ Hukuki Hata Bildirimi" formunu kullanın — bu, projedeki en kritik geri bildirim türüdür.
- Genel bir sorunuz varsa: [Discussions](https://github.com/mesutcandemir39/turkiye-legal/discussions).
