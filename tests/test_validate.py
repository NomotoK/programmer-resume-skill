import json, tempfile, unittest
from pathlib import Path
from scripts.validate import validate

VALID_SKILL = "---\nname: demo\ndescription: Use when X to do Y.\n---\n# Demo\nSee [rules](references/rules.md).\n"

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

if __name__ == "__main__":
    unittest.main()
