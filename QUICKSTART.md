# Hızlı Başlangıç (60 saniye)

Bu sayfa, `turkiye-legal`'i en hızlı şekilde kurup ilk skill'i çalıştırmanız için yazıldı. Tam referans için [`README.md`](README.md), adım adım rehber için [`docs/KURULUM.md`](docs/KURULUM.md).

## Hangi araç sizde var: Claude Code mu, Claude Cowork mu?

- **Terminalde bir `claude` komut satırı görüyorsanız** → Claude Code kullanıyorsunuz, aşağıdaki "Claude Code" adımlarını izleyin.
- **Bir masaüstü uygulaması açıyorsanız (terminal yok)** → Claude Cowork kullanıyorsunuz, "Cowork" adımlarını izleyin.

Emin değilseniz: Claude Code kullandığınızı varsayın, en yaygın kurulum budur.

## Claude Code ile (3 adım)

```bash
claude plugin marketplace add https://github.com/mesutcandemir39/turkiye-legal
claude plugin install kvkk-uyum@turkiye-legal
```

```
/kvkk-uyum:aydinlatma-review [aydınlatma metniniz]
```

## Claude Cowork ile (3 adım)

1. **Customize** → **Browse plugins** açın.
2. Marketplace URL'si olarak `https://github.com/mesutcandemir39/turkiye-legal` girin.
3. `kvkk-uyum` (veya ihtiyacınız olan başka bir plugin) kurun, ardından aynı `/kvkk-uyum:aydinlatma-review` komutunu kullanın.

## Hangi plugin bana lazım?

| İhtiyacınız | Plugin |
|---|---|
| KVKK / veri koruma | `kvkk-uyum` |
| İş hukuku (fesih, sözleşme, izin, mesai) | `is-hukuku` |
| Sözleşme incelemesi | `sozlesme` |
| İcra takibi | `icra-iflas` |
| Mevzuat/karar takibi | `mevzuat-takip` |
| Dava dilekçesi/dosyası | `dava-takip` |
| Şirket/genel kurul | `ticaret-sirketler` |
| Fikri mülkiyet/OSS lisans | `fikri-mulkiyet` |
| İdari işlem/vergi | `idare-vergi` |

Tam liste ve her plugin'in kapsamı için [README.md — Plugin haritası](README.md#-mimari-katmanlar).

## Önemli

- Her skill çıktısı bir **taslaktır** — nihai değerlendirme her zaman bir avukata aittir.
- Güncellemeler otomatik gelmez: `claude plugin update <plugin-adı>@turkiye-legal` veya `/cekirdek:surum-kontrolu` ile kontrol edin.
- Gerçek hukuki işlerinizde daima **"Stable / Latest Release"** etiketli sürümü kullanın.

Sorun mu yaşıyorsunuz? [Issues](https://github.com/mesutcandemir39/turkiye-legal/issues/new/choose) üzerinden bildirin.
