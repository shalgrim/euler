from unittest import TestCase

__author__ = 'Scott'

from prime_factorizer import PrimeFactorizer

class TestPrimeFactorizer(TestCase):

    def test_factor_2(self):
        n = 2
        system = PrimeFactorizer.factor(n)
        gold = [2]
        self.assertListEqual(system, gold, 'prime factorization of {} should '
                                           'be {}'.format(n, gold))

    def test_factor_3(self):
        n = 3
        system = PrimeFactorizer.factor(n)
        gold = [3]
        self.assertListEqual(system, gold, 'prime factorization of {} should '
                                           'be {}'.format(n, gold))

    def test_factor_4(self):
        n = 4
        system = PrimeFactorizer.factor(n)
        gold = [2, 2]
        self.assertListEqual(system, gold, 'prime factorization of {} should '
                                           'be {}'.format(n, gold))

    def test_factor_5(self):
        n = 5
        system = PrimeFactorizer.factor(n)
        gold = [5]
        self.assertListEqual(system, gold, 'prime factorization of {} should '
                                           'be {}'.format(n, gold))

    def test_factor_6(self):
        n = 6
        system = PrimeFactorizer.factor(n)
        gold = [2, 3]
        self.assertListEqual(system, gold, 'prime factorization of {} should '
                                           'be {}'.format(n, gold))
