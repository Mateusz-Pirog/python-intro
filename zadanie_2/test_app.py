import unittest
from app import is_valid_email, calculate_area, process_list, convert_date_format, is_palindrome


class TestFunctions(unittest.TestCase):
    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertFalse(is_valid_email("invalid-email"))
        self.assertFalse(is_valid_email("@example.com"))

    def test_calculate_area(self):
        self.assertEqual(calculate_area("circle", 3), 28.26)
        self.assertEqual(calculate_area("rectangle", 4, 5), 20)
        self.assertEqual(calculate_area("triangle", 6, 7), 21)
        with self.assertRaises(ValueError):
            calculate_area("hexagon", 3)

    def test_process_list(self):
        self.assertEqual(process_list([3, 1, 2, 3, 1]), [1, 2, 3])
        self.assertEqual(process_list(["b", "a", "b"]), ["a", "b"])

    def test_convert_date_format(self):
        self.assertEqual(convert_date_format("2024-03-23"), "23-03-2024")
        self.assertEqual(convert_date_format("23/03/2024", "%d/%m/%Y", "%Y-%m-%d"), "2024-03-23")
        self.assertEqual(convert_date_format("invalid-date"), "Invalid date format")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Ala ma kota, a kot ma Alę"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))


if __name__ == "__main__":
    unittest.main()
