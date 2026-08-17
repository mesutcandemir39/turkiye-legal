"""evaluations/golden/ icin ortak fixture'lar.

Bu paketteki testler @pytest.mark.llm ile isaretlenir ve gercek bir
ANTHROPIC_API_KEY gerektirir. Anahtar yoksa test SKIPPED olur — bu, CI'in
statik katmani (evaluations/static/) ile LLM katmanini ayiran ADR-007'nin
dogrudan uygulamasidir. `pytest evaluations/golden/ -v` calistirinca anahtar
yoksa hepsi SKIPPED gorunur; asla sessizce PASS denmez.
"""
from __future__ import annotations

import os

import pytest


def anthropic_key_present() -> bool:
    return bool(os.environ.get("ANTHROPIC_API_KEY"))


@pytest.fixture(scope="session")
def anthropic_client():
    if not anthropic_key_present():
        pytest.skip("ANTHROPIC_API_KEY tanimli degil — golden test SKIPPED (bkz. ADR-007)")
    try:
        import anthropic
    except ImportError:
        pytest.skip("`anthropic` paketi kurulu degil — `pip install -r scripts/requirements.txt`")
    return anthropic.Anthropic()
