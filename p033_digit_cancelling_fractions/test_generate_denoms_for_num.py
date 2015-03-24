from unittest import TestCase
from p033 import generate_denoms_for_num

__author__ = 'Scott'

LIST_99 = []
LIST_98 = []
LIST_97 = [98]
LIST_91 = [92, 93, 94, 95, 96, 97] + LIST_97
LIST_90 = [91] + LIST_91
LIST_89 = [90] + LIST_90
LIST_88 = [89, 98]
LIST_87 = [89, 97, 98]

class TestGenerate_denoms_for_num(TestCase):
    def test_input_99(self):
        correct_list = LIST_99
        sys_list = generate_denoms_for_num(99)
        self.assertEqual(correct_list, sys_list, 'gold: {}; sys: {}'.format(
                                                        correct_list, sys_list))
        return

    def test_input_98(self):
        correct_list = LIST_98
        sys_list = generate_denoms_for_num(98)
        self.assertEqual(correct_list, sys_list, 'gold: {}; sys: {}'.format(
                                                        correct_list, sys_list))
        return

    def test_input_97(self):
        correct_list = LIST_97
        sys_list = generate_denoms_for_num(97)
        self.assertEqual(correct_list, sys_list, 'gold: {}; sys: {}'.format(
                                                        correct_list, sys_list))
        return

    def test_input_91(self):
        correct_list = LIST_91
        sys_list = generate_denoms_for_num(91)
        self.assertEqual(correct_list, sys_list, 'gold: {}; sys: {}'.format(
                                                        correct_list, sys_list))
        return

    def test_input_90(self):
        correct_list = LIST_90
        sys_list = generate_denoms_for_num(90)
        self.assertEqual(correct_list, sys_list, 'gold: {}; sys: {}'.format(
                                                        correct_list, sys_list))
        return

    def test_input_89(self):
        correct_list = LIST_89
        sys_list = generate_denoms_for_num(89)
        self.assertEqual(correct_list, sys_list, 'gold: {}; sys: {}'.format(
                                                        correct_list, sys_list))
        return

    def test_input_88(self):
        correct_list = LIST_88
        sys_list = generate_denoms_for_num(88)
        self.assertEqual(correct_list, sys_list, 'gold: {}; sys: {}'.format(
                                                        correct_list, sys_list))
        return

    def test_input_87(self):
        correct_list = LIST_87
        sys_list = generate_denoms_for_num(87)
        self.assertEqual(correct_list, sys_list, 'gold: {}; sys: {}'.format(
                                                        correct_list, sys_list))
        return

    def test_too_small(self):
        self.assertRaises(AssertionError, generate_denoms_for_num, 9)
        return

    def test_too_big(self):
        self.assertRaises(AssertionError, generate_denoms_for_num, 100)
        return

    def test_string_input(self):
        self.assertRaises(AssertionError, generate_denoms_for_num, '9')
        return
