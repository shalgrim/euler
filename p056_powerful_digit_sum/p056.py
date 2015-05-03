"""
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?
"""

from constants import *

__author__ = 'Scott'

if __name__ == '__main__':
    biggest_sum = ZERO
    for a in range(ONE_HUNDRED):
        print 'a: {}'.format(a)
        for b in range(ONE_HUNDRED):
            number = a**b
            numstr = str(number)
            numsum = sum([int(ns) for ns in numstr])
            if numsum > biggest_sum:
                biggest_sum = numsum

    print 'answer: {}'.format(biggest_sum)
