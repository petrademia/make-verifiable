import unittest

from policy import retention_days


class RetentionTests(unittest.TestCase):
    def test_retention_period(self):
        self.assertEqual(retention_days(), 60)


if __name__ == "__main__":
    unittest.main()
