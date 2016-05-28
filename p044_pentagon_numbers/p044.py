"""
Pentagonal numbers are generated by the formula, P_n = n(3n-1)/2. The first ten
pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P_4 + P_7 = 22 + 70 = 92 = P_8. However, their difference,
70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, P_j and P_k, for which their sum and
difference are pentagonal and D = |P_k - P_j| is minimised; what is the value
of D?
"""

from constants import MAIN_PROCESS
import math

__author__ = 'Scott'


def compute_pentagonal(n):
    """
    Computes n'th pentagonal number
    :param n: int
    :return: n't pentagonal number
    """
    assert isinstance(n, int), "n must be integer, you sent in {}".format(n)
    assert n >=1, "n must be >= 1, you sent in {}".format(n)

    return (n * (3 * n - 1)) / 2


def solve_quadratic(a, b, c):
    """
    Solves quadratic equation
    :param a: coefficient of x^2
    :param b: coefficient of x^1
    :param c: coefficient of x^0
    :return (r1, r2): roots of quadratic equation
    """
    # TODO: make some unit tests
    radicand = b**2 - 4*a*c
    assert radicand >= 0, "We don't handle negative determinants"
    root = math.sqrt(b**2-4*a*c) # seems to always return positive and float
    denom = 2*a
    r1 = (-b + root) / denom
    r2 = (-b - root) / denom

    return r1, r2

# TODO: Fix this, it's only been copied from prime_generator and had a few
# variable name changes. I.e., I am turning prime_generator into
# pentagonal_generator but haven't got very far with it yet
# def pentagonal_generator(n):
# TODO: move into a pentagonal module
#     """
#     generates pentagonals less than or equal to n in order
#     :param n: upper limit of possible pentagonals, inclusive
#     :return: yields each pentagonal <= n
#     """
#     known_pents = []
#     i = 0
#     while i < n:
#         i += 1
#         pents_to_check = [kp for kp in known_pents if kp <= i/2]
#         for prime in pents_to_check:
#             if i % prime == 0:
#                 break
#         else:
#             known_pents.append(i)
#             yield i


if __name__ == MAIN_PROCESS:
    pass
    # bad pseudocode:
    # base case: P_j = 1 -> search for first P_j s.t. P_j + P_k = pentagonal and
    #            P_k - P_j = pentagonal. Set D = P_k - P_j
    # search:
    #   for each P_j > 1, conduct the same search as in the base case unless you
    #       get to a point where P_k - P_j > D
    # termination:
    #   P_j+1 - P_j > D

    # My next step is clearly setting up unit tests for is_pentagonal
