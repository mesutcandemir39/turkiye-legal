# Güvenlik Politikası

Bu belge, Turkish Legal projesinde güvenlik zafiyetlerini nasıl bildireceğinizi açıklar.

## 🔐 Güvenlik İlkeleri

Turkish Legal hukuki karar almada kullanıldığından, güvenlik kritiktir:

1. **Prompt Injection Savunması**: MCP'ler ve skill'ler, kullanıcı girdisini doğrulayan parametrelendirilmiş sorgular kullanır
2. **Hallucination Savunması**: Sahte kanun/karar üretme imkânı yoktur (doğrulama CI'da zorunlu)
3. **Veri Gizliliği**: Hiçbir kişisel veri veya dava dosyası lokal olarak tutulmaz; MCP'ler read-only erişim sağlar
4. **Lisans Uyumluluğu**: Bağımlılıklar GPL gibi restrictive lisanslarla karşılamaz

## 🚨 Zafiyetleri Bildirin

### Gizli Bildirimi Tercih Edin

Eğer kamu olmayan bir güvenlik sorunu buldunuz, lütfen şu adrese yazın:

**Email**: `security@turkiye-legal.dev` (planlı — şimdilik issues'da açın)

## 📋 Bildirim Maliyesi

Zafiyeti bildirirken:

1. **Etkilenen sürüm**: (örn. v0.5.0)
2. **Tür**: (prompt injection, hallucination, veri sızıntısı, vb.)
3. **Adımlar**: Sorunu yeniden üretmek için minimum adımlar
4. **Etkisi**: Teorik etkiyi ve pratik riski açıklayın
5. **Öneriniz**: Varsa düzeltme tavsiyesi

## ✅ Yapılanlar

### Statik Analiz

Tüm PR'lar için:
- `validate_skills.py --strict` (frontmatter kontrolü)
- `validate_sources.py` (hallucination kontrol)
- `lint_prompts.py` (prompt injection taraması)

### Bağımlılık Taraması

```bash
pip audit  # Her release öncesi
```

### Entegrasyon Testleri

```bash
pytest evaluations/static/  # Unit tests
python3 evaluations/golden/*.py  # Golden scenarios
```

## 📜 Desteklenen Sürümler

| Sürüm | Destek | EOL |
|-------|--------|-----|
| v0.5.0 | ✅ LTS | 2027-08-17 |
| v0.4.0 | ✅ Active | 2026-12-31 |
| < v0.4.0 | ❌ EOL | — |

## 🔍 Bilinen Sorunlar

### v0.5.0

- ❓ upstream veri sorunu: 11 skill'de "1" referansı (TMK m.1) — Faz 4'te temizlenecek
- ✅ Durum: Düzeltilmiş

## 📞 İletişim

- **Güvenlik**: `security@github.com` → Mesut Can Demir
- **GitHub Security Advisory**: [Link](https://github.com/mesutcandemir39/turkiye-legal/security/advisories)
- **Discussions**: [Gizli kategorı](https://github.com/mesutcandemir39/turkiye-legal/discussions) (yok ama talep edebilirsiniz)

---

Güvenlik araştırması için teşekkürler! 🙏
