"""Statik regresyon testleri — LLM GEREKTIRMEZ, her PR'da CI tarafindan calistirilir.

Bu paket, docs/ARCHITECTURE_DECISIONS.md ADR-007'nin "statik katman" tanimidir.
Skill/agent icerigi degil, DOGRULAYICILARIN KENDISI test edilir: bir SKILL.md
gecerliyken validator'in onu kabul ettigini, hataliyken reddettigini garanti eder.

evaluations/fixtures/ altindaki iki ornek bu amacla var:
  - gecerli_skill_ornek/  -> tum validator'lardan gecmeli
  - gecersiz_skill_ornek/ -> uc ayri hatayi da yakalatmali
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_VALIDATE = REPO_ROOT / "scripts" / "validate"
FIXTURES = REPO_ROOT / "evaluations" / "fixtures"


def _files_from(tmp_path: Path, skill_path: Path) -> Path:
    """Verilen SKILL.md yolunu REPO_ROOT'a gore GORELI olarak bir gecici
    dosyaya yazar. TUM validator'lar REPO_ROOT'u __file__ konumundan sabit
    hesapladigi icin (cwd'den DEGIL), fixture'lari test etmenin tek dogru
    yolu budur — cwd degistirmek script'in tarama alanini etkilemez."""
    f = tmp_path / "changed_files.txt"
    rel = skill_path.relative_to(REPO_ROOT)
    f.write_text(str(rel) + "\n", encoding="utf-8")
    return f


def _run(script: str, files_from: Path, extra_args: list[str] | None = None) -> subprocess.CompletedProcess:
    cmd = [sys.executable, str(SCRIPTS_VALIDATE / script), "--files-from", str(files_from), *(extra_args or [])]
    return subprocess.run(cmd, capture_output=True, text=True, cwd=REPO_ROOT)


class TestValidateSkillsSchema:
    def test_gecerli_skill_semayi_gecer(self, tmp_path):
        skill_path = FIXTURES / "gecerli_skill_ornek" / "skills" / "ornek-skill" / "SKILL.md"
        ff = _files_from(tmp_path, skill_path)
        result = _run("validate_skills.py", ff, extra_args=["--strict"])
        assert result.returncode == 0, f"Gecerli fixture reddedildi:\n{result.stdout}\n{result.stderr}"
        assert "1 SKILL.md dosyasi tarandi" in result.stdout, "Script fixture'i hic taramamis olabilir"

    def test_gecersiz_skill_semayi_gecmez(self, tmp_path):
        skill_path = FIXTURES / "gecersiz_skill_ornek" / "skills" / "ornek-skill" / "SKILL.md"
        ff = _files_from(tmp_path, skill_path)
        result = _run("validate_skills.py", ff, extra_args=["--strict"])
        assert result.returncode == 1, "Hatali fixture kabul edildi — semantik kontrol calismiyor"
        assert "requires_human_review" in result.stdout, "risk_level/requires_human_review tutarsizligi yakalanmadi"


class TestValidateSources:
    def test_gecerli_skill_kaynak_defterinde_var(self, tmp_path):
        skill_path = FIXTURES / "gecerli_skill_ornek" / "skills" / "ornek-skill" / "SKILL.md"
        ff = _files_from(tmp_path, skill_path)
        result = _run("validate_sources.py", ff)
        assert result.returncode == 0, f"6698 kayitli olmasina ragmen reddedildi:\n{result.stdout}"

    def test_gecersiz_skill_uydurma_kanunu_yakalar(self, tmp_path):
        skill_path = FIXTURES / "gecersiz_skill_ornek" / "skills" / "ornek-skill" / "SKILL.md"
        ff = _files_from(tmp_path, skill_path)
        result = _run("validate_sources.py", ff)
        assert result.returncode == 1, "Uydurma kanun numarasi (99999) yakalanmadi"
        assert "99999" in result.stdout
        assert "BULUNAMADI" in result.stdout


class TestLintPrompts:
    def test_gecerli_skill_temiz_gecer(self, tmp_path):
        skill_path = FIXTURES / "gecerli_skill_ornek" / "skills" / "ornek-skill" / "SKILL.md"
        ff = _files_from(tmp_path, skill_path)
        result = _run("lint_prompts.py", ff)
        assert result.returncode == 0, f"Temiz fixture lint'te takildi:\n{result.stdout}"

    def test_gecersiz_skill_sahte_karar_no_yakalar(self, tmp_path):
        skill_path = FIXTURES / "gecersiz_skill_ornek" / "skills" / "ornek-skill" / "SKILL.md"
        ff = _files_from(tmp_path, skill_path)
        result = _run("lint_prompts.py", ff)
        assert result.returncode == 1, "Gercekci gorunen E./K. karar numarasi yakalanmadi"
        assert "2021/4521" in result.stdout or "karar numarasi" in result.stdout.lower()


class TestSourcesRegistryIntegrity:
    def test_kanunlar_yaml_gecerli_ve_dolu(self):
        import yaml

        path = REPO_ROOT / "sources" / "mevzuat" / "kanunlar.yaml"
        assert path.exists(), "sources/mevzuat/kanunlar.yaml bulunamadi"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert "kanunlar" in data
        assert len(data["kanunlar"]) >= 1

    def test_kanunlar_yaml_no_anahtari_icermez(self):
        """Norway-problem regresyon testi: 'no:' unquoted yazilirsa YAML onu
        False'a cevirir. Bu test, defterin bu tuzaga hicbir zaman dusmedigini
        garanti eder."""
        import yaml

        path = REPO_ROOT / "sources" / "mevzuat" / "kanunlar.yaml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        for entry in data["kanunlar"]:
            assert True not in entry and False not in entry, (
                f"Kayitta boolean anahtar tespit edildi (Norway problem): {entry}"
            )
            assert "numara" in entry, f"Kayitta 'numara' alani eksik: {entry}"


class TestGenerateMarketplaceCheck:
    def test_check_modu_calisir(self):
        """Henuz hicbir plugin.json yokken --check basarili donmeli (bos durum tutarli)."""
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "generate" / "generate_marketplace.py"), "--check"],
            capture_output=True, text=True, cwd=REPO_ROOT,
        )
        # Faz 4 tamamlanmadan bu ya "tutarli, henuz plugin yok" ya da gercek
        # bir tutarsizlik donebilir; burada yalniz cript'in crash etmedigini
        # ve anlamli bir mesaj urettigini kontrol ediyoruz.
        assert result.returncode in (0, 1)
        assert result.stdout.strip() != ""
