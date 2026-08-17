# scripts/generate/

Bu script'ler, tek bir kaynaktan (plugin manifest'leri, SKILL.md frontmatter'ları) türetilen dosyaları üretir. Amaç, aynı bilginin iki yerde elle senkron tutulmasını önlemektir (bkz. `ADR-004`'ün "tek doğruluk kaynağı" ilkesi).

| Script | Girdi | Çıktı | `--check` modu |
|---|---|---|---|
| `generate_marketplace.py` | Her `*/. claude-plugin/plugin.json` | Kök `.claude-plugin/marketplace.json` | Mevcut dosyanın güncel olup olmadığını doğrular, CI'da kullanılır |
| `generate_index.py` | Her `*/skills/*/SKILL.md` frontmatter'ı | Kök `index.json` (insan/araç tüketimi için katalog) | Aynı |

**Kural:** Bir geliştirici bir `plugin.json` veya `SKILL.md`'yi değiştirdiğinde, ilgili generator'ı çalıştırıp çıktı dosyasını commit'e dahil etmesi gerekir. `--check` modu bunu unutursa CI'da yakalar (`ci.yml`'deki "marketplace.json ↔ plugin.json tutarlılığı" adımı).

```bash
python scripts/generate/generate_marketplace.py
python scripts/generate/generate_index.py
```
