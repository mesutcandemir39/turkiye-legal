# mevzuat-takip

**Kademe:** Tier A · **Dayanak:** genel mevzuat takibi (sabit bir kanuna bağlı değil)

## İçerik

| Tür | Ad | Ne yapar |
|---|---|---|
| Skill | `mevzuat-degisiklik-analizi` | Bir mevzuatın eski/yeni halini karşılaştırıp redline (değişiklik) özeti çıkarır |
| Skill | `yargitay-karar-ozeti` | Kullanıcının verdiği bir karar metnini özetler — **karar metni verilmeden asla çağrılmaz**, karar numarası üretmez |
| Skill | `kurul-karari-takibi` | Kullanıcının verdiği bir KVKK Kurulu veya Rekabet Kurulu kararını özetler — **karar metni verilmeden asla çağrılmaz**, karar üretmez |
| Agent | `resmi-gazete-gunluk` | Resmî Gazete günlük takip rutini — `NOT_IMPLEMENTED`, henüz bir kaynağa bağlı değil (Layer 5, ROADMAP Q3) |

## Kurulum

```bash
claude plugin install mevzuat-takip@turkiye-legal
```

## Kullanım

```
/mevzuat-takip:mevzuat-degisiklik-analizi [eski metin] [yeni metin]
/mevzuat-takip:yargitay-karar-ozeti [karar metni]
/mevzuat-takip:kurul-karari-takibi [kurul kararı metni]
```

`yargitay-karar-ozeti`, projenin en kritik halüsinasyon savunma noktalarından biridir.ADR-005.
