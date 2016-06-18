"""
Methods regarding pentagonal numbers

Pentagonal numbers are generated by the formula, P_n = n(3n-1)/2. The first ten
pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
"""

import constants
import functools
from misc import solve_quadratic


def compute_pentagonal(n):
    """
    Computes n'th pentagonal number
    :param n: int
    :return: n't pentagonal number
    """
    assert isinstance(n, int), "n must be integer, you sent in {}".format(n)
    assert n >= 1, "n must be >= 1, you sent in {}".format(n)

    return (n * (3 * n - 1)) / 2


@functools.lru_cache(maxsize=1024)
def is_pentagonal(n):
    """
    Determines if n is a pentagonal number
    :param n: int
    :return True if n is pentagonal, False otherwise
    """
    assert isinstance(n, int), "n must be integer, you sent in {}".format(n)
    assert n >=1, "n must be >= 1, you sent in {}".format(n)
    r1, r2 = solve_quadratic(1.5, -0.5, -n)
    # r1 will be my larger root
    if r1 > 0 and r1 == int(r1):
        return True
    return False


def pentagonal_generator(n=constants.INFINITY, n_with_start=None):
    """
    generates pentagonals less than or equal to n in order
    :param n: upper limit of possible pentagonals, inclusive
    :param n_with_start: if not None then n is start and this is n
    :return: yields each pentagonal <= n
    """
    if n_with_start:
        real_n = n_with_start
        i = n
    else:
        real_n = n
        i = 0

    while i < real_n:
        i += 1
        if is_pentagonal(i):
            yield i