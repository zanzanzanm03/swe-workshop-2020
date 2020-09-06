import unittest
from app.utility.validator import validate_name, validate_id, validate_phone_number


class TestUtility(unittest.TestCase):
    def test_validate_name_with_valid_input(self):
        self.assertEqual(True, validate_name("por"))

    def test_validate_name_with_valid_input_string_of_int(self):
        self.assertEqual(False, validate_name("007"))

    def test_validate_name_with_valid_input_string_of_int(self):
        self.assertEqual(False, validate_name("ชายปอzaa007"))

    def test_validate_name_with_valid_input_string_of_specail_characters(self):
        self.assertEqual(False, validate_name("!!"))

    def test_validate_name_with_valid_input_string_of_specail_characters2(self):
        self.assertEqual(False, validate_name("$อะไร!!เนี่ย$"))

    def test_validate_name_with_valid_empty_input(self):
        self.assertEqual(False, validate_name(""))

    def test_validate_name_with_valid_spacber_input(self):
        self.assertEqual(False, validate_name("ปอ ซ่า"))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
