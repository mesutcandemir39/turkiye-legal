"""evaluations/golden/*.yaml dosyalarindan dinamik olarak pytest testleri uretir.

Her .yaml dosyasi bir test_id tasir ve su akisi izler:
1. skill_path fixture'da belirtilen SKILL.md gercekten var mi? Yoksa SKIPPED
   (NOT_IMPLEMENTED — skill henuz yazilmadi, Faz 4 bekleniyor).
2. ANTHROPIC_API_KEY tanimli mi? Degilse SKIPPED (bkz. conftest.py, ADR-007).
3. Ikisi de varsa: SKILL.md'nin govdesini sistem promptu olarak kullanip
   girdi senaryosunu modele gonder, must_include/must_not_include kontrol et.

CI'da bu dosya `pytest evaluations/golden/ -v -m llm` ile, yalniz nightly/
etiket tetikli golden-eval.yml workflow'unda calisir — normal PR CI'inde
(ci.yml) DEGIL, cunku API cagrisi maliyetli ve yavastir.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
GOLDEN_DIR = Path(__file__).resolve().parent
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def _load_golden_cases() -> list[dict]:
    cases = []
    for yaml_path in sorted(GOLDEN_DIR.glob("*.yaml")):
        data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
        data["_yaml_path"] = str(yaml_path.relative_to(REPO_ROOT))
        cases.append(data)
    return cases


GOLDEN_CASES = _load_golden_cases()


@pytest.mark.llm
@pytest.mark.parametrize("case", GOLDEN_CASES, ids=[c["test_id"] for c in GOLDEN_CASES])
def test_golden_scenario(case: dict, anthropic_client):
    skill_path = REPO_ROOT / case["skill_path"]
    if not skill_path.exists():
        pytest.skip(
            f"NOT_IMPLEMENTED: {case['skill_path']} henuz yazilmadi "
            f"(golden senaryo Faz 4'u bekliyor: {case['_yaml_path']})"
        )

    text = skill_path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    system_prompt = m.group(2).strip() if m else text

    input_file = case.get("input_file")
    if input_file:
        input_path = REPO_ROOT / input_file
        if not input_path.exists():
            pytest.skip(f"NOT_IMPLEMENTED: girdi dosyasi eksik: {input_file}")
        user_content = input_path.read_text(encoding="utf-8")
    else:
        user_content = case.get("input_scenario", "")

    response = anthropic_client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_content}],
    )
    output_text = "".join(
        block.text for block in response.content if getattr(block, "type", None) == "text"
    )

    missing = [term for term in case.get("must_include", []) if term.lower() not in output_text.lower()]
    leaked = [term for term in case.get("must_not_include", []) if term.lower() in output_text.lower()]

    assert not missing, f"[{case['test_id']}] Beklenen ifadeler ciktida yok: {missing}\n--- Cikti ---\n{output_text}"
    assert not leaked, f"[{case['test_id']}] Yasakli ifadeler ciktida VAR: {leaked}\n--- Cikti ---\n{output_text}"


def test_golden_cases_discovered():
    """En az bir golden senaryo dosyasinin gercekten okundugunu dogrular —
    yaml parse hatasi sessizce yutulup 0 test toplanmasin diye."""
    assert len(GOLDEN_CASES) >= 1, f"{GOLDEN_DIR} altinda hic .yaml bulunamadi"
    for case in GOLDEN_CASES:
        assert "test_id" in case, f"{case.get('_yaml_path')}: test_id eksik"
        assert "must_include" in case, f"{case['test_id']}: must_include eksik"
