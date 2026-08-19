import json, tempfile, unittest
from pathlib import Path
from scripts.validate import validate

VALID_SKILL = "---\nname: demo\ndescription: Use when X to do Y.\n---\n# Demo\nSee [rules](references/rules.md).\n"
VALID_TEMPLATE = """<<NAME>> <<EMAIL>> <<PHONE>> <<GITHUB_USERNAME>>
% RESUME-SKILL:BEGIN EDUCATION
% RESUME-SKILL:END EDUCATION
% RESUME-SKILL:BEGIN EXPERIENCE
% RESUME-SKILL:END EXPERIENCE
% RESUME-SKILL:BEGIN SKILLS
% RESUME-SKILL:END SKILLS
"""
VALID_HTML = """<style>@page { size: A4; margin: 0.5in; }</style>
<header></header><main><section><!-- RESUME-SKILL:BEGIN EDUCATION --><!-- RESUME-SKILL:END EDUCATION --></section>
<section><!-- RESUME-SKILL:BEGIN EXPERIENCE --><!-- RESUME-SKILL:END EXPERIENCE --></section>
<section><!-- RESUME-SKILL:BEGIN SKILLS --><!-- RESUME-SKILL:END SKILLS --></section></main>
"""
VALID_MARKDOWN = """# <<NAME>>
<!-- RESUME-SKILL:BEGIN EDUCATION -->
<!-- RESUME-SKILL:END EDUCATION -->
<!-- RESUME-SKILL:BEGIN EXPERIENCE -->
<!-- RESUME-SKILL:END EXPERIENCE -->
<!-- RESUME-SKILL:BEGIN SKILLS -->
<!-- RESUME-SKILL:END SKILLS -->
"""

class ValidateTests(unittest.TestCase):
    def _tree(self, root, files):
        for rel, content in files.items():
            p = root / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")

    def _base(self):
        return {
            ".claude-plugin/plugin.json": json.dumps({"name": "demo", "description": "d"}),
            ".codex-plugin/plugin.json": json.dumps({"name": "demo", "description": "d"}),
            "skills/demo/SKILL.md": VALID_SKILL,
            "skills/demo/references/rules.md": "# rules\n",
            "templates/latex/TEMPLATE_GUIDE.md": "Tokens: <<NAME>> <<EMAIL>> <<PHONE>> <<GITHUB_USERNAME>>\n",
            "templates/latex/resume-cn.tex": VALID_TEMPLATE,
            "templates/latex/resume-na.tex": VALID_TEMPLATE,
            "templates/html/resume.html": VALID_HTML,
            "templates/markdown/resume.md": VALID_MARKDOWN,
            "templates/json/resume.schema.json": "{}\n",
        }

    def _run(self, files):
        d = Path(tempfile.mkdtemp())
        self._tree(d, files)
        return validate(d)

    def test_valid_tree_has_no_errors(self):
        self.assertEqual(self._run(self._base()), [])

    def test_missing_frontmatter_fails(self):
        files = self._base(); files["skills/demo/SKILL.md"] = "# Demo\nno frontmatter\n"
        self.assertTrue(any("frontmatter" in e for e in self._run(files)))

    def test_name_mismatch_fails(self):
        files = self._base(); files["skills/demo/SKILL.md"] = VALID_SKILL.replace("name: demo", "name: other")
        self.assertTrue(any("name 'other'" in e for e in self._run(files)))

    def test_empty_description_fails(self):
        files = self._base(); files["skills/demo/SKILL.md"] = VALID_SKILL.replace("description: Use when X to do Y.", "description:")
        self.assertTrue(any("empty description" in e for e in self._run(files)))

    def test_missing_reference_fails(self):
        files = self._base()
        files["skills/demo/SKILL.md"] = "---\nname: demo\ndescription: d\n---\nSee [x](references/missing.md).\n"
        self.assertTrue(any("references missing file 'references/missing.md'" in e for e in self._run(files)))

    def test_parent_ref_fails(self):
        files = self._base()
        files["skills/demo/SKILL.md"] = "---\nname: demo\ndescription: d\n---\nSee ../other/rules.md\n"
        self.assertTrue(any("../" in e and "self-containment" in e for e in self._run(files)))

    def test_bad_manifest_json_fails(self):
        files = self._base(); files[".claude-plugin/plugin.json"] = "{not json"
        self.assertTrue(any("invalid JSON" in e for e in self._run(files)))

    def test_undocumented_template_var_fails(self):
        files = self._base()
        files["templates/latex/TEMPLATE_GUIDE.md"] = "Tokens: <<NAME>>"
        files["templates/latex/resume-na.tex"] = "<<NAME>> <<SECRET>>"
        self.assertTrue(any("<<SECRET>>" in e and "TEMPLATE_GUIDE" in e for e in self._run(files)))

    def test_missing_built_in_template_fails(self):
        files = self._base()
        del files["templates/latex/resume-na.tex"]
        self.assertTrue(any("resume-na.tex" in e and "missing" in e for e in self._run(files)))

    def test_unpaired_export_region_fails(self):
        files = self._base()
        files["templates/latex/resume-cn.tex"] = VALID_TEMPLATE.replace(
            "% RESUME-SKILL:END EDUCATION\n", ""
        )
        self.assertTrue(any("EDUCATION" in e and "region" in e for e in self._run(files)))

    def test_reversed_export_region_fails(self):
        files = self._base()
        files["templates/latex/resume-cn.tex"] = VALID_TEMPLATE.replace(
            "% RESUME-SKILL:BEGIN EDUCATION\n% RESUME-SKILL:END EDUCATION",
            "% RESUME-SKILL:END EDUCATION\n% RESUME-SKILL:BEGIN EDUCATION",
        )
        self.assertTrue(any("EDUCATION" in e and "order" in e for e in self._run(files)))

    def test_legacy_language_token_fails(self):
        files = self._base()
        files["templates/latex/resume-na.tex"] = VALID_TEMPLATE.replace(
            "<<GITHUB_USERNAME>>", "<<GITHUB_USERNAME>> <<LANGUAGE_SCORE>>"
        )
        self.assertTrue(any("LANGUAGE_SCORE" in e and "token" in e for e in self._run(files)))

    def test_html_without_semantic_print_contract_fails(self):
        files = self._base()
        files["templates/html/resume.html"] = "<h1>Resume</h1>"
        self.assertTrue(any("HTML" in e and "semantic" in e for e in self._run(files)))

    def test_html_without_export_region_fails(self):
        files = self._base()
        files["templates/html/resume.html"] = VALID_HTML.replace(
            "<!-- RESUME-SKILL:END SKILLS -->", ""
        )
        self.assertTrue(any("resume.html" in e and "SKILLS" in e for e in self._run(files)))

    def test_markdown_unsupported_token_fails(self):
        files = self._base()
        files["templates/markdown/resume.md"] = VALID_MARKDOWN.replace(
            "<<NAME>>", "<<NAME>> <<LANGUAGE_SCORE>>"
        )
        self.assertTrue(any("resume.md" in e and "LANGUAGE_SCORE" in e for e in self._run(files)))

if __name__ == "__main__":
    unittest.main()
