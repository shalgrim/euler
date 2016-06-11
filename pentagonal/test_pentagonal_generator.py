from unittest import TestCase
from pentagonal import pentagonal_generator

class TestPentagonal_generator(TestCase):
    FIRST_TEN_PENTS = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
    def test_pentagonal_generator_first_ten(self):
        gen = pentagonal_generator(145)
        for truth, generated in zip(self.FIRST_TEN_PENTS, gen):
            self.assertEqual(truth, generated)
