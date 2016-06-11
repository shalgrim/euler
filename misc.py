"""
Stuff I haven't figured out how to factor yet
"""

import math


def solve_quadratic(a, b, c):
    """
    Solves quadratic equation
    :param a: coefficient of x^2
    :param b: coefficient of x^1
    :param c: coefficient of x^0
    :return (r1, r2): roots of quadratic equation
    """
    radicand = b**2 - 4*a*c
    assert radicand >= 0, "We don't handle negative determinants"
    root = math.sqrt(radicand)  # seems to always return positive and float
    denom = 2*a
    r1 = (-b + root) / denom
    r2 = (-b - root) / denom

    return r1, r2

