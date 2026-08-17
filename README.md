<div align="center">

# ⚖️ turkiye-legal

**Türkiye hukuku için açık kaynak yapay zekâ araç kiti**

[![Lisans: Apache 2.0](https://img.shields.io/badge/Lisans-Apache%202.0-blue.svg)](LICENSE)
[![Sürüm](https://img.shields.io/badge/sürüm-v0.1.0%20stable-brightgreen.svg)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-uyumlu-5A67D8.svg)](https://code.claude.com)
[![Katkı](https://img.shields.io/badge/PR-kabul%20ediliyor-brightgreen.svg)](CONTRIBUTING.md)
[![İnsan denetimi](https://img.shields.io/badge/hukuki-insan%20denetimi%20şart-red.svg)](#️-hukuki-sorumluluk-reddi)

</div>

---

## Bu nedir?

`turkiye-legal`, Türk hukukunda çalışan avukat, hukuk müşaviri ve hukuk öğrencileri için hazırlanmış **açık kaynak bir yapay zekâ araç kitidir.** Claude Code'un eklenti (plugin) sistemi üzerine kuruludur.

Sıradan bir "prompt arşivi" değildir. Üç şeyi bir arada yapar:

1. **Yapılandırılmış görevler** — Dilekçe denetimi, sözleşme tarama, süre hesabı gibi işler tek tek tanımlanmış, tekrarlanabilir beceriler (skill) hâlindedir.
2. **Kaynak doğrulama** — Her hukuki atıf, depodaki doğrulanmış kanun defterine karşı otomatik denetlenir. Uydurma kanun maddesi CI'da yakalanır.
3. **Deterministik hesaplama** — Süre ve tatil hesapları dil modeline bırakılmaz; Python koduna devredilir.

**Kimin için:** Türkiye'de hukuk pratiği yapan herkes. Terminal bilgisi gerekmez — [kurulum rehberi](docs/KURULUM.md) sıfırdan anlatır.

---

## Ne yapabilir?

<table>
<tr><td width="50%" valign="top">

**📄 Dilekçe ve evrak**
- HMK m.119 zorunlu unsur denetimi
- Dilekçe kalite skorlaması
- Karşı argüman üretimi
- Delil haritası çıkarma
- Müvekkile sade dil açıklaması

</td><td width="50%" valign="top">

**📋 Sözleşme**
- Riskli hüküm taraması
- Kira sözleşmesi kontrolü
- NDA / hizmet sözleşmesi denetimi
- Redline ve alternatif lafız önerisi

</td></tr>
<tr><td valign="top">

**🔐 KVKK uyum**
- Aydınlatma metni incelemesi
- Açık rıza denetimi
- VERBİS kayıt triyajı
- Kişisel veri maskeleme

</td><td valign="top">

**👷 İş hukuku**
- Fesih triyajı
- İş sözleşmesi incelemesi
- Yıllık izin hesaplayıcı
- Fazla mesai hesaplayıcı

</td></tr>
<tr><td valign="top">

**⚖️ İcra ve idare**
- İcra dosyası triyajı
- Haciz ihbarnamesi süre analizi
- İdari işlem triyajı (İYUK m.7)
- Vergi uyuşmazlığı sınıflandırması

</td><td valign="top">

**📅 Mevzuat takibi**
- Resmî Gazete günlük kontrolü
- Mevzuat değişikliği redline analizi
- Yargıtay karar özeti
- Kurul kararı takibi

</td></tr>
</table>

**Ortak altyapı (tüm eklentilerde):** kaynak hiyerarşisi kuralı, `[DOĞRULANMADI]` etiketleme protokolü, adli tatil ve resmî tatili sayan deterministik süre hesaplayıcı.

---

## 🚀 Kurulum

### Claude Code ile (önerilen)

```bash
claude plugin marketplace add https://github.com/mesutcandemir39/turkiye-legal
```

Ardından ihtiyacınız olan eklentiyi kurun:

```bash
claude plugin install kvkk-veri-koruma@turkiye-legal
```

Kullanım:

```
/kvkk-veri-koruma:aydinlatma-yukumlulugu
```

> **⚠️ Güncellemeler otomatik gelmez.** Claude Code eklentiyi kurduğunuz sürüme sabitler. Güncel kalmak için:
> ```bash
> claude plugin update kvkk-veri-koruma@turkiye-legal
> ```
> Kurulu sürümünüzü kontrol etmek için: `/cekirdek:surum-kontrolu`

Adım adım rehber (terminal deneyimi olmayanlar için): [`docs/KURULUM.md`](docs/KURULUM.md)

### Claude web arayüzü ile

Claude Code kullanmıyorsanız, ilgili `skills/<ad>/SKILL.md` dosyasının içeriğini kopyalayıp Claude Projects'te özel talimat (custom instruction) olarak kullanabilirsiniz.

> ⚠️ Bu yöntemde **otomatik kaynak doğrulama ve süre hesaplayıcı çalışmaz.** Çıktıyı daha dikkatli değerlendirin.

### Geliştiriciler için

```bash
git clone https://github.com/mesutcandemir39/turkiye-legal.git
cd turkiye-legal
pip install -r scripts/requirements.txt
python scripts/validate/validate_skills.py --strict
pytest evaluations/static/ -v
```

Detay: [`CONTRIBUTING.md`](CONTRIBUTING.md)

---

## 📦 Kapsam

### Kurulabilir eklentiler (91)

Her pratik alanı ayrı bir eklentidir; yalnızca ihtiyacınız olanı kurarsınız.

**En çok kullanılanlar:**

| Eklenti | Odak |
|---|---|
| `kvkk-veri-koruma` | Aydınlatma metni, açık rıza, VERBİS (6698) |
| `is-hukuku-bireysel` | Fesih, iş sözleşmesi, kıdem/ihbar (4857) |
| `sozlesme-inceleme-redline` | Riskli hüküm taraması, redline, alternatif lafız |
| `dava-dilekce-atolyesi` | HMK m.119 denetimi, dilekçe kalite skoru (6100) |
| `icra-iflas-hukuku` | İtiraz/şikâyet süreleri, haciz ihbarnamesi (2004) |
| `kira-hukuku` | Kira sözleşmesi, tahliye, depozito (6098) |
| `vergi-davalari` | Vergi uyuşmazlığı, İYUK m.7 dava süresi |
| `ceza-muhakemesi` | Soruşturma/kovuşturma usulü, süreler (5271) |
| `miras-hukuku` | Tereke, tenkis, mirasçılık belgesi (4721) |
| `sirketler-hukuku` | Genel kurul, yönetici sorumluluğu (6102) |

Tam liste: [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json) — 81 pratik alanı eklentisi + 10 altyapı eklentisi.

### Beceri kütüphanesi (923 skill / 81 pratik alanı)

Aile hukukundan enerji hukukuna, sağlık hukukundan yapay zekâ hukukuna kadar
**81 pratik alanında 923 yapılandırılmış beceri**. Her beceri şema doğrulamasından
ve kaynak defteri denetiminden geçer.

> **Dürüstlük notu:** `cekirdek`, `kvkk-uyum`, `is-hukuku`, `sozlesme`, `icra-iflas`,
> `mevzuat-takip`, `dava-takip`, `ticaret-sirketler`, `fikri-mulkiyet` ve `idare-vergi`
> altyapı eklentileri hook, script ve referans sağlar ancak **kendi `skills/` dizinleri
> henüz boştur.** Bu boşluk `M7 — Eklenti Bütünlüğü` milestone'unda takip edilmektedir.
> Beceriler yukarıdaki pratik alanı eklentilerindedir.

### MCP sunucuları (2)

Model, bir kanun maddesine atıf yapmadan önce metni **hafızadan değil resmî
kaynaktan** alır. Her iki sunucu da stdio taşıması kullanır ve Claude Code ile
doğrudan çalışır.

| Sunucu | Araçlar | Kaynak |
|---|---|---|
| `turkiye-legal-mevzuat` | `madde_getir`, `kanun_metni_getir`, `mevzuat_ara`, `bilinen_kanunlar` | mevzuat.gov.tr |
| `turkiye-legal-ictihat` | `ictihat_ara`, `karar_getir` | İçtihat veri tabanları |

Depo Claude Code'da açıldığında [`.mcp.json`](.mcp.json) otomatik devreye girer.
Elle çalıştırmak için:

```bash
uv run --directory mcp/mevzuat turkiye-legal-mevzuat
uv run --directory mcp/ictihat turkiye-legal-ictihat
```

Bağlantı rehberi: [`docs/CONNECTORS.md`](docs/CONNECTORS.md)

---

## 🛡️ Doğruluk nasıl sağlanıyor?

Bu projenin ayırt edici yanı budur.

| Katman | Ne yapar |
|---|---|
| **Kaynak defteri** | `sources/mevzuat/kanunlar.yaml` — doğrulanmış kanun kayıtları. Deftere yazılmamış bir kanuna atıf yapılamaz. |
| **CI doğrulaması** | Her PR'da `validate_skills.py` ve `validate_sources.py` çalışır. Deftere karşılığı olmayan atıf içeren PR **birleştirilemez.** |
| **Statik testler** | `evaluations/static/` — LLM gerektirmez, her PR'da zorunlu geçiş kapısıdır. |
| **Golden testler** | `evaluations/golden/` — gerçek model üzerinde regresyon senaryoları. |
| **`[DOĞRULANMADI]` protokolü** | Kaynağı doğrulanamayan bilgi kesin ifadeyle sunulmaz, açıkça etiketlenir. |
| **Deterministik hesap** | Süre/tatil hesabı dil modeline bırakılmaz — `cekirdek/scripts/sure_hesapla.py` yapar. |

---

## 📌 Sürüm politikası

**v0.1.0, projenin ilk kararlı (Stable) sürümüdür.**

> **Gerçek hukuki işlerinizde daima "Stable / Latest Release" etiketli sürümleri kullanın.**

`main` dalındaki anlık değişiklikleri doğrudan çekmek veya `alpha` / `beta` / `rc` sürümlerini gerçek işlerde kullanmak **halüsinasyon riski** taşır — golden testlerden geçmemiş bir beceri uydurma kanun maddesi üretebilir.

**Destek penceresi:** Her zaman yalnızca en güncel **2 Stable** sürüm desteklenir. Daha eskiler EOL kabul edilir — bkz. [`SECURITY.md`](SECURITY.md).

---

## ⚖️ Hukuki sorumluluk reddi

**`turkiye-legal` bir yardımcı araçtır. Avukat değildir, avukatlık hizmeti vermez.**

- ✅ Ön inceleme, taslak hazırlama ve araştırma için kullanın
- ✅ Her çıktıyı birincil kaynaktan (kanun metni, resmî kurum rehberi) doğrulayın
- ✅ Nihai kararı her zaman yetkin bir hukukçu versin
- ❌ Avukat–müvekkil ilişkisi doğurmaz
- ❌ Hukuki mütalaa veya danışmanlık yerine geçmez
- ❌ Çıktılardan doğan zarardan proje sahibi ve katkıcılar sorumlu tutulamaz

**Özellikle dikkat:** Ceza, emeklilik, vergi ve süreye bağlı işlerde mutlaka uzmana danışın. Süre kaçırmak geri dönüşü olmayan hak kaybı doğurur.

---

## 🤝 Katkı

Hukukçu ve yazılımcı katkısı aynı ölçüde değerlidir. PR şablonundan issue formlarına kadar her şey, hiç terminal kullanmamış bir avukatın da katkı sağlayabileceği şekilde tasarlandı.

- **Nasıl katkı sağlarım?** → [`CONTRIBUTING.md`](CONTRIBUTING.md)
- **Davranış kuralları** → [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)
- **Yönetişim** → [`GOVERNANCE.md`](GOVERNANCE.md)
- **Güvenlik açığı bildirimi** → [`SECURITY.md`](SECURITY.md) (public issue **açmayın**)

---

## 📚 Dokümantasyon

| Belge | İçerik |
|---|---|
| [`QUICKSTART.md`](QUICKSTART.md) | 60 saniyede başlangıç |
| [`docs/KURULUM.md`](docs/KURULUM.md) | Sıfırdan kurulum ve güncelleme |
| [`docs/CONNECTORS.md`](docs/CONNECTORS.md) | MCP sunucu bağlantıları |
| [`docs/TOPLULUK_SKILL_GUVENI.md`](docs/TOPLULUK_SKILL_GUVENI.md) | Topluluk becerilerine güven modeli |
| [`CHANGELOG.md`](CHANGELOG.md) | Sürüm geçmişi |
| [`CREDITS.md`](CREDITS.md) | Künye ve atıf |

---

## 📄 Lisans

Apache License 2.0 — bkz. [`LICENSE`](LICENSE) ve [`NOTICE`](NOTICE).

Bu depoyu fork'larsanız veya türev çalışmada kullanırsanız `NOTICE` dosyasını korumanız Apache-2.0 Madde 4(d) gereği **hukuki zorunluluktur.**

Atıf ve üst çalışma beyanları: [`CREDITS.md`](CREDITS.md)

---

## 📮 İletişim

- **Hata bildirimi:** [GitHub Issues](https://github.com/mesutcandemir39/turkiye-legal/issues)
- **Öneri ve tartışma:** [GitHub Discussions](https://github.com/mesutcandemir39/turkiye-legal/discussions)
- **Telegram:** [@MesutCan](https://t.me/MesutCan)
- **Güvenlik açığı:** [`SECURITY.md`](SECURITY.md) — public issue açmayın

---

<div align="center">

**Türk hukukunu herkes için erişilebilir kılmak üzere geliştirildi.**

Apache-2.0 · Açık kaynak · Bakımcı: [Mesut Can Demir](https://github.com/mesutcandemir39)

</div>
