from unittest import TestCase

__author__ = 'Scott'

from p049 import find_first_arithmetic_sequence

class TestFind_first_arithmetic_sequence(TestCase):

    def setUp(self):
        self.known_answer = [1487, 4817, 8147]
        self.input_set = set(self.known_answer)

    def tearDown(self):
        del self.known_answer
        del self.input_set

    def test_find_first_arithmetic_sequence_equal_1(self):
        result = find_first_arithmetic_sequence(self.input_set)
        self.assertEqual(self.known_answer, result)
        return

    def test_find_first_arithmetic_sequence_equal_2(self):
        self.input_set.add(9999)
        result = find_first_arithmetic_sequence(self.input_set)
        self.assertEqual(self.known_answer, result)
        return

    def test_find_first_arithmetic_sequence_equal_3(self):
        self.input_set.add(1)
        result = find_first_arithmetic_sequence(self.input_set)
        self.assertEqual(self.known_answer, result)
        return

    def test_find_first_arithmetic_sequence_too_long(self):
        result = find_first_arithmetic_sequence(self.input_set, 4)
        self.assertIsNone(result)
        return

    def test_find_first_arithmetic_sequence_none(self):
        self.input_set.pop()
        self.input_set.add(1)
        result = find_first_arithmetic_sequence(self.input_set)
        self.assertIsNone(result)

        return



