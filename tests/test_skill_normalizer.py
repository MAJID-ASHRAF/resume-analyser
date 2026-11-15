import unittest

from services.skill_normalizer import normalize_skills


class NormalizeSkillsTests(unittest.TestCase):
    def test_normalizes_aliases_case_insensitively(self):
        skills = ["js", "POSTGRES", "reactjs", "nodejs", "ts"]
        self.assertEqual(
            normalize_skills(skills),
            ["JavaScript", "PostgreSQL", "React", "Node.js", "TypeScript"],
        )

    def test_trims_whitespace_and_normalizes_spacing(self):
        self.assertEqual(
            normalize_skills(["  Python  ", "  Java   Script  "]),
            ["Python", "Java Script"],
        )

    def test_deduplicates_canonical_and_alias_names_in_order(self):
        self.assertEqual(
            normalize_skills(["JS", "JavaScript", "js", "Python", "Python"]),
            ["JavaScript", "Python"],
        )

    def test_preserves_unknown_skills(self):
        self.assertEqual(
            normalize_skills(["Rust", "Go"]),
            ["Rust", "Go"],
        )

    def test_rejects_a_string_instead_of_an_iterable_of_skills(self):
        with self.assertRaises(TypeError):
            normalize_skills("JavaScript")

    def test_rejects_non_string_items(self):
        with self.assertRaises(TypeError):
            normalize_skills(["Python", None])


if __name__ == "__main__":
    unittest.main()
