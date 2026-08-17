---
name: ornek-skill
description: "Bu, yalnızca validator'ları test etmek için kullanılan bir fixture'dır — gerçek bir skill değildir."
argument-hint: "[dosya yolu]"
user-invocable: true
turkiye_legal:
  version: 0.0.1
  category: test
  jurisdiction:
    country: TR
    legal_system: civil_law
    scope: [TR]
  risk_level: high
  requires_human_review: true
  inputs:
    - "Test girdisi"
  outputs:
    - "Test çıktısı"
  sources:
    - tur: kanun
      numara: "6698"
      ad: "Kişisel Verilerin Korunması Kanunu"
      madde: "10"
  attribution:
    original_author: "Mesut Can Demir"
    original_repository: "https://github.com/mesutcandemir39/turkiye-legal"
    license: "Apache-2.0"
---

# Örnek Skill (Fixture)

Bu dosya bir test fixture'ıdır; `evaluations/static/test_validators.py` tarafından validator'ların **geçerli** bir SKILL.md'yi doğru şekilde kabul ettiğini doğrulamak için kullanılır.

Örnek karar numarası gösterirken placeholder kullanılır: E. ____/____, K. ____/____.
