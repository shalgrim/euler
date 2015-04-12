from unittest import TestCase
from fraction import Fraction

__author__ = 'Scott'


class TestFraction(TestCase):
    def test_get_reduced_1_1(self):
        original_fraction = Fraction(1, 1)
        reduced_fraction = original_fraction.get_reduced()
        self.assertTrue(original_fraction == reduced_fraction)
        return

    def test_get_reduced_1_2(self):
        original_fraction = Fraction(1, 2)
        reduced_fraction = original_fraction.get_reduced()
        self.assertTrue(original_fraction == reduced_fraction)
        return

    def test_get_reduced_2_3(self):
        original_fraction = Fraction(2, 3)
        reduced_fraction = original_fraction.get_reduced()
        self.assertTrue(original_fraction == reduced_fraction)
        return

    def test_get_reduced_2_4(self):
        original_fraction = Fraction(2, 4)
        reduced_fraction = original_fraction.get_reduced()
        correct_reduced_fraction = Fraction(1, 2)
        self.assertEqual(correct_reduced_fraction, reduced_fraction)
        return

    def test_get_reduced_6_9(self):
        original_fraction = Fraction(6, 9)
        reduced_fraction = original_fraction.get_reduced()
        correct_reduced_fraction = Fraction(2, 3)
        self.assertEqual(correct_reduced_fraction, reduced_fraction)
        return

    def test_get_gcd_1_2(self):
        f = Fraction(1, 2)
        self.assertEqual(1, f.get_gcd())
        return

    def test_get_gcd_2_3(self):
        f = Fraction(2, 3)
        self.assertEqual(1, f.get_gcd())
        return

    def test_get_gcd_2_4(self):
        f = Fraction(2, 4)
        self.assertEqual(2, f.get_gcd())
        return

    def test_get_gcd_8_12(self):
        f = Fraction(8, 12)
        self.assertEqual(4, f.get_gcd())
        return

    def test_get_common_digits_1(self):
        f = Fraction(12, 24)
        answer = set('2')
        self.assertEqual(answer, f.get_common_digits())
        return

    def test_get_common_digits_2(self):
        f = Fraction(12, 21)
        answer = set('12')
        self.assertEqual(answer, f.get_common_digits())
        return

    def test_generate_cancelled_fractions_1(self):
        f = Fraction(13, 39)
        answer = [Fraction(1, 9)]
        self.assertEqual(answer, f.generate_cancelled_fractions())
        return

    def test_generate_cancelled_fractions_2(self):
        f = Fraction(23, 32)
        answer = [Fraction(2, 2), Fraction(3, 3)]
        self.assertEqual(answer, f.generate_cancelled_fractions())
        return


