from unittest import TestCase
from p033 import get_two_digit_nums_from_single_digit

__author__ = 'Scott'


class TestGet_two_digit_nums_from_single_digit(TestCase):
    def test_AssertionError_on_string(self):
        self.assertRaises(AssertionError,
                          get_two_digit_nums_from_single_digit,'1')
        return

    def test_AssertionError_on_too_small(self):
        self.assertRaises(AssertionError,
                          get_two_digit_nums_from_single_digit, -1)
        return

    def test_AssertionError_on_too_big(self):
        self.assertRaises(AssertionError,
                          get_two_digit_nums_from_single_digit, 10)
        return

    def test_input_0(self):
        correct_set = set([10, 20, 30, 40, 50, 60, 70, 80, 90])
        sys_set = get_two_digit_nums_from_single_digit(0)
        self.assertEqual(correct_set, sys_set, 'gold: {}; sys: {}'.format(
                                                        correct_set, sys_set))
        return

    def test_input_1(self):
        correct_set = set([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 31,
                           41, 51, 61, 71, 81, 91])
        sys_set = get_two_digit_nums_from_single_digit(1)
        self.assertEqual(correct_set, sys_set, 'gold: {}; sys: {}'.format(
                                                        correct_set, sys_set))
        return
