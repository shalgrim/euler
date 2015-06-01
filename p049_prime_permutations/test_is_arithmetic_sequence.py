from unittest import TestCase

__author__ = 'Scott'

from p049 import is_arithmetic_sequence

class TestIs_arithmetic_sequence(TestCase):
    def test_is_arithmetic_sequence_true_1(self):
        self.assertTrue(is_arithmetic_sequence([1, 2, 3]))

    def test_is_arithmetic_sequence_true_2(self):
        self.assertTrue(is_arithmetic_sequence([1]))

    def test_is_arithmetic_sequence_true_3(self):
        self.assertTrue(is_arithmetic_sequence([1, 7]))

    def test_is_arithmetic_sequence_true_4(self):
        self.assertTrue(is_arithmetic_sequence([1487, 4817, 8147]))

    def test_is_arithmetic_sequence_true_5(self):
        self.assertTrue(is_arithmetic_sequence([4817, 1487, 8147]))

    def test_is_arithmetic_sequence_true_6(self):
        self.assertTrue(is_arithmetic_sequence([4817, 1487, 8147, 11477]))

    def test_is_arithmetic_sequence_false_1(self):
        self.assertFalse(is_arithmetic_sequence([]))

    def test_is_arithmetic_sequence_false_2(self):
        self.assertTrue(is_arithmetic_sequence([1487, 4817, 8148]))

    def test_is_arithmetic_sequence_error_1(self):
        self.assertRaises(is_arithmetic_sequence(15), AssertionError)

    def test_is_arithmetic_sequence_error_2(self):
        self.assertRaises(is_arithmetic_sequence([15, 7.5, 0]), AssertionError)
