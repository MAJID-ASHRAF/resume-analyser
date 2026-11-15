import unittest

from validators.input_validator import validate_text


class ValidateTextTests(unittest.TestCase):
    def test_rejects_non_string_values(self):
        for value in (None, 123):
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError, "resume must be a string"):
                    validate_text(value, "resume")

    def test_rejects_empty_or_whitespace_only_strings(self):
        for value in ("", "       "):
            with self.subTest(value=repr(value)):
                with self.assertRaisesRegex(ValueError, "resume cannot be empty"):
                    validate_text(value, "resume")

    def test_rejects_strings_shorter_than_20_characters(self):
        with self.assertRaisesRegex(ValueError, "at least 20 characters"):
            validate_text("Hello", "resume")

    def test_accepts_valid_resume_text(self):
        value = "I am a Python developer with four years of experience."
        self.assertEqual(validate_text(value, "resume"), value)

    def test_strips_whitespace_and_accepts_exactly_20_characters(self):
        value = "  12345678901234567890  "
        self.assertEqual(validate_text(value, "resume"), "12345678901234567890")

    def test_rejects_boolean_values(self):
        with self.assertRaises(TypeError):
            validate_text(True, "resume")

    def test_rejects_float_values(self):
        with self.assertRaises(TypeError):
            validate_text(12.5, "resume")    


if __name__ == "__main__":
    unittest.main()