from unittest import TestCase
from misc import solve_quadratic


class TestSolve_quadratic(TestCase):
    def test_solve_quadratric_1(self):
        r1, r2 = solve_quadratic(1.5, -.5, -1)
        self.assertTrue(r1 == 1.0)
        self.assertTrue(int(r1) == 1)
