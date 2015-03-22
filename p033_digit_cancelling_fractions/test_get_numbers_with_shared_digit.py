from unittest import TestCase
from p033 import get_numbers_with_shared_digit

__author__ = 'Scott'


class TestGet_numbers_with_shared_digit_success(TestCase):
    def test_AssertionError_if_too_small(self):
        self.assertRaises(AssertionError, get_numbers_with_shared_digit, 9)
        return

    def test_AssertionError_if_too_small(self):
        self.assertRaises(AssertionError, get_numbers_with_shared_digit, 100)
        return

    def test_input_10(self):
        correct_set = set([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                           30, 31, 40, 41, 50, 51, 60, 61, 70, 71, 80, 81,
                           90, 91])
        sys_set = get_numbers_with_shared_digit(10)
        self.assertEqual(correct_set, sys_set, 'gold: {}; sys: {}'.format(
                                                        correct_set, sys_set))
        return

    def test_input_11(self):
        correct_set = set([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 31,
                           41, 51, 61, 71, 81, 91])
        sys_set = get_numbers_with_shared_digit(11)
        self.assertEqual(correct_set, sys_set, 'gold: {}; sys: {}'.format(
                                                        correct_set, sys_set))
        return

    def test_input_12(self):
        correct_set = set([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                           22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 41, 42,
                           51, 52, 61, 62, 71, 72, 81, 82, 91, 92])
        sys_set = get_numbers_with_shared_digit(12)
        self.assertEqual(correct_set, sys_set, 'gold: {}; sys: {}'.format(
                                                        correct_set, sys_set))

        return
