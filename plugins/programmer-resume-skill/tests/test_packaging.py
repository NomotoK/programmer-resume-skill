import json
import unittest
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parent.parent
REPOSITORY_ROOT = PLUGIN_ROOT.parent.parent


class PackagingTests(unittest.TestCase):
    def test_codex_marketplace_contract(self):
        marketplace = json.loads(
            (REPOSITORY_ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8")
        )
        self.assertEqual(marketplace["name"], "programmer-resume")
        self.assertEqual(marketplace["interface"]["displayName"], "Programmer Resume")
        self.assertEqual(
            marketplace["plugins"],
            [
                {
                    "name": "programmer-resume-skill",
                    "source": {"source": "local", "path": "./plugins/programmer-resume-skill"},
                    "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                    "category": "Developer Tools",
                }
            ],
        )

    def test_opencode_uses_the_packaged_skills_as_a_project_source(self):
        config = json.loads((REPOSITORY_ROOT / "opencode.json").read_text(encoding="utf-8"))
        self.assertEqual(config["$schema"], "https://opencode.ai/config.json")
        self.assertEqual(config["skills"], {"paths": ["./plugins/programmer-resume-skill/skills"]})

    def test_codex_manifest_exposes_the_packaged_skills(self):
        manifest = json.loads(
            (PLUGIN_ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8")
        )
        self.assertEqual(manifest["name"], "programmer-resume-skill")
        self.assertEqual(manifest["version"], "0.2.0")
        self.assertEqual(manifest["author"]["name"], "NomotoK")
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertEqual(manifest["interface"]["capabilities"], ["Interactive", "Write"])
        self.assertEqual(len(manifest["interface"]["defaultPrompt"]), 3)
        self.assertNotIn("apps", manifest)
        self.assertNotIn("hooks", manifest)
        self.assertNotIn("mcpServers", manifest)

    def test_plugin_package_contains_export_and_research_resources(self):
        required = (
            "skills/resume-optimizer/SKILL.md",
            "templates/latex/resume-cn.tex",
            "templates/latex/resume-na.tex",
            "templates/html/resume.html",
            "templates/markdown/resume.md",
            "templates/json/resume.schema.json",
            "scripts/validate.py",
            "scripts/render_smoke.py",
            "examples/README.md",
            "docs/research/2026-07-02-cn-resume-norms.md",
        )
        for relative_path in required:
            self.assertTrue((PLUGIN_ROOT / relative_path).is_file(), relative_path)


if __name__ == "__main__":
    unittest.main()
