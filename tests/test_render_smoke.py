import json
import tempfile
import unittest
from pathlib import Path

from scripts.render_smoke import compile_tex, escape_latex, find_xelatex, render_fixture


ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "tests" / "fixtures"


class RenderSmokeTests(unittest.TestCase):
    def _fixture(self, name):
        return json.loads((FIXTURES / name).read_text(encoding="utf-8"))

    def test_cn_fixture_renders_bachelor_only_non_cs_education(self):
        rendered = render_fixture(
            ROOT / "templates/latex/resume-cn.tex", self._fixture("minimal-cn.json"), "CN"
        )
        self.assertIn("北京外国语大学", rendered)
        self.assertIn("文学学士 in 英语", rendered)
        self.assertIn("翻译理论", rendered)
        self.assertNotIn("<<SCHOOL_BACHELOR>>", rendered)
        self.assertNotIn("计算机科学 工学硕士", rendered)

    def test_na_fixture_omits_language_score_and_uses_category(self):
        rendered = render_fixture(
            ROOT / "templates/latex/resume-na.tex", self._fixture("minimal-na.json"), "NA"
        )
        self.assertIn("Languages:", rendered)
        self.assertNotIn("CET", rendered)
        self.assertNotIn("LANGUAGE_SCORE", rendered)
        self.assertNotIn("Proficient", rendered)

    def test_escape_latex_handles_resume_special_characters(self):
        self.assertEqual(
            escape_latex("C# & 95% at foo_bar"), "C\\# \\& 95\\% at foo\\_bar"
        )

    @unittest.skipIf(find_xelatex() is None, "XeLaTeX is not installed")
    def test_cn_fixture_compiles_with_bundled_fandol_fontset(self):
        with tempfile.TemporaryDirectory() as directory:
            tex_path = Path(directory) / "resume-cn.tex"
            tex_path.write_text(
                render_fixture(
                    ROOT / "templates/latex/resume-cn.tex", self._fixture("minimal-cn.json"), "CN"
                ),
                encoding="utf-8",
            )
            compile_tex(tex_path)
            self.assertTrue(tex_path.with_suffix(".pdf").is_file())


if __name__ == "__main__":
    unittest.main()
