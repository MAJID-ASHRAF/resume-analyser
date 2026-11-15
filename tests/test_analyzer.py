import unittest
from unittest.mock import patch

from services.analyze import analyze_resume
from services.skill_extractor import extract_skills


class AnalyzeResumeTests(unittest.TestCase):
    def test_returns_normalized_skills(self):
        with patch(
            "services.analyze.extract_skills",
            return_value=["JS", "Postgres", "ReactJS"],
        ):
            result = analyze_resume(
                "I have worked in software development for four years."
            )

        self.assertEqual(
            result,
            {"skills": ["JavaScript", "PostgreSQL", "React"]},
        )

    def test_rejects_invalid_resume_text(self):
        with self.assertRaises(ValueError):
            analyze_resume("Too short")


class ExtractSkillsTests(unittest.TestCase):
    def test_react_native_does_not_extract_react(self):
        result = extract_skills(
            "I have worked with React Native for four years."
        )

        self.assertIn("React Native", result)
        self.assertNotIn("React", result)

    def test_javascript_does_not_extract_java(self):
        result = extract_skills(
            "I have worked with JavaScript for four years."
        )

        self.assertIn("JavaScript", result)
        self.assertNotIn("Java", result)

    def test_extracts_both_independent_skills(self):
        result = extract_skills(
            "I have worked with React Native and React for four years."
        )

        self.assertIn("React Native", result)
        self.assertIn("React", result)

    def test_react_native_and_react_are_both_extracted_when_separate(self):
        result = extract_skills(
            "I have used React Native, and separately built a React application."
        )
        self.assertEqual(result.count("React Native"), 1)
        self.assertEqual(result.count("React"), 1)


if __name__ == "__main__":
    unittest.main()
