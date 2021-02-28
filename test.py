import unittest
from algorithm_test_challenge1 import compress


class TestAlgorithm(unittest.TestCase):

    def setUp(self):
        self.test_str1 = "bbcceeee"
        self.test_str2 = "aaabbbcccaaa"
        self.test_str3 = "a"

    def test_str(self):
        self.assertEqual(compress(self.test_str1), "b2c2e4")
        self.assertEqual(compress(self.test_str2), "a3b3c3a3")
        self.assertEqual(compress(self.test_str3), "a")


if __name__ == "__main__":
    unittest.main()
