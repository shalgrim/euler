from unittest import TestCase

__author__ = 'Scott'

from p046 import fits_conjecture

class TestFitsConjecture(TestCase):
    def test_fits_conjecture_9(self):
        self.assertTrue(fits_conjecture(9))

    def test_fits_conjecture_15(self):
        self.assertTrue(fits_conjecture(15))

    def test_fits_conjecture_6(self):
        self.assertRaises(AssertionError, fits_conjecture, 6)

    def test_fits_conjecture_7(self):
        self.assertRaises(AssertionError, fits_conjecture, 7)
