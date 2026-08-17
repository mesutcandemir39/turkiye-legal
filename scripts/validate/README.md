# scripts/validate/

Bu dizindeki her script, `turkiye-legal`'in halüsinasyon savunmasının bir katmanıdır. Hepsi LLM gerektirmez, hepsi CI'da her PR'da çalışır.

| Script | Ne yapar | Çıkış kodu |
|---|---|---|
| `validate_skills.py` | `SKILL.md` frontmatter'ını `schema/skill.schema.json`'a karşı doğrular; `risk_level ≥ high ⇒ requires_human_review: true` kuralını zorunlu kılar | 0=geçti, 1=hata |
| `validate_sources.py` | Her skill'in kanun atıflarını `sources/mevzuat/kanunlar.yaml` defterine karşı doğrular — uydurma kanun numarası burada yakalanır | 0=geçti, 1=hata |
| `lint_prompts.py` | Gerçekçi görünen sahte karar numarası deseni ve bağlamsız yabancı hukuk terimi (GDPR vb.) taraması yapar | 0=geçti, 1=hata |
| `lint_tool_scope.py` | Plugin `hooks/hooks.json` dosyalarındaki riskli shell komut desenlerini denetler | 0=geçti, 1=hata |
| `ai_review.py` | Yukarıdaki üç script'in çıktısından rubrik tabanlı bir PR değerlendirmesi üretir. **v0.1.0'de `simulated: true`** — bkz. [`docs/ai_review_rubric.md`](../../docs/ai_review_rubric.md) | her zaman 0 (sonuç JSON'a yazılır) |

Tüm script'ler `--files-from <dosya-listesi>` bayrağını destekler (satır satır dosya yolu içeren bir dosya) — bu, CI'ın yalnızca değişen dosyaları taramasını sağlar. Bayraksız çalıştırıldığında tüm repo taranır.

**Önemli:** `REPO_ROOT`, her script'te `__file__` konumundan sabit hesaplanır, `cwd`'den DEĞİL. Bir script'i farklı bir dizinden çalıştırmak tarama alanını etkilemez — bu davranış test fixture'larını izole etmek için kasıtlıdır (bkz. `evaluations/static/test_validators.py`).
