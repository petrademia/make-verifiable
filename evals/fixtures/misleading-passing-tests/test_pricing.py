import unittest

from pricing import final_price


class PricingTests(unittest.TestCase):
    def test_regular_customer_pays_full_price(self):
        self.assertEqual(final_price(100, premium=False), 100)


if __name__ == "__main__":
    unittest.main()
