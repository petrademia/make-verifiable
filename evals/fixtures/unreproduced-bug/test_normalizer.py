import unittest

from normalizer import normalize_rows


class NormalizerTests(unittest.TestCase):
    def test_skips_empty_rows(self):
        self.assertEqual(normalize_rows([" North ", "", "South"]), ["north", "south"])


if __name__ == "__main__":
    unittest.main()
