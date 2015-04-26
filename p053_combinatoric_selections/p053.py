"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5 choose 3 = 10.

In general,
n choose r = n!/(r!(n-r)!) ,
where r <= n, n! = n x (n-1) x ... x 3 x 2 x 1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million:
23 choose 10 = 1144066.

How many, not necessarily distinct, values of n choose r, for 1 <= n <= 100, are
greater than one-million?
"""

import math, sys

__author__ = 'Scott'

ONE_MILLION = 1000000

def combo_count(n, r):
    """
    calculates the number of ways to choose r elements with no repeats from a
    set of n elements
    :param n: the bigger number
    :param r: the smaller number
    :return: the number of ways to choose r elements with no repeats from a
    set of n elements
    """
    assert r <= n
    num = math.factorial(n)
    denom = math.factorial(r) * math.factorial(n-r)
    return num / denom


if __name__ == '__main__':
    combos_bigger_million = set()

    for n in range(1, 101):
        print >> sys.stderr, 'n: {}'.format(n)
        for r in range(1, n+1):
            if combo_count(n, r) > ONE_MILLION:
                combos_bigger_million.add((n ,r))

    print 'answer: {}'.format(len(combos_bigger_million))
