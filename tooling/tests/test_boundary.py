import tempfile
import unittest
from pathlib import Path
from tooling.check_boundary import source_files


class BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / "product").mkdir()
        (self.root / "product/skill.md").write_text("candidate")
        (self.root / "research.md").write_text("internal")

    def test_empty_and_explicit_sources(self):
        self.assertEqual(source_files(self.root, {"files": []}), [])
        self.assertEqual(source_files(self.root, {"files": ["product/skill.md"]}),
                         [self.root / "product/skill.md"])

    def test_rejects_escape_glob_directory_duplicate_and_bad_manifest(self):
        for path in ["research.md", "product/../research.md", "/product/skill.md",
                     "product/*", "product", "product/missing", "product//skill.md",
                     "product/./skill.md", "product\\skill.md"]:
            with self.subTest(path=path), self.assertRaises(ValueError):
                source_files(self.root, {"files": [path]})
        for manifest in [{"files": ["product/skill.md"] * 2}, {"files": "*"},
                         {"files": [], "glob": "**/*"}, {"files": [3]}]:
            with self.subTest(manifest=manifest), self.assertRaises(ValueError):
                source_files(self.root, manifest)

    def test_rejects_symlink_file_directory_and_product_root(self):
        (self.root / "product/link").symlink_to(self.root / "research.md")
        (self.root / "product/dir").symlink_to(self.root, target_is_directory=True)
        for path in ["product/link", "product/dir/research.md"]:
            with self.assertRaises(ValueError):
                source_files(self.root, {"files": [path]})
        (self.root / "alias").mkdir()
        (self.root / "alias/file").write_text("x")
        other = self.root / "other"
        other.mkdir()
        (other / "product").symlink_to(self.root / "alias", target_is_directory=True)
        with self.assertRaises(ValueError):
            source_files(other, {"files": ["product/file"]})
