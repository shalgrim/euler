from unittest import TestCase
from project_euler.primes.PrimeChecker import PrimeChecker

__author__ = 'Scott'

class TestPrimeChecker(TestCase):
    def test_is_prime_lo_to_hi(self):
        pc = PrimeChecker()
        self.assertTrue(pc.is_prime(2))
        self.assertTrue(pc.is_prime(3))
        self.assertFalse(pc.is_prime(4))
        self.assertTrue(pc.is_prime(5))
        self.assertFalse(pc.is_prime(6))
        self.assertTrue(pc.is_prime(7))
        self.assertFalse(pc.is_prime(8))
        self.assertFalse(pc.is_prime(9))
        self.assertFalse(pc.is_prime(10))
        self.assertTrue(pc.is_prime(11))
        self.assertFalse(pc.is_prime(12))
        self.assertTrue(pc.is_prime(13))
        self.assertFalse(pc.is_prime(14))
        self.assertFalse(pc.is_prime(15))
        self.assertFalse(pc.is_prime(16))
        self.assertTrue(pc.is_prime(17))
        self.assertFalse(pc.is_prime(18))
        self.assertTrue(pc.is_prime(19))
        self.assertFalse(pc.is_prime(20))
        self.assertFalse(pc.is_prime(21))
        self.assertFalse(pc.is_prime(22))
        self.assertTrue(pc.is_prime(23))
        return

    def test_is_prime_hi_to_lo(self):
        pc = PrimeChecker()
        self.assertFalse(pc.is_prime(100))
        self.assertTrue(pc.is_prime(29))
        self.assertTrue(pc.is_prime(23))
        self.assertFalse(pc.is_prime(22))
        self.assertFalse(pc.is_prime(21))
        self.assertFalse(pc.is_prime(20))
        self.assertTrue(pc.is_prime(19))
        self.assertFalse(pc.is_prime(18))
        self.assertTrue(pc.is_prime(17))
        self.assertFalse(pc.is_prime(16))
        self.assertFalse(pc.is_prime(15))
        self.assertFalse(pc.is_prime(14))
        self.assertTrue(pc.is_prime(13))
        self.assertFalse(pc.is_prime(12))
        self.assertTrue(pc.is_prime(11))
        self.assertFalse(pc.is_prime(10))
        self.assertFalse(pc.is_prime(9))
        self.assertFalse(pc.is_prime(8))
        self.assertTrue(pc.is_prime(7))
        self.assertFalse(pc.is_prime(6))
        self.assertTrue(pc.is_prime(5))
        self.assertFalse(pc.is_prime(4))
        self.assertTrue(pc.is_prime(3))
        self.assertTrue(pc.is_prime(2))

        return

    def test_is_truncatable_prime(self):
        pc = PrimeChecker()
        self.assertTrue(pc.is_truncatable_prime(3797))
        return
