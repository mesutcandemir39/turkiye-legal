---
name: ornek-skill
description: "Bu, yalnızca validator'ları test etmek için kullanılan bir fixture'dır — kasıtlı olarak HATALIDIR."
user-invocable: true
turkiye_legal:
  version: 0.0.1
  category: test
  jurisdiction:
    country: TR
    legal_system: civil_law
    scope: [TR]
  risk_level: critical
  requires_human_review: false
  inputs:
    - "Test girdisi"
  outputs:
    - "Test çıktısı"
  sources:
    - tur: kanun
      numara: "99999"
      ad: "Var Olmayan Uydurma Kanun"
  attribution:
    original_author: "Mesut Can Demir"
    original_repository: "https://github.com/mesutcandemir39/turkiye-legal"
    license: "Apache-2.0"
---

# Örnek Hatalı Skill (Fixture)

Bu dosya kasıtlı olarak üç ayrı hata içerir ve `evaluations/static/test_validators.py` tarafından validator'ların bunları YAKALADIĞINI doğrulamak için kullanılır:

1. `risk_level: critical` iken `requires_human_review: false` — ADR-005 ihlali.
2. `numara: "99999"` — `sources/mevzuat/kanunlar.yaml` defterinde olmayan uydurma bir kanun numarası.
3. Aşağıda gerçekçi görünen bir karar numarası: E. 2021/4521, K. 2022/887 — bu `lint_prompts.py` tarafından yakalanmalıdır.
