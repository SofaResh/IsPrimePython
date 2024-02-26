import unittest

from IsPrime import is_prime


class TestCalculator(unittest.TestCase):

    def test_is_prime1(self):
        self.assertEqual(is_prime(11), True)
        self.assertTrue(is_prime(11))

    def test_is_prime2(self):
        self.assertEqual(is_prime(10), False)

    def test_is_prime3(self):
        self.assertEqual(is_prime(7), True)

    def test_is_prime4(self):
        self.assertEqual(is_prime(5), True)

    def test_is_prime5(self):
        self.assertEqual(is_prime(6), False)

    def test_is_prime6(self):
        self.assertEqual(is_prime(12), False)
