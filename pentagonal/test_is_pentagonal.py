from unittest import TestCase
from pentagonal import is_pentagonal


class TestIs_pentagonal(TestCase):
    def test_is_pentagonal_1(self):
        self.assertTrue(is_pentagonal(1))


    def test_is_not_pentagonal_2(self):
        self.assertFalse(is_pentagonal(2))


    def test_is_pentagonal_5(self):
        self.assertTrue(is_pentagonal(5))
